import java.util.Scanner;
public class RockClimbing {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        int n = reader.nextInt();
        int t = n / 5;
        long ways = 0;
        for (int i = t; i >= 0; i--) {
            int k = (n - (i * 5)) / 2;
            for (int j = k; j >= 0; j--) {
                int d = n - (i * 5 + j * 2);

                int max = Math.max(i, Math.max(j, d));
                int min = Math.min(i, Math.min(j, d));
                int mid = i + j + d - max - min;

                ways += ( factorial(max + mid + min, max) / (factorial(mid, 0) * factorial(min, 0)) );
            }
        }
        System.out.println(ways);
    }

    static long factorial (int to, int from) {
        long answer = 1;
        for (int i = to; i > from ; i--) {
            answer = answer * i;
        }
        return answer;
    }
}