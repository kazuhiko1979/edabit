function generateRug(n) {
  if (n === 1) {
    return [[0]]
  }

  let rug = Array.from({ length: n}, () => Array(n).fill(0));
  let layers = Math.floor(n / 2);

  for (let layer = 0; layer < layers; layer++){
    let value = layers - layer;
    for (let i = layer; i < n - layer; i++){
      rug[layer][i] = value;
      rug[n - 1 - layer][i] = value;
      rug[i][layer] = value;
      rug[i][n - 1 - layer] = value;
    }
  }

  return rug
}

// Test cases
console.log(generateRug(1));
console.log(generateRug(3));
console.log(generateRug(5));
console.log(generateRug(7));
console.log(generateRug(9));