/*
Robot Path 🤖
Mubashir created a simple robot that is navigated by a series of North, East, South, and West [n, e, s, w] commands. Each command moves the robot one step in the given direction. The robot is designed for only two destinations:

Destination No. 1: e, n, e, e, n
Destination No. 2: w, n, w, n, w, w, n
Create a function that takes a list of commands and returns True if the robot reaches any of the destinations, False otherwise.

Examples
robot_path(["s", "e", "e", "n", "n", "e", "n"]) ➞ True
# Robot will end up at destination no. 1

robot_path(["n", "e", "s", "w", "n", "e", "s", "w", "w", "s", "n", "e"]) ➞ False
# Robot will be lost somewhere

robot_path(["n", "s", "n", "n", "e", "n", "w", "w", "s", "w", "w", "w", "n"]) ➞ True
*/

function robotPath(commands) {
    const destinations = [[3, 2], [-4, 3]];
    const x = commands.split('e').length - commands.split('w').length;
    const y = commands.split('n').length - commands.split('s').length;
    return destinations.some(dest => dest[0] === x && dest[1] === y);
}


// テスト
console.log(robotPath("s e e n n e n")); // true
console.log(robotPath("n e s w n e s w w s n e")); // false
console.log(robotPath("n s n n e n w w s w w w n")); // true
