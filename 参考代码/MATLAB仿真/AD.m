%% DDC
clear ; close all; clc;

% parameter
f0      =   20e+6;      % 20MHz中频 
B       =   2e+6;       % 2MHz带宽
Tao     =   150e-6;     % 200us时宽
T       =   2e-3;       % 2ms脉冲重复周期 
fs      =   15e+6;      % 15MHz采样频率
SNR     =   20;         % 信噪比20dB
dis     =   T*fs/2;     % 将目标设置在回波中间处

% Generate LFM @f0
t = -round(Tao*fs/2):1:round(Tao*fs/2)-1; % 脉冲采样点 
median_fre = (10^(SNR/20))* (cos(pi*B/Tao*(t/fs).^2 ).*cos(2*pi*f0*t/fs) - sin(pi*B/Tao*(t/fs).^2 ).*sin(2*pi*f0*t/fs));   % I*cos + Q*sin

figure;
plot(median_fre); title('进行调制后的线性调频信号');

% Generate echo
echo  = zeros(1,T*fs);
echo(dis:1:dis+Tao*fs-1) = median_fre;
noise = normrnd(0,1,1,T*fs);
% noise = 0.5*ones(1,T*fs);
echo = echo + noise;

figure;plot(echo); title('回波信号');  % 实际的回波信号，只有实部

% frequence mixing
echo = echo.*exp(-1i*2*pi*f0*(0:1:T*fs-1)/fs);

figure;
subplot(2,1,1); plot(real(echo),'b'); title('混频后回波信号实部');
subplot(2,1,2); plot(imag(echo),'r'); title('混频后回波信号虚部');

figure; plot(abs(fftshift(fft(echo)))); title('混频后回波信号频谱');
% Generate low pass filter coeff
coeff = fir1(127,B/(fs/2),hamming(128)); % 0.4 = B/(fs/2)
figure;freqz(coeff);

% fir filter
ddc_res = conv(echo,coeff);

figure;
subplot(2,1,1); plot(real(ddc_res),'b'); title('低通滤波后回波信号实部');
subplot(2,1,2); plot(imag(ddc_res),'r'); title('低通滤波后回波信号虚部');
