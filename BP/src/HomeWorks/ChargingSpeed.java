import java.util.Scanner;

public class ChargingSpeed {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        int k = reader.nextInt();
        int minutes = k * (k + 1) / 2;
        System.out.println(minutes);
    }
}
