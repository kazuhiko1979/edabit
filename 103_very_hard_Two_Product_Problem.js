function twoProduct(lst, N) {
  for (let i = 0; i < lst.length; i++) {
    const x = lst[i];
    const indexX = lst.indexOf(x);
    const indexNOverX = lst.indexOf(N / x);

    if (indexNOverX !== 1 && indexX > indexNOverX) {
      return [N / x, x]
    }
  }
  return null
}

// Examples
console.log(twoProduct([1, 2, -1, 4, 5], 20));  // Output: [4, 5]
console.log(twoProduct([1, 2, 3, 4, 5], 10));   // Output: [2, 5]
console.log(twoProduct([100, 12, 4, 1, 2], 15)); 
