function isLadderSafe(ldr) {
  ldr = ldr.slice(1, -1);
  const rung = ldr.map((row, index) => row === '#'.repeat(ldr[0].length) ? index : -1).filter(index => index !== -1);

  if (rung.length === 0) {
    return false;
  }

  const diff = rung[1] - rung[0];
  return (
    rung.every((value, index, array) => index === array.length - 1 || array[index + 1] - value === diff) &&
    diff <= 3 &&
    diff * rung.length >= ldr.length &&
    ldr[0].length >= 5
  );
}

console.log(isLadderSafe([
  "#   #",
  "#####",
  "#   #",
  "#   #",
  "#####",
  "#   #",
  "#   #",
  "#####",
  "#   #"
]));

console.log(isLadderSafe([
  "#   #",
  "#####",
  "#   #",
  "#####",
  "#   #",
  "#   #",
  "#####",
  "#   #"
]));

console.log(isLadderSafe([
  "#   #",
  "#  ##",
  "#   #",
  "#   #",
  "#####",
  "#   #",
  "#   #",
  "#####",
  "#   #"
]));
