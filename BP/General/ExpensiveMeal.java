import java.util.ArrayList;
import java.util.Scanner;

public class ExpensiveMeal {
    static int containers = 0;
    static int sum = 0;
    static int[] indexes;

    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        int n = reader.nextInt();
        indexes = new int[n];

        ArrayList<Integer> ones = new ArrayList<>();
        ArrayList<Integer> twos = new ArrayList<>();
        ArrayList<Integer> threes = new ArrayList<>();
        ArrayList<Integer> fours = new ArrayList<>();
        ArrayList<Integer> fives = new ArrayList<>();
        ArrayList<Integer> sixes = new ArrayList<>();
        ArrayList<Integer> sevens = new ArrayList<>();
        ArrayList<Integer> eights = new ArrayList<>();
        ArrayList<Integer> nines = new ArrayList<>();
        ArrayList<Integer> tens = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            int input = reader.nextInt();
            switch (input) {
                case 1:
                    ones.add(i);
                    break;
                case 2:
                    twos.add(i);
                    break;
                case 3:
                    threes.add(i);
                    break;
                case 4:
                    fours.add(i);
                    break;
                case 5:
                    fives.add(i);
                    break;
                case 6:
                    sixes.add(i);
                    break;
                case 7:
                    sevens.add(i);
                    break;
                case 8:
                    eights.add(i);
                    break;
                case 9:
                    nines.add(i);
                    break;
                case 10:
                    tens.add(i);
                    break;
            }
        }

        indexLoads(1, ones);
        indexLoads(2, twos);
        indexLoads(3, threes);
        indexLoads(4, fours);
        indexLoads(5, fives);
        indexLoads(6, sixes);
        indexLoads(7, sevens);
        indexLoads(8, eights);
        indexLoads(9, nines);
        indexLoads(10, tens);

        System.out.println(containers + 1);
        for (int i = 0; i < n-1; i++) {
            System.out.print(indexes[i] + " ");
        }
        System.out.print(indexes[n - 1]);
    }

    static void indexLoads(int loadsWeight, ArrayList<Integer> loadsList) {
        for (int index : loadsList) {
            if (sum + loadsWeight > 20) {
                sum = 0;
                containers++;
            }
            sum += loadsWeight;
            indexes[index] = containers + 1;
        }
    }
}
