
import java.io.*;
import java.util.*;

public class Main {
    static FastReader scan = new FastReader();
    static StringBuilder sb = new StringBuilder();

    static int N, M, V;
    static ArrayList<Integer>[] adj;
    static boolean[] visit;

    static void input() {
        N = scan.nextInt();
        M = scan.nextInt();
        V = scan.nextInt();
        adj = new ArrayList[N + 1];
        visit = new boolean[N + 1];
        for (int i = 1;i <= N; i++)
            adj[i] = new ArrayList<>();
        for(int i=0; i<M; i++) {
            int x = scan.nextInt(), y = scan.nextInt();
            adj[x].add(y);
            adj[y].add(x);
        }

        /* TODO */
        for(int i=1; i<=N; i++) {
            Collections.sort(adj[i]);
        }
    }

    // x 를 갈 수 있다는 걸 알고 방문한 상태
    static void dfs(int x) {
        /* TODO */
        visit[x] = true;
        sb.append(x).append(' ');
        
        // x 에서 갈 수 있는 곳들을 작은 번호부터 모두 방문
        for (int y : adj[x]) {
            // y 를 이미 갈 수 있다는 사실을 아는 경우
            if(visit[y]) continue;
            
            // y 에서 갈 수 있는 곳들도 확인
            dfs(y);
        }
    }

    // start 에서 시작해서 갈 수 있는 정점들을 모두 탐색하기
    static void bfs(int start) {
        Queue<Integer> que = new LinkedList<>();
        /* TODO */
        
        // start 는 방문 가능한 점이므로 큐에 추가
        que.add(start);
        visit[start] = true;
        
        while(!que.isEmpty()) {
            int x = que.poll();
            
            sb.append(x).append(' ');
            for (int y : adj[x]) {
                if(visit[y]) continue;
                
                que.add(y);
                visit[y] = true;
            }
        }
    }

    static void pro() {
        visit = new boolean[N + 1];
        // 모든 x에 대해서 adj[x] 정렬하기
        /* TODO */

        // DFS, BFS 결과 구하기
        /* TODO */
        dfs(V);
        sb.append('\n');
        for(int i=1; i<=N; i++) visit[i] = false;
        bfs(V);

        System.out.println(sb);
    }

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