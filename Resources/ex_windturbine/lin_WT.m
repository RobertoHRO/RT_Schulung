if ~all([license('test','control_toolbox'), ...
        license('test','matlab'), ...
        license('test','simulink'),...
        license('test','power_system_blocks'),...
        license('test','simscape')])
    error('You need all licenses: control_toolbox, matlab, simulink, power_system_blocks and simscape')
end

%%
clearvars;

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

% Process with som model uncertainty
GProcReal=zpk_min(1,1);
% GProcReal=zpk_min(1,1)*tf([-0.1,1],[0.2,1]);

%% PI-Regler
GRegPI = -1*(tf(10,1) + tf(140,[1,0]));

%% Vorsteuerung 1
GW2 = minreal(GRegPI*GProc/(1+GRegPI*GProc));

n=3;
GDes = tf(1,[1/n 1])^n;
% step(GDes,5);
% grid

GFF = GDes/GW2;

%% Vorsteurung 2
n=3;
GDes = tf(1,[1/n 1])^n;
step(GDes,5);

GFF2 = GDes/GProc;

open_system('Ctrl_WT');

