# Vorsteuerung 2

---

## Ansatz

![\|700](Untitled-2021-03-25-1449.png)

* Forderung wird: $y(t) = w(t) \quad \forall \quad t$
* Dann ist $e(t) =0$
* Daraus folgt der Regler ist inaktiv  - immer!


---

## Entwurf 
![\|700](Untitled-2021-03-25-1449.png)

Der Ansatz: $\Large G_{Vorsteuerung}(s)\cdot G_{Sollwertformung}(s)\cdot G_{Strecke}(s)=1$ ist schön, aber nicht realisierbar.

Besser ist: $\Large G_{Vorsteuerung}(s)\cdot G_{Sollwertformung}(s)\cdot G_{Strecke}(s)=G_{Des}(s)$

Es folgt: $\Large G_{{Vorsteuerung}}(s) = G_{Strecke}^{-1}(s)\quad$ und $\Large\quad G_{Sollwertformung}(s) = G_{Des}(s)$

--> Vorsteuerung und Sollwertformung sind unabhängig vom Regler!

---

## Wunschverhalten

Wunschverhalten kann so angesetzt werden:
$$G_{Des}(s)=\frac{1}{\left(\frac{T}{n}\,s+1\right)^n}$$
Die Ordnung n ist so zu wählen, dass die Systeme realisierbar sind.

![\|400](Pasted%20image%2020210415170134.png)

----



````
https://excalidraw.com/#room=50f7410a7f942f568068,UxoBuOr752lfflBNz4a34Q
<iframe src="https://excalidraw.com/#room=05d389222c14e9f26e97,9xJMzwvdc4UURxS2prlByQ" style="position:relative; width:700px; border:none;  height:400px" sandbox="allow-modals;"></iframe>
````

