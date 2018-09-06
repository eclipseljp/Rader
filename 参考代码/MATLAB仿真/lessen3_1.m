clear all;
close all;
RF=2.3*1e7;%230MHz
PW=8*1e-5;%80us
PRI=4*1e-4;%400us
PA=1;
per=PW/PRI;
N=PRI*RF;
t=linspace(0,5*PRI,20*N);
y1=(1+square(2*pi*t/PRI,100*per))/2;
% plot(t,y1)
x=(1+sin(1000*pi*RF*t))/2;
%plot(t,x)
y=y1.*x;
subplot(211);
plot(t,y);
title('简单体制雷达信号');
axis([0,5*PRI,-0.2,1.2]);
Hy=fft(y);
subplot(212);
plot(fftshift(abs(Hy)));
title('幅频特性');