

Z-Transformation
---


## Einführung!

- *mathematisches Verfahren* der Systemtheorie zur Behandlung und Berechnung von kontinuierlich (zyklisch) abgetasteten Signalen und linearen zeitinvarianten zeitdiskreten dynamischen Systemen. 
- Sie ist aus der Laplace-Transformation entstanden und hat auch ähnliche Eigenschaften und Berechnungsregeln. 
- Die z-Transformation gilt für Signale im diskreten Zeitbereich (Wertefolgen), während die Laplace-Transformation für entsprechende Berechnungen im kontinuierlichen Zeitbereich dient. 

- Ein Vorteil der Anwendung der z-Transformation ergibt sich, wenn eine Wertefolge und eine systembeschreibende Differenzengleichung in eine algebraisch zusammengefasste z-Übertragungsfunktion überführt wird. 
- Die z-Übertragungsfunktion dient der Systemanalyse, d. h. der Analyse des Systemverhalten bei verschiedenen Anregungen und insbesondere auch der Stabilitätsanalyse. 
- Der Verlauf der Systemausgangsgröße y kann bei gegebener Eingangsgröße u durch verschiedene Methoden der inversen z-Transformation in den zeitdiskreten Bereich f ( k ) und dann im Zeitbereich f ( t ) dargestellt werden.
- Die z-Transformation wird größtenteils für die digitale Steuer- und Regelungstechnik und zur Berechnung digitaler Filter angewendet. Man kann sie aber auch zur Gewinnung von expliziten Formeln für rekursiv definierte Zahlenfolgen einsetzen. 

---

### Bilaterale z-Transformation 

Die bilaterale z-Transformation eines Signals $x[k]$ ist die formale
[Laurent-Reihe] $X(z)$:

$$X(z) = Z\{x[k]\} = \sum_{k=-\infty}^{\infty} x[k] z^{-k}$$,

wobei $k$ alle ganzen Zahlen durchläuft und $z$ im Allgemeinen eine
[komplexe Zahl] der Form:

$$z=A e^{j\varphi} = \sigma + j\omega$$

ist. $A$ ist der Betrag von $z$ und $\varphi$ der Winkel der komplexen
Zahl in [Polarkoordinaten]. Alternativ kann $z$ auch in [kartesischer
Form] als Realteil $\sigma$ und Imaginärteil $\omega$ beschrieben
werden.

Unter gewissen [Konvergenzbedingungen] ist die z-Transformierte eine
[holomorphe Funktion] auf einem Kreisring in der komplexen Zahlenebene,
unter schwächeren Bedingungen immerhin noch eine quadratintegrierbare
Funktion auf dem Einheitskreis.


### Unilaterale z-Transformation

Substituiert man in der Beschreibung einer Abtastfolge im Laplace-Bereich den Ausdruck $e^{sT_A}$ durch $z$, so erhält man eine Potenzreihe in $z$:

$$\sum_{k=0}^{\infty} x[k] e^{-skT}=\sum_{k=0}^{\infty} x[k]\cdot z^{-k}=x(0)+x(1)\cdot z^{-1}+x(2)\cdot z^{-2}+ \cdots$$
Dabei ist  $z=e^{sT_A}$ 

Wenn $x[k]$ nur nichtnegative $k$ Werte hat, kann die unilaterale z-Transformation definiert werden:

$$X(z)=Z\{x[k]\}= \sum_{k=0} ^\infty x[k] \cdot z^{-k}$$


In der [Signalverarbeitung] wird die *unilaterale* z-Transformation für
[kausale] Signale verwendet.

----

### Zusätzliche Eigenschaften der unilateralen z-Transformation [zusätzliche_eigenschaften_der_unilateralen_z_transformation]

Es sei $f_k = f(k)$ und $F(z)$ deren z-Transformierte. Weiter sei
folgende Schreibweise für die Transformation der diskreten Zeitfunktion
in die Bildebene definiert.

$f_{k} \circ\!\!-\!\!\bullet F(z)$

Dann gelten folgende Regeln:

$\begin{array}{llcl}
\text{Verschiebungssatz}
  & f_{k-n} & \circ\!\!-\!\!\bullet & z^{-n} F(z) \\
  & f_{k+n} & \circ\!\!-\!\!\bullet & z^{n} (F(z) - \sum_{i=0}^{n-1} f_i z^{-i})\\
  & f_{k+1} & \circ\!\!-\!\!\bullet & z^{1} (F(z) -  f_0) \\
  & f_{k+2} & \circ\!\!-\!\!\bullet & z^{2} (F(z) -  f_0 - f_1 z^{-1}) \\
\text{Dämpfungssatz}
  & a^{-k} \cdot f_k & \circ\!\!-\!\!\bullet & F(a \cdot z) \\
\text{Ableitung der Bildfunktion}
  & k \cdot f_k & \circ\!\!-\!\!\bullet & -z \frac{dF(z)}{dz} \\
\text{Spektraler}
  & W(z) &=& U(z) \cdot V(z) \\
\text{Multiplikationssatz}
  & w_k  &=&  \sum_{n=0}^k u_{k-n} \cdot v_n = \sum_{n=0}^k u_{n} \cdot v_{k-n} \\
\text{Differenzensatz}
  & \Delta f_k &=&  f_{k+1} - f_k \\
  & \Delta^2 f_k &=& \Delta f_{k+1} - \Delta f_k =  f_{k+2} - 2 f_{k+1} + f_k \\
  & \Delta^2 f_k & \circ\!\!-\!\!\bullet & (z-1)^2 F(z) - z ((z-1) f_0 + \Delta f_0) \\
  & \Delta^n f_k & \circ\!\!-\!\!\bullet & (z-1)^n F(z) - z \sum_{i=0}^{n-1} (z-1)^{n-i-1} \Delta ^i f_0 \\
\text{Summensatz}
  & \sum_{n=0}^k f_n & \circ\!\!-\!\!\bullet & z \frac{F(z)}{z-1} \\
\text{1. Grenzwertsatz}
  & f_n &=& \lim_{z \to \infty} z^n \cdot (F(z) - \sum_{k=0}^{n-1} z^{-k} f_k) \\
  & f_0 &=& \lim_{z \to \infty} F(z) \\
\text{2. Grenzwertsatz}
  & \lim_{k \to \infty} f_k &=& \lim_{z \to 1} (z-1) F(z) \\
\text{Stabilität}
  & |z_{PK}| < 1 && \rightarrow \text{asymptotische Stabilität}
\end{array}$



----

### Inverse z-Transformation 

Die *inverse z-Transformation* kann mit der Formel

$$x[k] = Z^{-1} \{X(z) \} \,=\, \frac{1}{2 \pi \mathrm{i}} \oint_{C} X(z) z^{k-1} dz$$

berechnet werden, wobei *C* eine beliebige geschlossene Kurve um den
Ursprung ist, die im Konvergenzbereich von $X(z)$ liegt.

Die (unilaterale) z-Transformation ist zeitdiskret und entspricht der
Laplace-Transformation für zeitkontinuierliche Signale.
  
----
  
###  Grundlagen der z-Transformation
Die z-Transformation ist ein mathematisches Verfahren der Systemtheorie zur Behandlung und Berechnung von kontinuierlich abgetasteten Signalen und linearen zeitinvarianten zeitdiskreten dynamischen Systemen. Ein zeitdiskretes dynamisches System wird durch Differenzengleichungen oder als z-Transformierte beschrieben. Im Gegensatz dazu wird die Laplace-Transformation für kontinuierlichen Signale und Systeme verwendet. 

#### Definition der Formelzeichen und Systemgrößen nachfolgender Systemdarstellungen

Liste der wichtigsten Formelzeichen und Systemgrößen, die im Folgenden verwendet werden:


| Formelzeichen                      | Erklärung                                   | Bemerkung                                                                                                                                                                                                                                                                                                                                |
|------------------------------------|---------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| $u(t)$                             | Eingangssignal                              | Werden in der Regelungstechnik [Regler](Regler "wikilink") und [Regelstrecke](Regelstrecke "wikilink") gleichzeitig betrachtet, wird die Eingangsgröße des Reglers als $e(t)$ ([Regelabweichung](Regelabweichung "wikilink")) bezeichnet. Die Ausgangsgröße des Reglers $u(t)$ ist dann gleichzeitig die Eingangsgröße der Regelstrecke. |
| $y(t)$                             | Ausgangssignal                              | meist Systemantwort, bei Regelkreisen die [Regelgröße](Regelgröße "wikilink").                                                                                                                                                                                                                                                           |
| Kleinbuchstaben                    | Zeitbereich                                 | z. B.: f, u, y                                                                                                                                                                                                                                                                                                                           |
| Großbuchstaben                     | Bildbereich                                 | z. B.: F, U, Y, G                                                                                                                                                                                                                                                                                                                        |
| ${T_A}, \ \text {auch} \ T_0, \ T$ | Abtastzeit                                  | Zeitlicher Abstand der Abtastungen eines zeitdiskreten Signals. Mit der Frequenz $f \ = 1 / {T_A}$ wird ein kontinuierliches Signal abgetastet.                                                                                                                                                                                          |
| $\Delta t$                         | Zeitintervall                               | $\Delta t$ ist ein Parameter der diskreten Zeit, keine reale Zeit. In Verbindung mit Abtastung kann $\Delta t= T_A$ sein. $\Delta t$ wird z. B. bei der Berechnung der Differenzengleichungen verwendet.                                                                                                                                 |
| $k$                                | Abtastfolge                                 | $k = (0, 1, 2, 3, \dots, \infty)$ in einer unendlichen oder $k = (0, 1, 2, 3, \dots, k_\mathrm{max})$ einer endlichen Folge. $k$ wird auch für die Nummerierung der Werte in einer Folge verwendet.                                                                                                                                      |
| $n, \ auch \ d$                    | Abtastschritte                              | $n=d= \text {Anzahl zusammenhängender Abtastschritte}$. (n ist auch eine Bezeichnung für die Potenz der s-Variablen eines Nennerpolynoms)                                                                                                                                                                                                |
| $f_{(k)}$                          | Wertefolge                                  | Eine Folge der Werte: $f_{(k)}=[f(0), f(T_A), f(2T_A), f(3T_A), \dots]$                                                                                                                                                                                                                                                                  |
| $f(t)$                             | Signal im Zeitbereich                       | Zeitsignal (allgemein)                                                                                                                                                                                                                                                                                                                   |
| $f(k \cdot T_A)$                   | Zeitdiskretes Signal                        | Wert des Signals $f(t)$ zum Zeitpunkt $k \cdot T_A$. Vereinfachte Schreibweise ist z. B. $u_{(k)}$ oder $y_{(k)}$.                                                                                                                                                                                                                       |
| $s = \sigma + \mathrm{i}\omega$    | Laplace Variable                            |                                                                                                                                                                                                                                                                                                                                          |
| e                                  | [Eulersche Zahl](Eulersche_Zahl "wikilink") | e = [Eulersche Zahl](Eulersche_Zahl "wikilink") ≈ 2,71828.                                                                                                                                                                                                                                                                               |
| $F(s)$                             | Laplace-Transformiert                       | Laplace-Transformiertes Signal für kontinuierliche Systeme: Polynomfunktion mit Zählergrad: $m$ und Nennergrad: $n$                                                                                                                                                                                                                      |
| $G(s) = \frac {Y(s)}{U(s)}$        | Laplace-Transformiert                       | Laplace-Übertragungsfunktion für kontinuierliche Systeme: Polynomfunktion mit Zählergrad: $m$ und Nennergrad: $n$                                                                                                                                                                                                                        |
| $z=e^{T_A \cdot s}$                | z-Variable                                  |                                                                                                                                                                                                                                                                                                                                          |
| $F(z)$, $G(z)$                     | z-transformiert                             | z-transformiertes Signal bzw. z-Übertragungsfunktion für diskrete Systeme: Polynomfunktion mit Zählergrad: $m$ und Nennergrad: $n$                                                                                                                                                                                                       |
| $T$                                | Zeitkonstante                               | Zeitkonstante eines dynamischen Systems. Bei mehreren Zeitkonstanten des dynamischen Systems werden die Zeitkonstanten indiziert: $T_{i}$                                                                                                                                                                                                |


---


### Vergleich der diskreten und der kontinuierlichen Übertragungssysteme {#vergleich_der_diskreten_und_der_kontinuierlichen_übertragungssysteme}

Eigenschaften der betrachteten Systeme

-   Linear, zeitinvariant, dynamisch
-   Mindestens ein Eingangssignal $u(t)$ und ein Ausgangssignal $y(t)$

| VERGLEICH                                | diskretes System                                                          | kontinuierliches System                                                             |
|------------------------------------------|---------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| Ein-/Ausgangssignal                      | reelle Folge, Zeitreihe mit fortlaufendem konstanten Zeitintervalls $T_A$ | kontinuierliches reelles Signal                                                     |
| Systembeschreibung im Zeitbereich        | [Differenzengleichung](Differenzengleichung "wikilink")                   | [gewöhnliche Differentialgleichungen](gewöhnliche_Differentialgleichung "wikilink") |
| Transformation in den Bildbereich        | **mit z-Transformation**                                                  | mit Laplace-Transformation                                                          |
| Operator-Schreibweise der Transformation | $F(z)= \mathcal Z \{f_{(k)} \}$                                           | $F(s)= \mathcal L \{f(t) \}$                                                        |
| Inverse Transformation                   | $f_{(k)}= \mathcal Z^{-1} \{F(z) \}$                                      | $f(t)= \mathcal L^{-1} \{F(s) \}$                                                   |
| Systembeschreibung im Bildbereich        | z-Übertragungsfunktion                                                    | s-Übertragungsfunktion                                                              |

Allgemeine Eigenschaften im Bildbereich: Beziehung der Stabilität in der
z-Ebene. Stabilität: Pole im Inneren des z-Einheitskreises.
Grenzstabilität: Pole auf der z-Kreislinie.

Nullstellenanalyse für Übertragungsfunktionen G(s), G(z). Die
Übertragungsfunktion wird im Bildbereich als Bruch mit Zähler- und
Nennerpolynom dargestellt.

-   Übertragungsfunktion = Ausgangssignal / Eingangssignal =
    Zählerpolynom / Nennerpolynom
-   Die Auswertung des Nennerpolynoms führt zu Aussagen über die
    Stabilität des Systems.
-   Stabilitätsgebiet „linke s-Halbebene“ wird in das Innere eines
    Einheitskreises der z-Ebene transformiert.
-   Einheitskreis mit Radius 1, Ordinate = Imaginärteil von z, Abszisse
    = Realteil von z.
-   Ablesung: Stabilität, Grenzstabilität, bei Instabilität liegen die
    Pole außerhalb des Einheitskreises.


---

## Grundlagen Differenzengleichungen für lineare zeitinvariante Systeme

Für die numerische Berechnung des Systemverhaltens eines zeitdiskreten dynamischen Systems können Differenzengleichungen $y_{(k)}=f(Systemparameter, k, k-1, \Delta t, u_{(k)})$ verwendet werden. Mit ihrer Hilfe lässt sich das Systemverhalten (der Verlauf der Systemausgangsgröße $y(t)$ ) für ein gegebenes Eingangssignal $u(t)$ im zeitdiskreten Bereich $f(k\Delta t)$ berechnen.

- Differenzengleichungen entstehen meist aus systembeschreibenden gewöhnlichen Differenzialgleichungen, deren Differentialquotienten durch Differenzenquotienten ersetzt werden. 

- Die kontinuierlichen mathematischen Operationen der Integration und Differentiation werden zeitdiskret durch Summen- und Differenzenbildung angenähert.


der Rückwärts-Differenzenquotient $\frac {\Delta y}{\Delta t}=\frac {y_{(k)}- y_{(k-1)}} {\Delta t}$ näherungsweise eingeführt wird.

In der Regel wird davon ausgegangen, dass die inneren Systemspeicher des Übertragungssystems sich im Ruhezustand befinden und die Anfangswerte bei t = 0 für $y_{(0)}=0$ und alle Ableitungen von $y_{(0)}$ Null sind.


Differenzengleichung als Rekursionsgleichung , weil jedes Folgeglied eine Funktion des vorherigen Folgegliedes ist.

Die [rekursive](Rekursion "wikilink") Anwendung von Differenzengleichungen zur Berechnung von Eingangs-Wertefolgen zu Ausgangs-Wertefolgen bedeutet die angenäherte Lösung der systembeschreibenden Differentialgleichung des Systemausgangssignals $y_{(k)}$

### Differenzengleichungen höherer Ordnung

Zeitkontinuierliche lineare Systeme werden im Zeitbereich durch die gewöhnlichen Differenzialgleichungen $n$-ter Ordnung mit konstanten Koeffizienten für $n \geq m$ beschrieben. Dabei sind $n$ und $m$ die höchsten Ableitungen der Ausgangssignale $y(t)$ und Eingangssignale $u(t)$.

Eine gegebene gewöhnliche Differentialgleichung wird durch den Koeffizienten $a_0$ dividiert, um $y(t)$ freistellen zu können. Diese Form der Differentialgleichung wird entsprechend der dargestellten Koeffizienten wie folgt neu geordnet.
  
$y(t)+ a_{1} \dot y(t)+ a_{2} \ddot y(t)+ \dots + a_ny^{(n)}(t) = b_0 u(t)+ b_1 \dot u(t) + b_2 \ddot u(t)+ \dots + b_m u^{(m)}(t)$.

Diese Differentialgleichung kann in eine Differenzengleichung überführt werden:

-   $f(kT_A)$ wird vereinfacht als $f_{(k)}$ geschrieben und entspricht einem aktuellen Folgeglied.
-   Die kontinuierlichen Systemgrößen $y(t)\to y_{(k)}$ und $u(t) \to u_{(k)}$ werden zeitdiskret dargestellt.
-   Die Ableitungen im Zeitbereich $dy/dt$ werden entsprechend der Ordnung durch Differenzenquotienten $\Delta y / \Delta t$ der zugehörigen Ordnung ersetzt.

  
Jede Ableitung der Systemgrößen wird im zeitdiskreten Bereich entsprechend der Ordnung als zurückliegende Folgeglieder der Eingangs- und Ausgangsfolgen k-1 bis k-n oder k-m berücksichtigt.

Daraus folgt die Differenzengleichung:

  
${y_{(k)} + a_1 \cdot y_{(k-1)} + a_2 \cdot y_{(k-2)} + \dots + a_n \cdot y_{(k-n)} = b_0 \cdot u_{(k)}+ b_{1} \cdot u_{(k-1)}+ b_2 \cdot u_{(k-2)} + \dots + b_m \cdot u_{(k-m)}}$.

Damit kann die allgemeine Form der Differenzengleichung nach $y_{(k)}$ aufgelöst werden:

  
${y_{(k)}=b_0 \cdot u_{(k)}+ b_{1} \cdot u_{(k-1)}+ b_2 \cdot u_{(k-2)} + \dots + b_m \cdot u_{(k-m)} -a_1 \cdot y_{(k-1)} -a_2 \cdot y_{(k-2)} - \dots - a_n \cdot y_{(k-n)}}$.

Für die numerische Berechnung eines dynamischen Systems wird die s-Übertragungsfunktion oder die zugehörige Differentialgleichung benötigt. Die Umsetzung einer systembeschreibenden Differentialgleichung in eine angenäherte Differenzengleichung zur Beschreibung von Eingangsfolgen und Ausgangsfolgen eines dynamischen Systems wird ermöglicht, wenn die Differentiale der Differentialgleichung durch Rückwärts-Differenzenquotienten über die Abtastperiode ersetzt werden.[1]

Die folgenden Ableitungen der Differentialquotienten in Differenzenquotienten der 1. 2. und 3. Ordnung sind gegeben:

Differenzenquotient 1. Ordnung:  
$$\dot y(t)=\frac {dy}{dt} \approx \frac {\Delta y}{\Delta t}= \frac {\Delta y_k}{T_A}=\frac {y_{(k)}- y_{(k-1)}}{T_A}$$

Der Differenzenquotient 2. Ordnung entsteht aus Differenzen der Differenz:
$$\ddot y(t)=\frac {d^2y}{dt^2} \approx \frac {\Delta^2y_k}{T_A^2} = \frac {y_{(k)}-2y_{(k-1)} +y_{(k-2)} }{T_A^2}$$


Der Differenzenquotient 3. Ordnung lautet:
$$y^{(3)}(t)=\frac {d^3y}{dt^3} \approx \frac {\Delta^3y_k}{T_A^3} = \frac {y_{(k)}-3y_{(k-1)}+3y_{(k-2)}-y_{(k-3)}}{T_A^3}$$

Nach erfolgtem Einsetzen der Differenzenquotienten in die Differenzengleichung eines dynamischen Systems lassen sich die neuen Koeffizienten aus den Koeffizienten der Differentialgleichung berechnen.


---


### Rechenregeln der z-Transformation

Die Transformationen und Rücktransformationen der z-Transformation erfolgen meist mit Hilfe von Transformations-Tabellen.


#### Die wichtigsten Eigenschaften der z-Transformation:

-   Grundlagen der Definitionen im z-Bereich:
 
z-Variable:
$$z=e^{T_A \cdot s}$$

z-Transformierte einer Folge $f_{(k)}$:
$$F(z)= \mathcal Z \{f_{(k)} \}$$

Inverse z-Transformation von F(z):  
$$f_{(k)}= \mathcal Z^{-1} \{F(z) \}$$

####  Für **Grenzbetrachtungen** treten häufig folgende Fälle auf:

  Für den s-Bildbereich gilt für die s-Variable.

  
$$\lim_{t \to +0} f(t) = \lim_{s \to \infty} s \cdot F(s)$$

$$\lim_{t \to \infty} f(t) = \lim_{s \to 0} s \cdot F(s)$$

Für den z-Bildbereich gilt für die z-Variable:  
$$f(k=0) = \lim_{z \to \infty} F(z)$$

$$\lim_{k \to \infty} f(k) = \lim_{z \to 1} (z-1) \cdot F(z)$$

**Anfangswert einer zeitdiskreten Folge:**
$$u(k=0) = \lim_{z \to \infty} U(z)$$

**Rückwärtsverschiebung (nach rechts):**
Die Berechnung einer Totzeit $T_t = d \cdot T_A$ einer Abtastfolge entspricht einer Rückwärtsverschiebung (Rechtsverschiebung) der Abtastfolge (Zahlenwerte) um d Abtastschritte von $T_A$. Diese mathematische Operation bedeutet im s-Bereich für die Totzeit $e^{-s \cdot T_t}$ und im z-Bereich:

$$u_{(k-d)} \ \circ \!\!-\!\!\bullet \ z^{-d} \cdot U(z)$$

**Vorwärtsverschiebung (nach links):**
Eine Vorhersage um die Zeit $T_P = d \cdot T_A$ einer Wertefolge entspricht einer Vorwärtsverschiebung nach links um d-Abtastschritte. Diese Operation entspricht der Laplace-Transformierten $e^{s \cdot T_A}$ und bedeutet im z-Bereich:
$$u_{(k+d)}\ \circ \!\!-\!\!\bullet \ z^{d} \cdot U(z)$$

**Differentiation:**  
Die Differenz zweier aufeinander folgender Abtastwerte dividiert durch die Abtastzeit entspricht der Annäherung an einen Differenzialquotienten im Zeitbereich.

  
$$u_{(k)}-u_{(k-1)} \ \circ \!\!-\!\!\bullet \ \frac {z-1} z \cdot U(z)$$

**Integration:**  
Wird die Summe aller Abtastwerte mit der Abtastzeit T_(A) multipliziert, entsteht in Annäherung an den Zeitbereich die numerische Integration. Im s-Bereich entspricht die Integration 1 / s. Im z-Bereich gilt für die Integration:

$$\sum_{i=0} ^k u_{(i)} \ \circ \!\!-\!\!\bullet \ \frac z {z-1} \cdot U(z)$$

**Gewichtsfolge:** 
Die z-Übertragungsfunktion G(z) ist die z-Transformierte der Gewichtsfolge g(k).
  
$$G(z) \ \bullet \!\!-\!\!\circ \ g(k)$$


**Multiplikation:**
Ausgangssignal als Funktion des Eingangssignals und der z-Übertragungsfunktion
$$Y(z)=U(z) \cdot G(z)$$

**Faltung:**
$$y_{(k)}= \sum_{i=0}^k g_{(i)} \cdot u_{(k-i)}$$

### Tabelle der Korrespondenzen des Zeitbereichs f(t), des Laplace- und z-Bereichs 

| Funktion im Zeitbereich f(t)         | Laplace-Transformierte im Bildbereich F(s) | Diskrete Laplace-Transformierte nach der z-Transformation $F(z) = \mathcal Z \{ F(s) \}$       |
|--------------------------------------|--------------------------------------------|------------------------------------------------------------------------------------------------|
| δ-Impuls                             | 1                                          | 1                                                                                              |
| Einheitssprung 1                     | $\frac 1 s$                                | $\frac z {z-1}$                                                                                |
| t                                    | $\frac 1 {s^2}$                            | $\frac {T_A \cdot z} {(z-1)^2}$                                                                |
| $t^2$                                | $\frac 2 {s^3}$                            | $\frac {T_A^2 \cdot z \cdot (z+1)} {(z-1)^3}$                                                  |
| $e^{-a \cdot t}$                     | $\frac 1 {s+a}$                            | $\frac z {z-e^{-a\cdot T_A}}$                                                                  |
| $t \cdot e^{-a \cdot t}$             | $\frac 1 {(s+a)^2}$                        | $\frac {e^{-a \cdot T_A} \cdot T_A \cdot z} {(z-e^{-a \cdot T_A})^2}$                          |
| $1-e^{-a \cdot t}$                   | $\frac a {s \cdot (s+a)}$                  | $\frac {(1-e^{-a \cdot T_A}) \cdot z} {(z-1) \cdot (z-e^{-a\cdot T_A})}$                       |
| $1-e^{-t/T_1}$                       | $\frac 1 {s \cdot (1+T_1 \cdot s)}$        | $\frac {(1-e^{-T_A/T_1})\cdot z} {(z-1) \cdot (z-e^{-T_A/T_1})}$                               |
| $\sin \omega_0t$                     | $\frac {\omega_0} {s^2+ \omega^2_0 }$      | $\frac {z \cdot \sin (\omega_0 T_A)}{z^2-2z \cdot \cos (\omega_0 T_A)+1}$                      |
| $\cos \omega_0t$                     | $\frac {s} {s^2+ \omega^2_0 }$             | $\frac {z^2-z \cdot \cos(\omega_0 T_A)}{z^2-2z \cdot \cos(\omega_0 T_A)+1}$                    |
| $1-(1+at)e^{-at}$                    | $\frac {a^2} {s \cdot (s+a)^2}$            | $\frac z{z-1}-\frac z{z-c}-\frac {acT_Az}{(z-c)^2} \ ; \quad c=e^{-aT_A}$                      |
| $1+ \frac {be^{-at}-ae^{-bt}} {a-b}$ | $\frac {ab} {s \cdot (s+a)(s+b)}$          | $\frac z{z-1}+\frac {bz}{(a-b)(z-c)}-\frac {az}{(a-b)(z-d)}$ $c=e^{-aT_A} \ \quad d=e^{-bT_A}$ |
| $e^{-at}\sin \omega_0t$              | $\frac {\omega_0} {(s+a)^2+ \omega^2_0 }$  | $\frac {cz \sin(\omega_0T_A)}{z^2-2cz \cos(\omega_0T_A)+c^2}\ ; \quad c=e^{-aT_A}$             |
| $e^{-at}\cos \omega_0t$              | $\frac {s+a} {(s+a)^2+ \omega^2_0 }$       | $\frac {z^2-cz \cos (\omega_0T_A)}{z^2-2cz \cos(\omega_0T_A)+c^2}\ ; \quad c=e^{-aT_A}$        |
| $a^{t/T_A}$                          | $\frac 1 {s-(1/T_A)\ln a }$                | $\frac z {z-a}$                                                                                |

  
---

### Tabelle der Korrespondenzen der zeitdiskreten Funktionen $f_{(k )}$ zum z-Bereich $F(z)$ (Auszüge)

| Name der Zeitfunktion               | Wertefolge $f_{(k )}$                                                                                | z-Transformierte                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| δ-Impulsfolge                       | $f_{(k)}=[0(-T_A), 1(0T_A), 0(T_A), 0(2T_A), 0(3T_A), \dots]$                                        | 1                                                                                     |
| Sprungfolge                         | $f_{(k)}=[0(-T_A), 1(0T_A), 1(T_A), 1(2T_A), 1(3T_A), \dots]$                                        | $\frac z {z-1}$                                                                       |
| Anstiegsfolge                       | $u_{(k)}=[-u_1(-T_A), u_0(0T_A), u_1(T_A), u_2(2T_A), u_3(3T_A), \dots]$ $k=[-1, 0, 1, 2, 3, \dots]$ | $\frac z {(z-1)^2}$                                                                   |
| Potenzfolge                         | $a^k$                                                                                                | $\frac z {z-a}$                                                                       |
| e-Funktionsfolge                    | $e^{-ak}$                                                                                            | $\frac z {z-e^{-a}}$                                                                  |
| Sinusfunktionsfolge                 | $\sin(ak)$                                                                                           | $\frac {z \cdot \sin a} {z^2-2z \cdot \cos a+1}$                                      |
| Kosinusfunktionsfolge               | $\cos(ak)$                                                                                           | $\frac {z \cdot (z-\cos a)} {z^2-2z \cdot \cos a+1}$                                  |
| Abklingende Sinus- funktionsfolge   | $e^{-ak} \cdot \sin(bk)$                                                                             | $\frac {z \cdot e^{-a}\cdot \sin b} {z^2-2z \cdot e^{-a} \cdot \cos \ b+e^{-2a}}$     |
| Abklingende Cosinus- funktionsfolge | $e^{-ak} \cdot \cos(bk)$                                                                             | $\frac {z \cdot (z-e^{-a}\cdot \cos b)} {z^2-2z \cdot e^{-a} \cdot \cos \ b+e^{-2a}}$ |
| Linearitätssatz                     | $a_1f_1(k)+a_2f_2(k)+ \dots +a_nf_n(k)$                                                              | $a_1F_1(z)+a_2F_2(z)+ \dots +a_nF_n(z)$                                               |
| Rechts-Verschiebesatz               | $f(k-d)$                                                                                             | $z^{-d} \cdot F(z)$                                                                   |
| Faltungssumme                       | $\sum_{i=0}^k f_1(i) \cdot f_2(k-i)$                                                                 | $F_1(z) \cdot F_2(z)$                                                                 |
| Anfangswertsatz                     | $\lim_{k \to 0} f(k)$                                                                                | $\lim_{z \to \infty} F(z)$                                                            |
| Endwertsatz                         | $\lim_{k \to \infty} f(k)$                                                                           | $\lim_{z \to 1} \,(z-1) \cdot F(z)$                                                   |

---

## Z-Übertragungsfunktion (Impulsübertragungsfunktion) von zeitdiskreten Elementen

**Übersicht:**

>   Die Differenzengleichungen $y_{(k)}$ können ausschließlich mit Hilfe des Linearitätssatzes und Verschiebungssatzes in den komplexen z-Bildbereich und in die z-Übertragungsfunktionen $G(z)=Y(z) / U(z)$ überführt werden.

  
Wendet man auf die einzelnen Terme der Differenzengleichung den Linearitäts- und den rechts-Verschiebungssatz an und bringt alle Terme mit $y_{(k)}$ auf die linke Seite und alle Terme mit $u_{(k)}$ auf die rechte Seite der Differenzengleichung, so lässt sich das Verhältnis $G(z)=Y(z)/ U(z)$ mit den verbleibenden Elementen als gebrochen-rationale Funktion darstellen.

Die z-Übertragungsfunktion lautet:

$$G(z)=\frac {Y(z)} {U(z)}=\frac {\text {Zählerpolynom}\ (z)} {\text {Nennerpolynom}\ (z)}$$

-   Gegebene Übertragungsfunktionen des s-Bereiches in Verbindung mit Haltegliedern und Abtastelementen können ebenfalls mit Hilfe der Korrespondenztabellen als z-Übertragungsfunktion transformiert werden.
-   Die Rücktransformation von der z-Übertragungsfunktion in den zeitdiskreten Bereich als Differenzengleichung erfolgt durch den invers angewendeten Linearitätssatz und Verschiebungssatz für alle einzelnen Terme. Durch die kreuzweise Multiplikation von $y_{(k)}$ und $u_{(k)}$ mit den Polynomen im Zähler und Nenner der z-Übertragungsfunktion entsteht wieder eine Differenzengleichung $y_{(k)}$, wenn die einzelnen Terme der inversen Transformation unterzogen werden.

Mit der so errechneten Differenzengleichung des Übertragungssystems ist man nun in der Lage, für eine gegebene Eingangserregung $u_{(k)}$ des Systems die Ausgangsfolgen des Systems $y_{(k)}$ zu berechnen. Dies ist auf verschiedenen Arten möglich.

-   Analytische Berechnung mit Hilfe der Korrespondenztabellen der z-Transformation,
-   Rekursive Berechnung von Systemantworten der Differenzengleichungen mit Bezug auf zurückliegende Folgen k.

**Entstehung der z-Übertragungsfunktion:**

Ein zeitdiskretes dynamisches System wird durch eine rekursive Differenzengleichung beschrieben.

Wie bei zeitkontinuierlichen Systemen $g(t)$ und der Übertragungsfunktion $G(s)$ besteht eine vergleichbare Beziehung bei den zeitdiskreten Systemen zwischen der Gewichtsfolge $g(k)$ und z-Übertragungsfunktion G(z). Die Übertragungsfunktion $G(z)$ ist die z-Transformierte der Gewichtsfolge $g(k)$.

![Beziehung der Gewichtsfolge $g(k)$ zur z-Übertragungsfunktion $G(z)$.\|300](https://upload.wikimedia.org/wikipedia/commons/f/f6/Blockdiagramm_z-%C3%9Cbertragungsfunktion.png) 


$G(z) \ \bullet \!\!-\!\!\circ \ g(k)$

In G(z) und g(k) sind alle Eigenschaften eines dynamischen Systems enthalten. Zur Systemberechnung wird der Verlauf des Eingangssignals U(z) und das Systemverhalten G(z) oder g(k) benötigt.

Für die Ermittlung der z-Übertragungsfunktion ist die Gewichtsfunktion g(t) die Systemantwort (Impulsantwort) auf die Vorgabe eines Eingangs-DIRAC-Impulses $\delta$(t).

Bei der Laplace-Transformation eines Systems lautet die Übertragungsfunktion:

$$G(s) = \frac {Y(s)} {U(s)} = \frac {\text {Zählerpolynom}\ (s)} {\text {Nennerpolynom}\ (s)} \ | \qquad \text{mit } U(s)= \delta (t)$$

Aus der Gewichtsfunktion wird die Impulsfolgefunktion $g^*(t)$ oder die Gewichtsfolge g(kT_(A)) gebildet und in den z-Bereich transformiert. Die z-Übertragungsfunktion von zeitkontinuierlichen Systemen ergibt sich mit folgender Vorschrift:

  
$G(z)= \mathcal Z \{g(t) |_{t=kT_A} \}=\mathcal Z \{\mathcal L^{-1} \{G(s) \}|_{t=kT_A} \}$

Die Berechnung der Impulsübertragung von linearen zeitdiskreten Systemen vereinfacht sich, wenn aus der Differenzengleichung mit der z-Transformation die z-Übertragungsfunktion bestimmt wird. So können z. B. die Regelalgorithmen eines digitalen Reglers mit Differenzengleichungen formuliert werden.[1][2]

Ist die z-Übertragungsfunktion eines Systems G(z) gegeben, lässt sich die zugehörige z-Differenzengleichung bestimmen:

-   durch Ausmultiplizieren von Zähler und Nenner $y(z)$ und $u(z)$ und Gleichungsumstellung nach y(z),
-   Anwendung des rechts-Verschiebesatzes der z-Transformation zur Bestimmung der Ausgangsgröße $y_{(k)}$.

**Es wird eine lineare Differenzengleichung eines Regelalgorithmus gegeben:**

Die Eingangssignale der Differenzengleichung sind wieder $u_{(k)}$ und die Ausgangssignale $y_{(k)}$.

  
$a_n \cdot y_{(k+n)} + a_{n-1} \cdot y_{(k+n-1)} + \cdots + a_1 \cdot y_{(k+1)} + a_0 \cdot y_{(k)} = b_m \cdot u_{(k+m)}+ b_{m-1} \cdot u_{(k+m-1)}+ \cdots + b_1 \cdot u_{(k+1)} + b_0 \cdot u_{(k)} | \qquad n \geq m$

Unter der Voraussetzung, dass die Anfangswerte des zeitdiskreten Systems gleich Null sind, wird die Differenzengleichung transformiert. Mit den Rechenregeln des rechts-Verschiebungssatzes ergibt sich die Transformationsvorschrift:

  
$y_{(k)} \to y(z), \qquad y_{(k+i)} \to z^i \cdot y(z), \qquad y_{(k-i)} \to z^{-i} \cdot y(z)$,

&nbsp;

  
$u_{(k)} \to u(z), \qquad u_{(k+i)} \to z^i \cdot u(z), \qquad u_{(k-i)} \to z^{-i} \cdot u(z)$

Die z-transformierte Differenzengleichung ergibt sich zu:

  
$a_n \cdot z^n \cdot Y(z)+ a_{n-1} \cdot z^{n-1}\cdot Y(z)+ \cdots + a_1 \cdot z \cdot Y(z) + a_0 \cdot Y(z) = b_m \cdot z^m \cdot U(z)+ b_{m-1} \cdot z^{m-1}\cdot U(z)+ \cdots + b_1 \cdot z \cdot U(z) + b_0 \cdot U(z)$

Durch Ausklammern des Quotienten Y(z) / U(z) kann die Impulsübertragungsfunktion G(z) gebildet werden.

Damit lautet die z-Übertragungsfunktion:

  
{\|

\|- \| $G(z) = \frac {Y(z)} {U(z)} = \frac {b_m \cdot z^m + b_{m-1} \cdot z^{m-1} + \cdots + b_1 \cdot z + b_0 } {a_n \cdot z^n + a_{n-1} \cdot z^{n-1} + \cdots + a_1 \cdot z + a_0} = \frac {\text{Zähler}(z)} {\text{Nenner}(z)}$ \|}

Bei der Berechnung von Differenzengleichungen mit dem Digitalrechner ist die von n-Schritten nach rechts verschobene Gleichung besser geeignet.

  
$a_n \cdot y_{(k)} + a_{n-1} \cdot y_{(k-1)} + \cdots + a_1 \cdot y_{(k-n+1)} + a_0 \cdot y_{(k-n)} = b_m \cdot u_{(k-n+m)}+ b_{m-1} \cdot u_{(k-n+m-1)}+ \cdots + b_1 \cdot u_{(k-n+1)}+b_0 \cdot u_{(k-n)}$

Damit lautet die z-Übertragungsfunktion mit negativen Exponenten von z:

  
{\|

\|- \| $G(z) = \frac {Y(z)} {U(z)} = \frac {b_m \cdot z^{m-n} + b_{m-1} \cdot z^{m-1-n} + \cdots + b_1 \cdot z^{-n+1} + b_0 \cdot z^{-n}} {a_n + a_{n-1} \cdot z^{-1} + \cdots + a_1 \cdot z^{-n+1} + a_0 \cdot z^{-n}}$ \|}

**Beispiel:** Für eine gegebenen Differenzengleichung 3. Ordnung lautet die z-Übertragungsfunktion für Ordnungen m = 2 und n = 3:

  
$G(z) = \frac {Y(z)} {U(z)}=\frac {b_2 \cdot z^2+b_1 \cdot z + b_0} {a_3 \cdot z^3 + a_2 \cdot z^2+a_1 \cdot z+a_0}$

Mit der rechts-Verschiebung der zugehörigen Differenzengleichung um n = 3 Abtastschritte $T_A$ lautet die z-Übertragungsfunktion:

  
{\|

\|- \| $G(z) = \frac {Y(z)} {U(z)}=\frac {b_2 \cdot z^{-1}+b_1 \cdot z^{-2} + b_0 \cdot z^{-3}} {a_3 + a_2 \cdot z^{-1}+a_1 \cdot z^{-2}+a_0 \cdot z^{-3}}$ \|}

Es fällt auf, dass die z-Transformation einer Differenzengleichung eine große Ähnlichkeit mit der Polynomform einer s-Übertragungsfunktion für kontinuierliche Systeme hat. Ebenso fällt auf, dass die z-Übertragungsfunktion negative Potenzen hat. Allgemein werden z-Übertragungsfunktionen mit negativen Potenzen von z dargestellt.

Jede z-Übertragungsfunktion mit negativen Potenzen von z kann in eine Form mit positiven Potenzen von z gebracht werden, wenn Zähler und Nenner der z-Übertragungsfunktion mit der höchsten vorkommenden inversen z-Potenz multipliziert werden. Für die z-Übertragungsfunktion der Form mit positiven Exponenten muss gelten: Nennerpolynom &gt; Zählerpolynom. Ist diese Bedingung erfüllt, ist G(z) kausal.

Es können sowohl abgetastete Eingangssignale u(kT_(A)) als auch Differenzengleichungen f(kT_(A)), die im diskreten Zeitbereich das Verhalten eines Systems (z. B. den Regelalgorithmus eines Reglers) beschreiben, als z-Übertragungsfunktionen in den z-Bereich transformiert und als algebraische Gleichungen behandelt werden.

Wird eine inverse z-Transformation der z-Übertragungsfunktionen durchgeführt, entsteht die Lösung der zeitdiskreten Differenzengleichung $f_{(k)}= \mathcal Z^{-1} \{F(z) \}$ im $f(kT_A)$-Bereich. Mit Hilfe verschiedener Verfahren der Rücktransformation vom z-Bereich in den k-Bereich ergeben sich dann als Lösung die Differenzengleichungen des Regelalgorithmus für den diskreten Bereich f(kT_(A)).

Die typische Anwendung der z-Transformation eines digitalen Systems, eines [digitalen Reglers](Digitaler_Regler "wikilink") oder eines [digitalen Filters](Digitales_Filter "wikilink"), für den Regelalgorithmus lautet wie folgt:

-   Die Abtastfolge des Eingangssignals (Eingangsfolge) wird transformiert als z-Übertragungsfunktion $H(z)$,
-   Die Differenzengleichung $f_{(k \cdot T_A)}$ des gewünschten Reglerverhaltens wird transformiert als z-Übertragungsfunktion $G(z)$,
-   Die z-transformierten Systeme werden algebraisch entsprechend der z-Rechenregeln zusammengefasst,
-   Mit der inversen z-Transformation des z-Produktes von Signal und Regelalgorithmus entsteht der Berechnungsalgorithmus des digitalen Reglers (Mikro Computers) wieder als Differenzengleichung.

Die Analyse und die Synthese diskreter Signale und Systeme lässt sich mit der z-Transformation erleichtern, setzt aber auch umfangreiches mathematisches Spezialwissen voraus.

Für die häufig vorkommenden Transformationen des k- und z-Bereich stehen in vielen Fachbüchern der Regelungstechnik Transformationstafeln zur Verfügung.

### Z-Übertragungsfunktion einer Totzeit

Eine Totzeit T_(t) hat im Zeitbereich das Verhalten $\displaystyle y(t) = {u}(t-T_t)$.

Im s-Bereich lautet die Übertragungsfunktion eines Totzeitsystems:

$$G(s)=\frac{y(s)}{u(s)}=e^{-s\cdot T_t}$$

Es handelt sich hier bei der Verbindung einer s-Übertragungsfunktion als gebrochen-rationalen Funktion mit einem Totzeitglied um eine transzendente Funktion, die als Anhang einer Übertragungsfunktion – beispielsweise einer Regelstrecke – multiplikativ zugeordnet wird, mit der Einschränkung, dass keine algebraische Behandlung erlaubt ist.

Im z-Bereich entspricht eine Totzeit $T_t=d \cdot T_A$ einer Rückwärtsverschiebung (Verschiebung nach rechts) der Abtastfolgen um d Abtastschritte. Die z-Übertragungsfunktion des Totzeitgliedes in Verbindung mit weiteren z-Übertragungssystemen bleibt gebrochen-rational (Bruch mit Zähler- und Nennerpolynom).

Für die z-Transformation der Abtastfolge für das Signal $u_{(k-d)}$ gilt:

  
{\|

\|- \|$u_{(k-d)} \ \circ \!\!-\!\!\bullet \ z^{-d} \cdot U(z)$ \|}

Anders als bei der Laplace-Transformation bedeutet ein Totzeitglied in Verbindung mit einer z-Übertragungsfunktion keine Einschränkung der bestehenden Form der gebrochen-rationalen Funktion. Eine z-Übertragungsfunktion mit einer mit $d$ Abtastschritten $T_A$ definierten Totzeit $T_t=d \cdot T_A$ wird durch Hinzufügen eines Terms $z^{-d}$ berücksichtigt. Es können beliebige algebraische Operationen durchgeführt werden.

Beispiel einer z-Übertragungsfunktion mit Totzeit:

  
$G(z) = \frac {Y(z)} {U(z)} = \frac {b_m \cdot z^m + b_{m-1} \cdot z^{m-1} + \cdots + b_1 \cdot z + b_0 } {a_n \cdot z^n + a_{n-1} \cdot z^{n-1} + \cdots + a_1 \cdot z + a_0} \cdot z^{-d}$

### Z-Übertragungsfunktion von zeitkontinuierlichen Elementen G(s) mit Abtaster und Halteglied

**Definition der Signale:** Allgemein gilt für den Zeitbereich $f(t)$, zeitdiskreten Bereich $f(k)$ und Bildbereich $f(s)$, $f(z)$ die Eingangsgröße $u$ und die Ausgangsgröße $y$.

**[Abtastsysteme](Sample-and-Hold-Schaltung "wikilink")** erlauben eine Umwandlung kontinuierlicher Signale in zeitdiskrete Abtastfolgen (Impulsfolgen). Halteglieder erlauben eine Umwandlung zeitdiskreter Ausgangsfolgen (Impulsfolgen) in kontinuierliche gestufte Signale im Zeitbereich. Ein Abtaster setzt ein kontinuierliches Signal $u(t)$ in Verbindung mit einem nachgeschalteten A/D-Wandler in eine Zahlenfolge $u(k)$ mit digitalen Werten um.

Ein **Halteglied** nullter Ordnung setzt eine Zahlenfolge $u_{(k)}$ mit einem vorgeschalteten D/A-Wandler in ein gestuftes kontinuierliches Signal $u(t)$ um. Bei der Reihenschaltung von einem Abtastsystem (gewichteter δ-Abtaster) und einem Halteglied handelt es sich um die Umwandlung einer aus einem kontinuierlichen Eingangssignal modulierten Impulsfolge in eine gestufte Treppenfunktion $f(t)$, die in ein kontinuierliches dynamisches System eingeleitet werden kann.

Liegt ein kontinuierliches **dynamisches System** vor, erlaubt die Abtastung eines kontinuierlichen Signals, z. B. eine Regelabweichung, die Verarbeitung einer zeitdiskreten Eingangsfolge in einem Mikrocomputer als Regelalgorithmus zu einer zeitdiskreten Ausgangsfolge. Die über ein Halteglied geleitete Ausgangsfolge erzeugt ein quasi stetiges gestuftes Ausgangssignal zu einer analogen zeitabhängigen Stellgröße.

Je nach Anwendung des kontinuierlichen Systems $G(s)$, beispielsweise in der Regelungstechnik, werden unterschiedlich Funktionsblöcke zusammengefasst, die auch mehrere Abtaster und Halteglieder enthalten können.

Um ein kontinuierliches System $G(s)$ in eine z-Übertragungsfunktion (Impulsübertragungsfunktion) zu definieren, muss es im Eingang durch eine Abtastfolge $e_{(k)}$ als Eingangsfolge und am Ausgang des Systems zeitsynchron durch einen Abtaster die Ausgangsfolge $u_{(k)}$ zur Verfügung stellen.

![mini\|500px\|Berechnung der Varianten kontinuierlicher Systeme $G(s)$ mit Abtaster und Halteglied.](Varianten_kontinuierlicher_Systeme_mit_Abtaster_und_Halteglied.png "mini|500px|Berechnung der Varianten kontinuierlicher Systeme G(s) mit Abtaster und Halteglied.")

Je nachdem wie die Reihenfolge der Funktionsblöcke eines Haltegliedes $G_H(s)$, eines Systems $G(s)$ und eines Abtasters festgelegt sind, können diese Funktionsblöcke als ein Teil einer offenen Regelstrecke betrachtet werden. Die wären z. B.:

-   Ein Haltegliedsystem mit analogem Ausgang, ein dynamisches System $G(s)$ und Abtastsystem für eine Ausgangsfolge,
-   Ein Abtastsystem einer analogen Regelabweichung, Mikroprozessor für den Regelalgorithmus des Systems $G(s)$ und ein Haltegliedsystem für die Ausgabe eines kontinuierlichen Signals als Stellgröße für eine kontinuierliche Regelstrecke.

Das obere Grafikbild zeigt die Kombination der Funktionsblöcke Halteglied, kontinuierliches System $G(s)$ und Abtaster.

Damit ein kontinuierliches System $G(s)$ in eine (Impuls-)Übertragungsfunktion $G(z)$ definiert werden kann, muss das System durch eine Impulsfolge (Wertefolge) gespeist und am Ausgang ein Abtaster eingesetzt sein, der synchron zur Eingangsfolge eine Ausgangsfolge realisiert. Das Halteglied vor dem dynamischen System wandelt die Impulsfolge in ein quasikontinuierliches Signal um. Das kontinuierliche System-Ausgangssignal wird über einen Abtaster als Ausgangsfolge definiert.

Die s-Übertragungsfunktion des Haltegliedes $G_H(s)$ nullter Ordnung lautet: [3]

$$G_H(s)=\frac {\bar U(s)}{ \hat U(s)}=\frac {1-e^{T_A \cdot s}} s$$

Die z-Übertragungsfunktion (Impulsübertragungsfunktion) des Haltegliedes $G_H(s)$ und der Regelstrecke $G_S(s)$ wird durch die z-Transformation von $\mathcal Z \{ G_H(s) \cdot G_S(s) \}$ berechnet.

Die z-Übertragungsfunktion von Halteglied und Regelstrecke lautet:

  
$G_{HS}(z)=\left. \mathcal Z \{ G_H(s) \cdot G_S(s) \right|_{t=kT_A} \}=\mathcal Z \{ G_H(s) \cdot G_S(s) \}$

In diese Gleichung wird $G_H(s)$ eingesetzt:

  
$G_{HS}(z)=\mathcal Z \biggl \{ \frac {1-e^{-T_As}} {s} \cdot G_S(s) \biggr \}= \mathcal Z \biggl \{ \frac {G_S(s)} s \biggr \} - \mathcal Z \biggl \{ \frac {e^{-T_As} \cdot G_S(s)} s \biggr \}$

Eine Multiplikation mit $e^{-sT_A}$ entspricht im z-Bereich eine Rechtsverschiebung um einen Abtastzyklus $T_A$ und damit einer Multiplikation mit $z^{-1}$.

  
$G_{HS}(z)=\mathcal Z \biggl \{ \frac {1-e^{-T_As}} {s} \cdot G_S(s) \biggr \}=(1-z^{-1}) \cdot \mathcal Z \biggl \{ \frac {G_S(s)} s \biggr \}$

Die z-Übertragungsfunktion der Reihenschaltung eines Haltegliedes nullter Ordnung mit einem kontinuierlichen System ergibt sich aus der Laplace-Transformierten der Sprungantwort $G_S(s)$, multipliziert mit $\frac {z-1} z$. (Siehe Tabelle $\frac 1 s \ \circ \!\!-\!\!\bullet \ \frac z {z-1}$):

  
{\|

\|- \| $G_{HS}(z)= \frac {Y{(z)}} {U{(z)}}= \frac {z-1} z \cdot \mathcal Z \biggl \{ \frac {G_S(s)} s \biggr \}$ \|}

Analog wie bei der Regelstrecke $G_S(s)$ kann für die im 2. Teil des Bildes dargestellte Anordnung der Funktionsblöcke Abtaster, Regelalgorithmus des Reglers und Halteglied die gleiche Form der Gleichung der z-Transformation benutzt werden. Ein- und Ausgangsgröße und die Systemgröße des Reglers $G_R(s)$ werden getauscht:

  
{\|

\|- \| $G_{HR}(z)= \frac {U{(z)}} {E{(z)}}= \frac {z-1} z \cdot \mathcal Z \biggl \{ \frac {G_R(s)} s \biggr \}$ \|}

Um die z-Transformation des kontinuierlichen Systems $G(s)$ bilden zu können, werden die Korrespondenztabellen angewendet. Steht für die gegebene s-Übertragungsfunktion $G(s)$ kein Eintrag für die z-Transformation zur Verfügung, muss eine Partialbruchzerlegung von $G(s)/s$ vorgenommen werden.

**Beispiel:** z-Transformation eines $IT_1$-Gliedes.

  
$G(s)=\frac 1 {s \cdot (s+1)}$

Gesucht z-Übertragungsfunktion $G_{HS}(z)$ des kombinierten Systems:

  
$G_{HS}(z)= \frac {Y{(z)}} {U{(z)}}= \frac {z-1} z \cdot \mathcal Z \biggl \{ \frac 1 {s^2 \cdot (s+1)} \biggr \}$

Partialbruchzerlegung von

  
$\frac 1 {s^2 \cdot (1+s)}= \frac 1 {s^2} - \frac 1 s + \frac 1 {(s+1)}$

z-Transformation der Partialbrüche in den z-Bereich:

  
$G_{HS}(z)= \frac {Y{(z)}} {U{(z)}}= \frac {z-1} z \cdot \mathcal Z \biggl \{ \frac 1 {s^2} - \frac 1 s + \frac 1 {(s+1)} \biggr \} = \frac {z-1} z \cdot \biggl \{ \frac {T_A \cdot z}{(z-1)^2} - \frac z {z-1} + \frac z {z-e^{-T_A}} \biggr \}$

Durch Ausmultiplizieren der Brüche ergibt sich die z-Transformation:

  
{\|

\|- \| $G_{HS}(z)=\frac {Y(z)}{U(z)}=\frac {T_A}{z-1} -1 + \frac {z-1} {z-e^{-T_A}}$ \|}

### Z-Übertragungsfunktionen der Standardregler

Es gelten hier allgemein die formalen Begriffe der Ein- und Ausgangsgrößen der Systemtheorie: Eingangssignal = $U(z)$, Ausgangssignal $Y(z)$. Für die Belange der Regler gelten die Eingangs- und Ausgangsgrößen des Reglers zu einem Regelkreis lauten: $E(z)$ und $U(z)$.

Die Regelalgorithmen mit den allgemeinen Koeffizienten lauten nach der rekursiven Rechenvorschrift: [4]

  
$y_{(k)}=a_1 \cdot y_{(k-1)}+b_0 \cdot u_{(k)}+b_1 \cdot u_{(k-1)}+b_2 \cdot u_{(k-2)}$

Die z-Transformation der Differenzengleichung liefert die z-Übertragungsfunktion G_(R)(z) des Reglers:

  
$G_R(z) = \frac {Y(z)} {U(z)}=\frac{b_0+b_1 \cdot z^{-1}+b_2 \cdot z^{-2}} {1-a_1 \cdot z^{-1}}=\frac {b_0 \cdot z^2+b_1 \cdot z+b_2}{z^2-a_1 \cdot z}$

**Tabelle der z-Übertragungsfunktionen der Standardregler (Typ II, Obersumme)**

(a_(i) = Koeffizienten des Nennerpolynoms, b_(i) = Koeffizienten der Zählerpolynoms, T_(I) = T_(N) = 1 / K_(I) = Zeitkonstante = Nachstellzeit, T_(V) = Vorhaltezeit, T_(A) = Abtastzeit)

| Reglerart  | z-Übertragungsfunktion G_(R)(z) der Standardregler                                                                                                                                                                                                                                                                         |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| P-Regler   | $G_R(z) =b_0, \ b_0 = K_R$                                                                                                                                                                                                                                                                                                 |
| I-Regler   | $G_R(z)= \frac {b_0 \cdot z}{z-a_1}= \frac {b_0}{1-a_1 \cdot z^{-1}}$ $a_1 = 1; \ b_0=K_I \cdot T_A$                                                                                                                                                                                                                       |
| PD-Regler  | $G_R(z)=\frac {b_0 \cdot z +b_1}z=b_0+b_1 \cdot z^{-1}$ $b_0=K_R \cdot \left[1+ \frac {T_V} {T_A}\right]; \ b_1=-K_R \cdot \frac {T_V} {T_A}$                                                                                                                                                                              |
| PI-Regler  | $G_R(z)= \frac {b_0 \cdot z+b_1} {z-a_1}= \frac {b_0+b_1 \cdot z^{-1}} {1-a_1 \cdot z^{-1}}$ $a_1=1; \ b_0 = K_R \cdot \left[1+ \frac {T_A}{T_N}\right]; \ b_1 = -K_R$                                                                                                                                                     |
| PID-Regler | $G_R(z)=\frac {b_0 \cdot z^2 + b_1 \cdot z +b_2} {z^2 -a_1 \cdot z} = \frac {b_0 + b_1 \cdot z^{-1}+ b_2 \cdot z^{-2}}{1-a_1 \cdot z^{-1}}$ $a_1=1; \ b_0=K_R \cdot \left[1+ \frac {T_A} {T_N}+ \frac {T_V} {T_A}\right]; \ b_1=-K_R \cdot \left[1 + 2 \cdot \frac {T_V} {T_A}\right]; \ b_2 =K_R \cdot \frac {T_V} {T_A}$ |

### Umwandlung einer z-Übertragungsfunktion in eine Differenzengleichung

Eine gegebene z-Übertragungsfunktion lässt sich in eine Differenzengleichung umwandeln. Dazu sind folgende Schritte erforderlich.[5]

Die Übertragungsfunktion wurde durch den Koeffizienten $a_n$ dividiert, um $z^n$ freistellen zu können.

Diese Form der Übertragungsfunktion wurde entsprechend der dargestellten Koeffizienten wie folgt neu geordnet.

$$G(z) = \frac {Y(z)} {U(z)} = \frac {b_m \cdot z^m + b_{m-1} \cdot z^{m-1} + b_{m-2}\cdot z^{m-2} \cdots + b_1 \cdot z + b_0 } {z^n + a_{n-1} \cdot z^{n-1} + a_{n-2} \cdot z^{n-2} + \cdots + a_1 \cdot z + a_0} = \frac {\text{Zähler}(z)} {\text{Nenner}(z)}$$

-   Die Systemausgangsgröße Y(z) und die Systemeingangsgröße U(z) werden kreuzweise mit den Polynomen der z-Übertragungsfunktion multipliziert:

$${b_m \cdot z^m \cdot U(z) + b_{m-1} \cdot z^{m-1}\cdot U(z) + b_{m-2}\cdot z^{m-2}\cdot U(z)+ \cdots + b_1 \cdot z \cdot U(z)+ b_0 \cdot U(z)=
z^n\cdot Y(z) + a_{n-1} \cdot z^{n-1}\cdot Y(z) + a_{n-2} \cdot z^{n-2}\cdot Y(z) + \cdots + a_1 \cdot z\cdot Y(z) + a_0\cdot Y(z)}$$

-   Die Zähler- und Nennerpolynome werden durch die höchste Potenz von z dividiert:

$${b_m \cdot z^{-(n-m)} \cdot U(z) + b_{m-1} \cdot z^{-(n-m+1)}\cdot U(z) + b_{m-2}\cdot z^{-(n-m+2)}\cdot U(z)+ \cdots + b_0 \cdot z^{-n} \cdot U(z)= Y(z) + a_1 \cdot z^{-(n-1)}\cdot Y(z) + a_2 \cdot z^{-(n-2)}\cdot Y(z) + a_0 \cdot z^{-n}\cdot Y(z)}$$

-   Mit der Anwendung des Rechtsverschiebungssatzes der z-Transformation entsteht die Differenzengleichung:

  
  
${b_m \cdot u[k-n+m]+b_{m-1} \cdot u[k-n+m-1]+\dots +b_1 \cdot u[k-n+1]+b_0 \cdot u[k-n]=y[k]+a_{n-1} \cdot y[k-1]+ \dots +a_1 \cdot y[k-n+1]+a_0 \cdot y[k-n]}$

-   Die Differenzengleichung wird nach y(k) aufgelöst. Damit entsteht eine Rekursionsgleichung zur Berechnung der Ausgangsgröße $y_{(k)}$ des Systems für beliebige Eingangssignale $u_{(k)}$.

  
  
{\|

\|- \|$y_{k}= -a_{n-1} \cdot y_{(k-1)}- \dots - a_1 \cdot y_{(k-n+1)} -a_0 \cdot y_{(k-n)} + b_m \cdot u_{(k-n+m)} + \dots + b_1 \cdot u_{(k-n+1)}+ b_0 \cdot u_{(k-n)}$ \|}

[1] Holger Lutz, Wolfgang Wendt: *Taschenbuch der Regelungstechnik* *mit MATLAB und Simulink*, 11. Auflage, Verlag Europa-Lehrmittel, 2019, ISBN 978-3-8085-5869-0, Kapitel: *z-Übertragungsfunktion (Impulsübertragungsfunktion)*.

[2] Gerd Schulz: *Regelungstechnik 2 Mehrgrößenregelung, Digitale Regelungstechnik, Fuzzyregelung.* 2. Auflage, Oldenbourg Verlag, 2008, Kapitel: *Diskrete Übertragungsfunktion*.

[3] Holger Lutz, Wolfgang Wendt: *Taschenbuch der Regelungstechnik* *mit MATLAB und Simulink*, 11. Auflage, Verlag Europa-Lehrmittel, 2019, ISBN 978-3-8085-5869-0, Kapitel: *z-Übertragungsfunktion von zeitkontinuierlichen Elementen*.

[4] Holger Lutz, Wolfgang Wendt: *Taschenbuch der Regelungstechnik mit MATLAB und Simulink*, 11. Auflage, Verlag Europa-Lehrmittel, 2019, ISBN 978-3-8085-5869-0, Kapitel: *z-Transformation / z-Übertragungsfunktion von Regelalgorithmen*.

[5] Prof. Dr. Ferdinand Svaricek: Universität Bundeswehr München, Vorlesungsskript: 83 Seiten, erstellt April 2012, Kapitel: *z-Übertragungsfunktion und Differenzengleichung*.
