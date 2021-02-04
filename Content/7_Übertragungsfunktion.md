Die Übertragungsfunktion
===================

Bald können wir Dinge in Python machen ....

---

... noch aber nicht ...

---
## Einführungsbeispiel Reihenschwingkreis 1/ 
![Ersatzschaltbild des Reihenschwingkreises Quelle: Abb. 4.2 aus [Lunze2016](Lunze2016.md) ](Schaltung%20Reihenschwingkreis.png)
Strom-Spannungsbeziehungen für R, L, C:
$$
\begin{eqnarray}
C\,L\frac{d^2}{dt^2}y(t)+C\,R\frac{d}{dt}y(t)+y(t) &=& C\,R\frac{d}{dt}u(t)+u(t)
\end{eqnarray}
$$

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
| 1\. Ableitung im Originalbereich                                                                                      | $f'(t) \,$                                                        | $sF(s)-f(0) \,$                                                   |
| 2\. Ableitung im Originalbereich                                                                                      | $f''(t) \,$                                                       | $s^{2}F(s)-sf(0)-f'(0) \,$                                        |

Wir nehmen an die Anfangsbedingungen sind null.

Zugehörige algebraische Gleichung im Bildbereich:
$$
\begin{eqnarray}
C\,L\,s^2\,Y(s)+C\,R\,s\,Y(s)+Y(s) &=& C\,R\,s\,U(s) + U(s)
\end{eqnarray}
$$

## Einführungsbeispiel Reihenschwingkreis 3/
#### Umformen
$$
\begin{eqnarray}
C\,L\,s^2\,Y(s)+C\,R\,s\,Y(s)+Y(s) &=& C\,R\,s\,U(s) + U(s) \\
\big(C\,L\,s^2+C\,R\,s+1\big)Y(s) &=& \big(C\,R\,s + 1\big)\,U(s) \\[1cm]
Y(s) &=& \underbrace{\frac{C\,R\,s + 1}{C\,L\,s^2+C\,R\,s+1}}_{\huge G(s)}\,U(s)
\end{eqnarray}
$$

$G(s)$ wird als Übertragungsfunktion bezeichnet.

Hier ist die Sprungantwort - danke Maple:
$$y(t)=1+{\frac {1}{\sqrt {{{\it CR}}^{2}-4\,{\it CL}}} \left( {\it CR}\,
\sinh \left( 1/2\,{\frac {t\sqrt {{{\it CR}}^{2}-4\,{\it CL}}}{{\it CL
}}} \right) -\cosh \left( 1/2\,{\frac {t\sqrt {{{\it CR}}^{2}-4\,{\it 
CL}}}{{\it CL}}} \right) \sqrt {{{\it CR}}^{2}-4\,{\it CL}} \right) {
{\rm e}^{-1/2\,{\frac {t{\it CR}}{{\it CL}}}}}}
$$


Hier sind weitere Korrespondenzen: https://www-user.tu-chemnitz.de/~syha/lehre/mbIV/laplace.pdf 

--> Niemand berechnet so Systemantworten!!!

Hier ist der Link zu WolframAlpha: https://www.wolframalpha.com/input/?i=InverseLaplaceTransform%5B%28CR*s+%2B+1%29%2F%28%28CL*s%5E2+%2B+CR*s+%2B+1%29*s%29%2C+s%2C+t%5D


$$
1-\frac{\text{CR} e^{t \left(-\frac{\sqrt{\text{CR}^2-4 \text{CL}}}{2
   \text{CL}}-\frac{\text{CR}}{2 \text{CL}}\right)}-\text{CR} e^{t
   \left(\frac{\sqrt{\text{CR}^2-4 \text{CL}}}{2 \text{CL}}-\frac{\text{CR}}{2
   \text{CL}}\right)}+\sqrt{\text{CR}^2-4 \text{CL}} e^{t
   \left(-\frac{\sqrt{\text{CR}^2-4 \text{CL}}}{2 \text{CL}}-\frac{\text{CR}}{2
   \text{CL}}\right)}+\sqrt{\text{CR}^2-4 \text{CL}} e^{t
   \left(\frac{\sqrt{\text{CR}^2-4 \text{CL}}}{2 \text{CL}}-\frac{\text{CR}}{2
   \text{CL}}\right)}}{2 \sqrt{\text{CR}^2-4 \text{CL}}}
$$

TeXForm in Wolfram Alpha


--- 
## Die Übertragungsfunktion

![Quelle: [Lunze2016](Lunze2016.md)](Pasted%20image%2020210202222015.png)


Die ist wirklich wichtig!!!

---


