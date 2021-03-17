## Windenergieanlagen
 ### Einfachste Bauart: "Typ 1" 
 ![\|400](Type1_WT.png)
 - Asynchrongenerator
 - einfachste Art eines [Kurzschlussläufer](https://de.wikipedia.org/wiki/Kurzschlussl%C3%A4ufer "Kurzschlussläufer"). 
 - Ist nicht polumschaltbar, kann man ihn direkt am Netz nur mit einer Drehzahl betreiben: bei einer [Polpaarzahl](https://de.wikipedia.org/wiki/Polpaarzahl "Polpaarzahl") von z. B. 2 (d. h. vier Pole) ergibt sich mit der [Netzfrequenz](https://de.wikipedia.org/wiki/Netzfrequenz "Netzfrequenz") von 50 [Hertz](https://de.wikipedia.org/wiki/Hertz_(Einheit) "Hertz (Einheit)") eine synchrone Drehzahl von 1500/min. 
 - Im Generatorbetrieb liegt die Läuferdrehzahl (Drehzahl der Generatorwelle) über der der synchronen Drehzahl (im Motorbetrieb darunter, daher der Name Asynchronmaschine).

---

### Modell
![](Pasted%20image%2020210317211714.png)

---

#### Anlage
![](Pasted%20image%2020210317211058.png)

---

#### Netz
![](Pasted%20image%2020210317205833.png)

---

## Übersicht

| Eingänge | Ausgänge |
| --- |---|
| Windgeschwindigkeit, Pitch | Elektrische Leistung, Drehzahl |

**Regelaufgabe**
Leistungsregelung in einer Umgebung des Pitches von 5°.

---

## Modellbildung

Matlab-Code
```Matlab
open_system('power_wind_ig2')
sim('power_wind_ig2')

% nach der Simulation liegt die Variable 
% power_wind_ig2_Timed_Based_Linearization im workspace
temp = power_wind_ig2_Timed_Based_Linearization;
temp = rmfield(temp,'OperPoint');

% StateSpace Modell erzeugen
A = temp.a;
B = temp.b;
C = temp.c;
D = temp.d;
sys = ss(A,B,C,D,temp);

% Kürzen
sys_min = minreal(sys);

% in Pol-Nullstellen-Form transformieren
zpk_min = zpk(sys_min);

% Regelstrecke selektieren
G1=zpk_min(1,1);

```

---

## Modellbildung

Matlab Ausgabe
```
zpk_min =
 
  From input "power_wind_ig2/u_Pitch" to output...
                              -3.2937 (s+3.45) (s^2 + 83.36s + 1.904e05)
   power_wind_ig2/P:  ----------------------------------------------------------
                      (s+3.363) (s^2 + 4.746s + 81.81) (s^2 + 61.41s + 2.674e05)
 
                      -0.0029538 (s^2 + 8.1s + 18.18) (s^2 + 61.41s + 2.674e05)
   power_wind_ig2/w:  ----------------------------------------------------------
                      (s+3.363) (s^2 + 4.746s + 81.81) (s^2 + 61.41s + 2.674e05)
 
  From input "power_wind_ig2/u_Wind" to output...
                              19.931 (s+3.45) (s^2 + 83.36s + 1.904e05)
   power_wind_ig2/P:  ----------------------------------------------------------
                      (s+3.363) (s^2 + 4.746s + 81.81) (s^2 + 61.41s + 2.674e05)
 
                       0.017874 (s^2 + 8.1s + 18.18) (s^2 + 61.41s + 2.674e05)
   power_wind_ig2/w:  ----------------------------------------------------------
                      (s+3.363) (s^2 + 4.746s + 81.81) (s^2 + 61.41s + 2.674e05)
```

---

## Modellbildung
Sprungantworten
![](Pasted%20image%2020210317222302.png)


## Modellbildung

Übertragungsfunktionen:

| | Pitch | Wind|
|---|---|---|
| Leistung | $\frac{-3.2937 (s+3.45) (s^2 + 83.36s + 1.904e05)}{(s+3.363) (s^2 + 4.746s + 81.81) (s^2 + 61.41s + 2.674e05)}$ | $\frac{19.931 (s+3.45) (s^2 + 83.36s + 1.904e05)}{(s+3.363) (s^2 + 4.746s + 81.81) (s^2 + 61.41s + 2.674e05)}$ |
| Drehzahl | $\frac{-0.0029538 (s^2 + 8.1s + 18.18) (s^2 + 61.41s + 2.674e05)}{(s+3.363) (s^2 + 4.746s + 81.81) (s^2 + 61.41s + 2.674e05)}$ | $\frac{0.017874 (s^2 + 8.1s + 18.18) (s^2 + 61.41s + 2.674e05)}{(s+3.363) (s^2 + 4.746s + 81.81) (s^2 + 61.41s + 2.674e05)}$ | 


Für die Regelung entscheidend:
$$\Large G(s) = \frac{U_{pitch}(s)}{Y_P(s)} = \frac{-3.2937 (s+3.45) (s^2 + 83.36s + 1.904e05)}{(s+3.363) (s^2 + 4.746s + 81.81) (s^2 + 61.41s + 2.674e05)}$$


$$\Large G(s) = \frac{U_{pitch}(s)}{Y_P(s)} = \frac{-3.294 s^3 - 285.9 s^2 - 6.282e05 s - 2.164e06}{s^5 + 69.52 s^4 + 2.68e05 s^3 + 2.175e06 s^2 + 2.616e07 s + 7.358e07}$$
