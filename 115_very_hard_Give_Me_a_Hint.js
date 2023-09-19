function grantTheHint(txt) {
  const words = txt.split(' ');
  const maxLength = Math.max(...words.map(word => word.length)) + 1;
  const hintLines = [];

  for (let i = 0; i < maxLength; i++) {
    const hintWords = words.map(word => {
      if (i < word.length) {
        return word.slice(0, i) + '_'.repeat(word.length - i);
      } else {
        return word;
      }
    });
    hintLines.push(hintWords.join(' '));
  }

  return hintLines;
}

// テストケース
const testCases = [
  'The River Nile',
  'Mary Queen of Scots',
  'The Life of Pi'
];

for (const testCase of testCases) {
  const hintLines = grantTheHint(testCase);
  console.log(`Input: "${testCase}"`);
  console.log('Hint Lines:');
  hintLines.forEach(line => console.log(line));
  console.log('---');
}

