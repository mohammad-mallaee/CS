import java.util.Scanner;

public class MilkBottles {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        double sum = 0;
        double[] bottles = new double[3];
        for (int i = 0; i < bottles.length; i++) {
            double number = reader.nextDouble();
            bottles[i] = number;
            sum += number;
        }
        double average = sum / bottles.length;
        int steps = 0;
        for (int i = 0; i < bottles.length - 1; i++) {
            if (bottles[i] != average) {
                bottles[i + 1] += bottles[i] - average;
                bottles[i] = average;
                steps++;
            }
        }
        System.out.println(steps);
    }
}
