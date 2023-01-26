import java.util.Scanner;

public class Palindromic {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        int N = reader.nextInt();
        long maxNumerator = (long) Math.pow(10, N) - 1;
        long maxSum = 2 * maxNumerator;
        for (long i = maxSum; i >= 0 ; i--) {
            long firstNumerator = (long) Math.ceil(i / 2.0);
            long secondNumerator = i - firstNumerator;
            do {
                long num = Math.multiplyExact(firstNumerator, secondNumerator);
                if (isPalindromic(num)) {
                    System.out.println(firstNumerator + " * " + secondNumerator + " = " + num);
                    return;
                }
                firstNumerator++;
                secondNumerator--;
            } while (firstNumerator <= maxNumerator);
        }
    }

    static boolean isPalindromic(long number) {
        char[] numberChars = Long.toString(number).toCharArray();
        for (int i = 0; i < numberChars.length; i++) {
            if (numberChars[i] != numberChars[numberChars.length - i - 1]) {
                return false;
            }
        }
        return true;
    }
}
