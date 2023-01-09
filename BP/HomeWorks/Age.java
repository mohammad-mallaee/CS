import java.util.Scanner;

public class Age {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        String age = reader.next();
        String currentTime = reader.next();
        String[] ageParts = age.split("/");
        String[] currentTimeParts = currentTime.split("/");

        int elapsedDays = Integer.parseInt(currentTimeParts[0]) * 360
                + Integer.parseInt(currentTimeParts[1]) * 30
                + Integer.parseInt(currentTimeParts[2]);
        int birthDays = Integer.parseInt(ageParts[0]) * 360
                + Integer.parseInt(ageParts[1]) * 30
                + Integer.parseInt(ageParts[2]);

        int livedDays = elapsedDays - birthDays;
        int years = livedDays / 360;
        int months = (livedDays % 360) / 30;
        int days = livedDays - ((years * 360) + (months * 30));

        String date = extend(years, 4) + "/" + extend(months, 2) + "/" + extend(days, 2);
        System.out.println(date);
        System.out.println(livedDays);
    }

    static String extend(int number, int digitsCount) {
        String extendedNumber = "";
        extendedNumber += number;
        int extendedLength = extendedNumber.length();
        for (int i = 0; i < (digitsCount - extendedLength); i++) {
            extendedNumber = "0" + extendedNumber;
        }
        return extendedNumber;
    }
}
