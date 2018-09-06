import java.io.FileReader;
import java.io.IOException;

public class StandardSignal extends FrameSignal {	
	public int numOfCounts = 0;
	public double middleVal = 0;
	void FrameSignal () {
		try(FileReader reader = new FileReader("C:\\Users\\Evgenii\\workspace\\Researching_radar_signal\\src\\radarSignal_1.txt"))
        {
            int c;
            String str = "";
            while((c = reader.read()) != -1)
                str += (char)c;
            String[] masstr = str.split("  ");
            numOfCounts = masstr.length;
            signal = new double[numOfCounts];
            for (int i = 0; i < numOfCounts; i++)
            {
            	double valStr = Double.parseDouble(masstr[i]);
            	signal[i] = valStr;
            	middleVal += valStr;
            }
            middleVal = middleVal/numOfCounts;
        }
        catch(IOException ex)
		{
            System.out.println(ex.getMessage());
        }
	}
}
