//"""
//Breaking News!
//A local news station needs your help to generate the scrolling text for the headlines!
//
//Create a function that returns a list of strings, where each string contains a single frame of what the scrolling text will look like.
//
//Text will scroll from right to left.
//The screen will have a width of n characters.
//Start and stop when no letters appear on the screen.
//The example below will demonstrate the output when the screen width is 10.
//
//Examples
//news_at_ten("edabit", 10) ➞ [
//  "          ",
//  "         e",
//  "        ed",
//  "       eda",
//  "      edab",
//  "     edabi",
//  "    edabit",
//  "   edabit ",
//  "  edabit  ",
//  " edabit   ",
//  "edabit    ",
//  "dabit     ",
//  "abit      ",
//  "bit       ",
//  "it        ",
//  "t         ",
//  "          "
//]
//Notes
//Every string should be n characters long, so you should pad the string with spaces if the text isn't long enough.
//Similarly, if the text is too long for the screen width, then it's only possible to display a fraction of the text at a time.
//See the Tests tab for more examples.
//"""

function news_at_ten(txt, n) {

    let str_1 = ' '.repeat(n) + txt + ' '.repeat(n);
    let lst_1 = [];

    for (let i = 0; i < txt.length + n + 1; i++) {
        lst_1.push(str_1.slice(0, n));
        str_1 = str_1.slice(1) + str_1[0]
    }
    
    return lst_1

    }

// Test cases
const testCases = [
    ['edabit', 10],
    ['The latest news from News at Ten', 17],
    ['Woman singlehandedly boosts seaside town economy with sea-shell business!', 7],
    ['news', 30],
    ['Hello World', 11]
];

for (const [txt, n] of testCases) {
    const result = news_at_ten(txt, n);
    for (const line of result) {
        console.log(line);
    }
}

