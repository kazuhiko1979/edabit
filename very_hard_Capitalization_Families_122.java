import java.util.*;

public class very_hard_Capitalization_Families_122 {

  public static Map<Integer, List<String>> grouping(String[] words) {
    Arrays.sort(words, String.CASE_INSENSITIVE_ORDER);
    Map<Integer, List<String>> groups = new HashMap<>();

    for (String word : words) {
      int cap = countCapitalLetters(word);
      groups.computeIfAbsent(cap, k -> new ArrayList<>()).add(word);
    }
    return groups;
  }

  public static int countCapitalLetters(String word) {
    int count = 0;
    for (char c : word.toCharArray()) {
      if (Character.isUpperCase(c)) {
        count++;
      }
    }
    return count;
  }

  public static void main(String[] args) {

    // Test cases
    Map<Integer, List<String>> result1 = grouping(new String[] { "HaPPy", "mOOdy", "yummy", "mayBE" });
    System.out.println(result1);

    Map<Integer, List<String>> result2 = grouping(new String[] { "eeny", "meeny", "miny", "moe" });
    System.out.println(result2);

    Map<Integer, List<String>> result3 = grouping(new String[] { "FORe", "MoR", "bOR", "tOR", "sOr", "lor" });
    System.out.println(result3);

  }
}
