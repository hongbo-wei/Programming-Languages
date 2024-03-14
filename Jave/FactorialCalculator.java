public class FactorialCalculator {
    public static void main(String[] args) {
        int n = 171;
        // long factorial = computeFactorial(n);
        double factorial = dfact(n);
        System.out.println("The factorial of " + n + " is: " + factorial);
    }

    /**
     * Calculate factorial.
     * requires: 0 <= n
     * 
     * @param n number whose factorial is to be calculated
     * @return factorial of n
     */
    public static double dfact(int n) {
        double a = 1;
        for (int i = 1; i <= n; i++) {
            a = a * i;
        }
        return a;
    }

    public static long computeFactorial(int n) {
        if (n == 0 || n == 1) {
            return 1;
        } else {
            long result = 1;
            for (int i = 2; i <= n; i++) {
                result *= i;
            }
            return result;
        }
    }
}
