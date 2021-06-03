Modellbasierte Regelung
-------------------------


---


## Struktur 1 

- performante Regelungen berücksichtigen das Streckenverhalten
- bei der Modellbasierten Regelung wird das Streckenmodell direkt in der Struktur berücksichtigt:

![Quelle: Lunze 2016 Abbildung 12.4 \|600](Pasted%20image%2020210421121602.png)

- Oft auch als *Internal Model Control (IMC)* bezeichnet
-  Es wird der Modellfehler $Y(s)-\hat{Y}(s)$ zurückgeführt

----

## Struktur 2


![Quelle: Lunze 2016 Abbildung 12.4 \|400](Pasted%20image%2020210421121602.png)
![Quelle: Lunze 2016 Abbildung 12.5 \|300](Pasted%20image%2020210421122229.png)

Beide Strukturen liefern bei gleicher Anregung gleiche Stell- und Regelgrößen! - Strukturen sind äquivalent.

----

## Analyse
![Quelle: Lunze 2016 Abbildung 12.4 \|400](Pasted%20image%2020210421121602.png)

- Wenn Modell und Regelstrecke perfekt passen, und keine Störungen auftreten gilt:  $Y(s)-\hat{Y}(s) = 0$. --> Dann arbeitet der IMC-Regler als Vorsteuerung und kann als solche entworfen werden.
- der Regelkreis ist genau dann stabil, wenn die Strecke G und der IMC-Regler stabil sind.


| Führungsübertragungsfunktion | Störübertragungsfunktion |
| --- | --- |
| $\large G_\mathsf{W}(s) = \frac{Y(s)}{W(s)} = \frac{G(s)\,K_\mathsf{IMC}}{1+\left(G(s)-\hat{G}(s)\right)\,K_\mathsf{IMC}}$ | $\large G_\mathsf{D}(s) = \frac{Y(s)}{W(s)} = \frac{1 - \hat{G}(s)\,K_\mathsf{IMC}}{1+\left(G(s)-\hat{G}(s)\right)\,K_\mathsf{IMC}}$ |


--- 

## Design
 **Führungsübertragungsfunktion**:  $\large G_\mathsf{W}(s) = \frac{Y(s)}{W(s)} = \frac{G(s)\,K_\mathsf{IMC}}{1+\left(G(s)-\hat{G}(s)\right)\,K_\mathsf{IMC}}$
 
 **Für perfektes Modell**:  $\large G_\mathsf{W}(s) = \frac{Y(s)}{W(s)} = G(s)\,K_\mathsf{IMC}(s)$
 
 **Ziel**:  $G(s)\,K_\mathsf{IMC}(s) = G_\mathsf{Des}(s)$
 
 
 **Regler**:   $\Large K_\mathsf{IMC}(s) = \frac{G_\mathsf{Des}(s)}{\hat{G}(s)}$
 
**Was wenn Strecke instabile Nullstellen hat - also nicht minimalphasig ist?**:
1. Zerlegung in minimalphasigen Anteil und Allpassanteil: $G(s) = G_\mathsf{MP}(s)\,G_\mathsf{A}(s)$.
2. Kompensation des minimalphasigen Anteils $G_\mathsf{MP}(s)$:

$$ K_\mathsf{IMC}(s) = \frac{G_\mathsf{Des}(s)}{\hat{G}_\mathsf{MP}(s)}$$

Dieser Regler ist bezüglich des integral square error-Kriteriums immernoch optimal. 