% improved algorithm for estimating PRIs applies to interleaved pulse
% trains  with PRI jitter.
clear all
clc
N=1000;
t1=0:333;
t2=0.1:sqrt(2):(0.1+332*sqrt(2));
t3=0.2:sqrt(5):(0.2+332*sqrt(5));
t=[t1 t2 t3];
clear t1 t2 t3
a=0.1;
jitter=(1-2*rand(1,1000))*a;
t=t+jitter; 
t=sort(t);             
K=201;
taumin=0;
taumax=10;
epsilon=a;          %epsilon为PRI抖动上限(=a)
zetazero=0.03;
O=zeros(1,K);
D=zeros(1,K);          %初始化D(k)
for i=1:K            
    tauk(i)=(i-1/2)*(taumax-taumin)/K+taumin;
    flag(i)=1;
end
n=2;
while n<=N
    m=n-1;
    while m>=1
        tau=t(n)-t(m);
        if (tau>(1-epsilon)*taumin)&(tau<=(1+epsilon)*taumax)
            k1=fix((tau/(1+epsilon)-taumin)*K/(taumax-taumin)+1);
            k2=fix((tau/(1-epsilon)-taumin)*K/(taumax-taumin)+1);
            if k2>201
                break
            end
            for k=k1:k2
                if flag(k)==1
                    O(k)=t(n);
                end
                etazero=(t(n)-O(k))/tauk(k);
                nu=etazero+0.4999999;
                zeta=etazero/nu-1;
                nu=fix(nu);
                if ((nu==1)&(t(m)==O(k)))|((nu>=2)&(abs(zeta)<=zetazero))
                    O(k)=t(n);
                end
                eta=(t(n)-O(k))/tauk(k);
                D(k)=D(k)+exp(2*pi*j*eta);
                flag(k)=0;
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
plot(tauk,abs(D))
axis([0 10 0 800])
                
                