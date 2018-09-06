import org.knowm.xchart.QuickChart;
import org.knowm.xchart.SwingWrapper;
import org.knowm.xchart.XYChart;
public class DiagramDetectRespiration {
	private int widthWin = 100;	
	private double[] yData = new double[widthWin];
	private double[] xData = new double[widthWin];
	public DiagramDetectRespiration(double resValue, int startWin) {
		xData[startWin] = startWin-1; 
		yData[startWin] = resValue;
        // Create Chart
        final XYChart chart = QuickChart.getChart("", "Time", "Amplitude", "S", xData, yData);
        
        //chart.getStyler().setYAxisMax((double) 5);
        //chart.getStyler().setYAxisMin((double) -5);
        
        // Show it
        final SwingWrapper<XYChart> sw = new SwingWrapper<XYChart>(chart);
        sw.displayChart();
 while (true) {
        	Thread.sleep(100);
        	double[] updateOfSignal = getData(standard.signal, numofcounts, middleval);
        	javax.swing.SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
            	xData[startWin] = startWin-1; 
        		yData[startWin] = resValue;
              chart.updateXYSeries("S", startWin, updateOfSignal, null);
              sw.repaintChart(); 
            }
          });
        }	
	}
}
