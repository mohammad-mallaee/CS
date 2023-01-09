import java.util.Scanner;

public class MatrixMultiplication {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        int m1 = reader.nextInt();
        int n1 = reader.nextInt();
        String[][] firstMatrix = new String[m1][n1];
        for (int i = 0; i < m1; i++) {
            for (int j = 0; j < n1; j++) {
                firstMatrix[i][j] = reader.next();
            }
        }

        int m2 = reader.nextInt();
        int n2 = reader.nextInt();
        String[][] secondMatrix = new String[m2][n2];
        for (int i = 0; i < m2; i++) {
            for (int j = 0; j < n2; j++) {
                secondMatrix[i][j] = reader.next();
            }
        }

        for (int i = 0; i < m1; i++) {
            for (int j = 0; j < n2; j++) {
                int[] index = new int[2];
                for (int k = 0; k < n1; k++) {
                    int[] firstComplex = parseComplex(firstMatrix[i][k]);
                    int[] secondComplex = parseComplex(secondMatrix[k][j]);
                    int[] multipliedComplex = multiplyComplexes(firstComplex, secondComplex);
                    index = addComplexes(index, multipliedComplex);
                }
                System.out.print(j == n2 - 1 ? complexToString(index) : complexToString(index) + " ");
            }
            System.out.println();
        }
    }

    static int[] addComplexes(int[] a, int[] b) {
        return new int[]{a[0] + b[0], a[1] + b[1]};
    }

    static int[] multiplyComplexes(int[] a, int[] b) {
        int real = (a[0] * b[0]) + (-1) * (a[1] * b[1]);
        int imaginary = (a[0] * b[1]) + (a[1] * b[0]);
        return new int[]{real, imaginary};
    }

    static String complexToString(int[] complexNumber) {
        boolean hasRealPart = complexNumber[0] != 0;
        boolean hasImaginaryPart = complexNumber[1] != 0;
        String divider = "";
        if (hasRealPart && hasImaginaryPart && complexNumber[1] > 0) {
            divider = "+";
        }
        String realPart = hasRealPart ? complexNumber[0] + "" : "";
        String imaginaryPart = hasImaginaryPart ? complexNumber[1] + "i" : "";
        if (complexNumber[1] == 1 || complexNumber[1] == -1) {
            imaginaryPart = imaginaryPart.replace("1", "");
        }
        return realPart + divider + imaginaryPart;
    }

    static int[] parseComplex(String complexString) {
        int[] complexNumber = new int[2];
        char[] complexChars = complexString.toCharArray();
        int part = 0, pow = 0;
        for (int i = complexString.length() - 1; i >= 0; i--) {
            char ch = complexChars[i];
            if (ch == 'i') {
                complexNumber[1] = 1;
                part = 1;
                continue;
            }
            if (ch == '+' || ch == '-') {
                if (ch == '-') {
                    complexNumber[part] *= (-1);
                }
                pow = 0;
                part = 0;
                continue;
            }
            complexNumber[part] += Integer.parseInt(ch + "") * Math.pow(10, pow);
            pow++;
        }
        if (complexNumber[1] > 1) {
            complexNumber[1] -= 1;
        } else if (complexNumber[1] < -1) {
            complexNumber[1] += 1;
        }
        return complexNumber;
    }
}