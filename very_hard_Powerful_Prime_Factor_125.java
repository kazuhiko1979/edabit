import java.util.HashMap;
import java.util.Map;
import java.util.TreeSet;

public class PrimeFactorExpression {

    public static String expressFactors(int n) {
        Map<Integer, Integer> res = new HashMap<>();
        int i = 2;

        while (i <= n) {
            while (n % i == 0) {
                res.put(i, res.getOrDefault(i, 0) + 1);
                n /= i;
            }
            i++;
        }

        StringBuilder result = new StringBuilder();
        TreeSet<Integer> sortedKeys = new TreeSet<>(res.keySet());

        for (int key : sortedKeys) {
            if (res.get(key) == 1) {
                result.append(key);
            } else {
                result.append(key).append("^").append(res.get(key));
            }
            result.append(" x ");
        }

        return result.substring(0, result.length() - 3); // Remove the extra " x "
    }

    public static void main(String[] args) {
        System.out.println(expressFactors(10));  // "2 x 5"
        System.out.println(expressFactors(60));  // "2^2 x 3 x 5"
        System.out.println(expressFactors(323)); // "17 x 19"
        System.out.println(expressFactors(5040)); // "2^4 x 3^2 x 5 x 7"
    }
}
