function constraint(txt) {
  if (/^[a-z]+$/.test(txt.toLowerCase())) {
      return 'Pangram';
  } else if ([...txt.toLowerCase()].every(ch => ch !== ' ' && txt.toLowerCase().split(txt.toLowerCase().indexOf(ch)).length === 1)) {
      return 'Heterogram';
  } else if (new Set(txt.toLowerCase().split(' ')[0]).size === 1) {
      return 'Tautogram';
  } else {
      const words = txt.toLowerCase().split(' ');
      if (words.some(word => word.split('').some(ch => txt.toLowerCase().split(ch).length > 1))) {
          return 'Transgram';
      } else {
          return 'Sentence';
      }
  }
}

// Test with examples
const sentence1 = "A cannibal alligator has attacked an unaware vegan alligator.";
const sentence2 = "Those loops could work without constants sometimes.";

console.log(constraint(sentence1)); // Should output 'Pangram'
console.log(constraint(sentence2)); // Should output 'Transgram'
