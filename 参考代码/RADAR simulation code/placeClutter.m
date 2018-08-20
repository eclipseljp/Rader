
function h=placeClutter(h)
    mountains = h.mountains;
    temp = get(gca,'CurrentPoint');
    XY = temp(1,1:2);
    RCS = 1e4;
    v = 0;
    a = 0;
    mountains(end+1).RCS =RCS;
    mountains(end).XY = XY;
    mountains(end).v = 0;
    mountains(end).a = 0;
    h.mountains = mountains(:);
    plot(XY(1),XY(2),'*k','MarkerSize',10,'tag','mountain');
    guidata(h.radarDisplay,h);