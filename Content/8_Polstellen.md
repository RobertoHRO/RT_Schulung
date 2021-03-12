Bedeutung der Polstellen für den Zeitbereich
===

---

## Rückblick

| Übertragungsfunktion | Polstellen | Nullstellen | Verstärkung |
| --- | ---|--- |
|$G(s)=\frac{5\,s + 10}{2\,s^2 + 5\,s + 10}$| $s_{1,2} = -1.25 \pm 1.85j$ | $s_{01} = -2$ |


| $G(s)$ in s-Ebene | Impulsantwort | Sprungantwort |
| -- | ---| -- |
|![TF1_lin_cont\|300](TF1_lin_cont.png)| ![](Pasted%20image%2020210310164326.png) | ![](Pasted%20image%2020210310164245.png)|

Wegen Nullstelle zuänchst ungeeignetes System für Analyse 


---

## Übertragungsglied 2. Ordnung

$\require{extpfeil}\Newextarrow{\xRightarrow}{5,5}{0x21D2}$

$$G(s) = \frac{k_s}{T^2s^2+2\,d\,T\,s+1} \qquad \xrightarrow[T=\frac{1}{\omega_0}]{} \qquad \frac{k_s}{\frac{1}{\omega_0^2}s^2+\frac{2\,d}{\omega_0}\,s+1}$$

$\omega_0$ - Eigenfrequenz, $d$ - Dämpfung

Das char. Polynom hat die Wurzeln: 
$$s_{1,2} = -\omega_0\,d \pm \omega_0\sqrt{d^2-1}$$
 
 Das sind die Polstellen von $G(s)$.
 
---

## Dämpfung $\mathsf d > 1$ (reelle Polstellen)

Es ergeben sich zwei negative reelle Pole:
$$s_{1} = -\omega_0\,d + \omega_0\sqrt{d^2-1} \qquad \textsf{und} \qquad s_{2} = -\omega_0\,d - \omega_0\sqrt{d^2-1}$$
Mit den  Zeitkonstanten $T_1 = -\frac{1}{s_1}$ und $T_2 = \frac{1}{s_2}$ erhält man die Übertragungsfunktion
$$G(s) = \frac{k_s}{(T_1s+)(T_2s+1)}$$

<iframe  style="border:none;" src="file:///C:/Users/beck_rb/Documents/Obsidian_Zettelkasten/RT_Schulung/Resources/T12reel.html" height="450" width="100%"></iframe>

---













## Dämpfung $0<\mathsf d<1$ (komplexe Polstellen)

Es ergibt sich ein konjugiert komplexes Polpaar
$$s_{1} = -\omega_0\,d + j\omega_0\sqrt{1-d^2} \qquad \textsf{und} \qquad s_{2} = -\omega_0\,d - j\omega_0\sqrt{1-d^2}$$

$$G(s) = \frac{k_s}{\frac{s^2}{\omega_0^2} + \frac{2\,d}{\omega_0}\,s + 1}$$

<iframe  style="border:none;" src="file:///C:/Users/beck_rb/Documents/Obsidian_Zettelkasten/RT_Schulung/Resources/T12compl.html" height="450" width="100%"></iframe>













------------

## Pole vs. Impulsantwort

![Time functions  associated with points  in the s\-plane (LHP, left  half-plane; RHP, right  half-plane) Quelle: Powell Figure 3.16\|600](Pasted%20image%2020210304194402.png)

Kategorien:

| | | |
| -- | -- | -- |
| schnell / langsam | periodisch / aperiodisch | stabil / instabil / grenzstabil |






