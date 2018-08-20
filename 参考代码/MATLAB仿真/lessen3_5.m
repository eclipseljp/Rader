clear all;
close all;
RF=3.3*1e7;%330MHz
PW=8*1e-5;%80us
PRI={4.3*1e-4 4.42*1e-4 
    4.22*1e-4 3.98*1e-4 
    4.1*1e-4 4.7*1e-4 
    4.53*1e-4 4.65*1e-4 
    4.38*1e-4 4.58*1e-4};%各个PRI集合
PA=1;
T=0;
for m=1:10
    T=T+PRI{m};
end
per=PW/T;%占空比
N=PRI{6}*RF;
t=linspace(0,2*T,40*N);%只画两个周期的信号
DT=0;
z=0;
for m=1:10
    y=(1+square(2*pi*(t-DT)/T,100*per))/2;
    DT=DT+PRI{m};
    z=z+y;
end
x=(1+sin(800*pi*RF*t))/2;
ym=z.*x;
plot(t,ym);
title('PRI跳变信号');
axis([0,2*T,-0.2,1.2]);
grid on;