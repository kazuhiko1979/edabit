import java.util.ArrayList;
import java.util.List;

public class very_hard_Same_Letter_Patterns_123 {

  public static boolean sameLetterPattern(String txt1, String txt2) {
    return allPos(txt1).equals(allPos(txt2));
  }

  private static List<Integer> allPos(String x) {
    List<Integer> positions = new ArrayList<>();

    for (int i = 0; i < x.length(); i++) {
      for (int j = 0; j < x.length(); j++) {
        if (x.charAt(i) == x.charAt(j)) {
          positions.add(j);
        }
      }
    }
    return positions;
  }

  public static void main(String[] args) {
    System.out.println(sameLetterPattern("ABAB", "CDCD")); // true
    System.out.println(sameLetterPattern("AAABBB", "CCCDDD")); // true
    System.out.println(sameLetterPattern("ABCBA", "BCDCB")); // true
    System.out.println(sameLetterPattern("FFGG", "FFG")); // false
    System.out.println(sameLetterPattern("FFGG", "CDCD")); // false
  }
}
