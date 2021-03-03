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

**Aufgabe:**  Berechne die Ausgangsspannung nach einem:
1) Spannungsimpuls zur Zeit $t_0$  
2) Spannungssprung  der Höhe 1 zur Zeit $t_0$  


---
## Einführungsbeispiel Reihenschwingkreis 2/
#### Transformation des Systems in den Bildbereich
Differentialgleichung im Zeitbereich:
$$
\begin{eqnarray}
C\,L\frac{d^2}{dt^2}y(t)+C\,R\frac{d}{dt}y(t)+y(t) &=& C\,R\frac{d}{dt}u(t)+u(t)
\end{eqnarray}
$$
Nötige Korrespondenzen und Eigenschaften:

|                                                                                   | Originalfunktion   | Bildfunktion         |
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
#### Transformation des Systems in den Bildbereich
Umformen
$$
\begin{eqnarray}
C\,L\,s^2\,Y(s)+C\,R\,s\,Y(s)+Y(s) &=& C\,R\,s\,U(s) + U(s) \\[1ex]
\big(C\,L\,s^2+C\,R\,s+1\big)Y(s) &=& \big(C\,R\,s + 1\big)\,U(s)
\end{eqnarray}
$$

$$Y(s)=\underbrace{\frac{C\,R\,s + 1}{C\,L\,s^2+C\,R\,s+1}}_{\huge G(s)}\,U(s)$$

$G(s)$ wird als Übertragungsfunktion bezeichnet.


---

## Einführungsbeispiel Reihenschwingkreis 4/
#### Eingangssignal im Bildbereich

**Aufgabe:**  Berechne die Ausgangsspannung nach einem:
1) Spannungsimpuls zur Zeit $t_0$  
2) Spannungssprung  der Höhe 1 zur Zeit $t_0$  

--> Kurze Zwischenaufgabe: Benenne die Laplacetransformierten von Dirac-Impuls und Einheitssprung!

---

## Einführungsbeispiel Reihenschwingkreis 5/
#### Eingangssignal im Bildbereich

Eingangssignal festlegen

1) Impuls zut Zeit $t_0$:  $\quad u(t)=δ(t-t_0)$

2) Sprung der Höhe 1  zur Zeit $t_0$:  $\quad u(t)=Θ(t-t_0)$

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

$$\tiny y(t)=\frac{\theta (t-\text{t0}) e^{-\frac{\left(\sqrt{\text{CR}^2-4 \text{CL}}+\text{CR}\right) (t-\text{t0})}{2 \text{CL}}} \left(\text{CR} \left(\sqrt{\text{CR}^2-4 \text{CL}}-\text{CR}\right) e^{\frac{\sqrt{\text{CR}^2-4 \text{CL}} (t-\text{t0})}{\text{CL}}}+2 \text{CL} \left(e^{\frac{\sqrt{\text{CR}^2-4 \text{CL}} (t-\text{t0})}{\text{CL}}}-1\right)+\text{CR} \left(\sqrt{\text{CR}^2-4 \text{CL}}+\text{CR}\right)\right)}{2 \text{CL} \sqrt{\text{CR}^2-4 \text{CL}}}$$


---

## Einführungsbeispiel Reihenschwingkreis 7/
#### Ausgangssignal

$$Y(s)=\frac{C\,R\,s + 1}{C\,L\,s^2+C\,R\,s+1}\,U(s)$$

##### 2. Sprung der Höhe 1 zur Zeit $t_0$:  $\quad U(s)=\frac{1}{s}e^{-t_0s}$

$$Y(s)=\frac{C\,R\,s + 1}{C\,L\,s^2+C\,R\,s+1}\,\frac{1}{s}e^{-t_0s}$$ 

Rücktransformiert in den Zeitbereich ergibt:

$$\tiny y(t)=-\frac{\theta (t-\text{t0}) e^{-\frac{\left(\sqrt{\text{CR}^2-4 \text{CL}}+\text{CR}\right) (t-\text{t0})}{2 \text{CL}}} \left(\text{CR} \left(-e^{\frac{\sqrt{\text{CR}^2-4 \text{CL}} (t-\text{t0})}{\text{CL}}}\right)+\sqrt{\text{CR}^2-4 \text{CL}} \left(e^{\frac{\sqrt{\text{CR}^2-4 \text{CL}} (t-\text{t0})}{\text{CL}}}-2 e^{\frac{\left(\sqrt{\text{CR}^2-4 \text{CL}}+\text{CR}\right) (t-\text{t0})}{2 \text{CL}}}+1\right)+\text{CR}\right)}{2 \sqrt{\text{CR}^2-4 \text{CL}}}$$

---

## Einführungsbeispiel Reihenschwingkreis 8/
#### Ausgangssignal

mit $CR = 0.5$ und $CL=0.2$  sieht so die Sprungantwort aus:

$$y(t) = \theta (t-\text{t0})\left(1+{\rm e}^{-\frac{-5}{4}\,\left(t-t0\right)}\left(\tfrac{\sqrt{55}}{11}\,{\rm sin}\left(\tfrac{\sqrt{55}}{4}\,\left(t-t0\right)\right)-{\rm cos}\left(\tfrac{\sqrt{55}}{4}\,\left(t-t0\right)\right)\right)\right)$$

bzw. gerundet und zusammengefasst:
$$y(t)=\theta (t-\text{t0})\Big(1-{{\rm e}^{- 1.25\,t+ 1.25\,{\it t0}}} \left(\cos \left(  1.86\,(t- {\it t0}) \right)-  0.674\,\sin \left(  1.86
\,(t-{\it t0}) \right)\right)\Big)
$$

![\|300](Pasted%20image%2020210206170423.png)

Wolfram Cloud Notebook: 
[[https://www.wolframcloud.com/obj/robert.beckmann/Published/basic_responses.nb]]|



			

--- 
## Die Übertragungsfunktion
Im Beispiel wurde die Übertragungsfunktion $G(s)$ benannt:
$$Y(s)=\underbrace{\frac{C\,R\,s + 1}{C\,L\,s^2+C\,R\,s+1}}_{\huge G(s)}\,U(s)$$

Allgemein ist Sie in [Lunze2016](Lunze2016.md) so definiert:

![Quelle: [Lunze2016](Lunze2016.md)](Pasted%20image%2020210202222015.png)

---

## Die Übertragungsfunktion

- ist eine komplexe gebrochen rationale Funktion, sie bildet aus dem komplexen Raum in den komplexen Raum ab.
- G(s) wird selten dargestellt - man kann es aber tun
- In dem Bild unten wird der Betrag der $|G(s)|$ dargestellt. 
- Typischerweise sieht man mit der logaritmischen z-Achse mehr

|lineare z-Achse|logarithmische z-Achse|
|---|---|
|![TF1_lin_abs](TF1_lin_abs2.png) |![TF1_lin_abs](TF1_lin_log2.png)|


---

## Die Übertragungsfunktion
- Draufsicht (Kontourplot)
![TF1_lin_cont\|400](TF1_lin_cont.png)
--> Die Kontourlinien zeigen [0.15, 0.6, 1, 2, 10, 20] von $|G(s)|$. Wie ist die Zuordnung zwischen Linien und Werten?
- Übertragungsfunktionen sind immer spiegelsymmetrisch zur reellen Achse.

---

## Übertragungsfunktion
### Darstellungen

| Darstellungsform | Notation im Frequenzbereich                                                                                                                |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------| 
| Polynom          | $G(s) = \frac{b_{m}s^{m} + b_{m-1}s^{m-1} + \dotsb + b_{1}s + b_{0}}{a_{n}s^{n} + a_{n-1}s^{n-1} + \dotsb + a_{1}s + a_{0}}$               | 
| Pol-Nullstellen  | $G(s) = k \cdot \frac{(s - s_{0,1})(s - s_{0,2} ) \dotsm (s - s_{0,m})}{(s - s_{1})(s - s_{2} ) \dotsm (s - s_{n} )}$ |
| Zeitkonstanten   | $G(s)=\frac{k}{s^l}\,\frac{\left(T_{0i}\,s+1\right)…\left(T_{0j}^2\,s^2+2\,d_{0j}\,T_{0j}\,s+1\right)}{\left(T_{k}\,s+1\right)…\left(T_{l}^2\,s^2+2\,d_{l}\,T_{l}\,s+1\right)}$ |
| Partialbruch     | $G(s) = \frac {A_1}{s-s_{1}} + \frac {A_2}{s-s_{2}} + \dotsb + \frac {A_n}{s-s_{n}}$                                  |

Die Darstellung in Partialbrüchen ist vor allem für die Rücktransformation in den Zeitbereich geeignet.


---

## Pol-Nullstellen-Form
$$G(s) = k \cdot \frac{(s - s_{0,1})(s - s_{0,2} ) \dotsm (s - s_{0,m})}{(s - s_{1})(s - s_{2} ) \dotsm (s - s_{n} )}$$

| Polstellen    | Nullstellen     | Konstante     |
|------------|-------------------------------|--|
|$s_{1}, …, s_{m}$  | $s_{0,1}, …, s_{0,m}$ | $k$|

- Pol- und Nullstellen können abgelesen werden
- Pol- und Nullstellen haben die Einheit Frequenz ($\tfrac{1}{\mathsf{s}}, \tfrac{1}{\mathsf{min}}$, …)
- "Polüberschuss" bzw "relativer Grad":  $d = n - m$ 
- für reale, technische, realisierbare Systeme gilt immer $d>0$ 
- Implementierung in Matlab, Octave, Python, …
$$\mathtt{G=zpk([s_{0,1}, s_{0,2}, …, s_{0,m}], [s_{1}, s_{2}, …, s_{n}, k])}$$


---
## Pol-Nullstellen-Form
### Beispiel: Reihenschwingkreis

$$G(s)= \frac{C\,R\,s + 1}{C\,L\,s^2+C\,R\,s+1}$$

| C | L | R | F1 | F2 | Sprungantwort |
| - | - | - | -- | -- | -- |
| 1 | 2 | 4 | $\frac{4\,s + 1}{2\,s^2+4\,s+1}$| $2\,\frac{s+\frac{1}{4}}{\left(s+\frac{2-\sqrt{2}}{2}\right)\left(s+\frac{2+\sqrt{2}}{2}\right)}$ | ![RSK_step2\|100](RSK_step1.png) |
| 1 | 1 | 2 | $\frac{2\,s + 1}{s^2+2\,s+1}$| $2\,\frac{s+\frac{1}{2}}{\left(s+1\right)\left(s+1\right)}$ |![RSK_step2\|100](RSK_step2.png) |
| 1 | 2 | 2 | $\frac{2\,s + 1}{2\,s^2+2\,s+1}$| $\frac{s+\frac{1}{2}}{\left(s+\frac{1}{2}+\frac{1}{2}j\right)\left(s+\frac{1}{2}-\frac{1}{2}j\right)}$ | ![RSK_step3\|100](RSK_step3.png)| 




---

## Eigenschaften von Polstellen

Pole und Nullstellen sind also keine spezifischen Kenngrößen der Übertragungsfunktion G(s), sondern beschreiben Eigenschaften des betrachteten Systems Σ.

Die Pole bestimmen die Exponenten der Modi $e^{-s_i\,t}$ und damit die Eigenbewegung und das Übergangsverhalten des Systems.

Haben sämtliche Pole negativen Realteil, so klingt die Eigenbewegung ab; das System ist stabil

Die Pole eines Systems werden ausschließlich durch die physikalischen Wirkprinzipien bestimmt. Sie sind unabhängig von den Angriffspunkten der  
Aktoren und Sensoren.

Die Nullstellen hängen von den Eingriffspunkten des Stellgliedes und des Messgliedes. Dies gilt sowohl für die Anzahl der Nullstellen als auch für deren Wert.

[Zitiert aus Lunze2016](Lunze2016.md)
   
---

## Übertragungsfunktion
      
$$G(s) = \frac{b_{m}s^{m} + b_{m-1}s^{m-1} + \dotsb + b_{1}s + b_{0}}{a_{n}s^{n} + a_{n-1}s^{n-1} + \dotsb + a_{1}s + a_{0}}$$

#### Chrakteristische Gleichung:
$$\overbrace{\underbrace{a_{n}s^{n} + a_{n-1}s^{n-1} + \dotsb + a_{1}s + a_{0}}_\textsf{charakteristisches Polynom}=0}^\textsf{chrakteristische Gleichung}$$


Implementierung in Matlab, Octave, Python, …
$$\mathtt{G=tf([b_{m}, b_{m-1}, …, b_{1}, b_{0}], [a_{n}, a_{n-1}, …, a_{1}, a_{0}])}$$


Bei Realen System gilt immer:  $n \geq m$ 
Begriff Polüberschuss: $d = n-m$ 
 
---


## Übertragungsfunktion
#### Zeitkonstanten - Form   
- i.d.R nur für stabile Systeme angewandt
- reele negative Pol- und Nullstellen werden in Zeitkonstanten überführt: $T_i = \frac{1}{|s_i|}$,   $T_{0i} = \frac{1}{|s_{0i}|}$
- Für Eigenvorgänge gilt damit: $e^{-s_i\,t} = e^{-t/T_i}$
- In der Zeit $t=T_i$ ist der Eigenvorgang auf $\frac{1}{e} = 0.368$ abgeklungen.
 
 
 $$G(s)=\frac{k}{s^l}\,\frac{\left(T_{0i}\,s+1\right)…\left(T_{0j}^2\,s^2+2\,d_{0j}\,T_{0j}\,s+1\right)}{\left(T_{k}\,s+1\right)…\left(T_{l}^2\,s^2+2\,d_{l}\,T_{l}\,s+1\right)}$$
 ---
 
 ## Gekoppelte Systeme
 ### Reihenschaltung $\qquad G_R(s) = G_1(s)\,G_2(s)$
 ![Quelle: Lunze](Lunze_Reihenschaltung.png)
 
 ### Parallelschalrung $\qquad G_R(s) = G_1(s) + G_2(s)$
 ![Quelle: Lunze](Lunze_Parallelschaltung.png)
 
 ### Rückkopplungsschaltung $\qquad G_R(s) = \frac{G_1(s)}{1+ G_1(s)\,G_2(s)}$
 ![Quelle: Lunze](Lunze_R%C3%BCckkopplungsschaltung.png)
 
### Umformregeln für Blockschaltbilder
 ![Quelle: Lunze](Lunze_Umformregeln_BSB.png)
 
 
 ## Der Frequenzgang
 
 ![](Lunze_Frequenzgang.png)