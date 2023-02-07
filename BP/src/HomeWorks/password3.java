import java.util.Arrays;
import java.util.Scanner;

public class password3 {

    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        double N = reader.nextInt();

        int start = (int) Math.pow(10, N - 1);
        int end = (int) Math.pow(10, N) - 1;

        primeNumbers = generatePrimeNumbersUpTo(end);

        for (int primeNumber : primeNumbers) {
            if (isRemovalPrime(primeNumber) && start < primeNumber && primeNumber < end) {
                System.out.println(primeNumber);
            }
        }
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

    private enum Marker {
        CROSSED, UNCROSSED
    }

    private static Marker[] crossedOut;

    public static int[] generatePrimeNumbersUpTo(int limit) {
            crossedOut = new Marker[limit + 1];
            Arrays.fill(crossedOut, Marker.UNCROSSED);
            int iterationLimit = (int) Math.sqrt(crossedOut.length);
            for (int i = 2; i <= iterationLimit; i++) {
                if (crossedOut[i] == Marker.UNCROSSED) {
                    for (int multiple = 2 * i;
                         multiple < crossedOut.length;
                         multiple += i) {
                        crossedOut[multiple] = Marker.CROSSED;
                    }
                }
            }
            int[] primes = new int[numberOfUncrossedIntegers()];
            for (int j = 0, i = 2; i < crossedOut.length; i++) {
                if (crossedOut[i] == Marker.UNCROSSED) {
                    primes[j++] = i;
                }
            }
            return primes;
    }

    private static int numberOfUncrossedIntegers() {
        int count = 0;
        for (int i = 2; i < crossedOut.length; i++) {
            if (crossedOut[i] == Marker.UNCROSSED) {
                count++;
            }
        }
        return count;
    }
}
