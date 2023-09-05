function isEarlyBird(r, n) {
  const numStringSequence = Array.from({ length: r + 2 }, (_, i) => i).join('');
  const numStr = String(n);
  const positions = [];

  for (let i = 0; i < numStringSequence.length - numStr.length + 1; i++) {
    if (numStringSequence.slice(i, i + numStr.length) === numStr) {
      positions.push(Array.from({ length: numStr.length }, (_, j) => i + j));
    }
  }

  if (positions.length > 1) {
    positions.push("Early Bird!");
  }

  return positions;
}

// テストケース
console.log(isEarlyBird(20, 14));
console.log(isEarlyBird(20, 12));
console.log(isEarlyBird(101, 101));
console.log(isEarlyBird(50, 34));
console.log(isEarlyBird(212, 156));
console.log(isEarlyBird(400, 240));
console.log(isEarlyBird(900, 888));
console.log(isEarlyBird(1200, 745));
console.log(isEarlyBird(2000, 666));