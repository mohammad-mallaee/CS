import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class StrongPassword {

    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        int N = reader.nextInt();
        printStrongPasswords(N);
    }
    static void printStrongPasswords(int N){
        List<Integer> strongPasswords = getStrongPasswords(N - 1);
        Collections.sort(strongPasswords);
        for(int strongPassword: strongPasswords) {
            System.out.println(strongPassword);
        }
    }
    static List<Integer> getStrongPasswords (int N) {
        List<Integer> strongPasswords = new ArrayList<>();

        int end = (int) Math.pow(10, N) - 1;
        int[] digits = new int[N + 1];
        int sum;

        for (int i = 0; i < N; i++) { digits[i] = 1; }

        do {
            sum = 0;
            for (int i = 0; i < digits.length; i++) {
                sum += (int) (digits[i] * Math.pow(10, i));
            }
            addStrongPasswordsToList(strongPasswords, N ,sum);

            digits[0] += 2;
            for (int i = 0; i < digits.length; i++) {
                if (digits[i] == 5) { digits[i] += 2; }
                if (digits[i] > 9) {
                    digits[i] = 1;
                    digits[i + 1] += 2;
                }
            }
        }
        while (sum < end);
        return strongPasswords;
    }

    static void addStrongPasswordsToList(List<Integer> numbers, int N, int sum) {
        int[] additionalNumbers = {2,3,5,7};
        int pow = (int) Math.pow(10, N);

        for(int number: additionalNumbers){
            if (isRemovalPrime(number * pow + sum)) {
                numbers.add(number * pow + sum);
            }
        }
    }

    static boolean isRemovalPrime(int number) {
        while (number > 0) {
            if(!isPrime(number)) { return false; }
            number = number / 10;
        }
        return true;
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
