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
T = 0.1;


%% PI-Controller

Kp=10;
Ki=20;
GRegPI = -1*(tf(Kp,1) + tf(Ki,[1,0]));
GRegPI_d = tf(c2d(GRegPI,T,'tustin'));

tf2diffeq(GRegPI_d,'ereg','ufbreg')

%% Feedforward control 1
GW2 = minreal(GRegPI*GProc/(1+GRegPI*GProc));

n=3;
GDes = tf(1,[0.2/n 1])^n;
GDes_d = tf(c2d(GDes,T,'tustin'));

GFF = GDes/GW2;
GFF_d = tf(c2d(GFF,T,'tustin'));

%% Feedforward control 2
n=3;
GDes = tf(1,[0.2/n 1])^n;
GDes_d = tf(c2d(GDes,T,'tustin'));
tf2diffeq(GDes_d,'rreg','ydesmod');

GFF2 = GDes/GProc;
GFF2_d = tf(c2d(GFF2,T,'tustin'));
tf2diffeq(GFF2_d,'rreg','uffreg')

%% IMC Controller

KIMC = GDes/GProc;

% open_system('Ctrl_WT');

%% discrete process modell
GProc_d = c2d(tf(GProc), T, 'zoh');


% desired dynamic of the controlled system
switch 2
    case 1
        Gdes2_d = tf([1],[1 0 0 0],T);
    case 2
        ord=25;
        Gdes2_d = tf(ones(1,ord),[ord zeros(1,ord)],T);
    case 3
        tt = [0.01 0.02 0.1 0.2 0.3 0.5 0.5 0.5 0.5 0.5 0.5 1 1 1];
        tt = [tt fliplr(tt)];
        Gdes2_d = tf(tt,[sum(tt) zeros(1,numel(tt))],T);
    case 4
        n=3;
        Gdes2_d = c2d(tf(1,[1/n 1])^n,T);
end

% calc controller
GCompReg_d = feedback(Gdes2_d,1,1)/GProc_d;

% plot
figure(1)
clf
subplot(1,3,1)
step(Gdes2_d,5)
title('desired')

subplot(1,3,2)
step(feedback(GCompReg_d,GProc_d),5)
title('manipulated variable')

subplot(1,3,3)
step(feedback(GCompReg_d*GProc_d,1),5)
title('controlled variable')