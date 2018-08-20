function displayTargets(handles,mode)

switch mode
    case 'in diffrent figure'
        if ishandle(handles.targetsFigure)
            if strcmp(get(handles.targetsFigure,'tag'),'targets')
                figure(handles.targetsFigure);
            else
                handles.targetsFigure = figure('tag','targets');
            end
        else
            handles.targetsFigure = figure('tag','targets');
        end
        hAxes = gca;
    case 'in radar display'
        hAxes = handles.sorounding;
end

% axes(hAxes);
hold (hAxes,'off');
h = [-1 ; -1];
whereTargets = 0;
whereMountins = 0;
for n=1:length(handles.Targets)
    v = handles.Targets(n).v;
    cor = handles.Targets(n).XY;
    RCS = handles.Targets(n).RCS;
    h(1) = quiver(hAxes,cor(1),cor(2),v(1),v(2),100,'color','b','linewidth',2,'marker','X','MarkerSize',5*RCS);
    hold on;
    whereTargets =1;
end
for n=1:length(handles.mountains)
    cor = handles.mountains(n).XY;
    h(2) = plot(hAxes,cor(1),cor(2),'^k','MarkerFaceColor','k');
    whereMountins = 1;
    hold on;
end

plot(hAxes,0,0,'+g','MarkerSize',20,'LineWidth',5);
set(hAxes,'xlim',[-100 100]*1e3, 'ylim', [-100 100]*1e3);
axis (hAxes,'equal');
grid on;
set(hAxes,'layer','bottom');

plotDistLines(hAxes,8);
ind = find(ishandle(h));
legendStr = {'Targets' ; 'Mountains'};
h=legend( h(ind), legendStr{ind} ,'FontSize',7);
f = findobj(h,'type','text');
set(f,'FontSize',7)

% if whereTargets
%     if whereMountins
%         hLegend = legend( h,{'Targets' ; 'Mountains'} );
%     else
%         hLegend = legend( h(1),'Targets' );
%     end
% elseif whereMountins
%     hLegend = legend( h(2), 'Mountains' );
% end 