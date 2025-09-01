package restart.java;

import java.io.IOException;
import java.io.InputStream;
import java.util.Arrays;

public class j2110 {
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
      int c, s = 1; int x = 0;
      do {
        c = read();
      } while (c <= ' ');

      if ( c == '-') {
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
      int c, s = 1; long x = 0;
      do {
        c = read();
      } while (c <= ' ');

      if ( c == '-') {
        s = -1;
        c = read();
      }
      
      while (c >= ' ') {
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

  static int[] a;
  static int N, C;
  public static void main(String[] args) throws Exception{
    FastScanner fs = new FastScanner();
    N = fs.nextInt();
    C = fs.nextInt();

    a = new int[N];

    for (int i = 0; i < N; i ++) {
      a[i] = fs.nextInt();
    }

    Arrays.sort(a);
    long answer = -1;
    long low = 1;
    long high = a[N - 1] - a[0];

    while (low <= high) {
      long mid = (low + high) >>> 1;
      if (can(mid)) {
        low = mid + 1;
        answer = mid;
      } else {
        high = mid - 1;
      }
    }

    System.out.println(answer);
  }

  static boolean can(long mid) {
    int cnt = 1;
    long last = a[0];

    for (int i = 1; i < N; i++) {
      if (a[i] - last >= mid) {
        cnt++;
        last = a[i];
      }
    }

    return cnt >= C;
  }
}
