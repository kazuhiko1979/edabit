import java.util.ArrayList;
import java.util.List;

public class very_hard_An_OSHA_Approved_Ladder {

    public static boolean isLadderSafe(List<String> ldr) {
        ldr = ldr.subList(1, ldr.size() - 1);
        List<Integer> rungs = new ArrayList<>();

        for (int i = 0; i < ldr.size(); i++) {
            if (ldr.get(i).equals("#".repeat(ldr.get(0).length()))) {
                rungs.add(i);
            }
        }

        if (rungs.size() == 0) {
            return false;
        }

        int diff = rungs.get(1) - rungs.get(0);
        for (int i = 0; i < rungs.size() - 1; i++) {
            if (rungs.get(i + 1) - rungs.get(i) != diff) {
                return false;
            }
        }

        return diff <= 3 && diff * rungs.size() >= ldr.size() && ldr.get(0).length() >= 5;
    }

    public static void main(String[] args) {
        List<String> ladder1 = List.of(
                "#   #",
                "#####",
                "#   #",
                "#   #",
                "#####",
                "#   #",
                "#   #",
                "#####",
                "#   #");

        List<String> ladder2 = List.of(
                "#   #",
                "#####",
                "#   #",
                "#####",
                "#   #",
                "#   #",
                "#####",
                "#   #");

        List<String> ladder3 = List.of(
                "#   #",
                "#  ##",
                "#   #",
                "#   #",
                "#####",
                "#   #",
                "#   #",
                "#####",
                "#   #");

        System.out.println(isLadderSafe(ladder1)); // Output: true
        System.out.println(isLadderSafe(ladder2)); // Output: false
        System.out.println(isLadderSafe(ladder3)); // Output: false
    }
}
