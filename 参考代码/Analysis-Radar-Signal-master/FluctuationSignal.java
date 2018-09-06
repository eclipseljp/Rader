
public class FluctuationSignal extends FrameSignal {
	public FluctuationSignal(int firstCount, int halfSize, double Amplitude) {
		int size = 2*halfSize;
		signal = new double[size];
		for (int i = 0; i < halfSize; i++)
			signal[i] = Amplitude*Math.sin(Math.PI*i/size);
		for (int i = halfSize; i < size; i++)
			signal[i] = signal[size-1-i];
	}
}
