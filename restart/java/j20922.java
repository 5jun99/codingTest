package restart.java;

import java.io.IOException;
import java.io.InputStream;

public class j20922 {
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
      int c,s = 1;
      int x = 0;

      do { c = read();} while(c <= ' ');
      if (c == '-') {
        s = -1;
        c = read();
      }
      while ( c >' ') {
        x = x * 10  + (c - '0');
        c = read(); 
      }
      return s == 1 ? x : -x;
    }
  }
  public static void main(String[] args) throws Exception{
    FastScanner fs = new FastScanner();
    int n = fs.nextInt();
    int k = fs.nextInt();

    int[] a = new int[n];
    int maxV = 0;
    for (int i = 0 ; i < n; i++) {
      a[i] = fs.nextInt();
      if (a[i] > maxV) maxV = a[i];
    }
    int[] cnt = new int[Math.max(maxV + 1, 1)];
    int left = 0;
    int ans = 0;

    for (int right = 0; right < n; right++) {
      int v = a[right];

      cnt[v] += 1;

      while (cnt[v] > k) {
        cnt[a[left++]]--;
      }

      ans = Math.max(ans, right - left + 1);
    } 

    StringBuilder sb = new StringBuilder();
    sb.append(ans).append('\n');
    System.out.print(sb);
  }
}
