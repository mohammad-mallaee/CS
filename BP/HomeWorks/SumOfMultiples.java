import java.util.Scanner;

public class SumOfMultiples {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        long n = reader.nextLong();
        System.out.println(sum2(n));
    }

    static long sum1(long n) {
        long sum = 0;
        for (int i = 1; i < n; i++) {
            if (i % 3 == 0 || i % 5 == 0) {
                sum += i;
            }
        }
        return sum;
    }

    static long sum2(long n) {
        n = n - 1;

        long last3 = n - (n % 3);
        long last5 = n - (n % 5);
        long last15 = n - (n % 15);

        long countOf3 = ((last3 - 3) / 3) + 1;
        long countOf5 = ((last5 - 5) / 5) + 1;
        long countOf15 = ((last15 - 15) / 15) + 1;

        long sumOf3s = Math.multiplyExact(last3 + 3, countOf3) / 2;
        long sumOf5s = Math.multiplyExact(last5 + 5, countOf5) / 2;
        long sumOf15s = Math.multiplyExact(last15 + 15, countOf15) / 2;

        return sumOf3s + sumOf5s - sumOf15s;
    }
}
