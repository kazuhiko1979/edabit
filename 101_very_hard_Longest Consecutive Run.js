// """
// Longest Consecutive Run
// A consecutive-run is a list of adjacent, consecutive integers. This list can be either increasing or decreasing. Create a function that takes a list of numbers and returns the length of the longest consecutive-run.

// To illustrate:

// longestRun([1, 2, 3, 5, 6, 7, 8, 9]) ➞ 5
// # Two consecutive runs: [1, 2, 3] and [5, 6, 7, 8, 9] (longest).
// Examples
// longest_run([1, 2, 3, 10, 11, 15]) ➞ 3
// # Longest consecutive-run: [1, 2, 3].

// longest_run([5, 4, 2, 1]) ➞ 2
// # Longest consecutive-run: [5, 4] and [2, 1].

// longest_run([3, 5, 7, 10, 15]) ➞ 1
// # No consecutive runs, so we return 1.
// Notes
// If there aren't any consecutive runs (there is a gap between each integer), return 1.
// """

function longestRun(lst) {
	if (lst.length < 2) {
			return lst.length;
	}

	function getDifference(a, b) {
			return (a > b) - (a < b);
	}

	let maxLength = 1;
	let length = 1;
	for (let i = 1; i < lst.length; i++) {
			const diff = lst[i] - lst[i - 1];
			if (diff === 0) {
					length = 1;
			} else {
					if (diff === lst[i - 1] - lst[i - 2]) {
							length += 1;
					} else {
							length = (diff !== lst[i - 1] - lst[i - 2]) ? 2 : 1;
					}
			}
			maxLength = Math.max(maxLength, length);
	}

	return maxLength;
}

// テスト
console.log(longestRun([1, 2, 3, 5, 6, 7, 8, 9]));    // 5
console.log(longestRun([1, 2, 3, 10, 11, 15]));       // 3
console.log(longestRun([-7, -6, -5, -4, -3, -2, -1]));  // 7
console.log(longestRun([3, 5, 6, 10, 15]));           // 2
console.log(longestRun([3, 5, 7, 10, 15]));           // 1
console.log(longestRun([5, 4, 3, 2, 1]));              // 5
console.log(longestRun([5, 4, 2, 1]));                 // 2
console.log(longestRun([10, 9, 0, 5]));               // 2
console.log(longestRun([1, 2, 3, 2, 1]));              // 3
console.log(longestRun([10, 9, 8, 7, 6, 2, 1]));      // 5


print(longest_run([1, 2, 3, 5, 6, 7, 8, 9]))
print(longest_run([1, 2, 3, 10, 11, 15]))
print(longest_run([-7, -6, -5, -4, -3, -2, -1]))
print(longest_run([3, 5, 6, 10, 15]))
print(longest_run([3, 5, 7, 10, 15]))
print(longest_run([5, 4, 3, 2, 1]))
print(longest_run([5, 4, 2, 1]))
print(longest_run([10, 9, 0, 5]))
print(longest_run([1, 2, 3, 2, 1]))
print(longest_run([10, 9, 8, 7, 6, 2, 1]))