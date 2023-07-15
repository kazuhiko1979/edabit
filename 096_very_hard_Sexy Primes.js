function sexy_primes(n, limit) {
    var primes = [];
    for (var x = 2; x < limit; x++) {
      if (isPrime(x)) {
        primes.push(x);
      }
    }
  
    var sexy = [];
    var sub_result = [];
  
    for (var i = 0; i < primes.length; i++) {
      for (var j = i + 1; j < primes.length; j++) {
        if (primes[i] + 6 === primes[j]) {
          sub_result.push(primes[i]);
          sub_result.push(primes[j]);
          sexy.push(sub_result);
          sub_result = [];
        }
      }
    }
  
    if (new Set(sexy.map((i) => i.length)).has(n)) {
      return sexy.map((s) => s.map((i) => i));
    } else {
      for (var k = 0; k < sexy.length; k++) {
        for (var l = 0; l < primes.length; l++) {
          if (sexy[k][sexy[k].length - 1] + 6 === primes[l]) {
            sexy[k].push(primes[l]);
            if (sexy[k].length === n) {
              break;
            }
          }
        }
      }
      return sexy.filter((i) => i.length === n).map((s) => s.map((i) => i));
    }
  }
  
  function isPrime(num) {
    if (num < 2) {
      return false;
    }
    for (var i = 2; i <= Math.sqrt(num); i++) {
      if (num % i === 0) {
        return false;
      }
    }
    return true;
  }

  console.log(sexy_primes(2, 100))
  console.log(sexy_primes(3, 100))
  console.log(sexy_primes(2, 300))
  
  