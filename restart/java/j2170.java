package restart.java;

import java.io.IOException;
import java.io.InputStream;
import java.util.Arrays;

public class j2170 {
  static class FastScanner{
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

    int nextInt() throws IOException{
      int c, s = 1;
      int x = 0;

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

    long nextLong() throws IOException{
      int c, s = 1;
      long x = 0;

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

    String next() throws IOException{
      int c;
      StringBuilder sb = new StringBuilder();

      do {
        c = read();
      } while (c <= ' ');
      if (c == '-') {
        sb.append(c);
        c = read();
      }
      return sb.toString();
    }

  }

  public static void main(String[] args) throws Exception{
    FastScanner fs = new FastScanner();

    int n = fs.nextInt();

    int[][] edges = new int[n][2];
    

    for (int i = 0; i < n; i++) {
      edges[i][0] = fs.nextInt();
      edges[i][1] = fs.nextInt();
    }

    Arrays.sort(edges, (a, b) -> {
      if (a[0] != b[0]) return Integer.compare(a[0], b[0]);
      return Integer.compare(a[1], b[1]);
    });
    int left = edges[0][0] - 1;
    int right = edges[0][0] - 1;

    long ans = 0;

    for (int[] edge : edges) {
      int s = edge[0];
      int e = edge[1];

      if (s > right) {
        ans += e - s;
        left = s;
        right = e;
      }
      else if (e > right) {
        ans += e - right;
        right = e;
      }
      
    }

    StringBuilder sb = new StringBuilder();
    sb.append(ans).append('\n');
    System.out.print(sb);
  }
}
