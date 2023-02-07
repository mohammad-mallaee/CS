import java.util.Scanner;

public class SumWith1 {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        int n = reader.nextInt();
        int biggestNumber = reader.nextInt();
        int smallestNumber = biggestNumber;
        for (int i = 1; i < n; i++) {
            int num = reader.nextInt();
            biggestNumber = Math.max(num, biggestNumber);
            smallestNumber = Math.min(num, smallestNumber);
        }
        System.out.println(biggestNumber - smallestNumber);
    }
}
