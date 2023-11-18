public class minPalindromeStep {

  public static int minPalindromeSteps(String txt) {
    for (int i = 0; i < txt.length(); i++) {
      if (txt.substring(i).equals(
          new StringBuffer(txt.substring(i)).reverse().toString())) {
        return i;
      }
    }
    return 0;
  }

  // public static int minPalindromeSteps(String txt) {

  // int count = 0;
  // String temp = "";

  // if (txt.equals(new StringBuilder(txt).reverse().toString())) {
  // return count;
  // }

  // for (char i : txt.toCharArray()) {
  // temp += i;
  // temp = new StringBuilder(temp).reverse().toString();
  // String result = txt + temp;
  // count++;
  // if (result.equals(new StringBuilder(result).reverse().toString())) {
  // return count;
  // } else {
  // temp = new StringBuilder(temp).reverse().toString();
  // }
  // }

  // return count;

  // }

  public static void main(String[] args) {

    System.out.println(minPalindromeSteps("race"));
    System.out.println(minPalindromeSteps("mada"));
    System.out.println(minPalindromeSteps("mirror"));
    System.out.println(minPalindromeSteps("maa"));
    System.out.println(minPalindromeSteps("m"));
    System.out.println(minPalindromeSteps("rad"));
    System.out.println(minPalindromeSteps("madam"));
    System.out.println(minPalindromeSteps("radar"));
    System.out.println(minPalindromeSteps("www"));
    System.out.println(minPalindromeSteps("me"));
    System.out.println(minPalindromeSteps("rorr"));
    System.out.println(minPalindromeSteps("pole"));

  }

}