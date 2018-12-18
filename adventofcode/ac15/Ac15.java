import java.util.*;
import java.util.stream.Collectors;

public class Ac15 {

    class Unit {
        boolean isGoblin;
        int x;
        int y;
        int hp = 200;

        public Unit(boolean goblin, int x, int y) {
            this.isGoblin = goblin;
            this.x = x;
            this.y = y;
        }
    }

    char[][] M = new char[32][32];
    Map<Character, Unit> units = new HashMap<>();


    public void resolveRound() {
        List<Unit> sortedUnits = units.values().stream()
                .sorted((o1, o2) -> o1.x == o2.x ? Integer.compare(o1.y, o2.y) :
                        Integer.compare(o1.x, o2.x)).collect(Collectors.toList());
        for (Unit sortedUnit : sortedUnits) {
            if (sortedUnit.hp > 0) {
                resolveUnitRound(sortedUnit);
            }
        }
    }

    class Point {
        int x, y;

        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public void resolveUnitRound(Unit unit) {
        int[][] d = new int[32][32];
        Queue<Point> q = new LinkedList<>();
        q.offer(new Point(unit.x, unit.y));
        while (!q.isEmpty()) {
            Point p = q.poll();
            if (M[p.x-1][p.y] == '.') {

            }
        }

    }

    private void addInput() {
        int i = 0;
        M[i++] = "################################".toCharArray();
        M[i++] = "#####################...########".toCharArray();
        M[i++] = "##########.##########..#########".toCharArray();
        M[i++] = "##########.##########...########".toCharArray();
        M[i++] = "#######....########..G.G########".toCharArray();
        M[i++] = "######.....######..........#####".toCharArray();
        M[i++] = "#######....######G.........#####".toCharArray();
        M[i++] = "#######...G#####...........#####".toCharArray();
        M[i++] = "#######..#.####............#####".toCharArray();
        M[i++] = "########....###..G.......E######".toCharArray();
        M[i++] = "######....####.............#####".toCharArray();
        M[i++] = "######.G###............G......##".toCharArray();
        M[i++] = "######..##G...#####............#".toCharArray();
        M[i++] = "#######......#######.E........##".toCharArray();
        M[i++] = "#######..G..#########.........##".toCharArray();
        M[i++] = "######..#.G.#########G........##".toCharArray();
        M[i++] = "#####.......#########G...E.E...#".toCharArray();
        M[i++] = "#####.G.....#########....E.....#".toCharArray();
        M[i++] = "###...###...#########..E.......#".toCharArray();
        M[i++] = "####.###.....#######E....E...E##".toCharArray();
        M[i++] = "####.##.......#####....#.....###".toCharArray();
        M[i++] = "##..G.#..G............####....##".toCharArray();
        M[i++] = "##..............##########..E###".toCharArray();
        M[i++] = "#....#.G........#.##########.###".toCharArray();
        M[i++] = "#.........G.......##########.###".toCharArray();
        M[i++] = "##......GG##G.....##############".toCharArray();
        M[i++] = "#........#####....##############".toCharArray();
        M[i++] = "#..###.########...##############".toCharArray();
        M[i++] = "#..#############..##############".toCharArray();
        M[i++] = "##.#############################".toCharArray();
        M[i++] = "##.#############################".toCharArray();
        M[i] = "################################".toCharArray();
    }

    private void findUnits() {
        char goblin = 'a';
        char elve = 'F';

        for (int i = 0; i < M.length; i++) {
            for (int j = 0; j < M[i].length; j++) {
                if (M[i][j] == 'G') {
                    M[i][j] = goblin;
                    units.put(goblin++, new Unit(true, i, j));
                } else if (M[i][j] == 'E') {
                    M[i][j] = elve;
                    units.put(elve++, new Unit(false, i, j));
                }
            }
        }
    }

    private void printMap() {
        for (char[] chars : M) {
            for (char aChar : chars) {
                System.out.print(aChar);
            }
            System.out.println();
        }
    }


    public static void main(String[] args) {
        new Ac15().solve();
    }

    private void solve() {
        addInput();
        findUnits();
        resolveRound();
        printMap();

    }
}
