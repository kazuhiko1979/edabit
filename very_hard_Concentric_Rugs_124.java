import java.util.Arrays;

public class very_hard_Concentric_Rugs_124 {

  public static int[][] generateRug(int n) {
    if (n == 1) {
      return new int[][] { { 0 } };
    }

    int[][] rug = new int[n][n];
    int layers = n / 2;

    for (int layer = 0; layer < layers; layer++) {
      int value = layers - layer;
      for (int i = layer; i < n - layer; i++) {
        rug[layer][i] = value;
        rug[n - 1 - layer][i] = value;
        rug[i][layer] = value;
        rug[i][n - 1 - layer] = value;
      }
    }

    return rug;
  }

  public static void main(String[] args) {
    System.out.println(Arrays.deepToString(generateRug(1)));
    System.out.println(Arrays.deepToString(generateRug(3)));
    System.out.println(Arrays.deepToString(generateRug(5)));
    System.out.println(Arrays.deepToString(generateRug(7)));
    System.out.println(Arrays.deepToString(generateRug(9)));

  }
}