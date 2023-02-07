import java.util.Scanner;

public class Car {
  public static void main(String[] args) {
    double money = 8;
    int cost = 24;

    Scanner scanner = new Scanner(System.in);
    System.out.println("Profit rate :");
    double rate = scanner.nextDouble();
    System.out.println("Waiting years :");
    int years = scanner.nextInt();

    for (int i = 0; i < years; i++) {
      money += money * rate / 100;
    }

    if (money >= cost) {
      System.out.println("You can buy the car in " + years + " years");
    } else {
      System.out.println("You won't be able to buy the car in " + years + " years");
    }

    scanner.close();
  }
}