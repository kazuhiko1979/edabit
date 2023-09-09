function strongPassword(password) {
  const digitCount = password.split('').filter(i => /\d/.test(i)).length;
  const lowerCount = password.split('').filter(i => /[a-z]/.test(i)).length;
  const upperCount = password.split('').filter(i => /[A-Z]/.test(i)).length;
  const specialCount = password.split('').filter(i => /[!@#$%^&*()-+]/.test(i)).length;

  const conditions = [
    digitCount === 0,
    lowerCount === 0,
    upperCount === 0,
    specialCount === 0
  ];

  const ans = conditions.filter(cond => cond).length;
  return Math.max(ans, 6 - password.length);
}

// Example usage:
console.log(strongPassword("#Edabit")); // 1
console.log(strongPassword("Cr3ateAStr0ng1")); // 1
console.log(strongPassword("CreateAStrongOne")); // 2
console.log(strongPassword("willthispass")); // 3
console.log(strongPassword("w1llth!spass?")); // 1
console.log(strongPassword("W1llth!spass?")); // 0
console.log(strongPassword("1sth!")); // 1
console.log(strongPassword("sth!")); // 2
console.log(strongPassword("bd")); // 4
console.log(strongPassword("d")); // 5
console.log(strongPassword("[?")); // 4