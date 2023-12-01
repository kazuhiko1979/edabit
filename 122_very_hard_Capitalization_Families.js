function grouping(words){
  words.sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));
  const groups = {};

  for (const word of words) {
    const cap = (word.match(/[A-Z]/g) || []).length;
    if (cap in groups) {
      groups[cap].push(word);
    } else {
        groups[cap] = [word];
    }
  }
  return groups;
}

// Test cases
console.log(grouping(["HaPPy", "mOOdy", "yummy", "mayBE"]));
console.log(grouping(["eeny", "meeny", "miny", "moe"]));
console.log(grouping(["FORe", "MoR", "bOR", "tOR", "sOr", "lor"]));