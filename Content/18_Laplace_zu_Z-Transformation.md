## Berechnung der z-Übertragungsfunktion kontinuierlicher Systeme

Lehrbuch: Unbehauen 2: Abschnitt    2.4.2.2 "Durchführung der exakten Transformation"
--> Leider zu kompliziert für diesen Rahmen ->SKIP<-

----

##  Durchführung der approximierten Transformation
### Ein Integrator:

| DGL                 | Übertragungsfunktion    |
| ------------------- | ----------------------- |
| $\dot{y}(t) = u(t)$ | $Y(S) = \frac 1 s U(s)$ |

	
**Kleine Übung**: Gesucht ist die 
1) Differenzengleichung $y_{(k)} = ...$
2) Z-Transformierte der Differenzengleichung $G(Z) = \frac{Y(z)}{U(z)} = ...$



---

##  Durchführung der approximierten Transformation
### Ein Integrator:

| DGL                 | Übertragungsfunktion    |
| ------------------- | ----------------------- |
| $\dot{y}(t) = u(t)$ | $Y(S) = \frac 1 s U(s)$ |

	
Differenzengleichung
$$y_{(k)} = y_{(k-1)}+T\cdot u_{(k)}$$

Übertragungsfunktion 
$$\begin{gather}
Y(z)-z^{-1}Y(z) = T\cdot U(z)\\
Y(z)(1-z^{-1}) = T\cdot U(z)\\
\frac{Y(z)}{U(z)} = \frac{T}{1-z^{-1}}\\[1cm]
\frac{Y(z)}{U(z)} = \frac{T\cdot z}{z-1}
\end{gather}
$$

----

##  Durchführung der approximierten Transformation
### Variante 1

| Integrator zeitkontinuierlich | Integrator zeitdiskret   |
| ----------------------------- | ------------------------ |
| $$\frac 1 s$$                 | $$\frac{T\cdot z}{z-1}$$ |
|                               |                          |

**Approximation** 
$$s \approx \frac{z-1}{T\cdot z}$$


Dieses Vorgehen entspricht genau der Anwendung der Differenzenquotienten $\frac{df(t)}{dt}=\frac{f_{(k)}-f_{(k-1)}}{T}$  auf die zugehorige Differentialgleichung.
   
--- 
 
 ##  Durchführung der approximierten Transformation
### Variante 2 (Tustin Approximation)

$$s \approx \frac 2 T \frac{z-1}{z+1}$$

-    Eine etwas genauere Approximationsbeziehung
-    Beschreibt die Integrations nach Trapezregel 


---

## Beispiel

$$Y(s)=\frac{C\,R\,s + 1}{C\,L\,s^2+C\,R\,s+1}\,U(s) \qquad \rightarrow \qquad Y(s)=\frac{0.5\,s + 1}{0.2\,s^2+0.5\,s+1}\,U(s) $$ 

$$Y(s)=\frac{0.5\,\left(\frac{z-1}{0.2\cdot z}\right) + 1}{0.2\,\left(\frac{z-1}{0.2\cdot z}\right)^2+0.5\,\left(\frac{z-1}{0.2\cdot z}\right)+1}\,U(s)$$

$$Y(z)=\frac{7z^2-5z}{17z^2-25z+10}\,U(z)$$

bzw:

$$Y(z)=\frac{7-5z^{-1}}{17-25z^{-1}+10z^{-2}}\,U(z)$$

Differenzengleichung:

....


----

## Beispiel Reihenschwingkreis

$$Y(s)=\frac{C\,R\,s + 1}{C\,L\,s^2+C\,R\,s+1}\,U(s) \qquad \rightarrow \qquad Y(s)=\frac{0.5\,s + 1}{0.2\,s^2+0.5\,s+1}\,U(s) $$ 

Approximation im Z-Bereich:
$$Y(z)=\frac{0.5\,\left(\frac{z-1}{0.2\cdot z}\right) + 1}{0.2\,\left(\frac{z-1}{0.2\cdot z}\right)^2+0.5\,\left(\frac{z-1}{0.2\cdot z}\right)+1}\,U(z)$$
$$Y(z)=\frac{7z^2-5z}{17z^2-25z+10}\,U(z)$$

bzw:

$$Y(z)=\frac{7-5z^{-1}}{17-25z^{-1}+10z^{-2}}\,U(z)$$

---

## Beispiel Reihenschwingkreis

Umformung:
$$
\begin{gather}
Y(z)\left(17-25z^{-1}+10z^{-2}\right)=\left(7-5z^{-1}\right)\,U(z) \\
17Y(z)-25z^{-1}Y(z)+10z^{-2}Y(z)=7U(z)-5z^{-1}U(z)
\end{gather}
$$

Transformation in Zeitbereich:
$$17y_{(k)}-25y_{(k-1)}+10y_{(k-2)}=7u_{(k)}-5u_{(k-1)}$$

Transformation in Zeitbereich:
$$y_{(k)}=\frac{25}{17} y_{(k-1)}-\frac{10}{17}y_{(k-2)}+\frac{7}{17}u_{(k)}-\frac{5}{17}u_{(k-1)}$$
























