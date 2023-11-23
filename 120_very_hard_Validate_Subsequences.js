/*
Validate Subsequences
Given two non-empty lists, write a function that determines whether the second list is a subsequence of the first list.

For instance, the numbers [1, 3, 4] form a subsequence of the list [1, 2, 3, 4], and so do the numbers [2, 4].

Examples
is_valid_subsequence([1, 1, 6, 1],[1, 1, 1, 6]) ➞ False

is_valid_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [22, 25, 6]) ➞ True

is_valid_subsequence([1, 2, 3, 4], [2, 4]) ➞ True
*/

function isValidSubsequence(lst, sub){
    let lstPtr = 0;
    let subPtr = 0;

    while (lstPtr < lst.length && subPtr.length) {
        if (lst[lstPtr] === sub[subPtr]) {
            subPtr++;
        }
        lstPtr++;
    }

    return subPtr === sub.length;
}

// Test cases
console.log(isValidSubsequence([1, 1, 6, 1], [1, 1, 1, 6])); // ➞ false
console.log(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [22, 25, 6])); // ➞ true
console.log(isValidSubsequence([1, 2, 3, 4], [2, 4])); // ➞ true