import java.util.Arrays;
import java.util.Scanner;

public class Multiples {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        int N = reader.nextInt();

        long startTime = System.nanoTime();

        int[] digits = new int[N > 1 ? 2 * N : 1];
        Arrays.fill(digits, 9);

        long start = (long) Math.pow(10, N - 1);
        long end = (long) Math.pow(10, N) - 1;

        for (long j = 0; j < end; j++) {
            long number = digitsToNumber(digits);
            if (number < 0) { return; }
            long[] multiples = findMultiples(number, start, end);
            if (multiples.length > 0) {
                System.out.println(multiples[1] + " * " + multiples[0] + " = " + number);
                printElapsedTime(startTime);
                return;
            }
            reduceMiddlesByOne(digits);
        }
    }

    static void printElapsedTime (long startTime) {
        long endTime = System.nanoTime();
        System.out.println((endTime - startTime) / 1000 / 1000 + " ms");
    }

    static long[] findMultiples(long number, long start, long end) {
        for (long i = end; i >= (start + end) / 2; i--) {
            long otherMultiple = number / i;
            if (number % i == 0 && otherMultiple < end) {
                return new long[] {i, otherMultiple};
            }
        }
        return new long[]{};
    }

    static void reduceMiddlesByOne(int[] digits) {
        digits[digits.length / 2]--;
        for (int i = digits.length / 2; i < digits.length; i++) {
            if (digits[i] < 0) {
                digits[i] = 9;
                digits[i + 1] -= 1;
            }
        }
        digits[digits.length / 2 - 1]--;
        for (int i = digits.length / 2 - 1; i >= 0; i--) {
            if (digits[i] < 0) {
                digits[i] = 9;
                digits[i - 1] -= 1;
            }
        }
    }

    static long digitsToNumber(int[] digits) {
        long sum = 0;
        for (int i = 0; i < digits.length; i++) {
            sum += (long) (digits[i] * Math.pow(10, digits.length - i - 1));
        }
        return sum;
    }
}
