const colors = ["red", "red-orange", "orange", "yellow-orange", "yellow", "yellow-green",  "green", "blue-green", "blue", "blue-violet", "violet", "red-violet"];

function findFourPoints(anchor, index, oppositeIndex, points) {
    const anchorRightTwoIndex = (index + points[0]) % 12;
    const anchorOppositeRightIndex = (anchorRightTwoIndex + points[1]) % 12;

    const anchorOppositeColor = colors[oppositeIndex];
    const anchorRightColor = colors[anchorRightTwoIndex];
    const anchorOppositeRightColor = colors[anchorOppositeRightIndex];

    return new Set([anchorOppositeRightColor, anchor, anchorOppositeColor, anchorRightColor]);
}

function findThreePoints(anchor, index, points) {
    const rightFourIndex = (index + points[0]) % 12;
    const leftFourIndex = (index - points[0] + 12) % 12;

    const rightFourColor = colors[rightFourIndex];
    const leftFourColor = colors[leftFourIndex];

    return new Set([anchor, rightFourColor, leftFourColor]);
}

function colourHarmony(anchor, combination) {
    const index = colors.indexOf(anchor);
    const numForComplementary = 6;
    const oppositeIndex = (index + numForComplementary) % 12;

    const numForRectangle = [2, 6];
    const numForSquare = [3, 6];
    const numForTriadic = [4];
    const numForSplitComplementary = [5];
    const numForAnalogous = [1];

    if (combination === "complementary") {
        const oppositeNumber = colors[oppositeIndex];
        return new Set([anchor, oppositeNumber]);
    }

    if (combination === "rectangle") {
        return findFourPoints(anchor, index, oppositeIndex, numForRectangle);
    }

    if (combination === "square") {
        return findFourPoints(anchor, index, oppositeIndex, numForSquare);
    }

    if (combination === "triadic") {
        return findThreePoints(anchor, index, numForTriadic);
    }

    if (combination === "split_complementary") {
        return findThreePoints(anchor, index, numForSplitComplementary);
    }

    if (combination === "analogous") {
        return findThreePoints(anchor, index, numForAnalogous);
    }
}

console.log(colourHarmony('blue-green', 'triadic'));
console.log(colourHarmony('blue', 'complementary'));
console.log(colourHarmony('violet', 'square'));
console.log(colourHarmony('yellow-green', 'analogous'));
console.log(colourHarmony('red', 'rectangle'));
console.log(colourHarmony('violet', 'split_complementary'));
console.log(colourHarmony('orange', 'analogous'));
console.log(colourHarmony('red-orange', 'complementary'));
console.log(colourHarmony('red-orange', 'square'));
console.log(colourHarmony('blue-violet', 'split_complementary'));
console.log(colourHarmony('red-violet', 'triadic'));
console.log(colourHarmony('red-violet', 'rectangle'));