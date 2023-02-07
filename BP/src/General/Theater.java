import java.util.Scanner;

public class Theater {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        int n = reader.nextInt();
        String[] names = new String[n];
        for (int i = 0; i < n; i++) {
            names[i] = reader.next();
            if (i > 0 && names[i].equals(names[i - 1])) {
                return;
            }
        }
        for (int i = 0; i < n - 1; i++) {
            System.out.println(names[i] + " to " + names[i + 1] + ": " + "ke ba in dar agar dar bande dar manand, dar manand.");
            for (int j = i + 1; j >= 1; j--) {
                System.out.println(names[j] + " to " + names[j - 1] + ": " + "dar manand?");
            }
            for (int k = 0; k <= i; k++) {
                System.out.println(names[k] + " to " + names[k + 1] + ": " + "dar manand.");
            }
        }
    }
}
