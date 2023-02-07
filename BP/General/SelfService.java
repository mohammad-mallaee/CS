import java.util.*;

public class SelfService {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        int n = reader.nextInt();

        List<Integer> caloriePeriods = new ArrayList<>();

        int positiveNumbersCount = 0;
        int positivePeriodsCount = 0;
        int sumOfAllPositives = 0;

        int caloriePeriod = 0;
        for (int i = 0; i < n; i++) {
            int calorie = reader.nextInt();
            if (calorie < 0) {
                if (caloriePeriod > 0) {
                    caloriePeriods.add(caloriePeriod);
                    positivePeriodsCount++;
                }
                caloriePeriods.add(calorie);
            }
            if (calorie >= 0) {
                sumOfAllPositives += calorie;
                positiveNumbersCount++;
                caloriePeriod += calorie;
                continue;
            }
            caloriePeriod = 0;
        }
        if (caloriePeriod > 0) {
            positivePeriodsCount++;
            caloriePeriods.add(caloriePeriod);
        }

        Collections.sort(caloriePeriods);
        Collections.reverse(caloriePeriods);

        int sumOfPeriods = 0;
        int k = 0;
        for (int i = 0; i < n; i++) {
            if (i < positiveNumbersCount && i >= positivePeriodsCount) {
                System.out.println(sumOfAllPositives);
                continue;
            }
            sumOfPeriods += caloriePeriods.get(k);
            System.out.println(sumOfPeriods);
            k++;
        }
    }
}
