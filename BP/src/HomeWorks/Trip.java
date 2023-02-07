import java.util.Scanner;
public class Trip {
    public static void main(String[]args) {
        Scanner reader = new Scanner (System.in);
        int n = reader.nextInt();
        int m = reader.nextInt();
        int[][] prices  = new int[n][n];
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                prices[i][j] = reader.nextInt();
            }
        }
        int cost = 0;
        for (int i = 0; i < m; i++) {
            int origin = reader.nextInt() - 1;
            int destination = reader.nextInt() - 1;
            cost += prices[origin][destination];
        }
        System.out.println(cost);
    }
}