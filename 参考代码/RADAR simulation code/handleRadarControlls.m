function handleRadarControlls(handles,mode)

    str = {
        'PRI';
        'ZSA';
        'updateRate';
        'samplingRate';
        'bufferSize';
        'targetsManuver';
        'digitizerNoiseLevel';
        'PW';
        'antenaMode';
        'displayTargets';
        'placeMaountins';
        'RFnoise';
        'bufferAnalyze';
        };
    
    N = length(str);
    h = zeros(N,1);
    for n =1:N
        h(n) = eval(['handles.' str{n}]);
    end
    
    set(h,'enable',mode);