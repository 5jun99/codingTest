package restart.java;

import java.io.IOException;
import java.io.InputStream;
import java.util.Arrays;

public class j2470 {
  static class FastScanner {
    private final InputStream io = System.in;
    private final byte[] buffer = new byte[1 << 16];

    private int ptr = 0, len = 0;

    private int read() throws IOException {
      if (ptr >= len) {
        len = io.read(buffer);
        ptr = 0;
        if (len < 0) {
          return -1;
        }
      }
      return buffer[ptr++];
    }

    int nextInt() throws IOException {
      int c, s = 1;
      int x = 0;

      do {
        c = read();
      } while (c <= ' ');

      if (c == '-') {
        s = -1;
        c = read();
      }

      while ( c> ' ') {
        x = x * 10 + (c - '0');
        c = read();
      }
      return x * s;
    }
  }

  public static void main(String[] args) throws Exception{
    FastScanner fs = new FastScanner();

    int n = fs.nextInt();
    int[] a = new int[n];

    for (int i = 0; i < n; i ++) {
      a[i] = fs.nextInt();
    }
    Arrays.sort(a);


    int left = 0;
    int right = n - 1;

    int bestL = a[left];
    int bestR = a[right];

    long best = Math.abs(a[left] + a[right]);

    while (left < right) {
      long sum = a[left] + a[right];
      long abs = Math.abs(sum);

      if (best > abs) {
        best = abs;
        bestL = a[left];
        bestR = a[right];
      }

      if (sum < 0) {
        left += 1;
      } else {
        right -= 1;
      }
    }
    System.out.print(bestL + " " + bestR);
  }
}
