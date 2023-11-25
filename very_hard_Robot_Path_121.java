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

import java.util.Arrays;
import java.util.List;

public class very_hard_Robot_Path_121 {
    
    public static boolean robotPath(String commands){
        List<List<Integer>> destinations = Arrays.asList(Arrays.asList(3, 2), Arrays.asList(-4, 3));
        int x = commands.split("e").length - commands.split("w").length;
        int y = commands.split("n").length - commands.split("s").length;

        System.out.println(x);
        System.out.println(y);
        

        for (List<Integer> dest: destinations){
            if (dest.get(0) == x && dest.get(1) == y){
                return true;
            }
        }
        return false;
    }

public static void main(String[] args) {
        System.out.println(robotPath("s e e n n e n")); // true
        System.out.println(robotPath("n e s w n e s w w s n e")); // false
        System.out.println(robotPath("n s n n e n w w s w w w n")); // true
    }
}