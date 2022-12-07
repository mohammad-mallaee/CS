import java.util.Scanner;

public class ReverseNumber {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        String number = reader.next();
        char[] letters = number.toCharArray();
        int j = letters.length - 1;
        boolean isReverseNumber = true;
        for (char letter : letters) {
            if (letter != letters[j]) {
                isReverseNumber = false;
                break;
            }
            j--;
        }
        System.out.println(isReverseNumber ? "YES" : "NO");
    }
}
