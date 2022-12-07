import java.util.Scanner;
public class Power {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        int number = reader.nextInt();
        int power = 0;
        for (power = 0; Math.pow(2, power) <= number ; power++) {}
        System.out.println((int) Math.pow(2, power));
    }
}
