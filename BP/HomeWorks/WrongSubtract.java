import java.util.Scanner;

public class WrongSubtract {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        int n = reader.nextInt();
        int m = reader.nextInt();
        for (int i = 0; i < m; i++) {
            if (n % 10 == 0) {
                n = n / 10;
            } else {
                n--;
            }
        }
        System.out.println(n);
    }
}
