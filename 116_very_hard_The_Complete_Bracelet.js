function completeBracelet(arr) {
  const n = arr.length;

  for (let length = 2; length <= n / 2; length++) {
    const subarrays = [];
    for (let i = 0; i <= n - length; i++) {
      subarrays.push(arr.slice(i, i + length));
    }

    if (subarrays.every(subarray => JSON.stringify(subarray) === JSON.stringify(subarrays[0])) && subarrays[0].length >= 2) {
      return true;
    }
  }

  return false;
}

console.log(completeBracelet([1, 2, 2, 1, 2, 2])); // ➞ true
console.log(completeBracelet([5, 5, 5])); // ➞ false
console.log(completeBracelet([5, 5, 7, 7])); // ➞ false
console.log(completeBracelet([5, 5, 7, 7, 5, 5, 7, 7])); // ➞ false
console.log(completeBracelet([1, 2, 1, 2, 1, 2])); // ➞ true
console.log(completeBracelet([1, 2, 2, 2, 1, 2, 2])); // ➞ true
console.log(completeBracelet([1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2])); // ➞ true
console.log(completeBracelet([5, 2, 5, 5, 2, 5, 2, 5, 2, 2, 5, 2, 5, 2, 5, 5, 2, 5, 2, 5, 2, 2, 5, 2])); // ➞ false
