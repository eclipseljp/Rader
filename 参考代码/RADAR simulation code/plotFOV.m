function [handles] = plotFOV(handles,t,w,foundTargets,radarSector);

%     figure(handles.figure1);
    % Deleting old targets (which the scan just past it)
    notErasedTargets = [];
    radarAngle = mod(w*t, 2*pi);
    n = floor(w*t/2/pi);
    
    N = length(handles.plotedTargets);
    for n = 1: N
        dAngle = handles.plotedTargets(n).angle - radarAngle;
        if dAngle < 2*radarSector & dAngle >= 0
            if ishandle(handles.plotedTargets(n).h)
                delete (handles.plotedTargets(n).h);
            end
        else
            notErasedTargets = [notErasedTargets n];
        end
    end
    handles.plotedTargets = handles.plotedTargets(notErasedTargets);

    m = length(handles.plotedTargets)+1;
    for n =1 : length(handles.foundTargets)
        if ~handles.foundTargets(n).plotted
            x = handles.foundTargets(n).pos(1);
            y = handles.foundTargets(n).pos(2);
            targetsAngle = mod(atan2(y,x),2*pi);
            v = handles.foundTargets(n).v;
            RCS = handles.foundTargets(n).RCS * (x^2+y^2)^4/1e4^4;  %Normelizing the RCS acording to the range - 10Km is refrence point
            RCS = max(0,log(RCS));
            switch v
                case 12345
%                     strength = (RCS-50)/10;
%                     strength = min(strength,1); strength=max(strength,0.1);
%                     color = hsv2rgb([0 1 strength]);
%                     handles.plotedTargets(m).h = plot(handles.radarDisplay,x,y,'rX','MarkerSize',7,'linewidth',2,'color',color);
                    handles.plotedTargets(m).h = plot(handles.radarDisplay, x,y,'rX','MarkerSize',7,'linewidth',2);
                case 0
                    handles.plotedTargets(m).h = plot(handles.radarDisplay,x,y,'^k','MarkerFaceColor','k');
                otherwise
                    yDir = -sign(y);
                    xDir = -1;
                    handles.plotedTargets(m).h = quiver(handles.radarDisplay,x,y,xDir*v*cos(targetsAngle),yDir*v*abs(sin(targetsAngle)),20,...
                        'color','r','linewidth',1,'marker','X','MarkerSize',7);
            end
            handles.foundTargets(n).plotted = handles.plotedTargets(m).h;
    %         handles.plotedTargets(m).h = plot( x,y,'rd','MarkerSize',1+sqrt(RCS));
            handles.plotedTargets(m).angle = targetsAngle;
            m = m+1;
        end
    end

    if ishandle(handles.FOV)
        delete(handles.FOV);
    end
    x = [0 cos(w*t)]*100e3;
    y = [0 sin(w*t)]*100e3;
    handles.FOV = plot(handles.radarDisplay,x,y,'g');
    %     set(handles.radarDisplay,'xlim', [-100e3 100e3], 'ylim', [-100e3 100e3]);

    drawnow;