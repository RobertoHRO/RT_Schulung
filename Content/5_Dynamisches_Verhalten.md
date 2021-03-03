Systemantworten
======================

$\newcommand{\dt}{\frac{{\rm d}}{{\rm d}t}}$ $\newcommand{\dtn}[1]{\frac{{\rm d^#1}}{{\rm d}t^#1}}$
---

### The What
- Wichtige Signale in der Regelungstechnik
- Linearität von Systemen
- Überleitung zur Faltung


### The Why
- Hinführung zur Laplace-Transformation
	- --> Viele Viele Methoden der linearen Regelungstechnik

---

## Wichtige Signale
### Einheitssprung 1(t), θ(t) "theta"
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


### Impulsantwort, Gewichtsfunktion g(t)
Systemantwort aus der Ruhelage in $y(t)=0 \quad \text{für}\; t < 0$ auf einen Dirac-Impuls
**Beispiel** Fahrzeuggeschwindigkeit:
 $$\dt v(t)  =- \frac{b}{m}\cdot v(t)+  \frac{\delta(t)}{m} \quad \rightarrow \quad y(t)=g(t)={\frac {1}{m}{{\rm e}^{-{\frac {tb}{m}}}}}$$ 
 
![](Fahrzeuggeschwindigkeit%20Impulsantwort.png)

 ---
 
 
## Superposition

[Superposition lt. Wikipedia:](https://en.wikipedia.org/wiki/Superposition_principle)
A function $F(x)$ that satisfies the superposition principle is called
a linear function. Superposition can be defined by two simpler
properties; additivity and homogeneity

$F(x_1+x_2)=F(x_1)+F(x_2) \,$ **Additivity**

$F(a x)=a F(x) \,$ **Homogeneity**


![](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Anas_platyrhynchos_with_ducklings_reflecting_water.jpg/220px-Anas_platyrhynchos_with_ducklings_reflecting_water.jpg)

----

##   Lineare Systeme – 
**Ein System ist linear, wenn das Superpositionsprinzip erfüllt ist.**
$$
\begin{gather}
α_1\,u_1(t)\longrightarrow\!\boxed{\Large \text{lin. Sys}}\!\longrightarrow α_1\,y_1(t)\\
α_2\,u_2(t)\!\longrightarrow\!\boxed{\Large \text{lin. Sys}}\!\longrightarrow\!α_1\,y_2(t)
\end{gather}$$

$$
\begin{gather}
α_1\,u_1(t) + α_2\,u_2(t) \longrightarrow\!\boxed{\Large \text{lin. Sys}}\!\longrightarrow α_1\,y_1(t)+α_2\,y_2(t)
\end{gather}$$

---

##  Beispiel Superposition
System beschrieben durch lineare DGL 1. Ordnung  $\dt y(t) + k\,y(t)=u(t)$

| System 1 | System 2 |
|-|-|
|$\dt y_1(t) + k\,y_1(t)=u_1(t)$|$\dt y_2(t) + k\,y_2(t)=u_2(t)$|

Überlagerung:
- Eingang: $u(t)=α_1\,u_1(t) + α_2\,u_2(t)$
- Ausgang: $y(t)=α_1\,y_1(t) + α_2\,y_2(t)$ und $\dt y(t)=α_1\,\dt y_1(t) + α_2\,\dt y_2(t)$

---

##  Beispiel Superposition
I. Ausgang ableiten
$$\dt y(t)=α_1\,\dt y_1(t) + α_2\,\dt y_2(t)$$
II. Einzelantworten einsetzen
$$\dt y(t)=α_1\,\left(-k\,y_1(t)+u_1(t)\right) + α_2\,\left( -k\,y_2(t)+u_2(t)\right)$$
III. Erwartbare Gesamtantwort einsetzen
$$-k\,y(t)+u(t)=α_1\,\left(-k\,y_1(t)+u_1(t)\right) + α_2\,\left( -k\,y_2(t)+u_2(t)\right)$$
IV. Überlagerung der Eingänge einsetzen
$$-k\,\left(α_1\,y_1(t) + α_2\,y_2(t)\right)+α_1\,u_1(t) + α_2\,u_2(t)=α_1\,\left(-k\,y_1(t)+u_1(t)\right) + α_2\,\left( -k\,y_2(t)+u_2(t)\right)$$
fertig!  --> Warum ist die Linearität so eine wichtige Eigenschaft?

---

## Ausblendeigenschaft 1/2
Die Ausblendeigenschaft des Dirac-Impulses brauchen wir später - deswegen hier die Herleitung.

Es wird das Integral analysiert:
 $$\int_{-\infty}^{+\infty}f(t)\delta(t){\rm d}t$$

Wir ersetzen $\delta(t)$ durch einen Rechteckimpuls: 
$$x(t)=\begin{cases}\frac{1}{T_0} & 0\leq t< T_0\\0 & \textsf{sonst}\end{cases}$$ 
Es ergibt sich:
$$\begin{align}\int_{0}^{T_0}f(t)\frac{1}{T_0}{\rm d}t &= \frac{1}{T_0}\int_{0}^{T_0}f(t){\rm d}t\\
  &=\frac{F(T_0)-F(0)}{T0}\\
\end{align}
$$

---

 ## Ausblendeigenschaft 2/2
Die Rechteckbreite $T_0$ wird reduziert $T_0\rightarrow 0$:
$$\lim_{T_0\rightarrow 0}\left(\frac{F(T_0)-F(0)}{T0}\right)=f(0)\qquad\textsf{es folgt:}\qquad
\int_{-\infty}^{+\infty}f(t)\delta(t){\rm d}t = f(0)$$

Für verschobene Dirac-Impulse gilt:
$$\int_{-\infty}^{+\infty}f(t)\delta(t-τ){\rm d}t = f(τ) \qquad \textsf{wechsel\;} t \textsf{\;und\;} τ \qquad \boxed{\int_{-\infty}^{+\infty}f(τ)\delta(τ-t){\rm d}τ = f(t)} $$
   

Das ist die Ausblendeigenschaft in der benötigten Form.

 ---
 
## Übergang zur Faltung
Einführung Schreibweise nach: [^Girod2003]
$$
u(t) \longrightarrow\!\boxed{\Large \text{lin. Sys }\mathcal{S}}\!\longrightarrow y(t) \qquad \text{wird zu} \qquad y(t) = \mathcal{S}\left\{u(t)\right\}
$$
Für den Spezialfall Gewichtsfunktion: $g(t) = \mathcal{S}\left\{δ(t)\right\}$
Mit der Ausblendeigenschaft des Dirc-Impulses: $$u(t)=\!\int\limits_{-\infty}^{+\infty}\!u(τ)\cdot δ(t-τ) {\rm d}τ \quad\textsf{kann man schreiben:}\quad y(t) = \mathcal{S}\left\{\int\limits_{-\infty}^{+\infty}\!u(τ)\cdot δ(t-τ) {\rm d}τ\right\}$$
Im Integral hängt nur $δ(t-τ)$ von $t$ ab; die Werte $u(τ)$ sind bezüglich $t$ nur Gewichtsfaktoren. Wegen der Linearität des Systems gilt daher
$$y(t) = \int\limits_{-\infty}^{+\infty}\!u(τ)\cdot \mathcal{S}\left\{δ(t-τ)\right\} {\rm d}τ\qquad \Large{⇨}\normalsize \qquad \boxed{y(t) = \int\limits_{-\infty}^{+\infty}\!u(τ)\cdot g(t-τ) {\rm d}τ}$$

[^Girod2003]: Girod, Bernd: "Einführung in die Systemtheorie: Signale und Systeme in der Elektrotechnik und Informationstechnik"; 2003; DOI: 10.1007/978-3-322-99346-5; ISBN: 978-3-322-99346-5


---
## Übergang zur Faltung
Wenn für den Eingang für  $t<0$ das gilt: $u(t)=0$, halbiert sich der Integrationsaufwand:
$$
y(t)=\!\int\limits_{0}^{+\infty}\!u(τ)\cdot g(t-τ) {\rm d}τ
$$

Noch einfacher wird es, wenn für $t<0$ die Gewichtfunktion null ist: $g(t)=0$. In diesem Fall spricht man von kausalen Systemen ([Kausalität](https://de.wikipedia.org/wiki/Systemtheorie_(Ingenieurwissenschaften)#Kausale_Systeme)) und die Faltung reduziert sich auf:
$$
\boxed{y(t)=\!\int\limits_{0}^{t}\!u(τ)\cdot g(t-τ) {\rm d}τ}
$$


---

## Beispiel für die Überlagerung
### Rechteck am Fahrzeugmodell: 
$$u(t)=\begin{cases}1 & 100\leq t< 300\\0 & \textsf{sonst}\end{cases}$$ 

|Eingang | Ausgang|
|---|---|
|![super_const_200_u](super_const_200_u.png) | ![super_const_200_y](super_const_200_y.png) |

$$y(t)=\tfrac{θ(t-100)}{50}\left(1-{\rm e}^{\frac{t-100}{20}}\right) - \tfrac{θ(t-300)}{50}\left(1-{\rm e}^{\frac{t-300}{20}}\right)$$

---

## Beispiel für die Überlagerung
### Schmaler rechteckförmiger Impuls

|Eingang | Ausgang|
|---|---|
|![super_const_200_u](super_const_5_u.png) | ![super_const_200_y](super_const_5_y.png) |

$$y(t)=\tfrac{θ(t-100)}{50}\left(1-{\rm e}^{\frac{t-100}{20}}\right) - \tfrac{θ(t-105)}{50}\left(1-{\rm e}^{\frac{t-105}{20}}\right)$$

---

## Beispiel für die Überlagerung
### Approximationen 1/

|Eingang | Ausgang|
|---|---|
|![super_ramp_100_u](super_ramp_100_u.png) | ![super_ramp_100_y](super_ramp_100_y.png) |

$$
\begin{split}
y(t)=&\tfrac{θ(t-200)}{5}\left(1-{\rm e}^{\frac{t-200}{20}}\right) - \tfrac{θ(t-300)}{5}\left(1-{\rm e}^{\frac{t-300}{20}}\right)\\
+&\tfrac{θ(t-300)}{2.5}\left(1-{\rm e}^{\frac{t-300}{20}}\right) - \tfrac{θ(t-400)}{2.5}\left(1-{\rm e}^{\frac{t-400}{20}}\right)
\end{split}
$$

zusammengefasst:
$$
y(t)=\tfrac{θ(t-200)}{5}\left(1-{\rm e}^{\frac{t-200}{20}}\right)+\tfrac{θ(t-300)}{5}\left(1-{\rm e}^{\frac{t-300}{20}}\right) - \tfrac{θ(t-400)}{2.5}\left(1-{\rm e}^{\frac{t-400}{20}}\right)
$$

---
## Beispiel für die Überlagerung
### Approximationen 2/

|Eingang | Ausgang|
|---|---|
|![super_triang_50_u](super_triang_50_u.png) | ![super_triang_50_u](super_triang_50_y.png) |

---
## Beispiel für die Überlagerung
### Approximationen 3/

|Eingang | Ausgang|
|---|---|
|![super_sin_25_u](super_sin_25_u.png) | ![super_sin_25_y](super_sin_25_y.png) |

---

## Beispiel für die Überlagerung
### Approximationen 4/

|Eingang | Ausgang|
|---|---|
|![super_sin_5_u](super_sin_5_u.png) | ![super_sin_5_y](super_sin_5_y.png) |

---



### Hinweise

- Die Impulsantwort g(t) charakterisiert ein lineares zeitinvariantes System vollständig.
- Bei linearen Systemen ist die Impulsantwort g(t) die zeitliche Ableitung der Sprungantwort h(t). 
