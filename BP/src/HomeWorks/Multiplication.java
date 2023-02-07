import java.util.Scanner;

public class Multiplication {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        String phrase = reader.nextLine();
        String[] numbers =  phrase.split(" ");
        long number1 = Integer.parseInt(numbers[0]);
        long number2 = Integer.parseInt(numbers[1]);
        System.out.println(number1 * number2);
    }
}
