## Abtastung
Prinzipieller Aufbau eines Abtastsystems - Prozessrechner wird als Regler eingesetzt:

![Quelle: Unbehauen2 ](Pasted%20image%2020210524070217.png)

die Regelabweichung $e(t)$ wird in den digitalen Wert $e(kT)$ umgewandelt.

--- 

### Analog Digital Umsetzung
- erfolgt periodisch mit Abtastzeit $T$
- Amplitudenquantisierung bzw. Diskretisierung

![\|300](Pasted%20image%2020210524071605.png)

- Die Zeit-diskretisierung ist linear, die Wert-Diskretisierung ist **nichtlinear**
- Quantisierungsstufen klein --> Quantisierungseffekt oft vernachlässigbar
- Wenn von diskreten Systemen die Rede ist, sind zeitdiskrete gemeint.
- Lineare Systeme sind nach der Abtastung auch linear, **weil die Systeme nur an den Zeitpunkten kT betrachtet werden.**
- Es ergibt sich eine diskrete Systemdarstellung in der alle Funktionen Zahlenfolgen sind.


--- 

### Digital Analog Umsetzung

- Prozessrechner berechnet Stellgröße $u(kT)$
- im D/A  Umsetzer wird $\bar{u}(t)$ erzeugt, das ist konstant $kT<T<(k+1)T$
- Stellsignal hat Treppenform

---

## Umwandlung zeitkontinuierlich --> zeitdiskret

- Verschiede Ansätze verfügbar
- einfachste Möglichkeit: Approximation des Differenzenquotienten:
![Quelle: Unbehauen2 \| 300 ](Pasted%20image%2020210525082643.png)




---

## Fahrzeugmodell zeitdiskret

Wiederholung aus [3_Modellbildung](3_Modellbildung.md):

| DGL                                                           | Lösung                                                                                                     | eingesetzt                                      |
| ------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| $$\tfrac{d}{d\,t}v(t)  = -\frac{b}{m}\cdot v(t)+\frac{F}{m}$$ | $$v \left( t \right) ={\frac {F}{b}}+{{\rm e}^{-{\frac {b\,t}{m}}}}\left( v_{0}-{\frac {F}{b}} \right)$$ | $$v \left( t \right) =10-5\,{{\rm e}^{-t/20}}$$ |


| ![Geschwindigkeitsregelung (Quelle: [[Franklin2015]]) \|200](Pasted%20image%2020201227100125.png) | ![Änderung der Fahrzeuggeschwindigekeit bei $F_u=500 N$ und $v(0)=5 \tfrac{m}{s}$ \|300](SprungantwortFahrzeuggeschwindigkeit.png) |
| ------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
|                                                                                                   |                                                                                                                              |

| Masse       | Reibwert                   | Kraft       |  
| ----------- | -------------------------- | ----------- | 
| $m=1000 kg$ | $b=50 \tfrac{N\cdot s}{m}$ | $F=500 N$ |       
 
Gesucht ist jetzt *ein* zeitdiskretes Modell








---

## Fahrzeugmodell zeitdiskret

DGL:  $$\tfrac{d}{d\,t}v(t)  = -\frac{b}{m}\cdot v(t)+\frac{F}{m}$$

ersetzen $v(t)=v(kT)$ und  $\frac{dv(t)}{dt}=\frac{v(kT)-v((k-1)T)}{T}$

fertig: $$\frac{v(kT)-v((k-1)T)}{T}= - \frac{b}{m}v(kT) + \frac{F}{m}$$




---

## Fahrzeugmodell zeitdiskret

$$\frac{v(kT)-v((k-1)T)}{T}= - \frac{b}{m}v(kT) + \frac{F}{m}$$

umstellen :

$$v(kT) = \frac{m\cdot v((k-1)T)}{T\cdot b+m}+\frac{F\cdot T}{T\cdot b+m}$$

verkürzt :

$$v_{(k)} = \frac{m}{T\cdot b+m}v_{(k-1)}+\frac{F\cdot T}{T\cdot b+m}$$

für T=5: 

$$v_{(k)} = 0.8\cdot v_{(k-1)}+2$$

---

## Fahrzeugmodell zeitdiskret

$$v_{(k)} = 0.8\cdot v_{(k-1)}+2$$

| k    | -1  | 0   | 1   | 2   | 3    | 4     | 5      | 6       | 7        |
| ---- | --- | --- | --- | --- | ---- | ----- | ------ | ------- | -------- |
| y(k) | 5   | 5   | 6   | 6.8 | 7.44 | 7.952 | 8.3616 | 8.68928 | 8.951424 | 

![discrete2](discrete2.png)

Explizite Form der rekursiven Differenzengleichung für $v_0=5$:

$$v_{(k)} = 10-5\left(\frac{4}{5}\right)^k$$


---

## Aufgabe Verzögerungsglied

DGL:  $\qquad \Large T_1 \frac{dy(t)}{dt} + y(t) = u(t)$

Gesucht ist:
1) die Differenzengleichung für  $T = 1$ und $T_1 = 4$:
2) die Werte von $y_{(k)}$ für k=1,2,3,4,5 $u_{(k)}=1$ und $y_{0}=0$


---

## Lösung Verzögerungsglied 1/

ersetzen $y(t)=y(kT)$, $u(t)=u(kT)$ und  $\frac{dy(t)}{dt}=\frac{y(kT)-y((k-1)T)}{T}$

fertig: $$T_1 \frac{dy(t)}{dt} + y(t) = u(t) \quad\rightarrow\quad T_1 \frac{y(kT)-y((k-1)T)}{T} + y(kT) = u(kT)$$


---

## Lösung Verzögerungsglied 2/

umstellen :$$\begin{gather}
\frac{T_1}{T}y(kT)-\frac{T_1}{T}y((k-1)T) + y(kT) = u(kT) \\
\frac{T_1}{T}y(kT) + y(kT) = u(kT) + \frac{T_1}{T}y((k-1)T)\\
\left(\frac{T_1}{T}+1\right)y(kT) = u(kT) + \frac{T_1}{T}y((k-1)T)\\
y(kT) = \left(\frac{T}{T_1+T}\right)\left(u(kT) + \frac{T_1}{T}y((k-1)T)\right)
\end{gather}$$

$$y(kT) = \left(\frac{T}{T_1+T}\right) u(kT) + \left(\frac{T_1}{T_1+T}\right) y((k-1)T)$$

---

## Lösung Verzögerungsglied 3/

vereinfachte Schreibweise:
$$y_{(k)} = \left(\frac{T_1}{T_1+T}\right) y_{(k-1)} + \left(\frac{T}{T_1+T}\right) u_{(k)} $$

Für $T = 1$ und $T_1 = 4$ und $y_{(0)}=0$:

$$y_{(k)} = 0.8 y_{(k-1)} + 0.2 u_{(k)} $$

| k    | -1  | 0   | 1   | 2    | 3     | 4      | 5       | 6        | 7         |     |
| ---- | --- | --- | --- | ---- | ----- | ------ | ------- | -------- | --------- |
| u(k) | 0   | 0   | 1   | 1    | 1     | 1      | 1       | 1        | 1         |     |
| y(k) | 0   | 0   | 0.2 | 0.36 | 0.488 | 0.5904 | 0.67232 | 0.737856 | 0.7902848 |     |


- Der Sprung ist bei k=0 noch 0 - erst bei k=1 wird er hier 1
- Mit dieser zeitdiskreten Sprungdefinition wird bei dem System mit Durchgriff die Anfangsbedingung $y_{(0)}=0$ eingehalten. 


---

## Lösung Verzögerungsglied 4/
$$y_{(k)} = 0.8 y_{(k-1)} + 0.2 u_{(k)}$$

![discrete1](discrete1.png)

- Das zeitdiskrete System ist rekursiv.
- Das zeitdiskrete System hat Durchgriff!!! 
- Wegen der Approximation: $\frac{dy(t)}{dt}=\frac{y(kT)-y((k-1)T)}{T}$ erzeugt die rekursive Gleichung nur eine  Näherungslösung der Differentialgleichung.
- Approximationsfehler werden kleiner für kleineres T

---

## Lösung Verzögerungsglied 5/
$$y_{(k)} = 0.8 y_{(k-1)} + 0.2 u_{(k)}$$

- Für bestimmte Eingangssignale $u_{(k)}$ kann eine explizite Lösung angegeben werden.
- z.B. $y_{(0)}=0$ und $u_{(k)}  = 1$:

$$y_{(k)} = 1-0.8^k$$

- Ist der Eingang $u_{(k)}$ unbekannt, kann keine explizite Lösung angeben werden.

---

## Reihenschwingkreis  1/
![Ersatzschaltbild des Reihenschwingkreises Quelle: Abb. 4.2 aus [Lunze2016](Lunze2016.md) ](Schaltung%20Reihenschwingkreis.png)
Strom-Spannungsbeziehungen für R, L, C:
$$
\begin{eqnarray}
C\,L\frac{d^2}{dt^2}y(t)+C\,R\frac{d}{dt}y(t)+y(t) &=& C\,R\frac{d}{dt}u(t)+u(t)
\end{eqnarray}
$$

---

## Reihenschwingkreis 2/
#### Ausgangssignal

mit $CR = 0.5$ und $CL=0.2$  sieht so die Sprungantwort aus:

$$y(t) = \theta (t-\text{t0})\left(1+{\rm e}^{-\frac{-5}{4}\,\left(t-t0\right)}\left(\tfrac{\sqrt{55}}{11}\,{\rm sin}\left(\tfrac{\sqrt{55}}{4}\,\left(t-t0\right)\right)-{\rm cos}\left(\tfrac{\sqrt{55}}{4}\,\left(t-t0\right)\right)\right)\right)$$

bzw. gerundet und zusammengefasst:
$$y(t)=\theta (t-\text{t0})\Big(1-{{\rm e}^{- 1.25\,t+ 1.25\,{\it t0}}} \left(\cos \left(  1.86\,(t- {\it t0}) \right)-  0.674\,\sin \left(  1.86
\,(t-{\it t0}) \right)\right)\Big)
$$

![\|300](Pasted%20image%2020210206170423.png)


---
## Reihenschwingkreis 3/

DGL:  $\qquad C\,L\frac{d^2}{dt^2}y(t)+C\,R\frac{d}{dt}y(t)+y(t) = C\,R\frac{d}{dt}u(t)+u(t)$

Approximationen:

| 1. Ordnung                                                                                                           | 2. OPrdnung                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| $$\dot y(t)=\frac {dy}{dt} \approx \frac {\Delta y}{\Delta t}= \frac {\Delta y_k}{T}=\frac {y_{(k)}- y_{(k-1)}}{T}$$ | $$\ddot y(t)=\frac {d^2y}{dt^2} \approx \frac {\Delta^2y_k}{T^2} = \frac {y_{(k)}-2y_{(k-1)} +y_{(k-2)} }{T^2}$$ | 

eingesetzt: 
$${\frac {{\it CL}\, \left( y_{(k)} -2\,y_{(k-1)} 
+y_{(k-2)}  \right) }{{T}^{2}}}+{\frac {{\it CR}\, \left( y_{(k)} -y_{(k-1)}  \right) }{T}}+y \left( k
 \right) ={\frac {{\it CR}\, \left( u_{(k)} -u_{(k-1)}  \right) }{T}}+u_{(k)} $$

umgestellt:
$$y_{(k)} =-{\frac {{T}^{2}u_{(k)} }{-{\it CR}\,T-{T}^{2}-{\it CL}} \left( {\frac {{\it CR}}{T}}+1 \right) }+{\frac {{\it CR}\,u_{(k-1)} T}{-{\it CR}\,T-{T}^{2}-{\it CL}}}+{\frac {{\it CL}\,y_{(k-2)} }{-{\it CR}\,T-{T}^{2}-{\it CL}}}+{\frac { \left( -{\it CR}\,T-2\,{\it CL} \right) y_{(k-1)} }{-{\it CR}\,T-{T}^{2}-{\it CL}}}
$$

---

## Reihenschwingkreis 4/

| T=1                             | T=0.5                         |
| ------------------------------- | ----------------------------- |
|                                 |                               |
| ![discrete3aa](discrete3aa.png) | ![discrete3a](discrete3a.png) |

| T=0.2                                                                                                                       | T=0.01                        |
| --------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| $y_{(k)} ={\frac {7\,u_{(k)}  }{17}}-{\frac {5\,u_{(k-1)} }{17}}-{\frac {10\,y_{(k-2)} }{17}}+{\frac {25\,y_{(k-1)} }{17}}$ |                               |
| ![discrete3aa](discrete3b.png)                                                                                              | ![discrete3a](discrete3c.png) |


---

## Allgemeine Form linearer Differenzengleichungen

-  Differenzengleichungen bilden lineare zeitdiskrete Systeme ab.
-  Übliche Form
$$\boxed{{y_{(k)}=-a_1 \cdot y_{(k-1)} -a_2 \cdot y_{(k-2)} - \dots - a_n \cdot y_{(k-n)}} \quad +\quad b_0 \cdot u_{(k)}+ b_{1} \cdot u_{(k-1)}+ b_2 \cdot u_{(k-2)} + \dots + b_m \cdot u_{(k-m)}}$$
- Analyse und Synthese von Regelkreisen ist im Bildbereich wieder einfacher --> [Z-Transformation](17_Z-Transformation.md)