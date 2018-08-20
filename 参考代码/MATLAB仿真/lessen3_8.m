clear all;
close all;
RF=2.3*1e7;%230MHz
PW1=1.5*1e-4;%150us
PW2=8*1e-5;%80us
PRI=4.3*1e-4;%430us
dt=4*1e-5;%脉冲间隔为40us
K=2;%每个PRI内发射K个脉冲
PA=1;
T=PRI;
per1=PW1/T;%占空比
per2=PW2/T;%占空比
N=PRI*RF;
t=linspace(0,2*T,40*N);%只画两个周期的信号
y1=(1+square(2*pi*t/T,100*per1))/2;%第一种脉冲
y2=(1+square(2*pi*(t-dt-PW1)/T,100*per2))/2;%第二种脉冲
y3=(1+square(2*pi*(t-dt-PW1)/T,100*per1))/2;%第一种脉冲
yn1=y1+y2;%不等宽的脉冲
yn2=y3+y1;%等宽的脉冲
x=(1+sin(8000*pi*RF*t))/2;
ym1=yn1.*x;%不等宽的脉冲
ym2=yn2.*x;%等宽的脉冲
subplot(211);
plot(t,ym1);
title('不等间隔双脉冲信号');
axis([0,2*T,-0.2,1.2]);
grid on;
subplot(212);
plot(t,ym2);
title('等间隔双脉冲信号');
axis([0,2*T,-0.2,1.2]);