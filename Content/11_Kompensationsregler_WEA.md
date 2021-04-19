# Kompensationsregler


---

## Ansatz 1
**Ziel** Das Führungsverhalten des Reglers wird als **Zähler- und Nennerpolynom **definiert - und daraus der nötige Regler berechnet:

$$\frac{G_\mathsf{R}(s)\cdot G_\mathsf{S}(s)}{1+ G_\mathsf{R}(s)\cdot G_\mathsf{S}(s)} = \frac{B_\mathsf{Des}(s)}{A_\mathsf{Des}(s)}$$


$$G_\mathsf{R} = \frac{B_\mathsf{Des}(s)}{G_\mathsf{S}(s)\cdot (A_\mathsf{Des}(s)-B_\mathsf{Des}(s))}$$

--> Wenn in $A_\mathsf{Des}(s)$, $B_\mathsf{Des}(s)$ das hier $a_0 = b_0$ gilt, dann hat der Regler einen I-Anteil! - **GRO?ARTIG!!1!!**

---

 ## Ansatz 2
**Ziel** Das Führungsverhalten des Reglers wird **als Übertragungsfunktion** definiert - und daraus der nötige Regler berechnet:

$$\frac{G_\mathsf{R}(s)\cdot G_\mathsf{S}(s)}{1+ G_\mathsf{R}(s)\cdot G_\mathsf{S}(s)} = G_\mathsf{Des}(s)$$


$$G_\mathsf{R} = \frac{G_\mathsf{Des}(s)}{1-G_\mathsf{Des}(s)}\cdot \frac{1}{G_\mathsf{S}(s)}$$

--> Die Gleichung entspricht diesem Blockschaltbild, und hat dadurch eine gute Anschaulichkeit.

![\|700](Untitled-2021-04-07-0837.png)


---

##  Beispiel



| Ziel- führungsüber- tragungsfunktion |  |  $G_{Des}(s) = \frac{1}{0.001 s^3 + 0.03 s^2 + 0.3 s + 1}$ |
| --- | --- | ---| 
| Regler | | $G_R(s)=\frac{-303.6 s^5 - 2.111e+04 s^4 - 8.136e+07 s^3 - 6.603e+08 s^2 - 7.942e+09 s - 2.234e+10}{s^6 + 116.8 s^5 + 1.936e+05 s^4 + 6.404e+06 s^3 + 7.692e+07 s^2 + 1.971e+08 s}$ |
| Führungsüber- tragungsfunktion | $G_W(s)=\frac{Y(s)}{W(s)} = \frac{G_R(s)G_S(S)}{1+G_R(s)G_S(S)}$| $\frac{1000}{s^3 + 30 s^2 + 300 s + 1000}$ |
| Störgrößenüber- tragungsfunktion | $G_D(s)=\frac{Y(s)}{D(s)} = \frac{1}{1+G_R(s)G_S(S)}$| $\frac{ s^3 + 30 s^2 + 300 s}{s^3 + 30 s^2 + 300 s + 1000}$ |
| Stellgrößenüber- tragungsfunktion | $G_U(s)=\frac{U(s)}{W(s)} = \frac{G_R(s)}{1+G_R(s)G_S(S)}$| $\frac{-303.6 s^5 - 2.111e+04 s^4 - 8.136e+07 s^3 - 6.603e+08 s^2 - 7.942e+09 s - 2.234e+10}{s^6 + 116.8 s^5 + 1.936e+05 s^4 + 6.405e+06 s^3 + 7.701e+07 s^2 + 3.878e+08 s + 6.57e+08}$ |


--- 
## Diskussion

### Vorraussetzungen
- Regelstrecke muss stabil sein
- inverse Modell der Strecke muss stabil sein (Nullstellen müssen negativ sein)
- hinreichende relative Ordnung der Zieldynamik $G_\mathsf{Des}(s)$  

### Vorteile
- Führungsverhalten kann präzise abgestimmt werden



### Nachteile
- Reglerordnung geht hoch
- Störungen und Führungsgrößen regen die gleiche Dynamik (Polstellen, char. Gleichung)  an. - Besser ist es das Führungsverhalten vom Störverhalten zu trennen.

----