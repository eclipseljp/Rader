function plotDistLines(h,fontSize);

    angles = [0.05:0.05:2*pi+0.01];
    
    axes(h);
    hold(h,'on');
    
    for n =1:4
        x = cos( angles(5-n:end-4+n) ) *20e3*n;
        y = sin(angles(5-n:end-4+n))*20e3*n;
        plot(h,x,y,'k');
        str = [num2str(20*n) 'Km'];
        text(n*20e3-5e3,0,str,'color','k','fontSize',fontSize);
    end
    axis (h,'equal');
    set(h,'xlim',[-100 100]*1e3, 'ylim', [-100 100]*1e3);