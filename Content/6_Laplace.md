Der Bildbereich
============
### (Laplace Transformation)
---
## Motivation
**Was**
Eine Funktion $f$ wird vom reellen Zeitbereich in eine Funktion $F$ im komplexen Spektralbereich (Frequenzbereich, Bildbereich) überführt.

**Warum**
Im Bildbereich sind bestimmte Berechnungen einfacher - Faltung wird zu Multiplikation!!!1!!!!elf

---

### Vorwärtstransformation
- Sei $f \colon {[0,\infty[}\rightarrow \mathbb{C}$ eine Funktion. Die Laplace-Transformation von $f(t)$ ist durch
$$F(s)
  = \mathcal{L} \left\{f\right\}(s)
  = \int_{0}^{\infty} f(t) e^{-st} \,\mathrm{d}t, \qquad s\in\mathbb{C}$$ 
  definiert, insofern das Integral existiert.   
- Die Funktion $F(s)$ wird Laplace-Transformierte der Funktion $f(t)$ genannt.

---

### Rückwärtstransformation
Die Zeitfunktion $f(t)$ kann durch die Umkehrformel[^1]

$$\mathcal{L}^{-1} \left\{F(s)\right\}
  = \frac{1}{2 \pi \mathrm i} \int_{ \gamma - \mathrm i \infty}^{ \gamma + \mathrm i \infty} e^{st} F(s)\,\mathrm ds
  = \begin{cases}
      f(t) & \text{für } t \geq 0 \\
      0    & \text{für } t < 0
    \end{cases}
  \qquad \text{mit } \gamma > s_0,$$

aus der Spektralfunktion $F(s)$ bestimmt werden, dabei ist $s_0$ der
größte Realteil einer Singularität von $F$.

[^1]: Bronstein, et al.: *Taschenbuch der Mathematik.* 7. Auflage,
    Verlag Harri Deutsch, S. 775, Kap. 15.2.1.1.

---

## Notationen
$$
\newcommand{\laplace}{\circ\hspace{-5pt}-\hspace{-5pt}\bullet}
\newcommand{\Laplace}{\bullet\hspace{-5pt}-\hspace{-5pt}\circ}
$$
- Festlegung: Signale und Syteme im 
	- Originalbereich bekommen Kleinbuchstaben $y(t)$, $u(t)$, $g(t)$
	- Bildbereich bekommen Großbuchstaben $Y(s)$, $U(s)$, $G(s)$
- Verbreitet sind diese Notationen für die Transformationen: $$f(t)\;\laplace\;F(s)$$$$F(s)\;\Laplace\;f(t)$$

BTW: Selbe Notation wird auch für die Fourier-Transformation verwendet:
- $Y(jω)$, $U(jω)$, $G(jω)$ 
- $f(t)\;\laplace\;F(jω)$, $\qquad F(jω)\;\Laplace\;f(t)$

 
---
## Allgemeine Eigenschaften bzw. Operationen
|                                                                                   | Originalfunktion $f(t) = \mathcal{L}^{-1} \left\{ F(s) \right\}$  | Bildfunktion $F(s) = \mathcal{L}\left\{ f(t) \right\}$            |
| ------------------------------------------------------------------------------------------------------------------------| ------------------------------------------------------------------| ------------------------------------------------------------------|
| Linearität                                                                                                            | $a_{1}f_{1}(t)+a_{2} f_{2}(t)\,$                                  | $a_{1}F_{1}(s)+ a_{2} F_{2}(s)\,$                                 |
| Ähnlichkeitssatz                                                                                                        | $f(at) \,$                                                        | $\frac{1}{a} F\left(\frac{s}{a}\right) \qquad (a > 0) \,$         |
| Verschiebung im Originalbereich (bei einseitiger Transformation nur $a > 0 \,$ oder $f(t)=0\,$ $\forall\,$ $t < a \,$)  | $f(t-a) \,$                                                       | $e^{-as}F(s) \,$                                                  |
| Verschiebung im Bildbereich (Dämpfungssatz)                                                                             | $e^{-at}\cdot f(t) \,$                                            | $F(s + a) \qquad (a \in \mathbb{C}) \,$                           |
| Komplexe Konjugation                                                                                                    | $f^*(t) \,$                                                       | $F^*(s^*) \,$                                                     |
| Zeitspiegelung (bei einseitiger Transformation nicht anwendbar!)                                                        | $f(-t) \,$                                                        | $F(-s) \,$                                                        |
| Zeitdehnung ($T \neq 0$; bei einseitiger Transformation nur für $T > 0$)                                                | $f\left(\frac{t}{T}\right) \,$                                    | $T F(s \cdot T) \,$                                               |

---

## Allgemeine Eigenschaften bzw. Operationen 2
|                                                                                   | Originalfunktion $f(t) = \mathcal{L}^{-1} \left\{ F(s) \right\}$  | Bildfunktion $F(s) = \mathcal{L}\left\{ f(t) \right\}$            |
| ------------------------------------------------------------------------------------------------------------------------| ------------------------------------------------------------------| ------------------------------------------------------------------|
| 1\. Ableitung im Originalbereich                                                                                      | $f'(t) \,$                                                        | $sF(s)-f(0) \,$                                                   |
| 2\. Ableitung im Originalbereich                                                                                      | $f''(t) \,$                                                       | $s^{2}F(s)-sf(0)-f'(0) \,$                                        |
| 1\. Ableitung im Bildbereich                                                                                          | $-tf(t) \,$                                                       | $F^\prime (s)\,$                                                  |
| 2\. Ableitung im Bildbereich                                                                                          | $t^{2}f(t) \,$                                                    | $F^{\prime\prime}(s)\,$                                           |
| Integration im Olriginalbereich                                                                                         | $\int_0^t f(u)\,\mathrm du$                                       | $\frac{1}{s} F(s)$                                                |
| Integration im Bildbereich                                                                                              | $\frac{1}{t} f(t)$                                                | $\int_s^{\infty} F(u)\,\mathrm du$                                |
| Faltung / Multiplitkation                                                                                               | $\int_0^t f(u)\,g(t-u)\,\mathrm du$                               | $F(s) \,G(s)$                                                     |
| Periodische Funktion                                                                                                    | $f(t)=f(t+T) \,$                                                  | $\frac{1}{1-e^{-sT}} \int_0^T f(t)\cdot e^{-st}\,\mathrm dt$      |

---

## Allgemeine Eigenschaften bzw. Operationen 3

|                                                                                   | Originalfunktion $f(t) = \mathcal{L}^{-1} \left\{ F(s) \right\}$  | Bildfunktion $F(s) = \mathcal{L}\left\{ f(t) \right\}$            |
| ------------------------------------------------------------------------------------------------------------------------| ------------------------------------------------------------------| ------------------------------------------------------------------|
| [Sinus]-Multiplikation                                                                                                  | $\sin(at)\cdot f(t)\,$                                            | $\frac{1}{2\mathrm i} \cdot (F(s-\mathrm ia) - F(s+\mathrm ia))$  |
| [Cosinus]-Multiplikation                                                                                                | $\cos(at)\cdot f(t)\,$                                            | $\frac{1}{2} \cdot (F(s-\mathrm ia) + F(s+\mathrm ia))$           |
|                                                                                                                         | $\sinh(at)\cdot f(t)\,$                                           | $\frac{1}{2} \cdot (F(s-a) - F(s+a))$                             |
|                                                                                                                         | $\cosh(at)\cdot f(t)\,$                                           | $\frac{1}{2} \cdot (F(s-a) + F(s+a))$                             |


---

## Korrenspondenzen 1

| Funktionsname                                  | Originalfunktion $f(t) = \mathcal{L}^{-1} \left\{ F(s) \right\}$  | Bildfunktion $F(s) = \mathcal{L}\left\{ f(t) \right\}$  |
| -----------------------------------------------| ------------------------------------------------------------------| --------------------------------------------------------|
| Diracsche Deltadistribution Einheitsimpuls   | $\delta(t)\,$ $\frac{\mathrm d^n}{\mathrm dt^n} \delta (t)\,$     | $1\,$ $s^{n}\,$                                         |
| Heavisidesche Sprungfunktion Einheitssprung  | $\Theta(t)\,$                                                     | $\frac{1}{s}$                                           |
| Exponentialfunktion                           | $e^{-at}\,$                                                       | $\frac{1}{s+a}$                                         |
| Exponentialverteilung                        | $1-e^{-at}\,$                                                     | $\frac{a}{s(s+a)}$                                      |
| 1-te Potenz                                  | $t$                                                              | $\frac{1}{s^2}$                                         |
| n-te Potenz                                    | $t^{n}\,$                                                         | ${ n! \over s^{n+1}}$                                   |

---

## Korrenspondenzen 2

| Funktionsname                                  | Originalfunktion $f(t) = \mathcal{L}^{-1} \left\{ F(s) \right\}$  | Bildfunktion $F(s) = \mathcal{L}\left\{ f(t) \right\}$  |
| -----------------------------------------------| ------------------------------------------------------------------| --------------------------------------------------------|
| Potenzreihe                                   | $\sum_{n=0}^{\infty} a_n (t-t_0)^{n}\,$                           | $\sum_{n=0}^{\infty} \frac{a_n n!}{s^{n+1}} e^{-t_0 s}$ |
| Gedämpfte Potenzfunktion                       | $t e^{-at}\,$                                                     | $\frac{1}{(s+a)^2}$                                     |
|                                                | $t^{n} e^{-at}\,$                                                 | $\frac{n!}{(s+a)^{n+1}}$                                |
|                                                | $\frac{t^{n-1}}{(n-1)!} \cdot e^{-at}\,$                          | $(s + a)^{-n}$                                          |
| n-te Wurzel                                  | $\sqrt[n]{t}$                                                     | $s^{-(n+1)/n} \cdot \Gamma\left(1+\frac{1}{n}\right)$   |
| Sinus                                        | $\sin(at) \,$                                                     | $\frac{a}{s^2 +a^2}$                                    |
| Cosinus                                      | $\cos(at) \,$                                                     | $\frac{s}{s^2 +a^2}$                                    |
| Sinus hyperbolicus                           | $\sinh(at) \,$                                                    | $\frac{a}{s^2 -a^2}$                                    |
| Cosinus hyperbolicus                         | $\cosh(at) \,$                                                    | $\frac{s}{s^2 -a^2}$                                    |

---

## Beispiel 1: Fahrzeugmodell 1/ 
- Betrachtet wird das Fahrzeug
![Geschwindigkeitsregelung (Quelle: [[Franklin2015]])|300](Pasted%20image%2020201227100125.png)
mit einer Masse von $m=1000 kg$ einem Reibbeiwert von $b=50 \tfrac{N\cdot s}{m}$ und einer beschleunigenden Kraft von $F_u=500 N$

**Aufgabe:** 
Mit den Korrespondenzen soll die Fahrzeuggeschwindugkeit nach einem:
1) Kraftimpuls zur Zeit $t_0$  
2) einem Kraftsprung  der Höhe $\hat{F}$ zur Zeit $t_0$  

berechnet werden.

----

## Beispiel 1: Fahrzeugmodell 2/ 
#### Systembeschreibung im Bildbereich
Das Fahrzeug folgt im Zeitbereich der Differentialgleichung :
$$\tfrac{d}{d\,t}v(t)  =- \frac{b}{m}\cdot v(t)+  \frac{1}{m}\,u(t)$$

mit der Korrespondenz

|                                                                                   | Originalfunktion | Bildfunktion             |
| ------------------------------------------------------------------------------------------------------------------------| ------------------------------------------------------------------| ------------------------------------------------------------------|
| 1\. Ableitung im Originalbereich                                                                                      | $f'(t) \,$                                                        | $sF(s)-f(0) \,$                                                   |

ergibt sich im Bildbereich diese algebraische Gleichung:
$$s\,V(s) = -\frac{b}{m}\cdot V(s)  +  \frac{1}{m}\,U(s)$$
(Wir nehmen an: $f(0) = 0$)

---

## Beispiel 1: Fahrzeugmodell 3/ 
#### Eingangssignal im Bildbereich

Eingangssignal festlegen

1) Impuls zut Zeit $t_0$:  $\quad u(t)=δ(t-t_0)$

2) Sprung der Höhe $\hat{F}$ zur Zeit $t_0$:  $\quad u(t)=\hat{F}\,Θ(t-t_0)$

| Funktionsname                                  | Originalfunktion   | Bildfunktion   |
| -----------------------------------------------| ------------------------------------------------------------------| --------------------------------------------------------|
| Diracsche Deltadistribution Einheitsimpuls   | $\delta(t)\,$     | $1\,$                                        |
| Heavisidesche Sprungfunktion Einheitssprung  | $\Theta(t)\,$                                                     | $\frac{1}{s}$                                           |
| Verschiebung im Originalbereich (bei einse...)  | $f(t-a) \,$                                                       | $e^{-as}F(s) \,$                                                  |
| Linearität                                                                | $a_{1}f_{1}(t)+a_{2} f_{2}(t)\,$                                  | $a_{1}F_{1}(s)+ a_{2} F_{2}(s)\,$                                 |


1) Impuls zur Zeit $t_0$: $\quad U(s)=e^{-t_0s}$

2) Sprung der Höhe $\hat{F}$ zur Zeit $t_0$: $\quad U(s)=\hat{F}\,\frac{1}{s}e^{-t_0s}$
 
 ----

## Beispiel 1: Fahrzeugmodell 4/ 
#### Ausgangssignal im Bildbereich

1.   System umformen
$$
\begin{gather}
s\,V(s) = -\frac{b}{m}\cdot V(s)  +  \frac{1}{m}\,U(s)\\
s\,V(s) + \frac{b}{m}\cdot V(s) = \frac{1}{m}\,U(s)\\
V(s) \left(s+\frac{b}{m}\right) = \frac{1}{m}\,U(s)\\
V(s) = \frac{\frac{1}{m}}{\left(s+\frac{b}{m}\right)}\,U(s)
\end{gather}
$$

---

## Beispiel 1: Fahrzeugmodell 5/ 
#### Ausgangssignal im Bildbereich

Mit dem Eingangssignal: $\quad U(s)=e^{-t_0s}$
$$
V(s) = \frac{\frac{1}{m}}{\left(s+\frac{b}{m}\right)}\,e^{-t_0s}
$$

| Funktionsname                                  | Originalfunktion   | Bildfunktion   |
| -----------------------------------------------| ------------------------------------------------------------------| --------------------------------------------------------|
| Exponentialfunktion                           | $e^{-at}\,$                                                       | $\frac{1}{s+a}$                                         |
| Verschiebung im Originalbereich (bei einseitiger Transformation nur $a > 0 \,$ oder $f(t)=0\,$ $\forall\,$ $t < a \,$)  | $f(t-a) \,$                                                       | $e^{-as}F(s) \,$                                                  |

Rücktransformiert im Zeitbereich:
$$
v(t) = \frac{1}{m}e^{-\frac{b}{m}(t-t_0)}
$$

----

## Beispiel 1: Fahrzeugmodell 6/ 
### Ausgangssignal im Bildbereich

Mit dem Eingangssignal: $\quad U(s)=\hat{F}\,\frac{1}{s}e^{-t_0s}$
$$
V(s) = \frac{\frac{1}{m}}{\left(s+\frac{b}{m}\right)}\,\hat{F}\,\frac{1}{s}e^{-t_0s}
$$

| Funktionsname                                  | Originalfunktion   | Bildfunktion   |
| -----------------------------------------------| ------------------------------------------------------------------| --------------------------------------------------------|
| Exponentialverteilung                        | $1-e^{-at}\,$                                                     | $\frac{a}{s(s+a)}$                                      |
| Verschiebung im Originalbereich (bei einseitiger Transformation nur $a > 0 \,$ oder $f(t)=0\,$ $\forall\,$ $t < a \,$)  | $f(t-a) \,$                                                       | $e^{-as}F(s) \,$                                                  |

Rücktransformiert im Zeitbereich:
$$
v(t) = \frac{\hat{F}}{b}\left(1-e^{-\frac{b}{m}\,(t-t_0)}\right)
$$


---

## Erkenntnisse

 ![Quelle: springer.com\|600](Pasted%20image%2020210131074116.png)

| |Impuls | Sprung |
|----|----|---|
|Eingangssignal|$u(t)=δ(t-t_0)$|$u(t)=Θ(t-t_0)$|
|Ausgangssignal|$v(t) = \frac{1}{m}e^{-\frac{b}{m}(t-t_0)}$  Impulsantwort |$v(t) = \frac{1}{b}\left(1-e^{-\frac{b}{m}\,(t-t_0)}\right)$ Sprungantwort|

- genau genommen ist die Sprungantwort (i.d.R. $h(t)$) die Reaktion auf den Einheitssprung (Höhe 1,  Zeitpunkt 0)
- Impulsantwort (≙Gewichtsfunktion) (i.d.R. $g(t)$)  ist die zeitliche Ableitung der Sprungantwort

----

## Literatur