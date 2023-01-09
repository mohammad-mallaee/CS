import java.util.Scanner;

public class PowerOf5 {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        int n = reader.nextInt();
        System.out.println(n == 1 ? 5 : 25);
    }
}
