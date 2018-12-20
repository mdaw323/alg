import java.util.*;

public class Ac20 {

    private char[] S;
    private HashSet<PointPosition> visited = new HashSet<>(1000000);
    private HashMap<Point, Set<Point>> edges = new HashMap<>();
    private HashMap<List<Integer>, Point> vectors = new HashMap<>();
    private HashMap<Integer, Group> groupMap = new HashMap<>();

    class Group {
        int left, right;
        List<Integer> pipes = new ArrayList<>();
    }

    class Point {
        final int x, y;

        Point(int x, int y) {
            this.x = x;
            this.y = y;
        }

        int d = -1;

        @Override public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Point point = (Point) o;
            return x == point.x &&
                    y == point.y;
        }

        @Override public int hashCode() {
            return Objects.hash(x, y);
        }
    }

    class PointPosition {
        final int x, y, position;

        PointPosition(int x, int y, int position) {
            this.x = x;
            this.y = y;
            this.position = position;
        }

        @Override public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            PointPosition that = (PointPosition) o;
            return x == that.x &&
                    y == that.y &&
                    position == that.position;
        }

        @Override public int hashCode() {
            return Objects.hash(x, y, position);
        }
    }

    private void findGroups() {
        Group x = new Group();
        Stack<Group> stack = new Stack<>();

        for (int i = 0; i < S.length; i++) {
            if (S[i] == '(') {
                x = new Group();
                x.left = i;
                stack.push(x);
            }
            if (S[i] == ')') {
                x = stack.pop();
                x.right = i;
                groupMap.put(x.left, x);
                groupMap.put(x.right, x);
                for (int z : x.pipes) {
                    groupMap.put(z, x);
                }
                if (!stack.isEmpty()) {
                    x = stack.peek();
                }
            }
            if (S[i] == '|') {
                x.pipes.add(i);
            }
        }
    }

    private void addEdge(int x1, int y1, int x2, int y2) {
        List<Integer> list1 = Arrays.asList(x1, y1);
        if (!vectors.containsKey(list1)) {
            vectors.put(list1, new Point(x1, y1));
        }
        List<Integer> list2 = Arrays.asList(x2, y2);
        if (!vectors.containsKey(list2)) {
            vectors.put(list2, new Point(x2, y2));
        }

        Point p1 = vectors.get(list1);
        Point p2 = vectors.get(list2);
        if (!edges.containsKey(p1)) {
            edges.put(p1, new HashSet<>());
        }
        if (!edges.containsKey(p2)) {
            edges.put(p2, new HashSet<>());
        }
        edges.get(p1).add(p2);
        edges.get(p2).add(p1);
    }

    private void go(PointPosition p) {
        if (visited.contains(p) || p.position >= S.length) {
            return;
        }
        visited.add(p);
        if (S[p.position] == '(') {
            Group g = groupMap.get(p.position);
            go(new PointPosition(p.x, p.y, p.position + 1));
            for (int pipe : g.pipes) {
                go(new PointPosition(p.x, p.y, pipe + 1));
            }
        } else if (S[p.position] == '|') {
            Group g = groupMap.get(p.position);
            go(new PointPosition(p.x, p.y, g.right + 1));
        } else if (S[p.position] == ')') {
            go(new PointPosition(p.x, p.y, p.position + 1));
        } else if (S[p.position] == 'W') {
            addEdge(p.x, p.y, p.x - 1, p.y);
            go(new PointPosition(p.x - 1, p.y, p.position + 1));
        } else if (S[p.position] == 'N') {
            addEdge(p.x, p.y, p.x, p.y + 1);
            go(new PointPosition(p.x, p.y + 1, p.position + 1));
        } else if (S[p.position] == 'E') {
            addEdge(p.x, p.y, p.x + 1, p.y);
            go(new PointPosition(p.x + 1, p.y, p.position + 1));
        } else if (S[p.position] == 'S') {
            addEdge(p.x, p.y, p.x, p.y - 1);
            go(new PointPosition(p.x, p.y - 1, p.position + 1));
        }
    }

    private int bfs() {
        Queue<Point> queue = new LinkedList<>();
        Point s = null;
        for (Point point : edges.keySet()) {
            if (point.x == 0 && point.y == 0) {
                s = point;
                break;
            }
        }
        assert s != null;
        s.d = 0;
        int maxd = 0;
        queue.offer(s);
        while (!queue.isEmpty()) {
            Point v = queue.poll();
            for (Point e : edges.get(v)) {
                if (e.d < 0) {
                    e.d = v.d + 1;
                    maxd = e.d;
                    queue.offer(e);
                }
            }

        }
        return maxd;
    }


    private void parseInput() {
        //S = "WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))".toCharArray();
        Scanner scanner = new Scanner(Ac20.class.getResourceAsStream("/a20.txt"));
        S = scanner.nextLine().toCharArray();


    }

    private void solve() {
        parseInput();
        findGroups();


        go(new PointPosition(0, 0, 0));
        int maxDistance = bfs();

        int sum1000 = 0;
        for (Point value : vectors.values()) {
            if (value.d >= 1000) {
                sum1000++;
            }
        }
        System.out.printf("max distance: %d, distance>1000: %d",maxDistance, sum1000);
    }


    public static void main(String[] args) {
        new Ac20().solve();
    }

}
