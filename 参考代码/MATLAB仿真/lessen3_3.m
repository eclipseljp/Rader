clear all;
close all;
RF=3.3*1e7;%330MHz
PW=8*1e-5;%80us
PRI1=4.3*1e-4;%430us
PRI2=6.7*1e-4;%670us
PRI3=3.1*1e-4;%310us
PA=1;
T=PRI1+PRI2+PRI3;
per=PW/T;
N=PRI2*RF;
t=linspace(0,5*T,20*N);
y1=(1+square(2*pi*t/T,100*per))/2;
y2=(1+square(2*pi*(t-PRI1)/T,100*per))/2;
y3=(1+square(2*pi*(t-PRI1-PRI2)/T,100*per))/2;
x=(1+sin(1000*pi*RF*t))/2;
ym=y1+y2+y3;
y=ym.*x;
plot(t,y);
title('÷ÿ∆µ≤Œ≤Ó–≈∫≈');
axis([0,2*T,-0.2,1.2]);