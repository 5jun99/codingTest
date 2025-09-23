package restart.java;

import java.io.IOException;
import java.io.InputStream;

public class j2003 {
  static class FastScanner {
    private final InputStream io = System.in;
    private final byte[] buffer = new byte[1 << 16];

    private int ptr = 0; int len = 0;

    private int read() throws IOException {
      while (ptr >= len) {
        len = io.read(buffer);
        ptr = 0;
        if (len < 0) {
          return -1;
        }
      }

      return buffer[ptr ++];
    }

    int nextInt() throws IOException {
      int c, s = 1; int x = 0;

      do {
        c = read();
      } while (c <= ' ');
      
      if (c == '-') {
        s = -1;
        c = read();
      }

      while (c > ' ') {
        x = x * 10 + (c - '0');
        c = read();
      }

      return x * s;
    }
  }

  public static void main(String[] args) throws Exception{
    FastScanner fs = new FastScanner();

    int n = fs.nextInt();
    int m = fs.nextInt();

    int[] a = new int[n];

    for (int i = 0; i < n; i++) {
      a[i] = fs.nextInt();
    }

    int left = 0;

    long curr = 0;
    long ans = 0;

    for (int right = 0; right < n; right++) {
      curr += a[right];

      while (curr > m) {
        curr -= a[left];
        left += 1;
      }

      if (curr == m) {
        ans += 1;
      }
    }
     StringBuilder sb = new StringBuilder();
      sb.append(ans).append('\n');
      System.out.print(sb);
  }
}
