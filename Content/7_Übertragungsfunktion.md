Die Übertragungsfunktion
===================

Bald können wir Dinge in Python machen ....

---

... noch aber nicht ...

---
## Einführungsbeispiel Reihenschwingkreis 1/ 
![Ersatzschaltbild des Reihenschwingkreises Quelle: Abb. 4.2 aus [Lunze2016](Lunze2016.md) |500](Schaltung%20Reihenschwingkreis.png)
Strom-Spannungsbeziehungen für R, L, C:
$$
\begin{eqnarray}
C\,L\frac{d^2}{dt^2}y(t)+C\,R\frac{d}{dt}y(t)+y(t) &=& C\,R\frac{d}{dt}u(t)+u(t)
\end{eqnarray}
$$

MEGA WICHTIG: Das Modell gilt nur für $i_3=0$! - (Rückwirkungsfreiheit!!!)

**Aufgabe:** 
Mit den Korrespondenzen soll die Ausgangsspannung nach einem:
1) Spannungsimpuls zur Zeit $t_0$  
2) einem Spannungssprung  der Höhe 1 zur Zeit $t_0$  

berechnet werden.

---
## Einführungsbeispiel Reihenschwingkreis 2/
#### Transformation in des Systems in den Bildbereich

Differentialgleichung im Zeitbereich:
$$
\begin{eqnarray}
C\,L\frac{d^2}{dt^2}y(t)+C\,R\frac{d}{dt}y(t)+y(t) &=& C\,R\frac{d}{dt}u(t)+u(t)
\end{eqnarray}
$$

Nötige Korrespondenzen und Eigenschaften:

|                                                                                   | Originalfunktion $f(t) = \mathcal{L}^{-1} \left\{ F(s) \right\}$  | Bildfunktion $F(s) = \mathcal{L}\left\{ f(t) \right\}$            |
| ------------------------------------------------------------------------------------------------------------------------| ------------------------------------------------------------------| ------------------------------------------------------------------|
| 1\. Ableitung im OB                                                                                      | $f'(t) \,$                                                        | $sF(s)-f(0) \,$                                                   |
| 2\. Ableitung im OB                                                                                      | $f''(t) \,$                                                       | $s^{2}F(s)-sf(0)-f'(0) \,$                                        |

Zugehörige algebraische Gleichung im Bildbereich (Wir nehmen an die Anfangsbedingungen sind null):
$$
\begin{eqnarray}
C\,L\,s^2\,Y(s)+C\,R\,s\,Y(s)+Y(s) &=& C\,R\,s\,U(s) + U(s)
\end{eqnarray}
$$

---

## Einführungsbeispiel Reihenschwingkreis 3/
#### Umformen
$$
\begin{eqnarray}
C\,L\,s^2\,Y(s)+C\,R\,s\,Y(s)+Y(s) &=& C\,R\,s\,U(s) + U(s) \\[1ex]
\big(C\,L\,s^2+C\,R\,s+1\big)Y(s) &=& \big(C\,R\,s + 1\big)\,U(s)
\end{eqnarray}
$$

$$Y(s)=\underbrace{\frac{C\,R\,s + 1}{C\,L\,s^2+C\,R\,s+1}}_{\huge G(s)}\,U(s)$$

- $G(s)$ wird als Übertragungsfunktion bezeichnet.


---

## Einführungsbeispiel Reihenschwingkreis 4/
#### Eingangssignal im Bildbereich

**Aufgabe:** 
Mit den Korrespondenzen soll die Ausgangsspannung nach einem:
1) Spannungsimpuls zur Zeit $t_0$  
2) einem Spannungssprung  der Höhe 1 zur Zeit $t_0$  

--> Kurze Zwischenaufgabe: Benenne die Laplacetransformierten von Dirac-Impuls und Einheitssprung!

---

## Einführungsbeispiel Reihenschwingkreis 5/
#### Eingangssignal im Bildbereich

Eingangssignal festlegen

1) Impuls zut Zeit $t_0$:  $\quad u(t)=δ(t-t_0)$

2) Sprung der Höhe 1  zur Zeit $t_0$:  $\quad u(t)=\hat{F}\,Θ(t-t_0)$

Nötige Korrespondenzen und Eigenschaften

|                                    |     |     |
| -----------------------------------------------| ------------------------------------------------------------------| --------------------------------------------------------|
| Diracsche Deltadistribution Einheitsimpuls   | $\delta(t)\,$     | $1\,$                                        |
| Heavisidesche Sprungfunktion Einheitssprung  | $\Theta(t)\,$                                                     | $\frac{1}{s}$                                           |
| Verschiebung im Originalbereich (bei einse...)  | $f(t-a) \,$                                                       | $e^{-as}F(s) \,$                                                  |
| Linearität                                                                | $a_{1}f_{1}(t)+a_{2} f_{2}(t)\,$                                  | $a_{1}F_{1}(s)+ a_{2} F_{2}(s)\,$                                 |

1) Impuls zut Zeit $t_0$: $\quad U(s)=e^{-t_0s}$

2) Sprung der Höhe 1 zur Zeit $t_0$: $\quad U(s)=\frac{1}{s}e^{-t_0s}$

---

## Einführungsbeispiel Reihenschwingkreis 6/
#### Ausgangssignal

$$Y(s)=\frac{C\,R\,s + 1}{C\,L\,s^2+C\,R\,s+1}\,U(s)$$

##### 1. Impuls zut Zeit $t_0$: $\quad U(s)=e^{-t_0s}$ 

$$Y(s)=\frac{C\,R\,s + 1}{C\,L\,s^2+C\,R\,s+1}\,e^{-t_0s}$$ 

Rücktransformiert in den Zeitbereich ergibt:

$$y(t)=\frac{\theta (t-\text{t0}) e^{-\frac{\left(\sqrt{\text{CR}^2-4 \text{CL}}+\text{CR}\right) (t-\text{t0})}{2 \text{CL}}} \left(\text{CR} \left(\sqrt{\text{CR}^2-4 \text{CL}}-\text{CR}\right) e^{\frac{\sqrt{\text{CR}^2-4 \text{CL}} (t-\text{t0})}{\text{CL}}}+2 \text{CL} \left(e^{\frac{\sqrt{\text{CR}^2-4 \text{CL}} (t-\text{t0})}{\text{CL}}}-1\right)+\text{CR} \left(\sqrt{\text{CR}^2-4 \text{CL}}+\text{CR}\right)\right)}{2 \text{CL} \sqrt{\text{CR}^2-4 \text{CL}}}$$


---

## Einführungsbeispiel Reihenschwingkreis 5/
#### Ausgangssignal

$$Y(s)=\frac{C\,R\,s + 1}{C\,L\,s^2+C\,R\,s+1}\,U(s)$$

##### 2. Sprung der Höhe 1 zur Zeit $t_0$:  $\quad U(s)=\frac{1}{s}e^{-t_0s}$

$$Y(s)=\frac{C\,R\,s + 1}{C\,L\,s^2+C\,R\,s+1}\,\frac{1}{s}e^{-t_0s}$$ 

Rücktransformiert in den Zeitbereich ergibt:

$$y(t)=-\frac{\theta (t-\text{t0}) e^{-\frac{\left(\sqrt{\text{CR}^2-4 \text{CL}}+\text{CR}\right) (t-\text{t0})}{2 \text{CL}}} \left(\text{CR} \left(-e^{\frac{\sqrt{\text{CR}^2-4 \text{CL}} (t-\text{t0})}{\text{CL}}}\right)+\sqrt{\text{CR}^2-4 \text{CL}} \left(e^{\frac{\sqrt{\text{CR}^2-4 \text{CL}} (t-\text{t0})}{\text{CL}}}-2 e^{\frac{\left(\sqrt{\text{CR}^2-4 \text{CL}}+\text{CR}\right) (t-\text{t0})}{2 \text{CL}}}+1\right)+\text{CR}\right)}{2 \sqrt{\text{CR}^2-4 \text{CL}}}$$

---

## Einführungsbeispiel Reihenschwingkreis 6/
#### Ausgangssignal

mit $CR = 0.5$ und $CL=0.2$  sieht so die Sprungantwort aus:

$$y(t) = \theta (t-\text{t0})\left(1+{\rm e}^{-\frac{-5}{4}\,\left(t-t0\right)}\left(\tfrac{\sqrt{55}}{11}\,{\rm sin}\left(\tfrac{\sqrt{55}}{4}\,\left(t-t0\right)\right)-{\rm cos}\left(\tfrac{\sqrt{55}}{4}\,\left(t-t0\right)\right)\right)\right)$$

bzw. gerundet und zusammengefasst:
$$y(t)=\theta (t-\text{t0})\Big(1-{{\rm e}^{- 1.25\,t+ 1.25\,{\it t0}}} \left(\cos \left(  1.86\,t- 1.86\,{\it t0} \right)-  0.674\,\sin \left(  1.86
\,t- 1.86\,{\it t0} \right)\right)\Big)
$$

![](Pasted%20image%2020210206170423.png)

Wolfram Cloud Notebook: 
[[https://www.wolframcloud.com/obj/robert.beckmann/Published/basic_responses.nb]]|



			

--- 
## Die Übertragungsfunktion

![Quelle: [Lunze2016](Lunze2016.md)](Pasted%20image%2020210202222015.png)

- ist eine komplexe Funktion, sie bildet aus dem komplexen Raum in den komplexen Raum ab.
- G(s) wird selten dargestell - man kann es aber tun
- In dem Bild unten wird der Betrag der $|G(s)|$ dargestellt. 
- Typischerweise sieht man man mit der logaritmischen z-Achse mehr

|lineare z-Achse|logarithmische z-Achse|
|---|---|
|![TF1_lin_abs](TF1_lin_abs.png) |![TF1_lin_abs](TF1_lin_log.png)|

---

![TF1_lin_cont](TF1_lin_cont.png)
--> Die Kontourlinien zeigen [0.15, 0.6, 1,2,10,20] von $|G(s)|$. Wie ist die Zuordnung zwischen Linien und Werten?




---

