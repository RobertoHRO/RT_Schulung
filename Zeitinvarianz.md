Die **Zeitinvarianz** ist in der [Systemtheorie](https://de.wikipedia.org/wiki/Systemtheorie_(Ingenieurwissenschaften) "Systemtheorie (Ingenieurwissenschaften)") die Eigenschaft eines Systems, zu jeder Zeit das gleiche Verhalten bei gleicher Eingabe zu zeigen – es ist über die Zeit [invariant](https://de.wikipedia.org/wiki/Invarianz "Invarianz"). Die Parameter seiner mathematischen Beschreibung sind zeitlich unveränderlich, und die [Matrizen](https://de.wikipedia.org/wiki/Matrix_(Mathematik) "Matrix (Mathematik)") der [Zustandsraumdarstellung](https://de.wikipedia.org/wiki/Zustandsraumdarstellung "Zustandsraumdarstellung") sind konstant.

Ein System ist ein Gebilde mehrerer Elemente, die eine Einheit bilden, z. B. eine elektronische Schaltung oder ein Pendel. Die Parameter eines Systems sind dann die Kenngrößen der elektronischen Bauteile oder geometrische Abmessungen.

Gemeinsam mit der [Linearität](https://de.wikipedia.org/wiki/Lineares_System_(Systemtheorie) "Lineares System (Systemtheorie)") vereinfacht sich die Systembeschreibung damit zu den [linearen, zeitinvarianten Systemen](https://de.wikipedia.org/wiki/Lineares_zeitinvariantes_System "Lineares zeitinvariantes System").

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Zeit_verschiebung.png/220px-Zeit_verschiebung.png)](https://de.wikipedia.org/wiki/Datei:Zeit_verschiebung.png)

Zeitinvarianz

Aus der [Systemeigenschaft](https://de.wikipedia.org/wiki/Systemeigenschaften "Systemeigenschaften") Zeitinvarianz folgt, dass die zeitliche Verschiebung des Eingangssignals des Systems zu einer gleichartigen Verschiebung des Ausgangssignals führt, ohne dessen zeitlichen Verlauf in anderer Form zu beeinflussen.

Das heißt, das System

y ( t ) \= H { x ( t ) } {\\displaystyle y(t)=H\\{x(t)\\}} ![{\displaystyle y(t)=H\{x(t)\}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/6a01af02f1c26aac3e84ab9604934f998e419a97) 

liefert auf ein Eingangssignal x {\\displaystyle x} ![x](https://wikimedia.org/api/rest_v1/media/math/render/svg/87f9e315fd7e2ba406057a97300593c4802b53e4) , das um die Zeit  t  0     {\\displaystyle t\_{0}} ![t_{0}](https://wikimedia.org/api/rest_v1/media/math/render/svg/02d3006c4190b1939b04d9b9bb21006fb4e6fa4a) verzögert wurde, ein gleiches, entsprechend verzögertes Ausgangssignal y   {\\displaystyle y} ![y](https://wikimedia.org/api/rest_v1/media/math/render/svg/b8a6208ec717213d4317e666f1ae872e00620a0d) :

y ( t − t 0 ) \= H { x ( t − t 0 ) } . {\\displaystyle y(t-t\_{0})=H\\{x(t-t\_{0})\\}.} ![{\displaystyle y(t-t_{0})=H\{x(t-t_{0})\}.}](https://wikimedia.org/api/rest_v1/media/math/render/svg/7192990299ae73be3be5782f9f6f31c6f787d770) 

Ein System, das die oben beschriebene Eigenschaft _nicht_ besitzt, wird als zeit_variant_ bezeichnet.

Energieerhaltung
----------------

Nach dem [Noether-Theorem](https://de.wikipedia.org/wiki/Noether-Theorem "Noether-Theorem") gehört in der [Physik](https://de.wikipedia.org/wiki/Physik "Physik") zu jeder kontinuierlichen [Symmetrie](https://de.wikipedia.org/wiki/Symmetrie_(Physik) "Symmetrie (Physik)") auch eine [Erhaltungsgröße](https://de.wikipedia.org/wiki/Erhaltungsgr%C3%B6%C3%9Fe "Erhaltungsgröße"). Zur Zeitinvarianz ([Homogenität](https://de.wikipedia.org/wiki/Homogenit%C3%A4t "Homogenität") der Zeit) gehört die [Energieerhaltung](https://de.wikipedia.org/wiki/Energieerhaltungssatz "Energieerhaltungssatz").

Beispiele für zeitlich invariante Systeme sind [abgeschlossene Systeme](https://de.wikipedia.org/wiki/Abgeschlossenes_System "Abgeschlossenes System"), z. B. ein [ideales](https://de.wikipedia.org/wiki/Idealisierung_(Physik) "Idealisierung (Physik)") [Pendel](https://de.wikipedia.org/wiki/Pendel "Pendel") ohne Berücksichtigung der [Reibung](https://de.wikipedia.org/wiki/Reibung "Reibung"). Bei diesem ändern sich zwar zusammen mit der Geschwindigkeit des Pendels (also des Systems) seine [kinetische Energie](https://de.wikipedia.org/wiki/Kinetische_Energie "Kinetische Energie") und mit dessen Lage im Raum seine [potentielle Energie](https://de.wikipedia.org/wiki/Potentielle_Energie "Potentielle Energie") zeitlich, jedoch bleibt deren Summe, die Gesamtenergie, konstant. Es ist egal, zu welchem Zeitpunkt das Pendel betrachtet wird; seine Energie E ist immer gleich:

d E d t \= 0 ⇔ E \= const. {\\displaystyle {\\frac {\\mathrm {d} E}{\\mathrm {d} t}}=0\\quad \\Leftrightarrow \\quad E={\\text{const.}}} ![{\displaystyle {\frac {\mathrm {d} E}{\mathrm {d} t}}=0\quad \Leftrightarrow \quad E={\text{const.}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/5b0c78248065173b1d16b1b4a2184d959d67e0f2) 

Beispiele
---------

**1\. Beispiel** Ein [elektrischer Widerstand](https://de.wikipedia.org/wiki/Elektrischer_Widerstand "Elektrischer Widerstand") R ist zeitinvariant. Fließt durch ihn ein konstanter Strom I, dann fällt an ihm eine Spannung U von U \= R ⋅ I {\\displaystyle U=R\\cdot I} ![{\displaystyle U=R\cdot I}](https://wikimedia.org/api/rest_v1/media/math/render/svg/4ba72ed476400f92d4bc06e68bce05489b404c5d) ab. Auch mehrere Minuten später liegt an ihm die gleiche Spannung an.

Bei genauerer Betrachtung ist die Spannung geringfügig höher, weil sich der Widerstand durch den Stromfluss erwärmt hat. Diese Erwärmung ist aber nicht direkt von der Zeit abhängig, sondern von dem Eingangssignal Strom, der Wärmeabgabe und der Ausgangstemperatur. Unter gleichen Ausgangsbedingungen wird er zu jeder Zeit die gleiche Spannung liefern.

**2\. Beispiel** Stellen Sie sich folgende zwei Systeme vor:

-   System A: y ( t ) \= t ⋅ x ( t ) {\\displaystyle y(t)=t\\cdot x(t)} ![{\displaystyle y(t)=t\cdot x(t)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/3df88b7d459f2501df6ec79587e26cd5166d3fae) 
-   System B: y ( t ) \= 10 ⋅ x ( t ) {\\displaystyle y(t)=10\\cdot x(t)} ![{\displaystyle y(t)=10\cdot x(t)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/be6262c80fb83ff200f608c8971ac6b9f1bd9808) 

Da System A eindeutig von _t_ abhängt, ist dieses zeitvariant. Das System B ist nicht direkt von _t_ abhängig und ist deswegen zeit_in_variant.