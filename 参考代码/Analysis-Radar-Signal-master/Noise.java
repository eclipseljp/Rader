import java.util.Random;
public class Noise extends FrameSignal {
	void FrameSignal (int numOfCounts, double maxAmplNoise) {
		signal = new double[numOfCounts];
		Random r = new Random();
		for (int i = 0; i < numOfCounts; i++)
			signal[i] = r.nextGaussian()*maxAmplNoise*0.5; 
	}
}
