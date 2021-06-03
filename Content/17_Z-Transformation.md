Der Bildbereich
============
### (Z-Transformation)
---
## Motivation
**Was**
Ein Signal im diskreten Zeitbereich (Wertefolge) $f(k) = f_k$ wird vom reellen Zeitbereich in eine Z-Transformierte $F(z)$ im komplexen Spektralbereich (Frequenzbereich, Bildbereich) überführt.

**Warum**
Im Bildbereich sind bestimmte Berechnungen einfacher - Faltung wird zu Multiplikation - das gilt auch für Wertefolgen im diskreten Zeitbereich!!!1!!!!elf

---

### Vorwärtstransformation

Sei $f_k \in \mathbb{C}$ eine Wertefolge mit $k\leq 0$. Die  unilaterale z-Transformation ist durch 
$$F(z)=\mathcal{Z}\{f_k\}= \sum_{k=0} ^\infty f_k \cdot z^{-k}$$
definiert.
- Die Summe $F(z)$ wird Z-Transformierte der Wertefolge $f_{k}$ genannt.


---

## Beispiel 1

Die Wertefolge 

| k     | -1  | 0   | 1   | 2   | 3   | ... |
| ----- | --- | --- | --- | --- | --- | --- |
| $f_k$ | 0   | 1   | 0   | 0   | 0   | 0   | 

soll transformiert werden. Hier noch mal die Transformationsglichung:
$$F(z)=\mathcal{Z}\{f_k\}= \sum_{k=0} ^\infty f_k \cdot z^{-k}$$
Ergebnis:
$$F(z) = 1\cdot z^{0} + 0\cdot z^{-1} + 0\cdot z^{-2} + 0\cdot z^{-3} + .. = 1$$

---

## Beispiel 2

Die Wertefolge 

| k     | -1  | 0   | 1   | 2   | 3   | ... |
| ----- | --- | --- | --- | --- | --- | --- |
| $f_k$ | 0   | 0   | 1   | 0   | 0   | 0   | 

soll transformiert werden. Hier noch mal die Transformationsglichung:
$$F(z)=\mathcal{Z}\{f_k\}= \sum_{k=0} ^\infty f_k \cdot z^{-k}$$
Ergebnis:
$$F(z) = 0\cdot z^{0} + 1\cdot z^{-1} + 0\cdot z^{-2} + 0\cdot z^{-3} + .. = \frac 1 z$$

---

## Beispiel 3

Die Wertefolge 

| k     | -1  | 0   | 1   | 2   | 3   | ... |
| ----- | --- | --- | --- | --- | --- | --- |
| $f_k$ | 0   | 1   | 1   | 1   | 1   | 1   | 

soll transformiert werden. Hier noch mal die Transformationsglichung:
$$F(z)=\mathcal{Z}\{f_k\}= \sum_{k=0} ^\infty f_k \cdot z^{-k}$$
Ergebnis:
$$F(z) = 1\cdot z^{-0} + 1\cdot z^{-1} + 1\cdot z^{-2} + 1\cdot z^{-3} + .. = \frac{z}{z-1} \qquad \textsf{Grenzwert dieser Reihe für } |z|>1$$

Maple:
```  
sum(z^(-k),k=0..infinity) assuming abs(z)>=1; 
```

---

## Beispiel 4

Die Wertefolge 

| k     | -1  | 0   | 1   | 2   | 3   | ... |
| ----- | --- | --- | --- | --- | --- | --- |
| $f_k$ | 0   | 0   | 1   | 1   | 1   | 1   | 

soll transformiert werden. Hier noch mal die Transformationsglichung:
$$F(z)=\mathcal{Z}\{f_k\}= \sum_{k=0} ^\infty f_k \cdot z^{-k}$$
Ergebnis:
$$F(z) = 0\cdot z^{-0} + 1\cdot z^{-1} + 1\cdot z^{-2} + 1\cdot z^{-3} + .. = \frac{1}{z-1} \qquad \textsf{Grenzwert dieser Reihe für } |z|>1$$

Maple:
```  
sum(z^(-k),k=1..infinity) assuming abs(z)>=1; 
```


---

## Beispiel 5

Die Wertefolge 

| k     | -1  | 0   | 1   | 2   | 3   | 4   | ... |
| ----- | --- | --- | --- | --- | --- | --- | --- |
| $f_k$ | 0   | 1   | 0   | 1   | 0   | 1   | ... | 

soll transformiert werden. Hier noch mal die Transformationsglichung:
$$F(z)=\mathcal{Z}\{f_k\}= \sum_{k=0} ^\infty f_k \cdot z^{-k}$$
Ergebnis:
$$F(z) = 1\cdot z^{-0} + 1\cdot z^{-2} + 1\cdot z^{-4} + 1\cdot z^{-6} + .. = \frac{z^2}{z^2-1} \qquad \textsf{Grenzwert dieser Reihe für } |z|>1$$


Maple:
```  
sum(z^(-2*k),k=0..infinity) assuming abs(z)>=1; 
```

---

### Rückwärtstransformation
Die *inverse z-Transformation* kann mit 

$$f_k = \mathcal{Z}^{-1} \{F(z) \} \,=\, \frac{1}{2 \pi \mathrm{i}} \oint_{C} F(z) z^{k-1} dz$$

berechnet werden, wobei *C* eine beliebige geschlossene Kurve um den Ursprung ist, die im Konvergenzbereich von $F(z)$ liegt.

---

## Notationen
$$
\newcommand{\laplace}{\circ\hspace{-5pt}-\hspace{-5pt}\bullet}
\newcommand{\Laplace}{\bullet\hspace{-5pt}-\hspace{-5pt}\circ}
$$
- Festlegung: Signale und Syteme im 
	- Originalbereich bekommen Kleinbuchstaben $y(k)$, $u(k)$, $g(k)$
	- Bildbereich bekommen Großbuchstaben $Y(z)$, $U(z)$, $G(z)$
- Verbreitet sind diese Notationen für die Transformationen: $$f(k)=f_k\;\laplace\;F(z)$$ $$F(z)\;\Laplace\;f_k$$

BTW: Selbe Notation wird auch für die Laplace-Transformation verwendet:
- $Y(s)$, $U(s)$, $G(s)$ 
- $f(t)\;\laplace\;F(s)$, $\qquad F(s)\;\Laplace\;f(t)$

BTW: Selbe Notation wird auch für die Fourier-Transformation verwendet:
- $Y(jω)$, $U(jω)$, $G(jω)$ 
- $f(t)\;\laplace\;F(jω)$, $\qquad F(jω)\;\Laplace\;f(t)$

---

## Allgemeine Eigenschaften bzw. Operationen
Es sei $f_k = f(k)$ und $F(z)$ deren z-Transformierte.

|                     | Originalfunktion $f_{k} = \mathcal{F}^{-1} \left\{ F(z) \right\}$ | Bildfunktion $F(z) = \mathcal{Z}\left\{ f_{k}\right\}$ |
| ------------------- | ----------------------------------------------------------------- | ------------------------------------------------------ |
| Linearität          | $a_{1}f_{k,1}+a_{2} f_{k,2}\,$                                    | $a_{1}F_{1}(z)+ a_{2}F_{2}(z)\,$                       |
| Verschiebung rechts | $f_{k-n}$                                                         | $z^{-n} F(z)$                                          |
| Verschiebung links  | $f_{k+1}$                                                         | $z^{1} (F(z) -  f_0)$                                  |
| Verschiebung links  | $f_{k+2}$                                                         | $z^{2} (F(z) -  f_0 - f_1 z^{-1})$                     |
| Verschiebung links  | $f_{k+n}$                                                         | $z^{n} (F(z) - \sum_{i=0}^{n-1} f_i z^{-i})$           |

---

## Allgemeine Eigenschaften bzw. Operationen
Es sei $f_k = f(k)$ und $F(z)$ deren z-Transformierte.

|                    | Originalfunktion $f_{k} = \mathcal{F}^{-1} \left\{ F(z) \right\}$ | Bildfunktion $F(z) = \mathcal{Z}\left\{ f_{k}\right\}$ |
| ------------------ | ----------------------------------------------------------------- | ------------------------------------------------------ |
| Rückwärtsdifferenz | $f_{k}-f_{k-1}$                                                   | $\frac{z-1}{z} F(z)$            |
| Vorwärtsdifferenz  | $f_{k+1}-f_k$                                                     | $z F(z) - z f_0 -F(z) = (z-1) F(z) - z f_0$            |
| Summensatz         | $\sum_{n=0}^k f_n$                                                | $\frac{z}{z-1}F(z)$                                    |

----

## Beispiel

Gesucht ist die Z-Transformierte des Systems:
$$y_{(k)} ={\frac {7\,u_{(k)}  }{17}}-{\frac {5\,u_{(k-1)} }{17}}-{\frac {10\,y_{(k-2)} }{17}}+{\frac {25\,y_{(k-1)} }{17}}$$

1) Variablen separieren
$y_{(k)} - {\frac {25 }{17}}\,y_{(k-1)} + {\frac {10}{17}}\,y_{(k-2)}={\frac {7}{17}}\,u_{(k)}-{\frac {5 }{17}}\,u_{(k-1)}$

2) Transformation durch Verschiebung
$Y(z) - {\frac {25 }{17}}\,z^{-1}Y(z) + {\frac {10}{17}}\,z^{-2}Y(z)={\frac {7}{17}}\,U(z)-{\frac {5 }{17}}\,z^{-1}U(z)$

3) Ausklammern
$Y(z)\left(1 - {\frac {25 }{17}}\,z^{-1} + {\frac {10}{17}}\,z^{-2}\right)=\left({\frac {7}{17}}-{\frac {5 }{17}}\,z^{-1}\right)U(z)$

4) Quotienten bilden
$$\frac{Y(z)}{U(z)} = \frac{{\frac {7}{17}}-{\frac {5 }{17}}\,z^{-1}}{1 - {\frac {25 }{17}}\,z^{-1} + {\frac {10}{17}}\,z^{-2}}$$

4) Erweitern mit $z^2$
$$\frac{Y(z)}{U(z)} = \frac{{\frac {7}{17}}\,z^2-{\frac {5 }{17}}\,z^{1}}{z^2 - {\frac {25 }{17}}\,z^{1} + {\frac {10}{17}}}$$