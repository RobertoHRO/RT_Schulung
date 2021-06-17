if ~all([license('test','control_toolbox'), ...
        license('test','matlab'), ...
        license('test','simulink'),...
        license('test','power_system_blocks'),...
        license('test','simscape')])
    error('You need all licenses: control_toolbox, matlab, simulink, power_system_blocks and simscape')
end

%%
clearvars;
if 0
    open_system('WT_4_lin');
    sim('WT_4_lin');
    close_system('WT_4_lin');
    
    temp = WT_4_lin_Timed_Based_Linearization;
    temp.InputName = strrep(temp.InputName,'WT_4_lin/','');
    temp.OutputName = strrep(temp.OutputName,'WT_4_lin/','');
    temp = rmfield(temp,'OperPoint');
    
    A = temp.a;
    B = temp.b;
    C = temp.c;
    D = temp.d;
    
    sys = ss(A,B,C,D,temp);
    sys_min = minreal(sys);
    zpk_min = zpk(sys_min);
    
    
    GProc=zpk_min(1,1);
    
    save GProc GProc
    
else
    load GProc
end

% Process with som model uncertainty
GProcReal=GProc*1;

% GProcReal=GProc*tf([-0.1 1],[1]);

AP_y = 0.8155;
AP_u = 5;
T = 0.02;
%% PI-Regler

Kp=10;
Ki=20;
GRegPI = -1*(tf(Kp,1) + tf(Ki,[1,0]));
GRegPI_d = tf(c2d(GRegPI,T,'tustin'));

tf2diffeq(GRegPI_d,'ereg','ufbreg')

%% Vorsteuerung 1
GW2 = minreal(GRegPI*GProc/(1+GRegPI*GProc));

n=3;
GDes = tf(1,[0.2/n 1])^n;
GDes_d = tf(c2d(GDes,T,'tustin'));

GFF = GDes/GW2;
GFF_d = tf(c2d(GFF,T,'tustin'));

%% Vorsteurung 2
n=3;
GDes = tf(1,[0.2/n 1])^n;
GDes_d = tf(c2d(GDes,T,'tustin'));
tf2diffeq(GDes_d,'rreg','ydes');



step(GDes,5);

GFF2 = GDes/GProc;
GFF2_d = tf(c2d(GFF2,T,'tustin'));
tf2diffeq(GFF2_d,'rreg','uffreg')

treg = 0:0.1:20;
rproc = 0.8-0.1*(treg>=10.0);
rreg = rproc-AP_y;

uffreg = 0*treg + dcgain(GFF2_d)*rreg(1)*1;

for k=10:numel(treg)
    uffreg(k)= -0.84007*uffreg(k-1) + 0.89317*uffreg(k-2) + 0.44274*uffreg(k-3) + -0.26837*uffreg(k-4) + 0.041262*uffreg(k-5) + -0.0020219*uffreg(k-6)+-19.1915*rreg(k-0)+-22.4428*rreg(k-1)+18.9386*rreg(k-2)+10.3965*rreg(k-3)+-21.2951*rreg(k-4)+-0.41804*rreg(k-5)+9.0836*rreg(k-6);
end

   
uffreg2 = lsim(GFF2_d, rreg);
uffreg3 = filter(GFF2_d.Numerator{1},GFF2_d.Denominator{1},rreg);

figure(1)
clf
plot(uffreg3)
hold on
plot(uffreg)
%% IMC Regler

KIMC = GDes/GProc;

% open_system('Ctrl_WT');

