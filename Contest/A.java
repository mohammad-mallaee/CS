import java.util.Scanner;

public class A {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        int n = reader.nextInt();
        int[] numbers = new int[n];
        for (int i = 0; i < n; i++) {
            numbers[i] = reader.nextInt();
        }
        int last_digit = numbers[0];
        int moves = 0;
        for (int i = 1; i < n; i++) {
            int number = numbers[i];
            if (number <= last_digit) {
                int newMoves = last_digit - number + 1;
                moves += newMoves;
                last_digit = number + newMoves;
            } else {
                last_digit = number;
            }
        }
        System.out.println(moves);
    }
}
