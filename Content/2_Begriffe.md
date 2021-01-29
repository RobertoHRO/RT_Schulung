Beispiele, Begriffe und Grundsätzliches
==========================
---
## Beispiele Regelungstechnik

Menschlicher Körper enthält eine Vielzahl an Regelkreisen:
- Körpertemperatur
- Blutzucker
- Blutdruck
- Herzfrequenz
- Alle Hormone ...

Starke Variation zw. verschiedenen menschlichen Körpern und große Änderungen der Umwelt erfordern sehr robuste Funktionsweise →Regelung!

--- 

## Beispiele Regelungstechnik
###  Blutdruckregulation

|![Quelle: https://www.wikiwand.com/de/Blutdruck \|400](Blutdruck.png)|![Quelle: https://abdominalkey.com/normal-blood-pressure-control-and-the-evaluation-of-hypertension/\|350](Blutdruckreaktionen.jpg)|
|---|---|

---

## Beispiele Regelungstechnik
### Inverses Pendel
**Ziel**: Das frei schwingende Pendel aufrichten, positionieren und Störungen kompensieren       

|![\|300](Inverses_Pendel.png)|![\|260](Cart-pole_swing_up.gif)|<iframe width="300" height="180" src="https://www.youtube.com/embed/BnK3x7yiRVY" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>|
|---|---|--|

Link zum Video: [https://www.youtube.com/embed/IDFYQ86t8lk](https://www.youtube.com/embed/IDFYQ86t8lk)

---
## Beispiele Regelungstechnik
### Inverses Dreifachpendel
|<iframe width="400" height="300" src="https://www.youtube.com/embed/cyN-CRNrb3E" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> |<iframe width="400" height="300" src="https://www.youtube.com/embed/Ep2lNMic_fk" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>|
|--|--|

Video 1:  [https://www.youtube.com/embed/cyN-CRNrb3E](https://www.youtube.com/embed/cyN-CRNrb3E)
Video 2: [https://www.youtube.com/embed/Ep2lNMic_fk](https://www.youtube.com/embed/Ep2lNMic_fk)

--- 

## Beispiele Regelungstechnik
### Anwendungen der inversen Pendel
|![File:Segway PT (2006).jpg - Wikimedia Commons\|300](https://upload.wikimedia.org/wikipedia/commons/4/4a/Segway_PT_%282006%29.jpg)|![File:Ховърборд.jpeg\|400](https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/%D0%A5%D0%BE%D0%B2%D1%8A%D1%80%D0%B1%D0%BE%D1%80%D0%B4.jpeg/800px-%D0%A5%D0%BE%D0%B2%D1%8A%D1%80%D0%B1%D0%BE%D1%80%D0%B4.jpeg)|<iframe width="400" height="300" src="https://www.youtube.com/embed/IDFYQ86t8lk" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>|
|---|---|---|

Video 1: [https://www.youtube.com/embed/IDFYQ86t8lk](https://www.youtube.com/embed/IDFYQ86t8lk)

---

## Beispiele Regelungstechnik
### Quadorcopter

![https://stocksnap.io/photo/camera-drone-PMPCA8UHSO\|400](Quadrocopter.jpg)

|![Šolc - Modelling and Control of a Quadrocopter.pdf\|280](Pasted%20image%2020210127200719.png)|<iframe width="300" height="200" src="https://www.youtube.com/embed/w2itwFJCgFQ" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>|<iframe width="300" height="200" src="https://www.youtube.com/embed/YIs8t3ro9Fw" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>|
|---|---|---|

Video 1: [https://www.youtube.com/embed/w2itwFJCgFQ](https://www.youtube.com/embed/w2itwFJCgFQ)
Video 2: [https://www.youtube.com/embed/YIs8t3ro9Fw](https://www.youtube.com/embed/YIs8t3ro9Fw)

---

## Wichtige Begriffe

---

## Wichtige Begriffe
![Blockdiagramm einer Regelstrecke](Strecke.png)
**Regelstrecke** 
- auch bezeichnet als Strecke, Prozess, *process*
- Maschine / Anlagenteil / System 
	- mit Stelleinrichtung (Stellmotoren, Ventile, etc.) - actuators
	- mit Messeinrichtung (Fühler, Transmitter, Sensoren etc.) - ensors
		
**Eingang** 
	- Stellgröße, *input*, *manipulated variable (MV)*
	
**Ausgang**
	- Regelgröße, *output*, *controlled variable (CV)*

---

## Beispiele für Regelstrecken
technische | ökologische | ökonomische
:------------|:-------------|:---------------
	- Raumtemperatur| 	- Fischbestand|	- Arbeitslosenzahl
	- Fahrzeuggeschwindigkeit|	- Infiziertenzahl|	- BIP
	- Fahrzeugabstand| 
	- Fahrstuhlposition|

---

## Duschen aus Sicht der Regelungstechnikerin

![Dusche als Regelaufgabe|400](Dusche_pur.svg)

Was gehört beim Duschen zur Regelstrecke?

---

## Lösungsweg für Regelungsaufgaben
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