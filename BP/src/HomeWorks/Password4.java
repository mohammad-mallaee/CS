import java.util.Arrays;
import java.util.BitSet;
import java.util.Scanner;

public class Password4 {

    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        double N = reader.nextInt();

        long startTime = System.nanoTime();

        int start = (int) Math.pow(10, N - 1);
        int end = (int) Math.pow(10, N) - 1;

        primeNumbers = generatePrimeNumbersUpTo(end);

        for (int primeNumber : primeNumbers) {
            if (start < primeNumber && primeNumber < end && isRemovalPrime(primeNumber)) {
                System.out.println(primeNumber);
            }
        }

        long stopTime = System.nanoTime();
        System.out.println("Elapsed time : " + (stopTime - startTime)/1000/1000 + " ms");
    }

    static boolean isRemovalPrime(int number) {
        while (number > 0) {
            if (!isPrime(number)) {
                return false;
            }
            number = number / 10;
        }
        return true;
    }

    static boolean isPrime(int number) {
        if (number == 0 || number == 1) {
            return false;
        }
        if (number != 2 && number % 2 == 0) {
            return false;
        }

        int index = Arrays.binarySearch(primeNumbers, number);
        return index >= 0;
    }

    private static int[] primeNumbers;
//    private static int[] crossedOut;
    private static BitSet crossedOut;

    public static int[] generatePrimeNumbersUpTo(int limit) {
//        crossedOut = new int[limit + 1];
        limit++;
        crossedOut = new BitSet(limit);
        int iterationLimit = (int) Math.sqrt(limit);
        for (int i = 2; i <= iterationLimit; i++) {
            if (!crossedOut.get(i)) {
                for (int multiple = 2 * i;
                     multiple < limit;
                     multiple += i) {
                    crossedOut.set(multiple);
                }
            }
        }
        int[] primes = new int[numberOfUncrossedIntegers(limit)];
        for (int j = 0, i = 2; i < limit; i++) {
            if (!crossedOut.get(i)) {
                primes[j++] = i;
            }
        }
        return primes;
    }

    private static int numberOfUncrossedIntegers(int limit) {
        int count = 0;
        for (int i = 2; i < limit; i++) {
            if (!crossedOut.get(i)) {
                count++;
            }
        }
        return count;
    }
}
