 ## Gekoppelte lineare Systeme
 
 ![](Pasted%20image%2020210311120833.png)
 
 
 
 
 
 
 
 
 
 
 
 
 




---
 
 ### Rückkopplungsschaltung 
 
 Man unterscheidet bei der Rückkopplung zwischen Gegen- und Mitkopplung.
 
  ![](Pasted%20image%2020210303224259.png)
  


















---
 
### Umformregeln für Blockschaltbilder
 ![Quelle: Lunze](Lunze_Umformregeln_BSB.png)
 

 











---
### kleines Beispiel
![](Pasted%20image%2020210311122130.png)

Wie ist die Gesamtübertragungsfunktion?

---

 ### kleines Beispiel
![](Pasted%20image%2020210311122130.png)

Wie ist die Gesamtübertragungsfunktion? --> 
$$\Large G(s) = \frac{\frac{2s+4}{s} \frac{1}{s}}{1+\frac{2s+4}{s} \frac{1}{s}} = 

\frac{2s+4}{s^2+2s+4}$$

---

## Praxis
### Python
So wird installiert: [Python Control Systems Library](Python%20Control%20Systems%20Library.md)


```Python
from control.matlab import *
import matplotlib.pyplot as plt  

sys = TransferFunction([10,2], [1, 2, 1])

# Step response for the system
plt.figure(1)
yout, T = step(sys,T=20)
plt.plot(T.T, yout.T)
plt.show()
```

vermutlich ist Julia mit: https://github.com/JuliaControl/ControlSystems.jl besser geeignet - wir probieren das mal aus