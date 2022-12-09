public class OddNumbersSystem {
    public static void main(String[] args) {
        int N = 2;
        int end = (int) Math.pow(10, N) - 1;
        int[] digits = new int[N + 1];
        int sum = 0;

        for (int i = 0; i < N; i++) { digits[i] = 1; }

        while (sum < end) {
            sum = 0;
            for (int i = 0; i < digits.length; i++) {
                sum += (int) (digits[i] * Math.pow(10, i));
            }
            System.out.println(sum);

            digits[0] += 2;
            for (int i = 0; i < digits.length; i++) {
                if (digits[i] > 9) {
                    digits[i] = 1;
                    digits[i + 1] += 2;
                }
            }
        }
    }
}
