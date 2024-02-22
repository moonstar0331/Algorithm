
import java.io.*;
import java.util.*;

public class Main {
    static FastReader scan = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static int N;
    static String[] a;

    static void input() {
        N = scan.nextInt();
        a = new String[N+1];
        for (int i = 1; i <= N; i++) {
            // 입력된 파일 이름을 . 을 기준으로 나눠서 확장자를 가져오기
            String[] str = scan.next().split("\\.");
            a[i] = str[1];
        }
    }

    static void pro() {
        // 정렬
        Arrays.sort(a, 1, N+1);

        // TODO: 확장자마다 몇 번 나타났나 count 하기
        int cnt = 1;

        for(int i=2; i<=N; i++) {
            if(a[i].equals(a[i-1])) cnt++;
            else {
                sb.append(a[i-1]).append(' ').append(cnt).append('\n');
                cnt = 1;
            }
        }
        sb.append(a[N]).append(' ').append(cnt);
        System.out.println(sb.toString());
    }

    // 파일을 확장자 별로 정리해서 몇 개씩 있는지
    // 확장자들을 사전 순으로 정렬
    public static void main(String[] args) {
        input();
        pro();
    }


    static class FastReader {
        BufferedReader br;
        StringTokenizer st;

        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        public FastReader(String s) throws FileNotFoundException {
            br = new BufferedReader(new FileReader(new File(s)));
        }

        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        long nextLong() {
            return Long.parseLong(next());
        }

        double nextDouble() {
            return Double.parseDouble(next());
        }

        String nextLine() {
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }
}