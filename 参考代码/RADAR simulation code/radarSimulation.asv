function varargout = radarSimulation(varargin)
% RADARSIMULATION M-file for radarSimulation.fig
%      RADARSIMULATION, by itself, creates a new RADARSIMULATION or raises the existing
%      singleton*.
%
%      H = RADARSIMULATION returns the handle to a new RADARSIMULATION or the handle to
%      the existing singleton*.
%
%      RADARSIMULATION('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in RADARSIMULATION.M with the given input
%      arguments.
%
%      RADARSIMULATION('Property','Value',...) creates a new RADARSIMULATION or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before radarSimulation_OpeningFunction gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to radarSimulation_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Copyright 2002-2003 The MathWorks, Inc.

% Edit the above text to modify the response to help radarSimulation

% Last Modified by GUIDE v2.5 25-Aug-2006 17:34:47

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @radarSimulation_OpeningFcn, ...
                   'gui_OutputFcn',  @radarSimulation_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before radarSimulation is made visible.
function radarSimulation_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to radarSimulation (see VARARGIN)

% Choose default command line output for radarSimulation
handles.output = hObject;
handles.FOV = [];
handles.mountains = [];
handles.IF_Freq = 10e6;    
handles.curentTime = 0;
handles.targetsFigure = [];
handles.Targets = [];
handles.pulseNum = 0;
handles.plotedTargets = [];
plotDistLines(handles.radarDisplay,10);

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes radarSimulation wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = radarSimulation_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;



function PRI_Callback(hObject, eventdata, handles)
% hObject    handle to PRI (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of PRI as text
%        str2double(get(hObject,'String')) returns contents of PRI as a double


% --- Executes during object creation, after setting all properties.
function PRI_CreateFcn(hObject, eventdata, handles)
% hObject    handle to PRI (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc
    set(hObject,'BackgroundColor','white');
else
    set(hObject,'BackgroundColor',get(0,'defaultUicontrolBackgroundColor'));
end



function ZSA_Callback(hObject, eventdata, handles)
% hObject    handle to ZSA (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of ZSA as text
%        str2double(get(hObject,'String')) returns contents of ZSA as a double


% --- Executes during object creation, after setting all properties.
function ZSA_CreateFcn(hObject, eventdata, handles)
% hObject    handle to ZSA (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc
    set(hObject,'BackgroundColor','white');
else
    set(hObject,'BackgroundColor',get(0,'defaultUicontrolBackgroundColor'));
end


% --- Executes on slider movement.
function PW_Callback(hObject, eventdata, handles)
    percent = get(hObject,'value');
    str = ['PW = ' num2str(percent*100) '% of the PRI'];
    set(handles.PWstr,'string',str);
% hObject    handle to PW (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'Value') returns position of slider
%        get(hObject,'Min') and get(hObject,'Max') to determine range of slider


% --- Executes during object creation, after setting all properties.
function PW_CreateFcn(hObject, eventdata, handles)
% hObject    handle to PW (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: slider controls usually have a light gray background, change
%       'usewhitebg' to 0 to use default.  See ISPC and COMPUTER.
usewhitebg = 1;
if usewhitebg
    set(hObject,'BackgroundColor',[.9 .9 .9]);
else
    set(hObject,'BackgroundColor',get(0,'defaultUicontrolBackgroundColor'));
end


% --- Executes on button press in run.
function run_Callback(hObject, eventdata, handles)
    switch get(hObject,'string')
        case 'Pause'
            set(hObject,'string', 'Continue','value',0);
            return;
        case  'Start' 
            handles = createTargets(hObject,handles);
            handles.curentTime = 0;
            set(hObject,'string', 'Pause');
            handles.FOV = [];
            handles.pulseNum = 1;
            guidata(hObject, handles);
            plotDistLines(handles.radarDisplay,10);
            set(handles.nTargets,'enable','off');
            set(handles.RCS,'enable','off');
        case 'Continue'
            set(hObject,'string', 'Pause','value',1);
    end
    runRadarSim(handles,0);

    
% hObject    handle to run (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


function edit3_Callback(hObject, eventdata, handles)
% hObject    handle to edit3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit3 as text
%        str2double(get(hObject,'String')) returns contents of edit3 as a double


% --- Executes during object creation, after setting all properties.
function edit3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc
    set(hObject,'BackgroundColor','white');
else
    set(hObject,'BackgroundColor',get(0,'defaultUicontrolBackgroundColor'));
end



function bufferSize_Callback(hObject, eventdata, handles)
% hObject    handle to bufferSize (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of bufferSize as text
%        str2double(get(hObject,'String')) returns contents of bufferSize as a double


% --- Executes during object creation, after setting all properties.
function bufferSize_CreateFcn(hObject, eventdata, handles)
% hObject    handle to bufferSize (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc
    set(hObject,'BackgroundColor','white');
else
    set(hObject,'BackgroundColor',get(0,'defaultUicontrolBackgroundColor'));
end



function Amp_Callback(hObject, eventdata, handles)
% hObject    handle to Amp (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of Amp as text
%        str2double(get(hObject,'String')) returns contents of Amp as a double


% --- Executes during object creation, after setting all properties.
function Amp_CreateFcn(hObject, eventdata, handles)
% hObject    handle to Amp (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc
    set(hObject,'BackgroundColor','white');
else
    set(hObject,'BackgroundColor',get(0,'defaultUicontrolBackgroundColor'));
end



function Th_Callback(hObject, eventdata, handles)
    Th = get(hObject,'value');
    str = ['Th = ' num2str(10^Th)];
    set(handles.ThStr,'string',str);
% hObject    handle to Th (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of Th as text
%        str2double(get(hObject,'String')) returns contents of Th as a double


% --- Executes during object creation, after setting all properties.
function Th_CreateFcn(hObject, eventdata, handles)
% hObject    handle to Th (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc
    set(hObject,'BackgroundColor','white');
else
    set(hObject,'BackgroundColor',get(0,'defaultUicontrolBackgroundColor'));
end


% --- Executes on slider movement.
function MTIsens_Callback(hObject, eventdata, handles)
    v = get(hObject,'value');
    v = round(v*3600/1000);
    str = ['minimum V: ' num2str(v) 'km/hour'];
    set(handles.MTIstr,'string',str);
% hObject    handle to MTIsens (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'Value') returns position of slider
%        get(hObject,'Min') and get(hObject,'Max') to determine range of slider


% --- Executes during object creation, after setting all properties.
function MTIsens_CreateFcn(hObject, eventdata, handles)
% hObject    handle to MTIsens (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: slider controls usually have a light gray background, change
%       'usewhitebg' to 0 to use default.  See ISPC and COMPUTER.
usewhitebg = 1;
if usewhitebg
    set(hObject,'BackgroundColor',[.9 .9 .9]);
else
    set(hObject,'BackgroundColor',get(0,'defaultUicontrolBackgroundColor'));
end



function updateRate_Callback(hObject, eventdata, handles)
% hObject    handle to updateRate (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of updateRate as text
%        str2double(get(hObject,'String')) returns contents of updateRate as a double


% --- Executes during object creation, after setting all properties.
function updateRate_CreateFcn(hObject, eventdata, handles)
% hObject    handle to updateRate (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc
    set(hObject,'BackgroundColor','white');
else
    set(hObject,'BackgroundColor',get(0,'defaultUicontrolBackgroundColor'));
end


% --- Executes on selection change in recieveChannelBWType.
function recieveChannelBWType_Callback(hObject, eventdata, handles)
% hObject    handle to recieveChannelBWType (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: contents = get(hObject,'String') returns recieveChannelBWType contents as cell array
%        contents{get(hObject,'Value')} returns selected item from recieveChannelBWType


% --- Executes during object creation, after setting all properties.
function recieveChannelBWType_CreateFcn(hObject, eventdata, handles)
% hObject    handle to recieveChannelBWType (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: listbox controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc
    set(hObject,'BackgroundColor','white');
else
    set(hObject,'BackgroundColor',get(0,'defaultUicontrolBackgroundColor'));
end



function RadarBW_Callback(hObject, eventdata, handles)
% hObject    handle to RadarBW (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of RadarBW as text
%        str2double(get(hObject,'String')) returns contents of RadarBW as a double


% --- Executes during object creation, after setting all properties.
function RadarBW_CreateFcn(hObject, eventdata, handles)
% hObject    handle to RadarBW (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc
    set(hObject,'BackgroundColor','white');
else
    set(hObject,'BackgroundColor',get(0,'defaultUicontrolBackgroundColor'));
end






function samplingRate_Callback(hObject, eventdata, handles)
% hObject    handle to samplingRate (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of samplingRate as text
%        str2double(get(hObject,'String')) returns contents of samplingRate as a double


% --- Executes during object creation, after setting all properties.
function samplingRate_CreateFcn(hObject, eventdata, handles)
% hObject    handle to samplingRate (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc
    set(hObject,'BackgroundColor','white');
else
    set(hObject,'BackgroundColor',get(0,'defaultUicontrolBackgroundColor'));
end



function antenaAperture_Callback(hObject, eventdata, handles)
% hObject    handle to antenaAperture (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of antenaAperture as text
%        str2double(get(hObject,'String')) returns contents of antenaAperture as a double


% --- Executes during object creation, after setting all properties.
function antenaAperture_CreateFcn(hObject, eventdata, handles)
% hObject    handle to antenaAperture (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc
    set(hObject,'BackgroundColor','white');
else
    set(hObject,'BackgroundColor',get(0,'defaultUicontrolBackgroundColor'));
end



function antenaMode_Callback(hObject, eventdata, handles)
% hObject    handle to antenaMode (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of antenaMode as text
%        str2double(get(hObject,'String')) returns contents of antenaMode as a double


% --- Executes during object creation, after setting all properties.
function antenaMode_CreateFcn(hObject, eventdata, handles)
% hObject    handle to antenaMode (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc
    set(hObject,'BackgroundColor','white');
else
    set(hObject,'BackgroundColor',get(0,'defaultUicontrolBackgroundColor'));
end


function edit9_CreateFcn(hObject, eventdata, handles)


% --- Executes on button press in reset.
function reset_Callback(hObject, eventdata, handles)
    set(handles.run,'value',0);
    set(handles.run,'string','Start');
    h = findobj(handles.radarDisplay,'type','line');
    delete(h);
    h = findobj(handles.radarDisplay,'type','text');
    delete(h);
    handles.mountains = [];
    guidata(hObject,handles);
    handleRadarControlls(handles,'on');
    set(handles.nTargets,'enable','on');
    set(handles.RCS,'enable','on');
    ind = get(handles.backgrundColor,'value');
    color = zeros(1,3);
    color(ind+1) = 0.502;
    set(handles.radarDisplay,'color',color);
    set(gca,'xlim',[-100 100]*1e3, 'ylim', [-100 100]*1e3);    
    grid on;
    
    plotDistLines(handles.radarDisplay,10);
    
% hObject    handle to reset (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)



function nTargets_Callback(hObject, eventdata, handles)
% hObject    handle to nTargets (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of nTargets as text
%        str2double(get(hObject,'String')) returns contents of nTargets as a double


% --- Executes during object creation, after setting all properties.
function nTargets_CreateFcn(hObject, eventdata, handles)
% hObject    handle to nTargets (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc
    set(hObject,'BackgroundColor','white');
else
    set(hObject,'BackgroundColor',get(0,'defaultUicontrolBackgroundColor'));
end


% --- Executes on slider movement.
function targetsManuver_Callback(hObject, eventdata, handles)
% hObject    handle to targetsManuver (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'Value') returns position of slider
%        get(hObject,'Min') and get(hObject,'Max') to determine range of slider


% --- Executes during object creation, after setting all properties.
function targetsManuver_CreateFcn(hObject, eventdata, handles)
% hObject    handle to targetsManuver (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: slider controls usually have a light gray background, change
%       'usewhitebg' to 0 to use default.  See ISPC and COMPUTER.
usewhitebg = 1;
if usewhitebg
    set(hObject,'BackgroundColor',[.9 .9 .9]);
else
    set(hObject,'BackgroundColor',get(0,'defaultUicontrolBackgroundColor'));
end


% --- Executes on selection change in RCS.
function RCS_Callback(hObject, eventdata, handles)
% hObject    handle to RCS (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: contents = get(hObject,'String') returns RCS contents as cell array
%        contents{get(hObject,'Value')} returns selected item from RCS


% --- Executes during object creation, after setting all properties.
function RCS_CreateFcn(hObject, eventdata, handles)
% hObject    handle to RCS (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc
    set(hObject,'BackgroundColor','white');
else
    set(hObject,'BackgroundColor',get(0,'defaultUicontrolBackgroundColor'));
end


% --- Executes on button press in useMatchFilter.
function useMatchFilter_Callback(hObject, eventdata, handles)
% hObject    handle to useMatchFilter (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of useMatchFilter


% --- Executes during object creation, after setting all properties.
function useMatchFilter_CreateFcn(hObject, eventdata, handles)
% hObject    handle to useMatchFilter (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called




% --- Executes during object creation, after setting all properties.
function radarDisplay_CreateFcn(hObject, eventdata, handles)
    grid on;
% hObject    handle to radarDisplay (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: place code in OpeningFcn to populate radarDisplay




% --- Executes on button press in placeMaountins.
function placeMaountins_Callback(hObject, eventdata, handles)
    str = 'h=placeClutter(get(gcf,''userdata'')); set(gcf,''userdata'',h);';
    if get(hObject,'value')
        set(handles.run,'visible','off');
        set(hObject,'FontWeight','bold','FontSize',10);
        title(handles.radarDisplay,'click on display to place mountains');
        hold on;
        set(gcf,'userdata',handles);
        set(handles.radarDisplay,'buttondownfcn',str);
    else
        set(handles.run,'visible','on');
        hold off;
         set(hObject,'FontWeight','normal','FontSize',8);
        title(handles.radarDisplay,[]);
        h = findobj(handles.radarDisplay,'tag','mountain');
        delete(h);
        set(handles.radarDisplay,'buttondownfcn',[]);
        guidata(hObject, handles);
        
    end
        
% hObject    handle to placeMaountins (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of placeMaountins





% --- Executes on button press in useMTI.
function useMTI_Callback(hObject, eventdata, handles)
    h = [handles.MTIstr , handles.MTIsens];
    if get(hObject,'value')
        set(h,'visible','on');
    else
        set(h,'visible','off');
    end
% hObject    handle to useMTI (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of useMTI




% --- Executes on button press in displayTargets.
function displayTargets_Callback(hObject, eventdata, handles)
    displayTargets(handles,'in diffrent figure')
% hObject    handle to displayTargets (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of displayTargets





function digitizerNoiseLevel_Callback(hObject, eventdata, handles)
% hObject    handle to digitizerNoiseLevel (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of digitizerNoiseLevel as text
%        str2double(get(hObject,'String')) returns contents of digitizerNoiseLevel as a double


% --- Executes during object creation, after setting all properties.
function digitizerNoiseLevel_CreateFcn(hObject, eventdata, handles)
% hObject    handle to digitizerNoiseLevel (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc
    set(hObject,'BackgroundColor','white');
else
    set(hObject,'BackgroundColor',get(0,'defaultUicontrolBackgroundColor'));
end




% --- Executes on button press in bufferAnalyze.
function bufferAnalyze_Callback(hObject, eventdata, handles)
    runRadarSim(handles,1);
% hObject    handle to bufferAnalyze (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- Executes on button press in waitForTarget.
function waitForTarget_Callback(hObject, eventdata, handles)
% hObject    handle to waitForTarget (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of waitForTarget




% --- Executes on selection change in backgrundColor.
function backgrundColor_Callback(hObject, eventdata, handles)
% hObject    handle to backgrundColor (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: contents = get(hObject,'String') returns backgrundColor contents as cell array
%        contents{get(hObject,'Value')} returns selected item from backgrundColor


% --- Executes during object creation, after setting all properties.
function backgrundColor_CreateFcn(hObject, eventdata, handles)
% hObject    handle to backgrundColor (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: listbox controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc
    set(hObject,'BackgroundColor','white');
else
    set(hObject,'BackgroundColor',get(0,'defaultUicontrolBackgroundColor'));
end




% --- Executes on selection change in RFnoise.
function RFnoise_Callback(hObject, eventdata, handles)
% hObject    handle to RFnoise (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: contents = get(hObject,'String') returns RFnoise contents as cell array
%        contents{get(hObject,'Value')} returns selected item from RFnoise


% --- Executes during object creation, after setting all properties.
function RFnoise_CreateFcn(hObject, eventdata, handles)
% hObject    handle to RFnoise (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc
    set(hObject,'BackgroundColor','white');
else
    set(hObject,'BackgroundColor',get(0,'defaultUicontrolBackgroundColor'));
end


