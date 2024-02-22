
import java.io.*;
import java.util.*;

public class Main {
    static FastReader scan = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static int N, M;
    static int[] selected, nums, last_printed, used;

    static void input() {
        FastReader scan = new FastReader();
        N = scan.nextInt();
        M = scan.nextInt();
        selected = new int[M + 1];
        nums = new int[N + 1];
        used = new int[N + 1];
        for (int i=1; i<=N; i++) {
            nums[i] = scan.nextInt();
        }
        Arrays.sort(nums, 1, N + 1);
    }

    static void rec_func(int k) {
        if (k == M + 1) {
            // selected[1..M] 배열이 새롭게 탐색된 결과
            for (int i = 1; i <= M; i++) {
                sb.append(selected[i]).append(' ');
            }
        } else {
            int last_cand = 0;
            for (int cand=1; cand<=N; cand++) {
                if (used[cand] == 1) continue;
                if (nums[cand] == last_cand) continue;

                last_cand = nums[cand];
                selected[k] = nums[cand];
                used[cand] = 1;
                rec_func(k + 1);
                selected[k] = 0;
                used[cand] = 0;
            }
        }
    }

    public static void main(String[] args) {
        input();
        // 1 번째 원소부터 M 번째 원소를 조건에 맞는 모든 방법 찾기
        rec_func(1);
        System.out.println(sb.toString());
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