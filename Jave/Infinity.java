import java.lang.Math;

public class Infinity {
    public static void main(String[] args) {
        // The expression -7.5/0 will result in -infinity, as the numerator is negative.
        System.out.println(-7.5 / 0);

        // The expression Math.sqrt(-1) will result in NaN,
        // as we cannot take square root of negative numbers.
        System.out.println(Math.sqrt(-1));
    }

}
