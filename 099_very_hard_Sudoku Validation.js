// """
// Sudoku Validation
// Write a sudoku validator. This function should return True if the 2-D array represents a valid sudoku and False otherwise. To be a valid sudoku:

// Each row must have the digits from 1 to 9 exactly once.
// Each column must have the digits from 1 to 9 exactly once.
// Each 3x3 box must have the digits from 1 to 9 exactly once.
// Examples
// sudoku_validator([
//   [ 1, 5, 2, 4, 8, 9, 3, 7, 6 ],
//   [ 7, 3, 9, 2, 5, 6, 8, 4, 1 ],
//   [ 4, 6, 8, 3, 7, 1, 2, 9, 5 ],
//   [ 3, 8, 7, 1, 2, 4, 6, 5, 9 ],
//   [ 5, 9, 1, 7, 6, 3, 4, 2, 8 ],
//   [ 2, 4, 6, 8, 9, 5, 7, 1, 3 ],
//   [ 9, 1, 4, 6, 3, 7, 5, 8, 2 ],
//   [ 6, 2, 5, 9, 4, 8, 1, 3, 7 ],
//   [ 8, 7, 3, 5, 1, 2, 9, 6, 4 ]
// ]) ➞ True

// sudoku_validator([
//   [ 1, 1, 2, 4, 8, 9, 3, 7, 6 ],
//   [ 7, 3, 9, 2, 5, 6, 8, 4, 1 ],
//   [ 4, 6, 8, 3, 7, 1, 2, 9, 5 ],
//   [ 3, 8, 7, 1, 2, 4, 6, 5, 9 ],
//   [ 5, 9, 1, 7, 6, 3, 4, 2, 8 ],
//   [ 2, 4, 6, 8, 9, 5, 7, 1, 3 ],
//   [ 9, 1, 4, 6, 3, 7, 5, 8, 2 ],
//   [ 6, 2, 5, 9, 4, 8, 1, 3, 7 ],
//   [ 8, 7, 3, 5, 1, 2, 9, 6, 4 ]
// ]) ➞ False
// """


function sudoku_validator(board) {
  function isUnique(nums) {
    const seen = new Set();

    for (const num of nums) {
      if (num !== 0 && seen.has(num)) {
        return false;
      }
      seen.add(num);
  }
  return true;
}

// 行列チェック
for (let i = 0; i < 9; i++) {
  if (!isUnique(board[i] || !isUnique(board.map(row => row[i])))) {
    return false
  }
}

// 3x3 box チェック
for (let i = 0; i < 9; i += 3) {
  for (let j = 0; j < 9; j += 3) {
    const box = [];
    for (let x = i; x < i + 3; x++) {
      for (let y = j; y < j + 3; y++) {
        box.push(board[x][y]);
      } 
    }
    if (!isUnique(box)) {
      return false
      }
    }
  }

  return true;
}

console.log(sudoku_validator([
  [ 1, 5, 2, 4, 8, 9, 3, 7, 6 ],
  [ 7, 3, 9, 2, 5, 6, 8, 4, 1 ],
  [ 4, 6, 8, 3, 7, 1, 2, 9, 5 ],
  [ 3, 8, 7, 1, 2, 4, 6, 5, 9 ],
  [ 5, 9, 1, 7, 6, 3, 4, 2, 8 ],
  [ 2, 4, 6, 8, 9, 5, 7, 1, 3 ],
  [ 9, 1, 4, 6, 3, 7, 5, 8, 2 ],
  [ 6, 2, 5, 9, 4, 8, 1, 3, 7 ],
  [ 8, 7, 3, 5, 1, 2, 9, 6, 4 ]
]))

console.log(sudoku_validator([
  [ 1, 1, 2, 4, 8, 9, 3, 7, 6 ],
  [ 7, 3, 9, 2, 5, 6, 8, 4, 1 ],
  [ 4, 6, 8, 3, 7, 1, 2, 9, 5 ],
  [ 3, 8, 7, 1, 2, 4, 6, 5, 9 ],
  [ 5, 9, 1, 7, 6, 3, 4, 2, 8 ],
  [ 2, 4, 6, 8, 9, 5, 7, 1, 3 ],
  [ 9, 1, 4, 6, 3, 7, 5, 8, 2 ],
  [ 6, 2, 5, 9, 4, 8, 1, 3, 7 ],
  [ 8, 7, 3, 5, 1, 2, 9, 6, 4 ]
]))

console.log(sudoku_validator(
[ [ 1, 3, 4, 6, 7, 8, 9, 1, 2 ],
  [ 6, 7, 2, 1, 9, 5, 3, 4, 8 ],
  [ 5, 9, 8, 3, 4, 2, 5, 6, 7 ],
  [ 8, 5, 9, 7, 6, 1, 4, 2, 3 ],
  [ 4, 2, 6, 8, 5, 3, 7, 9, 1 ],
  [ 7, 1, 3, 9, 2, 4, 8, 5, 6 ],
  [ 9, 6, 1, 5, 3, 7, 2, 8, 4 ],
  [ 2, 8, 7, 4, 1, 9, 6, 3, 5 ],
  [ 3, 4, 5, 2, 8, 6, 1, 7, 9 ] ]))

  console.log(sudoku_validator([
  [ 1, 5, 2, 4, 8, 9, 3, 7, 6 ],
  [ 7, 3, 9, 2, 5, 6, 8, 4, 1 ],
  [ 4, 6, 8, 3, 7, 1, 2, 9, 5 ],
  [ 3, 8, 7, 1, 2, 4, 6, 5, 9 ],
  [ 5, 9, 1, 7, 6, 3, 4, 2, 8 ],
  [ 2, 4, 6, 8, 9, 5, 7, 1, 3 ],
  [ 9, 1, 4, 6, 3, 7, 5, 8, 2 ],
  [ 6, 2, 5, 9, 4, 8, 1, 3, 7 ],
  [ 8, 7, 3, 5, 1, 2, 9, 6, 4 ]
]))






