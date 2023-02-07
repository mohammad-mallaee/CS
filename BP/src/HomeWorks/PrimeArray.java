import java.util.Scanner;

public class PrimeArray {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        int n = reader.nextInt();
        int wrongOddNumbers = 0;
        int wrongEvenNumbers = 0;
        for (int i = 0; i < n; i++) {
            int inputNumber = reader.nextInt();
            if (i % 2 == 0 && inputNumber % 2 == 1) {
                wrongOddNumbers++;
            } else if (i % 2 == 1 && inputNumber % 2 == 0) {
                wrongEvenNumbers++;
            }
        }
        System.out.println(wrongEvenNumbers == wrongOddNumbers ? wrongEvenNumbers : -1);
    }
}
