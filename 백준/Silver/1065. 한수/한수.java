
import java.io.*;
import java.util.*;

public class Main {
    static FastReader scan = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static int N;

    static void input() {
        FastReader scan = new FastReader();
        N = scan.nextInt();
    }

    static int arithetic_sequence(int num) {
        int cnt = 0;

        if (num < 100) {
            return num;
        } else {
            cnt = 99;

            for (int i = 100; i<=num; i++) {
                int hun = i / 100;
                int ten = (i / 10) % 10;
                int one = i % 10;
                
                if ((hun - ten) == (ten - one)) cnt++;
            }
        }
        return cnt;
    }

    public static void main(String[] args) {
        // 정수 X의 각 자리가 등차수열을 이루면, 그 수를 한수
        // 등차수열: 연속된 두 개의 수의 차이가 일정한 수열
        input();
        System.out.println(arithetic_sequence(N));
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