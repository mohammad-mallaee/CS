import java.util.Scanner;

public class Barcode {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        String[] rows = new String[9];
        for (int i = 0; i < 9; i++) {
            rows[i] = reader.nextLine();
        }

        String[] squares = new String[9];
        int c = 0;
        for (int i = 0; i < 9; i++) {
            char[] row = rows[i].toCharArray();

            if (squares[c] == null) { squares[c] = ""; }
            if (squares[c + 1] == null) { squares[c + 1] = ""; }
            if (squares[c + 2] == null) { squares[c + 2] = ""; }

            for (int j = 0; j < 9; j++) {
                if (j < 3) { squares[c] += row[j]; continue;}
                if (j < 6) { squares[c + 1] += row[j]; continue;}
                squares[c + 2] += row[j];
            }
            if ((i + 1) % 3 == 0) {
                c += 3;
            }
        }

        boolean squaresValidation = true;
        int disappearedNumbers = 0;
        for (int i = 0; i < 9; i++) {
            if (i == 0 || i == 2 || i == 6 || i == 8) {
                squaresValidation = isValidSquare(squares[i]);
                if (!squaresValidation) { break; }
            } else {
                disappearedNumbers += findDisappearedNumber(squares[i]);
            }
        }

        if (!squaresValidation) {
            System.out.println(0);
        } else {
            System.out.println((long) Math.pow(2, disappearedNumbers));
        }
    }

    static boolean isValidSquare(String square) {
        boolean isValid = true;
        char[] chars = square.toCharArray();
        for (int i = 0; i < 9; i++) {
            if (i == 4 && chars[i] == '1' ) { isValid = false; break; }
            if (i != 4 && chars[i] == '0') { isValid = false; break; }
        }
        return isValid;
    }

    static int findDisappearedNumber(String square) {
        int disappearedNumbers = 0;
        char[] chars = square.toCharArray();
        for (char ch: chars){
            if (ch == '2') { disappearedNumbers++; }
        }
        return disappearedNumbers;
    }
}
