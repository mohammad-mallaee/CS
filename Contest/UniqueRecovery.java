import java.util.Scanner;

public class UniqueRecovery {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        int n = reader.nextInt();
        String[] answers = new String[n];
        for (int i = 0; i < n; i++) {
            int numbersCount = reader.nextInt();
            int[] d = new int[numbersCount];
            for (int j = 0; j < numbersCount; j++) {
                d[j] = reader.nextInt();
            }
            answers[i] = recover(d);
        }
        for (String answer : answers) {
            System.out.println(answer);
        }
    }

    static String recover(int[] d) {
        int[] a = new int[d.length];
        a[0] = d[0];
        StringBuilder answer = new StringBuilder();
        for (int i = 1; i < d.length; i++) {
            if (a[i - 1] > d[i] && d[i] != 0) {
                return "-1";
            }
            a[i] = d[i] + a[i - 1];
        }
        for (int i = 0; i < a.length; i++) {
            answer.append(a[i]).append(i < a.length - 1 ? " " : "");
        }
        return answer.toString();
    }
}
