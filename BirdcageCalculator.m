%%%% BIRDCAGE COIL CALCULATOR %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Author: William Mathieu                                                 %
% References: Cheol Kim 2020                                              %
% Create: 27 May 2020                                                     %
% Last Modified: 12 Aug 2020                                              %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

format short eng
mu0 = 4*pi*10^(-7);

prompt = {'Number of Legs:','Coil Diameter (m):','Coil Length (m):',...
          'End-ring Width (m):','Leg Width (m):','Feed End-ring Caps "Cm" (pF):',...
          'Leg Caps "Cd" (pF):','Opposite-Feed End-ring Caps "Ct" (pF):'};
dlgtitle = 'Input'; 
dims = [1 40];
definput = {'8','0.210','0.25','0.0125','0.0125','33','8.2','33'};
answers = inputdlg(prompt,dlgtitle,dims,definput); %USER INPUT

CoilNumber = str2num(answers{2,1});
CoilName = answers{1,1};

N = str2num(answers{1,1});
coil_diameter = str2num(answers{2,1});
coil_height = str2num(answers{3,1});
width_endring = str2num(answers{4,1});
width_leg = str2num(answers{5,1});
Cm = str2num(answers{6,1})*1e-12;
Cd = str2num(answers{7,1})*1e-12;
Ct = str2num(answers{8,1})*1e-12;

answer2 = questdlg('What type of birdcage coil is this?','Coil Type',...
                   'band-pass','high-pass','low-pass','band-pass');

segLength_leg = coil_height-2*width_endring;
segArcAngle = (2*pi)/N;
segLength_endring = segArcAngle*(coil_diameter/2);

L_leg = ((mu0*segLength_leg)/(2*pi))*(log((2*segLength_leg)/width_leg)+0.5);
L_endring = ((mu0*segLength_endring)/(2*pi))*(log((2*segLength_endring)/width_endring)+0.5);

Leq = 2*L_leg + N*L_endring;

Ceq_BP = (2*Cm*Ct*Cd)/(4*Cm*Ct+N*Cd*(Ct+Cm));
Ceq_HP = (2*Cm*Ct)/(N*(Ct+Cm));
Ceq_LP = Cd/2;  

switch answer2
    case 'band-pass'
        Ceq = Ceq_BP;
    case 'high-pass'
        Ceq = Ceq_HP;
    case 'low-pass'
        Ceq = Ceq_LP;
end

f0 = 1/(2*pi*sqrt(Leq*Ceq))

f0_MHz = round(f0/1e6,3);

CreateStruct.Interpreter = 'tex';
CreateStruct.WindowStyle = 'modal';

h = msgbox(['f_0= ' num2str(f0_MHz) ' MHz'], 'Result',CreateStruct);
