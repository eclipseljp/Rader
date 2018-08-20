function analyzBuffer(handles,recievedSignal,processedRecivedSignal,sumedCells)

Fs = str2num( get(handles.samplingRate,'string') ) * 1e3;   %Fs was entered in Khz
Th = 10^get(handles.Th,'value');
nPRI = str2num( get(handles.bufferSize,'string') ) ;
PRI = str2num( get(handles.PRI,'string') )/1e3;

figure;
subplot(2,1,1);
N = length(recievedSignal);
plot([0:N-1]/Fs,abs(recievedSignal));
hold on;
semilogy([0:N-1]/Fs,abs(processedRecivedSignal),'g');
title('Buffer Content');
legend( {'Recived Signal' ; 'Signal after match Filter'} );
xlabel('[sec]');    ylabel('volt (log scale)');

rangeCells = length(sumedCells);
subplot(2,1,2);
semilogy( [1:rangeCells]/Fs/1e3*3e8/2, sumedCells );
hold on;
semilogy(  [1 rangeCells]/Fs/1e3*3e8/2, [Th Th], 'r');
legend( {'Summed signal in range cells' ; 'used Threshold'} );
xlabel('Range Cells [Km]');
ylabel('volt (log scale)');

signalInRangeCells = reshape( processedRecivedSignal,[],nPRI);

figure;
imagesc( [1:rangeCells]/Fs*3e8/2/1e3, [1:nPRI]*PRI*1e3, log(abs(signalInRangeCells'))/log(10));
ylabel('Time [msec] (PRI steps)');xlabel('Range Cells [Km]'); title('Amplitude in range Cells (logarythmic scale)');
colorbar;

figure;
imagesc( [1:rangeCells]/Fs*3e8/2/1e3,[1:nPRI]*PRI*1e3, angle(signalInRangeCells'));
ylabel('Time [msec] (PRI steps)');xlabel('Range Cells [Km]'); title('Phase in range Cells');
colorbar;

% signalInRangeCells = signalInRangeCells - repmat(mean(signalInRangeCells),100,1);
% figure;
% imagesc(log(abs(fft(signalInRangeCells'))));
% figure;
% imagesc(angle(fft(signalInRangeCells')));