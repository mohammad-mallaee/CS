import java.util.Scanner;
public class MagicWands {
    public static void main(String[] args) {
        Scanner reader = new Scanner (System.in);
        int n = reader.nextInt();
        System.out.println(n / 2 + n % 2);
    }
}