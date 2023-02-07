import java.util.Scanner;

public class CoordinateSnail {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        int n = reader.nextInt();
        int i = 0;
        int j = 0;
        int deltaI = 1;
        int deltaJ = 1;
        for (int k = 1; k < n; k += 2) {
            i += deltaI;
            deltaI = deltaI > 0 ? -1 * (deltaI + 1) : -1 * (deltaI - 1);
        }

        for (int k = 2; k < n; k += 2) {
            j += deltaJ;
            deltaJ = deltaJ > 0 ? -1 * (deltaJ + 1) : -1 * (deltaJ - 1);
        }
        System.out.println(i + " " + j);
    }
}
