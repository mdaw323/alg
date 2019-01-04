import java.util.*;

import static java.lang.Math.abs;

@SuppressWarnings("ALL") public class Ac25 {
    class Point {
        int a, b, c, d, g = -1;
        Set<Point> E = new HashSet<>();

        public Point(int a, int b, int c, int d) {
            this.a = a;
            this.b = b;
            this.c = c;
            this.d = d;
        }
    }

    Point[] V = new Point[2000];
    int N = 0;
    int G = 0;

    private void solve() {
        parseInput();
        for (int i = 0; i < N; i++) {
            for (int j = i + 1; j < N; j++) {
                if (len(V[i], V[j]) <= 3) {
                    V[i].E.add(V[j]);
                    V[j].E.add(V[i]);
                }
            }
        }
        for (int i = 0; i < N; i++) {
            if (V[i].g == -1) {
                bfs(V[i], ++G);
            }
        }
        System.out.println(G);
    }

    private void parseInput() {
        Scanner scanner = new Scanner(Ac13.class.getResourceAsStream("/a25.txt"));
        while (scanner.hasNext()) {
            V[N++] = new Point(scanner.nextInt(), scanner.nextInt(), scanner.nextInt(), scanner.nextInt());
        }
    }

    private void bfs(Point s, int gg) {
        Queue<Point> queue = new LinkedList<>();
        s.g = gg;
        queue.offer(s);
        while (!queue.isEmpty()) {
            Point v = queue.poll();
            for (Point e : v.E) {
                if (e.g != gg) {
                    e.g = gg;
                    queue.offer(e);
                }
            }
        }
    }

    int len(Point x, Point y) {
        return abs(x.a - y.a) + abs(x.b - y.b) + abs(x.c - y.c) + abs(x.d - y.d);
    }

    public static void main(String[] args) {
        new Ac25().solve();
    }
}
