import java.util.Scanner;

public class FormatNames {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        int n = reader.nextInt();
        String[] names = new String[n];
        for (int i = 0; i < n; i++) {
            String input = reader.next();
            names[i] = input.substring(0, 1).toUpperCase() + input.substring(1).toLowerCase();
        }
        for (String name: names) {
            System.out.println(name);
        }
    }
}
