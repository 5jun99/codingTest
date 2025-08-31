package restart.java;

import java.io.IOException;
import java.io.InputStream;

public class j1806 {
  static class FastScanner {
    private final InputStream in = System.in;
    private final byte[] buffer = new byte[1 << 16];

    private int ptr = 0, len = 0;

    private int read() throws IOException {
      if (ptr >= len) { len = in.read(buffer); ptr = 0; if (len < 0) return -1; }
      return buffer[ptr++];
    }

    int nextInt() throws IOException {
      int c, s = 1, x = 0;
      do { c = read(); } while (c <= ' ');
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

    long nextLong() throws IOException {
      int c, s = 1;
      long x = 0;
      do { c = read(); } while (c <= ' ');
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

    String next() throws IOException {
      int c;
      StringBuilder sb = new StringBuilder();
      do { c = read();} while ( c <= ' ');
      while (c > ' ') {
        sb.append((char)c);
        c = read();
      }
      return sb.toString();
    }
  }
  public static void main(String[] args) throws Exception {
    FastScanner fs = new FastScanner();

    int n = fs.nextInt();
    long s = fs.nextLong();

    int[] a = new int[n];

    for (int i = 0; i < n; i++) {
      a[i] = fs.nextInt();
    }

    int ans = minLenAtLeastS(a, s);
    StringBuilder sb = new StringBuilder();
    sb.append(ans).append('\n');
    System.out.print(sb);
  }

  static int minLenAtLeastS(int[] a, long s) {
    int n = a.length, ans = n + 1, left = 0;
    long sum = 0;
    for (int right = 0; right < n; right ++) {
      sum = sum + a[right];

      while (sum >= s) {
        int len = right - left + 1;
        if (len < ans) {
          ans = len;
        }
        sum -= a[left ++];
      }
    }

    return ans == n + 1 ? 0 : ans;
  }
}
