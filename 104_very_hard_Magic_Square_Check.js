function isMagic(square) {
    const n = square.length;
    if (n === 0) {
        return true;
    }

    const sideSquare = new Set([...Array(n * n).keys()].map(i => i + 1));
    const flatten = square.flat().sort((a, b) => a - b);

    if (!isEqualSets(new Set(flatten), sideSquare)) {
        return false;
    }

    const targetSum = square[0].reduce((sum, value) => sum + value, 0);

    for (const row of square) {
        if (row.reduce((sum, value) => sum + value, 0) !== targetSum) {
            return false;
        }
    }

    for (let col = 0; col < n; col++) {
        let colSum = 0;
        for (const row of square) {
            colSum += row[col];
        }
        if (colSum !== targetSum) {
            return false;
        }
    }

    let topLeft = 0;
    let topRight = 0;
    for (let i = 0; i < n; i++) {
        topLeft += square[i][i];
        topRight += square[i][n - 1 - i];
    }

    if (topLeft !== targetSum || topRight !== targetSum) {
        return false;
    }
    return true;
}

function isEqualSets(setA, setB) {
    if (setA.size !== setB.size) {
        return false;
    }
    for (const item of setA) {
        if (!setB.has(item)) {
            return false;
        }
    }
    return true;
}

// テストケース
console.log(isMagic([]));
console.log(isMagic([[1]]));
console.log(isMagic([[2]]));
// 他のテストケースも同様に追加
