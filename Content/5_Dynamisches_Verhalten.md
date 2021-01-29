Systemantworten
======================

$\newcommand{\dt}{\frac{{\rm d}}{{\rm d}t}}$ $\newcommand{\dtn}[1]{\frac{{\rm d^#1}}{{\rm d}t^#1}}$
---
## Motivation

**Ziel:** Herleitung von Analysemethoden für lineare Systeme, die eine qualitative, bzw. approximative Beschreibung des dynamischen Verhaltens erlauben.   

- Welche Systemeigenschaften führen zu welchem dynamischen Verhalten?
- Wie kann man Systemeigenschaften und dadurch dynamisches Verhalten durch Regelung beeinflussen?

Für genaue quantitative Wiedergabe des dynamischen Verhaltens verwenden wir meist numerische Methoden (Simulation).

Wir behandeln Untersuchungen des dynamischen Verhaltens im
- Laplace Bereich (s-Ebene)
- Frequenzbereich (Frequenzgang)
- Zustandsraum

---
## Wichtige Signale
### Einheitssprung 1(t)
$$\begin{align}
u(t)&=1(t)\\
u(t)&=\begin{cases}0 & t<0\\ 
undefined & t = 0 \\
1 &t>0\end{cases}
\end{align}$$
### Sprungantwort h(t)
Systemantwort aus der Ruhelage in $y(t)=0 \quad ∀\; t < 0$ auf einen Einheitssprung
**Beispiel** Fahrzeuggeschwindigkeit:
 $$\dt v(t)  =- \frac{b}{m}\cdot v(t)+  \frac{1(t)}{m} \quad \rightarrow \quad y(t)=h(t)={\frac {1}{b} \left( -{{\rm e}^{-{\frac {bt}{m}}}}+1 \right) }$$ 
 
 ![](Fahrzeuggeschwindigkeit%20Sprungantwort.png)

 --- 
 
## Wichtige Signale
### Dirac-Impuls δ(t)
Impuls mit unendlichem Augenblickswert in verschwindend geringer Zeit und der Fläche 1
$$ \delta(t) = \begin{cases} +\infty, & t = 0 \\ 0, & t \ne 0 \end{cases} \qquad \int_{-\infty}^{+\infty}\delta(t){\rm d}t = 1$$


### Impulsantwort g(t)
Systemantwort aus der Ruhelage in $y(t)=0 \quad \text{für}\; t < 0$ auf einen Dirac-Impuls
**Beispiel** Fahrzeuggeschwindigkeit:
 $$\dt v(t)  =- \frac{b}{m}\cdot v(t)+  \frac{\delta(t)}{m} \quad \rightarrow \quad y(t)=g(t)={\frac {1}{m}{{\rm e}^{-{\frac {tb}{m}}}}}$$ 
 
![](Fahrzeuggeschwindigkeit%20Impulsantwort.png)
 
----

##   Lineare Systeme – Superposition
**Ein System ist linear, wenn das Superpositionsprinzip erfüllt ist.**
$$
\begin{gather}
u_1(t)\longrightarrow\!\boxed{\Large \text{lin. Sys}}\!\longrightarrow y_1(t)\\
u_2(t)\!\longrightarrow\!\boxed{\Large \text{lin. Sys}}\!\longrightarrow\!y_2(t)
\end{gather}$$

$$
\begin{gather}
u_1(t) + u_2(t) \longrightarrow\!\boxed{\Large \text{lin. Sys}}\!\longrightarrow y_1(t)+y_2(t)
\end{gather}$$

---

##  Beispiel Superposition

System beschrieben durch lineare DGL 1. Ordnung  $\dt y(t) + k\,y(t)=u(t)$

System 1 | System 2
-|-
$\dt y_1(t) + k\,y_1(t)=u_1(t)$|$\dt y_2(t) + k\,y_2(t)=u_2(t)$

Überlagerung:
- Eingang: $u(t)=\alpha_1\,u_1(t) + \alpha_2\,u_2(t)$
- Ausgang: $y=\alpha_1\,y_1(t) + \alpha_2\,y_2(t)$ und $\dt y(t)=\alpha_1\,\dt y_1(t) + \alpha_2\,\dt y_2(t)$

$$\begin{gather}
\dt y(t)=\alpha_1\,\dt y_1(t) + \alpha_2\,\dt y_2(t)\\[16pt]
\dt y(t)=\alpha_1\,\left(-k\,y_1(t)+u_1(t)\right) + \alpha_2\,\left( -k\,y_2(t)+u_2(t)\right)\\[16pt]
-k\,y(t)+u(t)=\alpha_1\,\left(-k\,y_1(t)+u_1(t)\right) + \alpha_2\,\left( -k\,y_2(t)+u_2(t)\right)\\[16pt]
-k\,\left(\alpha_1\,y_1(t) + \alpha_2\,y_2(t)\right)+\alpha_1\,u_1(t) + \alpha_2\,u_2(t)=\alpha_1\,\left(-k\,y_1(t)+u_1(t)\right) + \alpha_2\,\left( -k\,y_2(t)+u_2(t)\right)
\end{gather}$$

--> Warum ist die Linearität so eine wichtige Eigenschaft?

---

## Beispiel für die Überlagerung
**Fahrzeugbeispiel** [Schnell mal die Impulsantwort berechnen](https://www.wolframalpha.com/input/?i=v%27+%2B+b%2Fm*v+%3D+Dirac%28t-10%29%2Fm%2C+v%280%29%3D0)
- Eingang: $\quad\Large u(t) = \delta(t-τ)$
- Systemausgang entspricht der um τ verschobenen Impulsantwort/Gewichtsfunktion:  

$$\quad\Large y(t) = \frac{1(t - τ)}{1000}\cdot e^{-\frac{1}{20}(t-τ)}$$


Eingang | Ausgang|Big Picture
---|---|---
![](Pasted%20image%2020210119195631.png) |![](Pasted%20image%2020210119195651.png)|![](Pasted%20image%2020210119195721.png)


---
## Beispiel für die Überlagerung
Eingang | Ausgang|Big Picture
---|---|--
![](Pasted%20image%2020210119195846.png)|![](Pasted%20image%2020210119195854.png)|![](Pasted%20image%2020210119195908.png)
![](Pasted%20image%2020210119200654.png)|![](Pasted%20image%2020210119200704.png)|![](Pasted%20image%2020210119200712.png)
![](Pasted%20image%2020210119200814.png)|![](Pasted%20image%2020210119200832.png)|![](Pasted%20image%2020210119200843.png)

---
## Übergang zur Faltung
Über Faltungsintegral kann der Ausgang y(t) für beliebige Eingangssignale u(t) und der Impulsantwort/Gewichtsfunktion berechnet werden.
$$
y(t)=\!\int\limits_{-\infty}^{+\infty}\!g(τ)\cdot u(t-τ) {\rm d}τ
$$

Wenn $u(t)<0$ für $t<0$:
$$
y(t)=\!\int\limits_{0}^{+\infty}\!g(τ)\cdot u(t-τ) {\rm d}τ
$$

Wenn $g(t)<0$ für $t<0$ ([Kausalität](https://de.wikipedia.org/wiki/Systemtheorie_(Ingenieurwissenschaften)#Kausale_Systeme)):
$$
y(t)=\!\int\limits_{0}^{t}\!g(τ)\cdot u(t-τ) {\rm d}τ
$$

---

### Hinweise
- Bisherige Methoden würden sehr viel "Integrationsarbeit" erfordern. 
- ==Ausgänge können auch mit DLG berechnet werden==
- Die Impulsantwort g(t) charakterisiert ein lineares zeitinvariantes System vollständig.
- Bei linearen Systemen ist die Impulsantwort g(t) die zeitliche Ableitung der Sprungantwort h(t). 
