function expressFactors(n) {
    let res = {};
    let i = 2;
    
    while (i <= n) {
        while (n % i === 0) {
            res[i] = (res[i] || 0) + 1;
            n /= i;
        }
        i++;
    }

    let result = [];
    Object.keys(res).sort((a, b) => a - b).forEach((key) => {
        if (res[key] === 1) {
            result.push(key.toString());
        } else {
            result.push(`${key}^${res[key]}`);
        }
    });

    return result.join(' x ');
}

// Test cases
console.log(expressFactors(10));  // "2 x 5"
console.log(expressFactors(60));  // "2^2 x 3 x 5"
console.log(expressFactors(323)); // "17 x 19"
console.log(expressFactors(5040)); // "2^4 x 3^2 x 5 x 7"
