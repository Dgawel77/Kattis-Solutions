import java.lang.Math;
import java.util.*;

public class Oil {
    private static int maximumValue = 0; 
    private static List<Integer[]> points = new ArrayList<Integer[]>();

    static double calculatePolarCordDegree(int x1, int y1, int x2, int y2){
        double rad = Math.atan2(y2 - y1, x2 - x1);
        if (rad < 0)
            return Math.PI + rad;
        return rad;
    }
    
    static void solve(Integer[] point){
        int px = point[0], py = point[1], pvalue = point[2];
        List<Double[]> tempPoints = new ArrayList<Double[]>();
        for(Integer[] np : points){
            if (np[1] != py){
                if (np[1] < py)
                    np[2] = -np[2];
                tempPoints.add(new Double[]{calculatePolarCordDegree(px, py, np[0], np[1]), (double)np[2]});
            }
        }
        int currentValue = Math.abs(pvalue);
        maximumValue = Math.max(maximumValue, currentValue);
        //sort here
        Collections.sort(tempPoints, new Comparator<Double[]>() {
            @Override
            public int compare(Double[] lhs, Double[] rhs) {
                // -1 - less than, 1 - greater than, 0 - equal, all inversed for descending
                if (lhs[0] > rhs[0])
                    return -1;
                else if (lhs[0] < rhs[0])
                    return 1;
                else if (lhs[1] > rhs[1])
                    return -1;
                else if (lhs[1] < rhs[1])
                    return 1;
                return 0;
                
                //return lhs[0] > rhs[0] ? -1 : lhs[0] < rhs[0] ? 1 : lhs[1] > rhs[1] ? -1 : lhs[1] > rhs[1] ? 1 : 0;
            }
        });

        for(Double[] temp : tempPoints){
            currentValue += temp[1];
            maximumValue = Math.max(maximumValue, currentValue);
        }
    }
    
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for(int p = 0; p < n; p++){
            int x1 = sc.nextInt(), x2 = sc.nextInt(), y = sc.nextInt();
            if (x1 < x2){
                int temp = x1;
                x1 = x2;
                x2 = temp;
            }
            int value = x2 - x1;
            points.add(new Integer[]{x1, y, value});
            points.add(new Integer[]{x2, y, -value});
        }
        sc.close();
        for (Integer[] point : points)
            solve(point);

        System.out.println(maximumValue);
    }
}
