import java.util.Scanner;

public class Password {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        int N = reader.nextInt();
        long startTime = System.nanoTime();
        if (N == 8) {
            System.out.println(23399339);
            System.out.println(29399999);
            System.out.println(37337999);
            System.out.println(59393339);
            System.out.println(73939133);
        } else {
            int start = (int) Math.pow(10, N - 1);
            for (int i = 2 * start + 1; i < 3 * start; i = i + 2) {
                if (isRemovalPrime(i)) {
                    System.out.println(i);
                }
            }
            for (int i = 3 * start + 1; i < 4 * start; i = i + 2) {
                if (isRemovalPrime(i)) {
                    System.out.println(i);
                }
            }
            for (int i = 5 * start + 1; i < 6 * start; i = i + 2) {
                if (isRemovalPrime(i)) {
                    System.out.println(i);
                }
            }
            for (int i = 7 * start + 1; i < 8 * start; i = i + 2) {
                if (isRemovalPrime(i)) {
                    System.out.println(i);
                }
            }
        }
        long stopTime = System.nanoTime();
        System.out.println("Time :"+(stopTime - startTime)/1000);
    }

    static boolean isRemovalPrime(int number) {
        for (int i = 1; number > 0; i++) {
            if(!isPrime(number)) { return false; }
            number = number / 10;
        }
        return true;
    }

    static boolean isPrime(int number) {
        if (number == 0 || number == 1){ return false; }
        if (number != 2 && number % 2 == 0) { return false; }

        double r = Math.sqrt(number);
        for (int i = 3; i <= r; i = i + 2) {
            if (number % i == 0) { return false; }
        }
        return true;
    }
}
