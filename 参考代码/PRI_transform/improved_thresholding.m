% improved algorithm for estimating PRIs applies to interleaved pulse
% trains  with PRI jitter.
clear all
clf
clc
N=1000;
%三部雷达的toa
t1=0:333;                         
t2=0.1:sqrt(2):(0.1+332*sqrt(2));
t3=0.2:sqrt(5):(0.2+332*sqrt(5));
toa=[t1 t2 t3];
clear t1 t2 t3
a=0.1;                                      %设置抖动程度
jitter=(1-2*rand(1,1000))*a;
toa=toa+jitter;                             %为每个脉冲的TOA加随机抖动
toa=sort(toa);                              %排序
K=201;
taumin=0;
taumax=10;
epsilon=a;                                  %epsilon为PRI抖动上限(=a)
zetazero=0.03;
O=zeros(1,K);
D=zeros(1,K);                               %初始化D(k)
C=zeros(1,K);
A=zeros(1,K);                               %初始化门限函数
for i=1:K                                   %PRI箱中心，验证标志
    tauk(i)=(i-1/2)*(taumax-taumin)/K+taumin;
    flag(i)=1;
end
bk=2*epsilon*tauk;                          %第k个PRI bin的width
n=2;
while n<=N
    m=n-1;
    while m>=1
        tau=toa(n)-toa(m);
        if (tau>(1-epsilon)*taumin)&(tau<=(1+epsilon)*taumax)                 %求tau值满足的PRI箱的范围
            k1=fix((tau/(1+epsilon)-taumin)*K/(taumax-taumin)+1);
            k2=fix((tau/(1-epsilon)-taumin)*K/(taumax-taumin)+1);
            if k2>201
                break
            end
            for k=k1:k2
                if flag(k)==1                                                  %检测第k个PRI箱是否第一次使用
                    O(k)=toa(n);
                end
                etazero=(toa(n)-O(k))/tauk(k);                                 %计算初始相位并分解 
                nu=etazero+0.4999999;
                zeta=etazero/nu-1;
                nu=fix(nu);
                if ((nu==1)&(toa(m)==O(k)))|((nu>=2)&(abs(zeta)<=zetazero))    %确定是否需要移动时间起点
                    O(k)=toa(n);
                end
                eta=(toa(n)-O(k))/tauk(k);                      %计算相位 
                D(k)=D(k)+exp(2*pi*j*eta);                      %升级PRI变换
                C(k)=C(k)+1;
                flag(k)=0;                                      %对已使用过的PRI箱设标志    
            end
        elseif tau>taumax*(1+epsilon)
            break
        else
            ;
        end
        m=m-1;
    end
    n=n+1;
end
D=abs(D);
plot(tauk,D)
axis([0 10 0 800])
hold on         
X=[225./tauk;0.15*C;4*sqrt(N*N*bk/750)]; 
A=max(X);                                                      %门限函数
plot(tauk,A,'r-')
xlabel('tauk')
ylabel('|D(k)|')
i=1;
for k=1:K
    if D(k)>A(k)
        p(i)=tauk(k);
        i=i+1;
    end
end
p=sort(p);                                                     %峰值处理，消除相邻区间，得到可能PRI 



         
                