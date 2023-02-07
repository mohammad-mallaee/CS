import java.util.Scanner;

public class Square {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        int n = reader.nextInt();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 || i == n - 1){
                    System.out.print("*");
                    continue;
                }
                if (j == 0 || j == n - 1)
                    System.out.print("*");
                else System.out.print(" ");
            }
            System.out.print("\n");
        }
    }
}
