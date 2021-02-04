Modellbildung: Was, Wie, Warum
========================

---

## Wiederholung
Welche Schritte gehören zur Bearbeitung einer Regelungsaufgabe?

---

## Wiederholung
#### Lösungsweg für Regelungsaufgaben
1.  Formulierung der Regelungsaufgabe
	1.  Festwertregelung
	2.  Folgeregelung
	3.  Änderung der Streckendynamik
2.  Auswahl der Regelgröße
3.  Auswahl der Stellgröße
4.  Modellierung der Regelstrecke
5.  Regelerentwurf
6.  Analyse des Verhaltens des geschlossenen Regelkreises
7.  Realisierung des Reglers

(nach [Lunze2016](Lunze2016.md))

---

## Modellbasierte Verfahren

![Prinzipeller Lösungsweg für Regelungsaufgaben Quelle: https://wiki.tum.de/download/attachments/5248843/ITK_Vortrag_Regeltungstechnik_in_aller_Ku%CC%88rze.pdf?version=1&modificationDate=1464601144013&api=v2|700](Pasted%20image%2020210128142713.png)

Es gibt modellfreie Regler**einstell**verfahren z.B. Ziegler-Nichols-Verfahren. Dabei werden die Parameter eine standardisierten Reglerstruktur (z.B. PID-Regler) **LIVE** eingestellt. 

--> Welche Vor- und Nachteile hat dieser Ansatz?   

---
## Modellbildung

1. Beschreibung des Modellierungsziels: Regelaufgabe definiert Anforderungen an Modell (Ein-/Ausgänge, Genauigkeit, linear od. nichtlinear, ...)
2. Auswahl der Modellannahmen: Was wird modelliert (Phänomene, Teilsysteme, Wechselwirkungen mit der Umgebung) - und was nicht (Einfach starten! - Mut zur Lücke!!!)
3. Verbale Beschreibung der Regelstrecke _"Dieses „Wortmodell“ kann von allen an der Modellbildung Beteiligten (und nicht nur von Regelungstechnikern) verstanden und überprüft werden"_
4. Aufstellung des Blockschaltbildes
	1. Teilkomponenten und deren Verbindungen werden im verbale Modell gefunden
	2. Blockschaltbild ist die graphische Darstellung 
5. Aufstellung der Modellgleichungen
	1. Jede Teilkomponente muss ihre Ausgänge aus ihrem Zustand und ihren Eingängen berechnen können.
6. Modellparametrierung
7. Modellvalidierung: Abgleich mit Erwartung oder Messung

(nach [Lunze2016](Lunze2016.md) mit Ergänzungen/Kommentaren)

---

## Modellbildung
Zitat aus Lunze:

"Als sehr wichtiges *Nebenergebnis* führt die Modellbildung aber auch zu einem tiefgründigen Verständnis der in dem zu steuernden Prozess ablaufenden physikalischen Vorgänge, denn: 

**Man muss die wichtigsten physikalischen Prozesse verstanden haben, um sie regeln zu können.**"

---

## Blockschaltbild 
**Elemente eines Blockschaltbildes (BSB)**
![Spezielle Symbole in Blockschaltbildern Quelle: Lunze 1 2016 (Abb. 3.2)|500](Uebertragungsglieder.png)

---

## Beispiel 1: Fahrzeugmodell 1/ 
- Betrachtet wird das Fahrzeug
![Geschwindigkeitsregelung (Quelle: [[Franklin2015]])](Pasted%20image%2020201227100125.png)
mit einer Masse von $m=1000 kg$ einem Reibbeiwert von $b=50 \tfrac{N\cdot s}{m}$ und einer beschleunigenden Kraft von $F_u=500 N$
1. Wie sieht das Übertragungsglied für das Blockschaltbild aus?
2. Wie lange dauert ein Beschleunigungsmanöver von $v_0=5\tfrac{m}{s}$ auf $v_0=10\tfrac{m}{s}$?

---

## Beispiel 1: Fahrzeugmodell 2/ 
### 1. Übertragungsglied
![[Bilder_RT_2.svg]]

---

## Beispiel 1: Fahrzeugmodell 3/ 
### 2. Dauer der Beschleunigung
- In der Aufgabe ist der Reibbeiwert $b$ angegeben --> Der antreibenden Kraft $F_u$ wirkt die Reibkraft $F_R = b\cdot \dot{x}(t)$ entgegen.
- Fahrzeugposition $x(t)$ wird durch Differentialgleichung mit Kräftebilanz beschrieben:
$$
\begin{eqnarray}
\tfrac{d^2}{d\,t^2}x(t)\cdot m &=& \Sigma F \\
\tfrac{d^2}{d\,t^2}x(t)\cdot m &=& F_u - F_R \\
\tfrac{d^2}{d\,t^2}x(t)\cdot m &=& F_u - b\cdot \dot{x}(t)
\end{eqnarray}
$$ 
- Uns interessiert die Fahrzeuggeschwindigkkeit: $v(t)=\tfrac{d}{d\,t}x(t)$
- Nach Umformung der folgt so: $$\tfrac{d}{d\,t}v(t)  =- \frac{b}{m}\cdot v(t)+  \frac{F_u}{m}$$

---

## Beispiel 1: Fahrzeugmodell 4/

DGL | Lösung | eingesetzt 
-----| -------- | -----------
$$\tfrac{d}{d\,t}v(t)  = -\frac{b}{m}\cdot v(t)+\frac{F_u}{m}$$ | $$v \left( t \right) ={\frac {F_u}{b}}+{{\rm e}^{-{\frac {b\,t}{m}}}}\left( v_{0}-{\frac {F_u}{b}} \right)$$ | $$v \left( t \right) =10-5\,{{\rm e}^{-t/20}}$$


![Änderung der Fahrzeuggeschwindigekeit bei $F_u=500 N$ und $v(0)=5 \tfrac{m}{s}$](SprungantwortFahrzeuggeschwindigkeit.png)
 
 Eine Geschwindigkeit von $9.9\frac{m}{s}$ wird nach $78,24 s$ erreicht, $10 \frac{m}{s}$ werden **theoretisch** nie erreicht.
 
 --> Wie kann können $8\frac{m}{s}$ erreicht werden,  (schnell)? <--

---

## Beispiel 2: Reihenschwingkreis 1/ 

- Betrachtet wird ein Reihenschwingkreis ΣRSK
- Spannung $u_1(t)$ ist von außen beeinflussbare Größe
- Spannung $u_2(t)$ ist die  Reaktion des Schwingkreises
- zur Zeit t = 0 fließt kein Strom durch die Induktivität
-  die Kondensatorspannung einen bekannten Wert $u_0$
-  der RSK ist unbelastet $i_3(t)=0$

![Ersatzschaltbild des Reihenschwingkreises Quelle: Abb. 4.2 aus [Lunze2016](Lunze2016.md) ](Schaltung%20Reihenschwingkreis.png)

---

## Beispiel 2: Reihenschwingkreis 2/ 
![Ersatzschaltbild des Reihenschwingkreises Quelle: Abb. 4.2 aus [Lunze2016](Lunze2016.md) ](Schaltung%20Reihenschwingkreis.png)
Strom-Spannungsbeziehungen für R, L, C:
$$
\begin{eqnarray}
u_R(t) &=& R\,i_1(t) \\
u_L(t) &=& L\frac{d\,i_1(t)}{d\,t}\\
u_C(t) &=& u_C(0) + \frac{1}{C}\int_0^ti_1(\tau)d\tau
\end{eqnarray}
$$

---

## Beispiel 2: Reihenschwingkreis 3/ 
*Kirchhoff'sche Gesetze* :
$$
\begin{eqnarray}
u_2(t) &=& u_R(t)+u_C(t)\\
u_1(t) &=& u_L(t) + u_R(t) + u_C(t)
\end{eqnarray}
$$

**Ziel:** Eine Differentialgleichung ableiten, in der nur noch die Eingangsgröße $u(t) = u_1(t)$ und die Ausgangsgröße $y(t) = u_2(t)$ sowie deren Ableitungen vorkommen.

---

## Beispiel 2: Reihenschwingkreis 3/ 
![Ersatzschaltbild des Reihenschwingkreises Quelle: Abb. 4.2 aus [Lunze2016](Lunze2016.md) ](Schaltung%20Reihenschwingkreis.png)
Strom-Spannungsbeziehungen für R, L, C:
$$
\begin{eqnarray}
C\,L\frac{d^2}{dt^2}u_2(t)+C\,R\frac{d}{dt}u_2(t)+u_2(t) &=& C\,R\frac{d}{dt}u_1(t)+u_1(t)
\end{eqnarray}
$$


#### Abschluss Modellbildung
- Bei der Modellierung sollte die Dynamik möglichst als Differentialgleichungssystem mit den Ausgängen als abhängige Variable dargestellt werden
