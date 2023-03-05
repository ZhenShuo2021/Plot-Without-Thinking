% 'o'	Circle
% '+'	Plus sign
% '*'	Asterisk
% '.'	Point
% 'x'	Cross
% '_'	Horizontal line
% '|'	Vertical line
% 'square' or 's'	Square
% 'diamond' or 'd'	Diamond
% '^'	Upward-pointing triangle
% 'v'	Downward-pointing triangle
% '>'	Right-pointing triangle
% '<'	Left-pointing triangle
% 'pentagram' or 'p'	Five-pointed star (pentagram)
% 'hexagram' or 'h'	Six-pointed star (hexagram)

x = 0:2:20;
% null
l.p1 = [0.05480471,0.01082922,0.00099901,0.00007284,0.00002404,0.00001643,0.00001268,0.00001082,0.00001085,0.00001047,0.00001023];
l.p2 = [0.17831602,0.11262871,0.05583773,0.01456559,0.00277051,0.00130143,0.00101074,0.00085550,0.00076331,0.00072396,0.00071003];
l.p3 = [0.24855752,0.19477913,0.13313952,0.07083177,0.02912350,0.01370124,0.00970833,0.00848493,0.00788818,0.00750563,0.00725166];
% null
l.p4 = [0.02171068,0.00637318,0.00102656,0.00015885,0.00004707,0.00002949,0.00002663,0.00002487,0.00002480,0.00002578,0.00002585];
l.p5 = [0.12515495,0.08952220,0.04703724,0.01852669,0.00743698,0.00442422,0.00366771,0.00352422,0.00354948,0.00361042,0.00364043];
l.p6 = [0.19864225,0.17553503,0.14429460,0.10658034,0.06967096,0.04314577,0.02913255,0.02326751,0.02115013,0.02042448,0.02018047];


f=figure;
f.Position = [0 42 1050 840];
LineWidth = 2;
MarkerSize = 18;
p1=semilogy(x,l.p1,'b-o','LineWidth',LineWidth,'MarkerSize',MarkerSize);grid on; hold on
p2=semilogy(x,l.p2,'b-s','LineWidth',LineWidth,'MarkerSize',MarkerSize);grid on; hold on
p3=semilogy(x,l.p3,'b-^','LineWidth',LineWidth,'MarkerSize',MarkerSize);grid on; hold on
p4=semilogy(x,l.p4,'r--o','LineWidth',LineWidth,'MarkerSize',MarkerSize);grid on; hold on
p5=semilogy(x,l.p5,'r--s','LineWidth',LineWidth,'MarkerSize',MarkerSize);grid on; hold on
p6=semilogy(x,l.p6,'r--^','LineWidth',LineWidth,'MarkerSize',MarkerSize);grid on; hold on

set(gca,'XTick',x,'FontName','Times','fontsize',18)
% title({'i.i.d. AER'},'FontWeight','normal','fontsize',24, 'interpreter', 'latex')
xlabel('SNR (dB)','FontName','Times','fontsize',24, 'interpreter', 'latex')
ylabel('Null','FontName','Times','fontsize',24, 'interpreter', 'latex')
axis([x(1) x(end) 1e-5 .4]);
grid on
gcf_set = [p1 p4 p2 p5 p3 p6];
lgd = legend(gcf_set, {'proposed UE=5', 'Compare \enspace UE=5', 'proposed UE=10', 'Compare \enspace UE=10', 'proposed UE=15', 'Compare \enspace UE=15'});
lgd.Interpreter = 'latex'; lgd.Location = 'northeast'; lgd.FontSize = 14;
