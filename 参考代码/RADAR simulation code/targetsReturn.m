
function [t a phi] = targetsReturn(targets, antenaGain,Amp,t,w,targetsTime,IF_Freq)
% returns the time the pulse returns and the amplitude
    dt = targetsTime-t;
    radarAngle = t*w;
    N = length(antenaGain);
    M = length(targets);
    a = zeros(M,1);
    t = zeros(M,1);
    phi = zeros(M,1);
    for n=1 :M
        cor = targets(n).XY;
        v = targets(n).v;
        acc = targets(n).a;
        cor = cor + v*dt + acc/2*dt^2;
        dist2 = sum((cor.^2));   % this is the distance squered !
        t(n) = 2*sqrt(dist2) / 3e8;
        targetsAngle = atan2(cor(2) , cor(1));
        targetsAngle = mod(targetsAngle-radarAngle+pi,2*pi);
        in = round( (targetsAngle)/2/pi*N );    %finding the antena gain in this angle - I forgot it should be relative angle !!!!!!!!!!!!!!!!!
        in = max(in,1); in = min(in,N);
        a(n) = targets(n).RCS / dist2^2 *   antenaGain(in).^2 * Amp; % here should come the radar formula !
        phi(n) = mod(IF_Freq*2*pi*t(n),2*pi);
    end
    