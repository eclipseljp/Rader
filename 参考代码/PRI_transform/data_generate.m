clear; 
clc; 
close all; 
 
% 雷达信号分选仿真数据产生 
% 四部雷达 
% 站间距离 100km 
% author: xiacx 
% 2008-3-10 
 
% 接收站和信号辐射源位置 
aStation = [50e3 0 0]'; % x轴上 
bStation = [-50e3 0 0]'; 
xCoordinate = random('unif',0,7e3,1,4);    % 4部雷达的x轴坐标 
yCoordinate = random('unif',0,4e3,1,4); 
zCoordinate = random('unif',0,4e3,1,4); 
radarCoordinate = [xCoordinate;yCoordinate;zCoordinate];   % 用矩阵表示四部雷达 
 
c = 3e8;  % 光速 
aDelay(1) = norm(aStation-radarCoordinate(:,1))/c;    % 目标1与a站的传输时间 
aDelay(2) = norm(aStation-radarCoordinate(:,2))/c; 
aDelay(3) = norm(aStation-radarCoordinate(:,3))/c; 
aDelay(4) = norm(aStation-radarCoordinate(:,4))/c; 
 
bDelay(1) = norm(bStation-radarCoordinate(:,1))/c;    % 目标1与b站的传输时间 
bDelay(2) = norm(bStation-radarCoordinate(:,2))/c; 
bDelay(3) = norm(bStation-radarCoordinate(:,3))/c; 
bDelay(4) = norm(bStation-radarCoordinate(:,4))/c; 
 
% 四部雷达的发射时间不一定相同 
% 由于基线只有100km，最大时差为330us，那么重频最大30k时，恰好脉冲周期为10us 
% 实际上信号的 时差 是小于10us的 
% 假设四部雷达信号到达a站的信号在10us内均匀分布 
% 由到达a站的时间再去计算信号发射时刻，从而得到到达b站的时间 
aToa(1) = random('unif',0,10e-6,1,1); 
aToa(2) = random('unif',0,30e-6,1,1); 
aToa(3) = random('unif',0,60e-6,1,1); 
aToa(4) = random('unif',0,80e-6,1,1); 
% 信号发射绝对时刻 
radarTime = aToa- aDelay; 
% b站到达时间的计算 
bToa = radarTime + bDelay;

% 采样率100M 
fs = 100e6; 
 
% 重复周期 
% 可以修改的参数 
pir = [100,1e3,10e3,100e3];  % 雷达信号重复频率 
pit = 1./pir;   
pw = [15e-6,15e-6,8e-6,0.8e-6];  % 脉宽 
pf = random('unif',23e6+20000,37e6-20000,1,4);  % 载频 


% 信号脉宽、幅度、载频都在这儿给出 
% 脉幅最后把所有数据得到后，统一给一个随机向量 
% 载频在15M带宽内给一个随机量 
%-------------------- 
k = fix(0.1/pit(1));      % 0.1s数据 
for i = 1 : k 
    aToaRadar1(i) = (i-1)*pit(1)+aToa(1);    %根据脉冲周期，计算每个脉冲的到达时间 
    bToaRadar1(i) = (i-1)*pit(1)+bToa(1); 
    pwRadar1(i) = pw(1);     %每个到达脉冲对应的脉宽和载频 
    pfRadar1(i) = pf(1); 
end 
k = fix(0.1/pit(2)); 
for i = 1 : k 
    aToaRadar2(i) = (i-1)*pit(2)+aToa(2); 
    bToaRadar2(i) = (i-1)*pit(2)+bToa(2); 
    if k>30 & k<=60                     % 体现参差频率，重复周期改变了 
        aToaRadar2(i) = (i-1)*1/1100+aToa(3); 
        bToaRadar2(i) = (i-1)*1/1100+bToa(3); 
    end 
    pwRadar2(i) = pw(2); 
    pfRadar2(i) = pf(2); 
end 
k = fix(0.1/pit(3)); 
for i = 1 : k 
    aToaRadar3(i) = (i-1)*pit(3)+aToa(3); 
    bToaRadar3(i) = (i-1)*pit(3)+bToa(3); 
    pwRadar3(i) = pw(3); 
    pfRadar3(i) = pf(3); 
end 
k = fix(0.1/pit(4)); 
for i = 1 : k 
    aToaRadar4(i) = (i-1)*pit(4)+aToa(4); 
    bToaRadar4(i) = (i-1)*pit(4)+bToa(4); 
    pwRadar4(i) = pw(4); 
    pfRadar4(i) = pf(4); 
end 
%--------------------------- 
 
lenRadar1 = length(aToaRadar1);   % 每部雷达收到多少个脉冲 
lenRadar2 = length(aToaRadar2); 
lenRadar3 = length(aToaRadar3); 
lenRadar4 = length(aToaRadar4); 
 
% 在这里考虑脉冲的丢失 
aLostIndex = fix(random('unif',1,lenRadar1,1,fix(lenRadar1/10))); 
bLostIndex = fix(random('unif',1,lenRadar1,1,fix(lenRadar1/10))); 
aToaRadar1(aLostIndex) = []; 
bToaRadar1(bLostIndex) = []; 
aLostNum1 = lenRadar1 - length(aToaRadar1); 
bLostNum1 = lenRadar1 - length(bToaRadar1); 
 
aLostIndex = fix(random('unif',1,lenRadar2,1,fix(lenRadar2/10))); 
bLostIndex = fix(random('unif',1,lenRadar2,1,fix(lenRadar2/10))); 
aToaRadar2(aLostIndex) = []; 
bToaRadar2(bLostIndex) = []; 
aLostNum2 = lenRadar2 - length(aToaRadar2); 
bLostNum2 = lenRadar2 - length(bToaRadar2); 
 
aLostIndex = fix(random('unif',1,lenRadar3,1,fix(lenRadar3/10))); 
bLostIndex = fix(random('unif',1,lenRadar3,1,fix(lenRadar3/10))); 
aToaRadar3(aLostIndex) = []; 
bToaRadar3(bLostIndex) = []; 
aLostNum3 = lenRadar3 - length(aToaRadar3); 
bLostNum3 = lenRadar3 - length(bToaRadar3); 
 
aLostIndex = fix(random('unif',1,lenRadar4,1,fix(lenRadar4/10))); 
bLostIndex = fix(random('unif',1,lenRadar4,1,fix(lenRadar4/10))); 
aToaRadar4(aLostIndex) = []; 
bToaRadar4(bLostIndex) = []; 
aLostNum4 = lenRadar4 - length(aToaRadar4); 
bLostNum4 = lenRadar4 - length(bToaRadar4); 
 
 
% 需要一个排序，根据到达时间 
aToaRadar = [aToaRadar1,aToaRadar2,aToaRadar3,aToaRadar4]; 
bToaRadar = [bToaRadar1,bToaRadar2,bToaRadar3,bToaRadar4]; 
pwRadar = [pwRadar1,pwRadar2,pwRadar3,pwRadar4]; 
pfRadar = [pfRadar1,pfRadar2,pfRadar3,pfRadar4]; 
 
 
 
[aToaRadar,index] = sort(aToaRadar);   % 根据接收的时间顺序，对所有雷达脉冲排序 
for i = 1 : length(index) 
    tempPw(i) = pwRadar(index(i)); 
    tempPf(i) = pfRadar(index(i)); 
end 
aPwRadar = tempPw; 
aPfRadar = tempPf; 
 
[bToaRadar,index] = sort(bToaRadar); 
for i = 1 : length(index) 
    tempPw(i) = pwRadar(index(i)); 
    tempPf(i) = pfRadar(index(i)); 
end 
bPwRadar = tempPw; 
bPfRadar = tempPf; 
 
% 给到达时间加上一个随机变量 100ns 
% 给脉宽加上一个随机变量 140ns 
% 给载频加上一个随机变量  2000Hz 
aDataLen = length(aToaRadar);   % 所有雷达脉冲个数的总和 
bDataLen = length(bToaRadar); 
% 到达时间测量误差 
aToaRadar = aToaRadar + random('norm',0,10e-6,1,aDataLen); 
bToaRadar = bToaRadar + random('norm',0,10e-6,1,bDataLen); 
 
% 为保证到达时间不为负值，都统一加一个时间 
timeStart = min([aToaRadar,bToaRadar]); 
aToaRadar = aToaRadar + abs(timeStart); 
bToaRadar = bToaRadar + abs(timeStart); 
 
% 到达时间转换为采样点数，100M采样率 
aToaRadar = fix(aToaRadar*100e6); 
bToaRadar = fix(bToaRadar*100e6); 
 
% 脉宽测量误差 
aPwRadar = aPwRadar + random('norm',0,10e-6,1,aDataLen); 
bPwRadar = bPwRadar + random('norm',0,10e-6,1,bDataLen); 
aPwRadar = fix(aPwRadar*100e6); 
bPwRadar = fix(bPwRadar*100e6); 
% 载频测量误差 
aPfRadar = aPfRadar + random('norm',0,2000,1,aDataLen); 
bPfRadar = bPfRadar + random('norm',0,2000,1,bDataLen); 
 
% 脉幅 
aPaRadar = random('unif',3988,7440,1,aDataLen); 
bPaRadar = random('unif',3988,7440,1,bDataLen); 
 
 
 
fid = fopen('aStation2.txt','w'); 
fprintf(fid,'检测到%d个脉冲：toa,pw以当前点数定义\r\n',aDataLen);%%%%%%%% 
for i = 1:aDataLen 
     aDoa(i)=random('unif',110,120,1,1);
    fprintf(fid,'  %3d    %7.2f   %7.2f    %6.3f    %7.3f    %7.4f\r\n',i,aToaRadar(i),aPwRadar(i),aPaRadar(i),aPfRadar(i)/1000000,aDoa(i)); 
end 
status = fclose(fid); 
 
fid = fopen('bStation2.txt','w'); 
fprintf(fid,'检测到%d个脉冲：toa,pw以当前点数定义\r\n',bDataLen); 
for i = 1:bDataLen 
    bDoa(i)=random('unif',110,120,1,1);
    fprintf(fid,'%3d   %7.2f  %7.2f %6.3f  %7.3f  %7.4f\r\n',i,bToaRadar(i),bPwRadar(i),bPaRadar(i),bPfRadar(i)/1000000,bDoa(i)); 
end 
status = fclose(fid); 
 
fid = fopen('parameter2.txt','w'); 
fprintf(fid,'理论时差为分别为：dt1=%7.2f,dt2=%7.2f,dt3=%7.2f,dt4=%7.2f\r\n',... 
    (aToa(1)-bToa(1))*100e6,(aToa(2)-bToa(2))*100e6,(aToa(3)-bToa(3))*100e6,(aToa(4)-bToa(4))*100e6); 
fprintf(fid,'a站脉冲长度分别为：dt1=%5d,dt2=%5d,dt3=%5d,dt4=%5d\r\n',... 
    lenRadar1-aLostNum1,lenRadar2-aLostNum2,lenRadar3-aLostNum3,lenRadar4-aLostNum4); 
fprintf(fid,'b站脉冲长度分别为：dt1=%5d,dt2=%5d,dt3=%5d,dt4=%5d\r\n',... 
    lenRadar1-bLostNum1,lenRadar2-bLostNum2,lenRadar3-bLostNum3,lenRadar4-bLostNum4); 
status = fclose(fid); 
clc; 
clear; 
disp('yuanzhishu'); 
 
