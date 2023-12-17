function sameLetterPattern(txt1, txt2) {
    return allPos(txt1).toString() === allPos(txt2).toString();
}

function allPos(x) {
    let positions = [];
    for (let i = 0; i < x.length; i++) {
        for (let j = 0; j < x.length; j++) {
            if (x[i] === x[j]) {
                positions.push(j);
            }
        }
    }
    return positions;
}

// function sameLetterPattern(txt1, txt2){
//   function generatePattern(txt){
//     let temp = {};
//     let pattern = '';
//     let currentPattern = 1;

//     for (let char of txt){
//       if (!temp[char]){
//         temp[char] = currentPattern;
//         currentPattern +=1;
//       }
//       pattern += temp[char];
//     }

//   return pattern;
//   }

//   return generatePattern(txt1) === generatePattern(txt2);
// }


// Examples
console.log(sameLetterPattern('ABAB', 'CDCD'));  // true
console.log(sameLetterPattern('AAABBB', 'CCCDDD'));  // true
console.log(sameLetterPattern('ABCBA', 'BCDCB'));  // true
console.log(sameLetterPattern('FFGG', 'FFG'));  // false
console.log(sameLetterPattern('FFGG', 'CDCD'));  