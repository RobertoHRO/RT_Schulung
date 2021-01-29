Erster Regler
==========
---

## Regelkreise
### Zweck von Regelungen
* **Festwertregelung** - Kompensation von Störungen z.B.
	- Anfangswerte
	- Umwelteinwirkungen
	- Modellunsicherheiten

* **Folgereglung** - Streckenausgänge folgen Führungsgrößen (Sollwerten)
* **Änderung der Streckendynamik** 
	- Stabilisierung der Regelstrecke
	-  Steigerung der Streckenperformance 

Regelsysteme erfüllen meist mehrere Zwecke.

---- 

## Regelkreise
### Bestandteile von Regelungen
**Regelstrecke:**  
Erzeugt aus den Stellgrößen die Regelgrößen.

**Abgleich der Regelgrößen mit den Führungsgrößen**
Berechnet aus den Führungsgrößen und den Regelgrößen die Regelabweichungen.

**Regeleinrichtung** 
Berechnet aus den Regelabweichungen die Stellgrößen.

### Blockschaltbild einschleifiger Regelkreis
![Der einschleifige Regelkreis Quelle: [Lunze2016](Lunze2016.md)](Regelkreis.png)

---
## Beispiel Dusche

![Dusche als Regelaufgabe|500](Dusche.svg)

---

## Beispiel 1: Geschwindigkeitsregelung 1/
Aufgabe: Fahrzeuggeschwindigkeit $y(t)$ soll einer zeitvariablen Führungsgröße $w(t)$ folgen.

- Wechsel der Symbole: 

$$\tfrac{d}{d\,t}v(t)  = - \frac{b}{m} v(t) + \frac{F_u}{m}$$  |![](Bilder_RT_3.svg)
---|---
$$\tfrac{d}{d\,t}y(t) = -\frac{b}{m} y(t) + \frac{u(t)}{m}$$ | ![](Bilder_RT_4.svg)

- Regelabweichung: $e(t) = w(t)-y(t)$
- Regeleinrichtung: $u(t) = K \cdot e(t)$
	- Verstärkung $K$ legt fest wie intensiv auf Regelabweichungen reagiert wird. 
 
 ---
 
 ## Beispiel 1: Geschwindigkeitsregelung 2/
 $$
\begin{eqnarray}
\tfrac{d}{d\,t}y(t) = -\frac{b}{m}\, y(t) + \frac{K}{m}\left(w(t)-y(t)\right)
\end{eqnarray}
 $$
 
  $$
\begin{eqnarray}
\tfrac{d}{d\,t}y(t)  = -\frac{b+K}{m}\, y(t)+\frac{K}{m}\,w(t)
\end{eqnarray}
 $$
 
 Lösung für $y(0)=5$ und $w(t)=8$:
$$y \left( t \right) ={w\cdot\frac {K}{b+K}}+{{\rm e}^{-{\frac { \left( b+K\right) t}{m}}}} \left( {\it y_0}-{w\cdot\frac {K}{b+K}} \right) 
$$ 

$K=500$|$K=1000$|$K=2000$
---|---|---
$y(t)=7.27- 2.27\,{{\rm e}^{- 0.550\,t}}$| y(t)=$7.62- 2.62\,{{\rm e}^{- 1.05\,t}}$ | $y(t)=7.80- 2.80\,{{\rm e}^{- 2.05\,t}}$
![Fahrzeuggeschwindigkeit für verschiedene Verstärkungen des P-Reglers](Fahrzeuggeschwindigkeiten%20mit%20P%20Regler.png) 

- Verstärkung wirkt auf Dynamik und Statik 
- Es bleibt aber immer eine bleibende Regelabweichung - Das ist charakteristisch für proportinale Regler an proportionalen Regelstrecken

**Aufgabe:**  Berechne und zeichne die Stellgrößen für die drei Verstärkungen.

---

## Beispiel 1: Geschwindigkeitsregelung 3/
Ergänzung eines Integrators in der  Regeleinrichtung: 
$$u(t) = K_P \cdot e(t) + K_I \cdot \int e(t)\,dt$$

- Jetzt wird die Stellgröße angepasst, bis die Regelabweichung verschwindet.
- Der Integrator ist ein weiterer (System)-Zustand. 
- Blockschaltbild: ![](PI-Regler.svg)
---

## Beispiel 1: Geschwindigkeitsregelung 4/
Aufstellen der Differentialgleichung 2. Ordnung:
1. Neuen Zustand einführen: $$
\begin{eqnarray}
\frac {\rm d}{{\rm d}t}x_1 \left( t \right)  &=& e(t)\\
u(t) &=& K_P \cdot e(t) + K_I \cdot x_1(t)
\end{eqnarray}
$$
2. Alle Gleichungen aufschreiben (Systemordnung steigt von $n=1$ auf $n=2$):
$$
\begin {eqnarray} 
{\frac {\rm d}{{\rm d}t}}y \left( t \right) 
&=&-{\frac {by \left( t \right) }{m}}+{\frac {u \left( t \right) }{m}}\\ 
{\frac {\rm d}{{\rm d}t}}{\it x1} \left( t \right) &=&e \left( t \right)\\
u \left( t \right) &=&K_{I}\,{\it x1} \left( t
 \right) +K_{P}\,e \left( t \right) \\ 
 e \left( t \right) &=&w \left( t \right) -y \left( t \right) \\ 
\end {eqnarray}
$$
3. Erste Gleichung ableiten, die übrigen einsetzen, umstellen,   --> fertig 😁
$${\frac {{\rm d}^{2}}{{\rm d}{t}^{2}}}y \left( t \right)\, m +  {\frac {\rm d}{{\rm d}t}}y \left( t \right) \, \left( K_{P}+b \right)  + y \left( t \right)\,K_{I} = K_{P}\,{\frac {\rm d}{{\rm d}t}}w \left( t \right) +K_{I}\,w \left( t \right)$$

---

## Beispiel 1: Geschwindigkeitsregelung 5/
$${\frac {{\rm d}^{2}}{{\rm d}{t}^{2}}}y \left( t \right)\, m +  {\frac {\rm d}{{\rm d}t}}y \left( t \right) \, \left( K_{P}+b \right)  + y \left( t \right)\,K_{I} = K_{P}\,{\frac {\rm d}{{\rm d}t}}w \left( t \right) +K_{I}\,w \left( t \right)$$

Lösung für $b = 50$, $m = 1000$  $y(0) = 5$, $y'(0) = 0$ ,$$ w \left( t \right) =
\cases{5&$t<0$\cr {\it undefined}&$t=0$\cr 8&$0<t$\cr}$$


$K_P = 500$ , $K_I = 200$|$K_P = 500$ , $K_I = 100$
---|---
![](Fahrzeug_Regel_200.png) |![](Fahrzeug_Regel_100.png)
![](Fahrzeug_Stell_200.png) |![](Fahrzeug_Stell_100.png)
$$\begin{align}u(t) = &400.0+ 620.0\,{{\rm e}^{- 0.28\,t}}\sin \left(  0.35\,t \right) \\&+ 1400.0\,{{\rm e}^{- 0.28\,t}}\cos \left(  0.35\,t \right)\end{align}$$ | $$\begin{align}u(t)=&400.0- 500.0\,{{\rm e}^{- 0.28\,t}}\sin \left(  0.16\,t \right) \\&+1400.0\,{{\rm e}^{- 0.28\,t}}\cos \left(  0.16\,t \right)\end{align}$$

----

## Beispiel 1: Geschwindigkeitsregelung 6/
- Gleiches Ein-/Ausgangsverhalten kann durch andere Strukturen erreicht werden

**Vorsteuerung:** 
![](Bilder_RT_5.svg)

Die DGL: $${\frac {{\rm d}^{2}}{{\rm d}{t}^{2}}}u \left( t \right)\,m + {\frac {\rm d}{{\rm d}t}}u \left( t \right) \, \left( K_{P}+b \right) +u \left( t \right)\,K_{I}= {\frac {{\rm d}^{2}}{{\rm d}{t}^{2}}}w \left( t \right)\,K_{P}\,m + {\frac {\rm d}{{\rm d}t}}w \left( t \right) \, \left( K_{I}\,m+K_{P}\,b \right) + w \left( t \right)\,K_{I}\,b
$$ erzeugt aus der Führungsgröße $$ w \left( t \right) =
\cases{5&$t<0$\cr {\it undefined}&$t=0$\cr 8&$0<t$\cr}$$ und passenden Anfangsbedingungen die gleichen Stellgrößen $u(t)$ wie der Regelkreis.


