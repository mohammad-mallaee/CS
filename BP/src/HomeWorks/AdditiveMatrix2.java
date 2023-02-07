import java.util.Scanner;

public class AdditiveMatrix2 {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        int m = reader.nextInt();
        int n = reader.nextInt();
        String[][] matrix = new String[n][m];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                matrix[j][i] = complexConjugate(reader.next());
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

    static String complexConjugate(String complexString) {
        boolean hasRealPart = false, hasImaginaryPart = false;
        String divider = "", bridge = "";
        int dividerIndex = 0;
        for (int i = complexString.length() - 1; i >= 0; i--) {
            char ch = complexString.charAt(i);
            if (ch == 'i') {
                hasImaginaryPart = true;
                continue;
            }
            if (hasImaginaryPart && (ch == '+' || ch == '-')) {
                divider = ch + "";
                dividerIndex = i;
                continue;
            }
            if (dividerIndex != 0) {
                hasRealPart = true;
            }
        }
        if (hasImaginaryPart && hasRealPart) {
            bridge = divider.equals("+") ? "-" : "+";
        } else if (hasImaginaryPart) {
            bridge = divider.equals("-") ? "" : "-";
        }
        return complexString.substring(0, dividerIndex) + bridge
                + complexString.substring(dividerIndex + divider.length());
    }
}
