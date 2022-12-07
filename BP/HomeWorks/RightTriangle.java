import java.util.Scanner;

public class RightTriangle {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        int firstLine = reader.nextInt();
        int secondLine = reader.nextInt();
        int thirdLine = reader.nextInt();

        boolean isRightTriangle = false;

        int a = firstLine * firstLine;
        int b = secondLine * secondLine;
        int c = thirdLine * thirdLine;

        isRightTriangle = a + b == c || isRightTriangle;
        isRightTriangle = a + c == b || isRightTriangle;
        isRightTriangle = c + b == a || isRightTriangle;

        System.out.println(isRightTriangle ? "Yes" : "No");
    }
}
