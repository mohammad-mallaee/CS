import java.util.Scanner;

public class Floor {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        float number = reader.nextFloat();
        int integer = (int) number;
        integer += number < 0 ? -1 : 0;
        System.out.println(integer);
    }
}
