import java.util.Scanner;

public class BiggestNumber {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);

        int n = reader.nextInt();

        reader.nextLine();
        String numbersStr = reader.nextLine();

        String[] numbers = numbersStr.split(" ");
        int biggestNumber = Integer.parseInt(numbers[0]);
        for (int i = 1; i < n; i++) {
            int num = Integer.parseInt(numbers[i]);
            biggestNumber = num > biggestNumber ? num : biggestNumber;
        }
        System.out.println(biggestNumber);
    }
}
