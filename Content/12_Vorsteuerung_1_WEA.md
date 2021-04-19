Vorsteuerung
---------------

----
## Ansatz


Idee: Entkopplung der Dynamiken von Führungsverhalten und Störunterdrückung

Zweistufiger Ansatz:
1. Entwurf der Regelung
2. Entwurf der kompensierenden Vorsteuerung

![\|700](Untitled-2021-03-12-0838(2).png)

---

## Ersatzübertragungsfunktionen
![\|700](Untitled-2021-03-12-0838(2).png)

| Führungs-ÜF | Führungs-ÜF | Störung-ÜF |
| ---- | --- | --- |
|$\Large \frac{Y(s)}{R(s)} = \frac{G_F(s) \; G_R(s)\; G_S(s)}{1+G_R(s)\;  G_S(s)}$| $\Large \frac{Y(s)}{W(s)} = \frac{G_R(s)\;  G_S(s)}{1+G_R(s) \; G_S(s)}$ | $\Large \frac{Y(s)}{D(s)} = \frac{1}{1+G_R(s) \; G_S(s)}$ |

 $G_F(s)$ wird genutzt um:
--> eine Wunschdynamik aufzuprägen oder anders ausgedrückt:
--> die Regelkreisdynamik zu kompensieren

---

## Berechnung der Vorsteurung

![\|700](Untitled-2021-03-12-0838(2).png)


$$ \frac{Y(s)}{R(s)} = \frac{G_F(s) \; G_R(s)\; G_S(s)}{1+G_R(s)\;  G_S(s)} \overset{!}{=} G_{Des}(s)$$

$$ G_F(s)=G_{Des}(s)\cdot\frac{1+G_R(s)\;  G_S(s)}{G_R(s)\; G_S(s)} $$

* Parametrierung von Regler und Vorfilter hängt von Regelaufgabe ab.
* Eine Möglichkeit ist, über den I-Anteil eine bleibende Regelabweichung z.B. durch Modellunsicherheit **langsam** auszuregeln

---

## Ergebnis
![\|700](Untitled-2021-03-12-0838(2).png)


| Störgrößenunterdrückung $\frac{Y(s)}{D(S)}$ | Führungsverhalten $\frac{Y(s)}{R(S)}$ | Vorfilter $\frac{W(s)}{R(S)}$ |  
| --- | ---| --- |
| ![](Pasted%20image%2020210407135952.png) | ![](Pasted%20image%2020210407154148.png) | ![](Pasted%20image%2020210407154242.png) |

--> Nachteil der Struktur: bei Sollwertänderungen wird der ganze Regelkreis angeregt.  - Besser wäre wenn er nur von Störungen angeregt wird.

---

