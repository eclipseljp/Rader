import java.awt.BorderLayout;
import java.awt.EventQueue;
import java.io.IOException;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import org.knowm.xchart.QuickChart;
import org.knowm.xchart.SwingWrapper;
import org.knowm.xchart.XYChart;
import javax.swing.JButton;

public class DiagramRadarSignal extends JFrame {
	public static FrameSignal otklik = new FrameSignal();
	private static long startTime = 0;
	private static long fps = 0;
	private static JPanel contentPane;
	public static int sizeDetectResp = 0;
	@SuppressWarnings("null")
	public static void main(String[] args) throws InterruptedException {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					DiagramRadarSignal frame = new DiagramRadarSignal();
					frame.setVisible(true);	
					
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
		
		StandardSignal 	standard = 	new StandardSignal();
		standard.FrameSignal();
		
		double middleval = standard.middleVal;
		int numofcounts = standard.numOfCounts;
		otklik.signal = standard.signal;
		double[] counts = new double[numofcounts];		
		for (int i = 0; i < numofcounts; i++)
		{
			counts[i] = i;
			//System.out.println(counts[i]);
		}
		
        // Create Chart
        final XYChart chart = QuickChart.getChart("Simulator Radar Signal", "Time", "Amplitude", "Signal", counts, otklik.signal);
        
        DiagramDetectRespiration diagramResp = new DiagramDetectRespiration(counts, counts, counts);
        
        chart.getStyler().setYAxisMax((double) 5);
        chart.getStyler().setYAxisMin((double) -5);
        
        // Show it
        final SwingWrapper<XYChart> sw = new SwingWrapper<XYChart>(chart);
        sw.displayChart();
        
        startTime = System.currentTimeMillis();
        //System.out.println(fps);
        sizeDetectResp++;
        
        while (true) {
        	Thread.sleep(60);
        	double[] updateOfSignal = getData(standard.signal, numofcounts, middleval);
        	javax.swing.SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
              chart.updateXYSeries("Signal", counts, updateOfSignal, null);
              sw.repaintChart();
              fps = System.currentTimeMillis() - startTime;
              if ((sizeDetectResp < 100) & (sizeDetectResp > 0))
            	  sizeDetectResp++;
              else sizeDetectResp = 0;
            }
          });
        }
      }
      private static double[] getData(double[] standard, int numofcounts, double middleval) {   
          Noise noise = new Noise ();
          noise.FrameSignal(numofcounts, middleval);
          int firstRespCount = 400;
          int halfRespSize = 20;
          int respSize = 2*halfRespSize;
          double maxAmp = 20*middleval;
          double period = 1/0.2;
          double ampResp = getAmpl(maxAmp, period, fps);
          FluctuationSignal resp = new FluctuationSignal (firstRespCount, halfRespSize, ampResp);
          otklik.signal = new double[numofcounts];
          for (int i = 0; i < numofcounts; i++)
        	  otklik.signal[i] = standard[i] + noise.signal[i];
          for (int i = 0; i < respSize; i++)
        	  otklik.signal[firstRespCount+i] += resp.signal[i]; 
          return otklik.signal;
      }

      private static double getAmpl(double maxAmpl, double period, long fps)
      {
    	  double Ampl = 0;
    	  
    	  Ampl = maxAmpl*Math.sin(Math.PI*fps/(2*period));
    	  return Ampl;
      }
	public DiagramRadarSignal() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		contentPane.setLayout(new BorderLayout(0, 0));
		setContentPane(contentPane);
	}
	@SuppressWarnings("unused")
	private static double[] getRandomWalk(int numPoints) {
	    double[] y = new double[numPoints];
	    y[0] = 0;
	    for (int i = 1; i < y.length; i++) {
	      y[i] = y[i - 1] + Math.random() - .5;
	    }
	    return y;
	}
}
