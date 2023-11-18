function minPalindromeSteps(txt){

  for (let i = 0; i < txt.length; i++) {
    if (txt.slice(i) === txt.slice(i).split("").reverse().join("")) {
      return i;
    }
  }

  // let count = 0;
  // let temp = "";

  // if (txt === txt.split("").reverse().join("")){
  //   return count;
  // }

  // for (let i of txt){
  //   temp += i;
  //   temp = temp.split("").reverse().join("");
  //   let reuslt = txt + temp;
  //   count++;
  //   if (reuslt == reuslt.split("").reverse().join("")){
  //     return count;
  //   } else {
  //     temp = temp.split("").reverse().join("");
  //   }
  // }
}

console.log(minPalindromeSteps("race")); 
console.log(minPalindromeSteps("mada"));
console.log(minPalindromeSteps("mirror"));
console.log(minPalindromeSteps("maa"));
console.log(minPalindromeSteps("m"));
console.log(minPalindromeSteps("rad"));
console.log(minPalindromeSteps("madam"));
console.log(minPalindromeSteps("radar"));  
console.log(minPalindromeSteps("www"));
console.log(minPalindromeSteps("me"));
console.log(minPalindromeSteps("rorr"));
console.log(minPalindromeSteps("pole"));