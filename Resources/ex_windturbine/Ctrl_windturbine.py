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
fmu.setReal([2], [10]) # Windgeschwindigkeit auf 10m/s


tend     = 20                       # simulation duration
dt_reg   = 0.1                     # sample time control system
dt_mod   = 0.001                     # sample time of model
n_fine   = round(dt_reg/dt_mod)     # number of model iterations per control system sample

# Control system operating point 
OP_u = 5.0          # pitch (deg)  
OP_y = 0.8155       # power (pu)

# initialize 
tmod = [0.0]        # model time vector
ymod = [1.0]        # model output vector


#  |-n0| ... |-3|-2|-1|0|1|2|3 .. |n|

n0 = 7                              # number of past samples for inital values
n  = round(tend/dt_reg);            # number of control system steps

# time vecor especially for plotting
treg = [x*dt_reg for x in range(-n0+1,1)] + [x*dt_reg for x in range(1,n+1)]

# reference values for power in process and control coordinates 
rproc = [0.8-0.1*(t>=10.0) for t in treg]
rreg  = [r-OP_y for r in rproc]

# initialize desired values for power in process and control coordinates 
ydesproc = [0.0 for t in treg]
ydesmod = [0.0 for t in treg]

# initialize output values for power in process and control coordinates 
yproc = [0.0 for t in treg]
yreg = [0.0 for t in treg]

# initialize manipulated variable (pitch) in process and control coordinates 
uproc = [0.0 for t in treg]
ureg = [0.0 for t in treg]

# initialize control error
ereg = [0.0 for t in treg]

# initialize feed forward and feedback signal vectors
uffreg = [0.5269 for t in treg]
ufbreg = [0.0 for t in treg]

memo = OP_y     # init memory to resolve algebraic loop
for k in range(n0,n+n0):
    
    # calc desired output from reference value
    ydesmod[k]= 0.42857*ydesmod[k-1] + -0.061224*ydesmod[k-2] + 0.0029155*ydesmod[k-3]+0.078717*rreg[k-0]+0.23615*rreg[k-1]+0.23615*rreg[k-2]+0.078717*rreg[k-3]
    ydesproc[k] = ydesmod[k]+OP_y
    
    # calc feedforward signal
    uffreg[k]= -0.84007*uffreg[k-1] + 0.89317*uffreg[k-2] + 0.44274*uffreg[k-3] + -0.26837*uffreg[k-4] + 0.041262*uffreg[k-5] + -0.0020219*uffreg[k-6]+-19.1915*rreg[k-0]+-22.4428*rreg[k-1]+18.9386*rreg[k-2]+10.3965*rreg[k-3]+-21.2951*rreg[k-4]+-0.41804*rreg[k-5]+9.0836*rreg[k-6]


    if treg[k]>-2.5:
        # control error
        ereg[k] = (ydesmod[k] - yreg[k-1])   

        # feedback controller           
        ufbreg[k]= 1*ufbreg[k-1]+-10.2*ereg[k-0]+9.8*ereg[k-1]
        ufbreg[k]= 1*ufbreg[k-1]+-11*ereg[k-0]+9*ereg[k-1]
        
        # control signal
        ureg[k]  = ufbreg[k] + uffreg[k]
        uproc[k] = ureg[k] + OP_u
    else:
        ereg[k] = 0
        ufbreg[k] = 0
        ureg[k]  = 0
        uproc[k] = OP_u
    
    
    # simulate process
    fmu.setReal([1], [uproc[k]])
    for ms in range(0,n_fine):
        ret = fmu.doStep(currentCommunicationPoint=tmod[-1], communicationStepSize=dt_mod)
        tmod += [tmod[-1]+dt_mod]
        ymod += fmu.getReal([3])

    # use last output 
    yproc[k] = memo
    yreg[k] = yproc[k]-OP_y
    
    # store last model output (process coordinates) in memory
    memo = ymod[-1]

    # print some values of the sim-step
    if k<=10:
        logging.info(' k: %3s | treg[k] %4.4s | yreg[k-1] %4.4s | rreg[k] %4.4s | ereg[k] %4.5s | yreg[k] %4.4s', k, treg[k], yreg[k-1],rreg[k],ereg[k],yreg[k])


# close fmu
fmu.terminate()
fmu.freeInstance ()
logging.info('Closed fmu, try deleting temp-dir: %s', fmu_unzipdir)

# delete temp dir
shutil.rmtree(fmu_unzipdir, ignore_errors=True)



# plot results
fig = plt.figure(1)
fig.clear()
fig, axs = plt.subplots(2,sharex='col',num=1)
axs[0].plot(tmod, ymod, label='power (cont)')
axs[0].step(treg, yproc, label='power (disc)')
axs[0].set_ylim(0.6,1.2)
axs[0].set_xlim(0,treg[-1])
axs[0].grid(color=[0.9,0.9,0.9])
axs[0].legend()

axs[1].step(treg, uproc,label = 'pitch')
# axs[1].step(treg, uff,label = 'feedforward')
axs[1].grid(color=[0.9,0.9,0.9])
axs[1].legend()
axs[1].set_ylim(5,10)
# axs[0].set_xlim(0,2.9)

fig.show()



