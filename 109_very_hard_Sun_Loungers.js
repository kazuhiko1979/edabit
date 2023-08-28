function sunLoungers(beach) {
  return ('0' + beach + '0').split('1').reduce((sum, segment) => sum + Math.floor((segment.length - 1) / 2), 0);
}

console.log(sunLoungers("10001"));
console.log(sunLoungers("00101"));
console.log(sunLoungers("000"));