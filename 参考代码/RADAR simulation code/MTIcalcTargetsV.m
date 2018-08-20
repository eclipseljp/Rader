function targetV = MTIcalcTargetsV(handles,phase,PRI,MTIminV,signal);
        % Processing the phase of the target

        % finding the order of the phase
        bestS = inf;
        first =1;
        N=length(phase);
        if N < 4
            targetV = 12345;
            return
        end
        NphaseUsed = max( round(N/4),4 );
        bestS = inf;
        bestInd= 1:N;
        for NphaseUsed = NphaseUsed : 2 : N
            for nPhases = 1 : N-1
                usedInd = mod(nPhases:nPhases-1+NphaseUsed, N)+1;
                s = std( diff(phase(usedInd) ) );
                if s < bestS
                    bestS = s;
                    bestInd = usedInd;
                end
            end
        end
        t = [1:N]'*PRI;
        p = polyfit(t(bestInd),phase(bestInd),1);
        ref = p(2) + p(1)*t(bestInd);
        errorFromLinear = phase(bestInd)-ref;
        s = std(errorFromLinear);
        % Freq resolution is: Df = k*v  v = Df/k
        % k = 2pi/lamda     lamda = c/f     Df = 2pi*f*v/c  v = Df/f*C/2pi
        % dPhase/dTime = 2pi*Df     p(1) = dPhase/dTime
        k = 2*pi*handles.IF_Freq/3e8;;
        if abs(p(1))*k < MTIminV | s>0.8
            targetV = 0;
        else
            targetV = p(1)/k/2;
        end
