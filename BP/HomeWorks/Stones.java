import java.util.Scanner;

public class Stones {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        int n = reader.nextInt();
        char[] stoneColors = reader.next().toCharArray();
        int removes = 0;
        for (int i = 1; i < n; i++) {
            if (stoneColors[i] == stoneColors[i - 1]) {
                removes++;
            }
        }
        System.out.println(removes);
    }
}
