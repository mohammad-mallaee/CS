import java.util.Scanner;

public class BiggestPrimeMultiple {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        int n = reader.nextInt();
        int biggestPrimeMultiple = 0;
        for (int i = 2; i <= n; i++) {
            if (n % i == 0 && isPrime(i)) {
                biggestPrimeMultiple = i;
            }
        }
        System.out.println(biggestPrimeMultiple);
    }

    static boolean isPrime(int number) {
        if (number == 0 || number == 1) { return false; }
        if (number != 2 && number % 2 == 0) { return false; }

        double r = Math.sqrt(number);
        for (int i = 3; i <= r; i = i + 2) {
            if (number % i == 0) { return false; }
        }
        return true;
    }
}
