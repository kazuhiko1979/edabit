//Fix the Right Answer
//Create a function that takes a string and returns the right answer.
//
//Examples
//post_fix("2 2 +") ➞ 4
//
//post_fix("2 2 /") ➞ 1
//
//post_fix("8 4 / 9 * 3 1 * /") ➞ 54
//Notes
//The operators + - * / may be supported.
//Output always returns an integer.

function post_fix(expr) {
    const numbers = expr.match(/\d{1,2}/g);
    const operators = expr.match(/[\+\-\*\/]/g);

    const max_length = Math.max(numbers.length, operators.length);
    const result = [];

    for (let i = 0; i < max_length; i++) {
        if (i < numbers.length) {
            result.push(numbers[i]);
        }
        if (i < operators.length) {
            result.push(operators[i]);
        }
    }

    return eval(result.join(''));
}

console.log(post_fix("2 2 +"))
console.log(post_fix("2 2 /"))
console.log(post_fix("5 6 * 2 1 + /"))
console.log(post_fix("10 10 * 10 /"))
console.log(post_fix("8 4 / 9 * 3 1 * /"))
console.log(post_fix("1 1 + 2 2 + -"))

