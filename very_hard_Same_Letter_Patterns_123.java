import java.util.HashMap;
import java.util.Map;

public class very_hard_Same_Letter_Patterns_123 {
  public static boolean sameLetterPattern(String txt1, String txt2) {
    return generatePattern(txt1).equals(generatePattern(txt2));
  }

  private static String generatePattern(String txt) {
    Map<Character, Integer> temp = new HashMap<>();
    StringBuilder pattern = new StringBuilder();
    int currentPattern = 1;

    for (char c : txt.toCharArray()) {
      if (!temp.containsKey(c)) {
        temp.put(c, currentPattern);
        currentPattern++;
      }
      pattern.append(temp.get(c));
    }
    return pattern.toString();
  }

  public static void main(String[] args) {
    System.out.println(sameLetterPattern("ABAB", "CDCD")); // true
    System.out.println(sameLetterPattern("AAABBB", "CCCDDD")); // true
    System.out.println(sameLetterPattern("ABCBA", "BCDCB")); // true
    System.out.println(sameLetterPattern("FFGG", "FFG")); // false
    System.out.println(sameLetterPattern("FFGG", "CDCD")); // false
  }
}
