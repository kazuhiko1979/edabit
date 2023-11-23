/*
Validate Subsequences
Given two non-empty lists, write a function that determines whether the second list is a subsequence of the first list.

For instance, the numbers [1, 3, 4] form a subsequence of the list [1, 2, 3, 4], and so do the numbers [2, 4].

Examples
is_valid_subsequence([1, 1, 6, 1],[1, 1, 1, 6]) ➞ False

is_valid_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [22, 25, 6]) ➞ True

is_valid_subsequence([1, 2, 3, 4], [2, 4]) ➞ True
*/
public class very_hard_Validate_Subsequences_120 {
    public static boolean isValidSubsequence(int[] lst, int[] sub){
        int lstPtr = 0;
        int subPtr = 0;

        while (lstPtr < lst.length && subPtr < sub.length) {
            if (lst[lstPtr] == sub[subPtr]) {
                subPtr++;

            }
            lstPtr++;
        }
        return subPtr == sub.length;
    }

    public static void main(String[] args) {
        // Test cases
        System.out.println(isValidSubsequence(new int[]{1, 1, 6, 1}, new int[]{1, 1, 1, 6})); // ➞ false
        System.out.println(isValidSubsequence(new int[]{5, 1, 22, 25, 6, -1, 8, 10}, new int[]{22, 25, 6})); // ➞ true
        System.out.println(isValidSubsequence(new int[]{1, 2, 3, 4}, new int[]{2, 4})); // ➞ true
    }
}