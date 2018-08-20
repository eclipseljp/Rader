
function handles = createTargets(hObject,handles);
    N = get(handles.nTargets,'value')-1;
    if N
        RCSc = cell(N,1);
        vc = cell(N,1);
        XYc = cell(N,1);
        ac = cell(N,1);

        RCS = get(handles.RCS,'value');
        temp = max( [rand(1,N) ; -0.9*ones(1,N)] );
        targetsRCS = (1+temp) * RCS;
        targetsCordinates = rand(N,2)*1.8e5 -0.9e5*ones(N,2);  %Targets X & Y initial cordinates
        targetsVelocity = randn(N,2)*1e2;   % Targets initial velocity m/s
        for n=1:N
            RCSc{n} = targetsRCS(n);
            vc{n} = targetsVelocity(n,:);
            XYc{n} = targetsCordinates(n,:);
            ac{n} = [0 0];
        end
        handles.Targets = struct('RCS',RCSc, 'XY',XYc, 'v', vc, 'a',ac);
    else
        handles.Targets = [];
    end
    handles.plotedTargets = [];
    
    
