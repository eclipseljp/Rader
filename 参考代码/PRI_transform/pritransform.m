%Original algorithm based on PRI transform applies to interleaved pulse
%train with constant PRIs 1¡¢sqrt(2)¡¢sqrt(5)
%parameter  number of pulses N=1000;range of PRI
%[taumin,taumax]=[0,10];numbers of PRI bins K=201
clear all
clc
t1=0:333;
t2=0.1:sqrt(2):(0.1+332*sqrt(2));
t3=0.2:sqrt(5):(0.2+332*sqrt(5));
t=[t1 t2 t3];
clear t1 t2 t3
t=sort(t);
N=length(t);
K=201;
taumin=0;
taumax=10;
b=(taumax-taumin)/K;
D=zeros(1,K);
for i=1:K
    tauk(i)=(i-1/2)*(taumax-taumin)/K+taumin;
end
n=2;
while n<=N
    m=n-1;
    while m>=1
        tau=t(n)-t(m);
        if (tau>taumin)&(tau<=taumax)
            for k=1:K
                if (tau>(tauk(k)-b/2))&(tau<=(tauk(k)+b/2))
                    D(k)=D(k)+exp(2*pi*t(n)*j/tau);
                end
            end
        elseif tau>taumax
            break
        else 
            ;
        end
        m=m-1;
    end
    n=n+1;
end
plot(tauk,abs(D))
axis([0 10 0 800])
