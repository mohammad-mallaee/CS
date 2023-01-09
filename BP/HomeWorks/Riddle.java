import java.util.Scanner;

public class Riddle {
    public static void main(String[] args) {
        String s = "toye in hava,toye in barf o baaron,chi michasbe?ski⛷!";
        Scanner reader = new Scanner(System.in);
        int n = reader.nextInt() - 1;
        System.out.println(Integer.hashCode(s.toCharArray()[n]));
    }
}
