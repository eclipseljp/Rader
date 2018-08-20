clear all;
close all;
RF=2.3*1e7;%230MHz
PW=8*1e-5;%80us
PRI1=4.3*1e-4;%430us
PRI2=2.1*1e-4;%210us
K=3;%每种PRI上发射K个脉冲
PA=1;
T=K*(PRI1+PRI2);
per=PW/T;%占空比
N=PRI1*RF;
t=linspace(0,2*T,40*N);%只画两个周期的信号
z1=0;
z2=0;
for m=1:K
    y1=(1+square(2*pi*(t-(m-1)*PRI1)/T,100*per))/2;%第一种PRI发射K个
    z1=z1+y1;
end
for m=1:K
    y2=(1+square(2*pi*(t-K*PRI1-(m-1)*PRI2)/T,100*per))/2;%第二种PRI发射K个
    z2=z2+y2;
end
z=z1+z2;
x=(1+sin(800*pi*RF*t))/2;
ym=z.*x;
plot(t,ym);
title('脉组PRI变化信号');
axis([0,2*T,-0.2,1.2]);
grid on;