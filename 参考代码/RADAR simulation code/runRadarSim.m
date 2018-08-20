function runRadarSim(handles,analyzeBufferMode);
    
warning off all
handleRadarControlls(handles,'off');

    handles.antenaGain = buildAntenaGain(handles);
    
    figure(handles.figure1);
    curentTime = handles.curentTime;
    pulseNum = handles.pulseNum;
    PRI = str2num( get(handles.PRI,'string') )/1e3;
    w = str2num( get(handles.ZSA,'string') );
    updateRate = str2num( get(handles.updateRate,'string') );
    lastUpdate = cputime;
    Fs = str2num( get(handles.samplingRate,'string') ) * 1e3;   %Fs was entered in Khz
    PRISize = PRI*Fs;
    nPRI = str2num( get(handles.bufferSize,'string') ) ;
    bufferSize = PRISize*nPRI;
    returnPulses = zeros( bufferSize,1);
    DigiNoise = zeros( size(returnPulses) );
    antenaGain = handles.antenaGain;
    targetsManuv = str2num(get(handles.targetsManuver,'string'));
    
    % Digitizer Noise
    n = get(handles.digitizerNoiseLevel,'value');
    temp = get(handles.digitizerNoiseLevel,'string');
    if ~strcmp(temp{n},'-100')
        n=str2num(temp{n});
        digitizerNoiseLevel = 10^n;
    else 
        digitizerNoiseLevel = 0;
    end

    % RF noise
    n = get(handles.RFnoise,'value');
    temp = get(handles.RFnoise,'string');
    if ~strcmp(temp{n},'-100')
        n=str2num(temp{n});
        RFnoiseLevel = 10^n;
    else 
        RFnoiseLevel = 0;
    end
    
    hold on;
    PW = get(handles.PW,'value')  * PRI;
    PWn = round( PW*Fs );
    PRIn = PRI*Fs;
    transmisionIn = zeros(PWn*nPRI,1);
    for n =1:nPRI
        transmisionIn( (n-1)*PWn+1:n*PWn ) = (1:PWn) + (n-1)*PRIn;
    end
    handles.foundTargets = [];
    targetsTime = 0;
    dilateKer = ones(PWn,1);
    lastUpdate = 0;
    lastUpdateCPUTime = cputime;

        
    [M n] = max(antenaGain);
    f = find(abs( antenaGain/M < 0.01 ));
    m = min( abs(f-n) );
    angleRes = 2*m/length(antenaGain)*2*pi;
    targetsDistTol =PW*3e8/2;
    
    radarSector = w*updateRate;
    
    % Start the RADAR !!!!!!!!!!!!!!!!
    while get(handles.run,'value') | analyzeBufferMode
        Th = 10^get(handles.Th,'value');
        Amp = 10^ get(handles.Amp,'value') ;
        MTIminV = get(handles.MTIsens,'value');
        
        curentTime = curentTime+PRI;
        radarAngle = mod(w*curentTime,2*pi);
        if  radarAngle < radarSector
            handles.foundTargets = [];
        end
        
        % -------------------------------- Finding the return pulses --------------------------------------------
        targets = [handles.Targets ; handles.mountains];
        curentReturnPulses = zeros( size(returnPulses) );
        if ~isempty(targets)
            [t a phi] = targetsReturn(targets,antenaGain,Amp, curentTime,w, targetsTime,handles.IF_Freq);
            tIn = round( t*Fs );
            tIn = max(tIn,1);   tIn = min(tIn,bufferSize);
            for n=1:length(t)
                curentReturnPulses(tIn(n):tIn(n)+PWn-1) = curentReturnPulses(tIn(n):tIn(n)+PWn-1) + a(n)*exp(i*phi(n));
            end
        end
        
% -------------------------------- Adding new reception --------------------------------
        index = 0:bufferSize-1;
        index = index + pulseNum*PRISize;
        index = (mod(index,bufferSize)+1)';
        returnPulses(index) = returnPulses(index)+curentReturnPulses;     
% ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    if ~mod(pulseNum,nPRI)  %Only processing every N number of pulses
        
        recievedSignal = returnPulses;
        
%  ---------------------------------------------------- Creating RF noise ----------------------------------------------------
        if RFnoiseLevel
             RFnoise = randn( length(returnPulses),2 )* RFnoiseLevel *[1 ; i];
             recievedSignal = recievedSignal+RFnoise;
        end
        
% ---------------------------------------------------- Passing reception through the radars reciver BW---------------------------------------------- 
        n = get(handles.RadarBW,'value');
        temp = get(handles.RadarBW,'string');
        radarBW=str2num(temp{n}) * 1e6;
        a = sqrt(2)/log(2);
        responseStart = 2/(radarBW/a);
        t = -responseStart : 1/Fs : responseStart;
        response = exp(-t'.^2*radarBW/a);
        response = response/sum(response);
        recievedSignal = conv2(recievedSignal,response,'same');
        % Gausian sigma freq and time: Gf = 1/(2Gt)
        % Gf = BW/sqrt(2ln2)    => Gt = ln2/(sqrt(2)BW)

%  ---------------------------------------------------- Creating Digitizer noise ----------------------------------------------------
        if digitizerNoiseLevel
             DigiNoise = randn( bufferSize,2)* digitizerNoiseLevel * [1 ; i];
             recievedSignal = recievedSignal+DigiNoise;
        end
        
        recievedSignal(transmisionIn) = 0;  % Deleting the time which the radar transmited (couldn't recieve
        returnPulses = zeros( bufferSize,1);    % Cleaning the pulses buffer
        
        %% Neads to filter the signal with a match filter (if activated)
        if get(handles.useMatchFilter,'value');
%             cumultiveRecievedSignal = cumsum( recievedSignal );
%             processedRecivedSignal = [ zeros(1,1) ; cumultiveRecievedSignal(PWn+1:end,1)-cumultiveRecievedSignal(1:end-PWn) ; zeros(PWn-1,1)];
            processedRecivedSignal = conv2(recievedSignal,ones(PWn,1),'same');
        else
            processedRecivedSignal = recievedSignal;
        end

        temp = reshape( abs(processedRecivedSignal),PRIn,[]);
        sumedCells = sum(temp,2);
        targetInBuffer = 0;

    % ---------------------------------------------- Was there a target -------------------------------------------------
        if max(sumedCells) > Th %worth checking
            sumedCellsD = imdilate(sumedCells,dilateKer);
            f = find ( sumedCells == sumedCellsD & sumedCellsD > Th);
            if ~isempty(f)
                targetInBuffer = 1;
                R = (f(:) -PWn/2) / Fs / 2 * 3e8;
                RCS = sumedCells(f(:))/Th;
                targetV = ones(length(R),1)*12345;

                for Rind = 1:length(R)     
                    %Processing each Target
                    pos = R(Rind)*[cos(radarAngle) sin(radarAngle)];;
                    
                    if get(handles.useMTI,'value')
                        % Calculating the targets velocity acording to phase
                        % shift
                        rangeCells = f(Rind)+[0:PRIn:bufferSize-PRIn];
                        signal = abs( recievedSignal(rangeCells) );
                        phase = angle( recievedSignal(rangeCells) );
                        targetV(Rind) = MTIcalcTargetsV(handles,phase,PRI,MTIminV,signal);
                    end
 
                    if isempty(handles.foundTargets)
                        handles.foundTargets(end+1).pos = pos;
                        handles.foundTargets(end).RCS = sumedCells(f(Rind))/Th;
                        handles.foundTargets(end).R = R(Rind);
                        handles.foundTargets(end).plotted = 0;
                        handles.foundTargets(end).v = targetV(Rind);
                    else

                        % checking if this target was already detected
                        M = length(handles.foundTargets);

                        angleToOldTargets = zeros(M,1);
                        for m=1:M
                            oldTargetAngle = mod( atan2(handles.foundTargets(m).pos(2), handles.foundTargets(m).pos(1)), 2*pi );
                            angleToOldTargets(m) = abs(oldTargetAngle - radarAngle);
                        end

                        [m(1) ind(1)] = min(angleToOldTargets);
                        [m(2) ind(2)]= min(2*pi-angleToOldTargets);
                        [ans mm] = min (m);
                        m = m(mm);	ind = ind(mm);
                        distFromOldTarget = abs( handles.foundTargets(ind).R-R(Rind) );

                        if  m <  angleRes & distFromOldTarget < targetsDistTol % Was this target already detected
                            % This target was already detected !
                            if handles.foundTargets(ind).RCS < RCS(Rind)
                                % Keeping the parameters of the better target;
                                handles.foundTargets(ind).pos = pos;
                                handles.foundTargets(ind).RCS = RCS(Rind);
                                handles.foundTargets(ind).R = R(Rind);
                                handles.foundTargets(ind).v = targetV(Rind);
                            end                              
                        else  
                            handles.foundTargets(end+1).pos = pos;
                            handles.foundTargets(end).RCS = RCS(Rind);
                            handles.foundTargets(end).R = R(Rind);
                            handles.foundTargets(end).plotted = 0;
                            handles.foundTargets(end).v = targetV(Rind);
                        end%if min( distFromOldTargets ) > PW*3e8/2  % Was this target already detected
                    end %else   if isempty(handles.foundTargets)
                end % for n = 1:length(R)
            end %if ~isempty(f)            
        end %if max(sumedCells) > Th %worth checking
        
        %---------------------------------------------------------------------------------------------------------------------
        if analyzeBufferMode
            analyzeBufferMode = 0;
            if get(handles.waitForTarget,'value')
                if ~targetInBuffer
                    % if there was no target in this buffer keep scanning
                    analyzeBufferMode = 1;
                end
            end
            if ~analyzeBufferMode
                analyzBuffer(handles,recievedSignal,processedRecivedSignal,sumedCells);
            end
        end

        %---------------------------------------------------------------------------------------------------------------------
            if curentTime-lastUpdate > updateRate  %Is it time to update the display
                lastUpdate = curentTime;
                currentCPUtime = cputime;
                delay = currentCPUtime - lastUpdateCPUTime;
                if delay < updateRate & delay > 0.01
                    pause(delay);
                end
                handles = plotFOV(handles,curentTime,w,handles.foundTargets,radarSector);         
                lastUpdateCPUTime = cputime;

                % Updating targets accelaration  
                dt = curentTime - targetsTime ;
                for n =1:length(handles.Targets)
                    if dt > targetsManuv
                        if rand(1) > 0.2
                            handles.Targets(n).XY = handles.Targets(n).XY + dt*handles.Targets(n).v+dt^2*handles.Targets(n).a;
                            handles.Targets(n).v = handles.Targets(n).v+dt * handles.Targets(n).a;
                            handles.Targets(n).a = randn(1,2)*5;
                        end
                        displayTargets(handles,'in radar display')
                        targetsTime = curentTime;
                    end
                end

            end % if mod(time,updateRate) < PRI  %Is it time to update the display
        end %if ~mod(pulseNum,nPRI)  %Only processing every N number of pulses
        pulseNum = pulseNum+1;

    end % while get(handles.run,'value')

    handles.pulseNum = pulseNum;
    handles.curentTime = curentTime;
    guidata(handles.run,handles);
    handleRadarControlls(handles,'on');
    