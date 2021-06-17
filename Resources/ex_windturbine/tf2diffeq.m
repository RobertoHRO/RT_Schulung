function tf2diffeq(GDes_d,invarname,outvarname)
a0 = GDes_d.den{1}(1);

eq_str = [outvarname '[k]= '];
for k=1:numel(GDes_d.den{1}(2:end))
    newelem = [num2str(-GDes_d.den{1}(k+1)/a0) '*' outvarname '[k-' num2str(k) ']'];
    
    if k>1
        newelem = [' + ' newelem];
    end
    eq_str = [eq_str newelem];
    
end

for k=1:numel(GDes_d.num{1})
    newelem = [num2str(GDes_d.num{1}(k)/a0) '*' invarname '[k-' num2str(k-1) ']'];
    eq_str = [eq_str '+' newelem];
    
end
disp(eq_str);