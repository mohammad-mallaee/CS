public class BiggestMultiple {
    public static void main(String[] args) {
        long aux = 2;
        long num = 990099;
        while (num != 1) {
            if (num % aux == 0) {
                num /= aux;
            } else aux++;
        }
        System.out.println(aux);
    }
}
