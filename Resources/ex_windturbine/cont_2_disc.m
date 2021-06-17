G =  tf([1],[1 1]);

figure(1)
step(G)

Gd = c2d(G,10,'zoh')
hold on
step(Gd)