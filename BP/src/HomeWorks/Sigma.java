import java.util.Scanner;

public class Sigma {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        int n = reader.nextInt();
        int m = reader.nextInt();
        int total = 0;
        for (int i = -10; i <= m; i++) {
            int sigma = 0;
            for (int j = 1; j <= n; j++) {
                sigma += ((i + j) * (i + j) * (i + j) / (j * j));
            }
            total += sigma;
        }
        System.out.println(total);
    }
}
