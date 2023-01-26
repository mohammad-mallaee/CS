import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Matrix {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        List<String[]> firstMatrix = new ArrayList<>();
        List<String[]> secondMatrix = new ArrayList<>();

        boolean validMatrix = true;

        while (true) {
            String line = reader.nextLine();
            if (line.equals("")) {
                break;
            }
            String[] numbersString = line.split(" ");
            firstMatrix.add(numbersString);
            if (numbersString.length != firstMatrix.get(0).length) {
                validMatrix = false;
            }
        }

        while (true) {
            String line = reader.nextLine();
            if (line.equals("")) {
                break;
            }
            String[] numbersString = line.split(" ");
            secondMatrix.add(numbersString);
            if (numbersString.length != secondMatrix.get(0).length) {
                validMatrix = false;
            }
        }

        if (!validMatrix || firstMatrix.get(0).length != secondMatrix.size()) {
            System.out.println("Invalid Inputs");
            return;
        }

        for (String[] firstRow : firstMatrix) {
            int columns = secondMatrix.get(0).length;
            for (int j = 0; j < columns; j++) {
                int index = 0;
                for (int k = 0; k < secondMatrix.size(); k++) {
                    index += (Integer.parseInt(firstRow[k]) * Integer.parseInt(secondMatrix.get(k)[j]));
                }
                System.out.print(j == columns - 1 ? index : index + " ");
            }
        }
        System.out.println();
    }
}
