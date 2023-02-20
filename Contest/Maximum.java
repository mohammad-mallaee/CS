import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Maximum {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        int n = reader.nextInt();
        ArrayList<Integer> numbers = new ArrayList<>();
        for (int i = 0; i < n * 2; i++) {
            numbers.add(reader.nextInt());
        }
        Collections.sort(numbers);
        int sum = 0;
        for (int i = 0; i < n * 2; i += 2) {
            sum += numbers.get(i);
        }
        System.out.println(sum);
    }
}
