import numpy
from fmpy import read_model_description, extract
from fmpy.fmi2 import FMU2Slave
import shutil
import matplotlib.pyplot as plt


import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)



fmu_filename = "windturbine.fmu"
fmu_model_description = read_model_description(fmu_filename)

print(fmu_model_description.modelVariables)

fmu_unzipdir = extract(fmu_filename)

fmu = FMU2Slave(guid=fmu_model_description.guid,
                     unzipDirectory=fmu_unzipdir,
                     modelIdentifier=fmu_model_description.coSimulation.modelIdentifier,
                     instanceName='instance1')

logging.info('Using this fmu: %s - extracting it to %s', fmu_filename ,fmu_unzipdir)

# initialize fmu
fmu.instantiate()
fmu.setupExperiment(startTime=0.0)
fmu.enterInitializationMode()
fmu.exitInitializationMode()

tend     = 20
dt_reg   = 0.02
dt_fine  = 0.001
n_fine   = round(dt_reg/dt_fine)

tfine = [0.0]
yfine = [1.0]


#  |-n0| ... |-3|-2|-1|0|1|2|3 .. |n|

n0 = 7
n  = round(tend/dt_reg);

treg = [x*dt_reg for x in range(-n0+1,1)] + [x*dt_reg for x in range(1,n+1)]
yreg = [1.0 for t in treg]
ureg = [0.0 for t in treg]
ereg = [0.0 for t in treg]
rreg = [0.8-0.1*(t>=10.0) for t in treg]

rreg_lin = [x-0.8 for x in rreg]
uff = [0.0 for t in treg]

Kp = 10
Ki = 20
T  = dt_reg

memo = yreg[0]
for k in range(n0,n+n0):
    
    

    tt = 4.207893221e10*rreg_lin[k] - 1.188447559e11*rreg_lin[k-1] + 1.144251045e11*rreg_lin[k-2] - 3.930999540e10*rreg_lin[k-3] + 2.046319496e9*rreg_lin[k-4] - 3.20218750e8*rreg_lin[k-5]
    uff[k] = -1/(2.892703283e9)*(tt - 9.516033468e9*uff[k-1] + 1.185270961e10*uff[k-2] - 6.768606472e9*uff[k-3] + 1.660759637e9*uff[k-4] - 1.34940625e8*uff[k-5] + 1.5625000e7*uff[k-6])

    if treg[k]>2.5:
        ereg[k] = -(rreg[k] - yreg[k-1])

        ureg[k] = ureg[k-1] + (Ki*T+Kp)*ereg[k]  - Kp*ereg[k-1]

    fmu.setReal([1], [ureg[k]+uff[k]])
    for ms in range(0,n_fine):
        ret = fmu.doStep(currentCommunicationPoint=tfine[-1], communicationStepSize=dt_fine)
        tfine += [tfine[-1]+dt_fine]
        yfine += fmu.getReal([3])


    yreg[k] = memo
    memo = yfine[-1]

    if k<=10:
        logging.info(' k: %3s | treg[k] %4.4s | yreg[k-1] %4.4s | rreg[k] %4.4s | ereg[k] %4.5s | yreg[k] %4.4s', k, treg[k], yreg[k-1],rreg[k],ereg[k],yreg[k])


# close fmu
fmu.terminate()
fmu.freeInstance()
logging.info('Closed fmu, try deleting temp-dir: %s', fmu_unzipdir)
# delete temp dir
shutil.rmtree(fmu_unzipdir, ignore_errors=True)


# plot results
fig = plt.figure(1)
fig.clear()
fig, axs = plt.subplots(2,sharex='col',num=1)
axs[0].plot(tfine, yfine, label='power (cont)')
axs[0].step(treg, yreg, label='power (disc)')
axs[0].step(treg, rreg,label = 'reference power')
axs[0].set_ylim(0.6,1.2)
axs[0].set_xlim(0,treg[-1])
axs[0].grid(color=[0.9,0.9,0.9])
axs[0].legend()

axs[1].step(treg, ureg,label = 'pitch')
axs[1].step(treg, uff,label = 'feedforward')
axs[1].grid(color=[0.9,0.9,0.9])
axs[1].grid(color='lightgray')
axs[1].legend()
fig.show()

# axs[1].plot(treg, ereg)


