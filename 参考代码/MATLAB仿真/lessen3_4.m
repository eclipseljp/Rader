%原题的PW=10us,频率抖动范围为5%
%为使结果更加明显，这里的PW=80us，频率抖动范围为50%
clear all;
close all;
RF=3.3*1e7;%330MHz
PW=8*1e-5;%10us
K=.5;%频率抖动百分比
PRI0=4.3*1e-4;%430us
A=5;%共取5个PRI
for m=1:A
    temp=rand(1,1);%产生一个0到1的随机数
    PRI(m)=PRI0*(1+K*temp);
end
PA=1;
T=0;
for m=1:A
    T=T+PRI(m);
end
per=PW/T;%占空比
N=max(PRI)*RF;
DT=0;
yn=0;
t=linspace(0,5*T,20*N);
for m=1:A
    y=(1+square(2*pi*(t-DT)/T,100*per))/2;
    yn=yn+y;
    DT=DT+PRI(m);
end
x=(1+sin(1000*pi*RF*t))/2;
y=yn.*x;
plot(t,y);
title('重频抖动信号');
axis([0,2*T,-0.2,1.2]);
grid on