import java.util.Arrays;
import java.util.Scanner;
public class SumAndLength {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        int m = reader.nextInt();
        int s = reader.nextInt();

        if (s == 0) {
            System.out.println("-1 -1");
            return;
        }

        int[] sDigits = new int[m];
        int[] gDigits = new int[m];

        sDigits[0] = 1;
        int smallestNumberSum = 1;

        Arrays.fill(gDigits, 9);
        int greatestNumberSum = 9 * m;

        String smallestNumber = "";
        String greatestNumber = "";

        for (int i = m - 1; i >= 0; i--) {
            while (sDigits[i] < 9 && smallestNumberSum < s) {
                sDigits[i]++;
                smallestNumberSum++;
            }
            while (gDigits[i] > 0 && greatestNumberSum > s) {
                gDigits[i]--;
                greatestNumberSum--;
            }
            smallestNumber = sDigits[i] + smallestNumber;
            greatestNumber = gDigits[i] + greatestNumber;
        }

        System.out.print(smallestNumberSum == s ? smallestNumber : "-1");
        System.out.print(" ");
        System.out.print(greatestNumberSum == s ? greatestNumber : "-1");
    }
}