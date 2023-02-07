import java.util.Scanner;

public class ReversePrint {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        int[] numbers = new int[1000];
        for (int i = 0;; i++) {
            int input = reader.nextInt();
            if (input == 0) { break; }
            numbers[i] = input;
        }
        for (int i = numbers.length - 1; i >= 0; i--) {
            if (numbers[i] != 0) {
                System.out.println(numbers[i]);
            }
        }
    }
}
