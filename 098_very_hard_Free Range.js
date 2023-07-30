// """
// Free Range
// Create a function which converts an ordered number list into a list of ranges (represented as strings). Note how some lists have some numbers missing.

// Examples
// numbers_to_ranges([1, 2, 3, 4, 5]) ➞ ["1-5"]

// numbers_to_ranges([3, 4, 5, 10, 11, 12]) ➞ ["3-5", "10-12"]

// numbers_to_ranges([1, 2, 3, 4, 99, 100]) ➞ ["1-4", "99-100"]

// numbers_to_ranges([1, 3, 4, 5, 6, 7, 8]) ➞ ["1", "3-8"]
// Notes
// If there are no numbers consecutive to a number in the list, represent it as only the string version of that number (see example #4).
// Return an empty list if the given list is empty.
// """

function numbers_to_ranges(lst) {
    if(!lst.length) {
        return lst;
    }

    const result = [];
    let start = lst[0];
    let end = lst[0];

    for (let i =1; i < lst.length; i++) {
        if (lst[i] === end + 1) {
            end = lst[i];
        } else {
            if (start === end) {
                result.push(start.toString());
            } else {
                result.push(`${start}-${end}`)
            }
            start = end = lst[i];
        }
    }

    if (start === end) {
        result.push(start.toString());
    } else {
        result.push(`${start}-${end}`);
    }

    return result;

}

console.log(numbers_to_ranges([1, 2, 3, 4, 5]));
console.log(numbers_to_ranges([3, 4, 5, 10, 11, 12]));
console.log(numbers_to_ranges([1, 2, 3, 4, 99, 100]));
console.log(numbers_to_ranges([1, 3, 4, 5, 6, 7, 8]));
