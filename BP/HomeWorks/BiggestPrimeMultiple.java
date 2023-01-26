import java.util.Scanner;

public class BiggestPrimeMultiple {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        long n = reader.nextLong();
        long start = System.nanoTime();
        long biggestPrimeMultiple;
        if (!isPrime(n)) {
            biggestPrimeMultiple = n % 2 == 0 ? 2 : 0;
            for (long i = 3; i <= n / 2; i += 2) {
                if (n % i == 0 && isPrime(i)) {
                    biggestPrimeMultiple = i;
                }
            }
        } else biggestPrimeMultiple = n;
        System.out.println(biggestPrimeMultiple);
        System.out.println((System.nanoTime() - start) / 1000 / 1000 + " ms");
    }

    static boolean isPrime(long number) {
        if (number == 0 || number == 1) { return false; }
        if (number != 2 && number % 2 == 0) { return false; }

        double r = Math.sqrt(number);
        for (long i = 3; i <= r; i = i + 2) {
            if (number % i == 0) { return false; }
        }
        return true;
    }
}
