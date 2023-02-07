import java.util.Scanner;

public class AdditiveMatrix {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        int m = reader.nextInt();
        int n = reader.nextInt();
        String [][] matrix = new String[n][m];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                String index = reader.next();
                if (index.contains("+")) {
                    index = index.replace("+", "-");
                } else if (index.contains("-")) {
                    index = index.replace("-", index.indexOf("-") == 0 ? "" : "+");
                } else if (index.equals("i")) {
                    index = "-i";
                }
                matrix[j][i] = index;
            }
        }
        for (int i = 0; i < matrix.length; i++) {
            String[] row = matrix[i];
            for (int j = 0; j < row.length; j++) {
                System.out.print(row[j] + (j == row.length - 1 ? "" : " "));
            }
            System.out.print(i == row.length ? "" : "\n");
        }
    }
}
