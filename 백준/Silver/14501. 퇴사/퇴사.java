
import java.io.*;
import java.util.*;

public class Main {
    static FastReader scan = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static int N, ans;
    static int[] T, P, selected;

    static void input() {
        FastReader scan = new FastReader();
        N = scan.nextInt();
        T = new int[N + 1];
        P = new int[N + 1];
        selected = new int[N + 1];

        for (int i=1; i<=N; i++) {
            T[i] = scan.nextInt();
            P[i] = scan.nextInt();
        }
    }

    static void rec_func(int k, int value) {
        if (k >= N + 1) {
            ans = Math.max(ans, value);
        } else {
            if (k + T[k] > N + 1) {
                rec_func(k + 1, value);
            } else {
                selected[k] = 1;
                rec_func(k + T[k], value + P[k]);
                selected[k] = 0;
                rec_func(k + 1, value);
            }
        }
    }

    public static void main(String[] args) {
        // N + 1 일째 되는 날 퇴사
        // 남은 N 일동안 최대한 많은 상담
        // 하루에 하나씩 서로 다른 사람의 상담 잡음
        // 각각 상담을 완료하는데 걸리는 기간 T[i]
        // 상담을 했을 때 받을 수 있는 금액 P[i]
        input();
        rec_func(1, 0);
        System.out.println(ans);
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
            while(st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch(IOException e) {
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
            } catch(IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }
}