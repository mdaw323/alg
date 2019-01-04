import java.util.*;
import java.util.stream.Collectors;

public class Ac15 {

    class ElveDiedException extends RuntimeException {

    }

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

        Optional<Unit> findEnemyToShoot() {
            Point p = new Point(x, y, -1);
            return p.getNeighbours()
                    .stream()
                    .filter(point -> point.isEnemyFor(this))
                    .map(point -> units.get(M[point.x][point.y]))
                    .min((u1, u2) -> {
                        int hpCompare = Integer.compare(u1.hp, u2.hp);
                        return hpCompare == 0 ? UNIT_COMPARATOR.compare(u1, u2) : hpCompare;
                    });
        }

        @Override public String toString() {
            return "Unit{" +
                    "isGoblin=" + isGoblin +
                    ", x=" + x +
                    ", y=" + y +
                    ", hp=" + hp +
                    '}';
        }

        void takeDamage() {
            int dmg = 3;
            if (isGoblin) dmg += elveHandicap;
            hp = Math.max(hp - dmg, 0);
            if (hp == 0) {
                if (!isGoblin) {
                    throw new ElveDiedException();
                }
                System.out.println("unit destroyed " + this);
                units.remove(M[x][y]);
                M[x][y] = '.';
            }
        }
    }

    private static Comparator<Unit> UNIT_COMPARATOR = (o1, o2) -> o1.y == o2.y ? Integer.compare(o1.x, o2.x) :
            Integer.compare(o1.y, o2.y);

    public static final int M_X = 32;
    public static final int M_Y = 32;
    char[][] M = new char[M_X][M_Y];
    Map<Character, Unit> units = new HashMap<>();
    private int round = 0;
    int elveHandicap = 1;


    public void resolveRound() {
        round++;
        List<Unit> sortedUnits = units.values().stream()
                .sorted(UNIT_COMPARATOR).collect(Collectors.toList());
        for (Unit sortedUnit : sortedUnits) {
            if (sortedUnit.hp > 0) {
                resolveUnitRound(sortedUnit);
            }
        }
    }

    class Point {
        int x, y, distance = -1;

        public Point(int x, int y, int distance) {
            this.x = x;
            this.y = y;
            this.distance = distance;
        }

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

        boolean isEmpty() {
            return M[x][y] == '.';
        }

        boolean isGoblin() {
            return M[x][y] >= 'a' && M[x][y] <= 'z';
        }

        boolean isElve() {
            return M[x][y] >= 'A' && M[x][y] <= 'Z';
        }

        boolean isEnemyFor(Unit unit) {
            return unit.isGoblin && isElve() || (!unit.isGoblin && isGoblin());
        }

        List<Point> getNeighbours() {
            return Arrays.asList(
                    new Point(x + 1, y, distance + 1),
                    new Point(x - 1, y, distance + 1),
                    new Point(x, y + 1, distance + 1),
                    new Point(x, y - 1, distance + 1)

            );
        }

        List<Point> getEmptyOrEnemyNeighbours(final Unit unit) {
            return getNeighbours()
                    .stream()
                    .filter(point -> point.isEnemyFor(unit) || point.isEmpty())
                    .collect(Collectors.toList());
        }

        @Override public String toString() {
            return "Point{" +
                    "x=" + x +
                    ", y=" + y +
                    ", distance=" + distance +
                    '}';
        }
    }

    class NearestEnemies {
        List<Unit> enemies;
        int distance;
        Point enemyApproachPoint;

        public NearestEnemies(List<Unit> enemies, int distance) {
            this.enemies = enemies;
            this.distance = distance;
        }

        Unit getFirstEnemy() {
            if (enemies.size() > 0) {
                enemies.sort(UNIT_COMPARATOR);
                return enemies.get(0);
            }
            throw new IllegalArgumentException("no enemies?");
        }
    }

    public NearestEnemies searchNearestEnemies(Unit unit) {
        int[][] d = createDistanceMatrix();
        Set<Point> visited = new HashSet<>();
        Queue<Point> q = new LinkedList<>();
        Point startingPoint = new Point(unit.x, unit.y, 0);
        q.offer(startingPoint);
        visited.add(startingPoint);
        d[startingPoint.x][startingPoint.y] = 0;

        int enemyDistance = Integer.MAX_VALUE;
        List<Unit> enemies = new ArrayList<>();
        while (!q.isEmpty()) {
            Point p = q.poll();
            if (p.distance + 1 > enemyDistance)
                break;
            for (Point neighbour : p.getEmptyOrEnemyNeighbours(unit)) {
                if (!visited.contains(neighbour)) {
                    if (neighbour.isEnemyFor(unit)) {
                        enemyDistance = p.distance + 1;
                        enemies.add(units.get(M[neighbour.x][neighbour.y]));
                    }
                    q.offer(neighbour);
                    visited.add(neighbour);
                    d[neighbour.x][neighbour.y] = p.distance + 1;
                    neighbour.distance = p.distance + 1;
                }
            }
        }
        NearestEnemies nearestEnemies = new NearestEnemies(enemies, enemyDistance);
        if (enemies.size() > 0 && enemyDistance > 1) {
            Unit e = nearestEnemies.getFirstEnemy();
            if (d[e.x][e.y - 1] == enemyDistance - 1) {
                nearestEnemies.enemyApproachPoint = new Point(e.x, e.y - 1, enemyDistance - 1);
            } else if (d[e.x - 1][e.y] == enemyDistance - 1) {
                nearestEnemies.enemyApproachPoint = new Point(e.x - 1, e.y, enemyDistance - 1);
            } else if (d[e.x + 1][e.y] == enemyDistance - 1) {
                nearestEnemies.enemyApproachPoint = new Point(e.x + 1, e.y, enemyDistance - 1);
            } else if (d[e.x][e.y + 1] == enemyDistance - 1) {
                nearestEnemies.enemyApproachPoint = new Point(e.x, e.y + 1, enemyDistance - 1);
            } else {
                throw new IllegalStateException("bug?");
            }
        }

        return nearestEnemies;
    }

    private int[][] createDistanceMatrix() {
        int[][] d = new int[M_X][M_Y];
        for (int x = 0; x < M_X; x++) {
            Arrays.fill(d[x], Integer.MAX_VALUE);
        }
        return d;
    }

    private Point findSquareToMoveFrom(Unit source, Unit destination, Point aproachPoint) {
        int[][] d = createDistanceMatrix();
        Map<List<Integer>, Point> visited = new HashMap<>();
        Queue<Point> q = new LinkedList<>();
        Point startingPoint = new Point(aproachPoint.x, aproachPoint.y, 0);
        q.offer(startingPoint);
        visited.put(Arrays.asList(startingPoint.x, startingPoint.y), startingPoint);
        d[startingPoint.x][startingPoint.y] = 0;

        int expectedDistance = Integer.MAX_VALUE;
        while (!q.isEmpty() && expectedDistance == Integer.MAX_VALUE) {
            Point p = q.poll();
            for (Point neighbour : p.getEmptyOrEnemyNeighbours(destination)) {
                if (!visited.containsKey(Arrays.asList(neighbour.x, neighbour.y))) {
                    if (neighbour.x == source.x && neighbour.y == source.y) {
                        expectedDistance = p.distance;
                        break;
                    }
                    if (neighbour.isEmpty()) {
                        q.offer(neighbour);
                        visited.put(Arrays.asList(neighbour.x, neighbour.y), neighbour);
                        neighbour.distance = p.distance + 1;
                        d[neighbour.x][neighbour.y] = p.distance + 1;
                    }
                }
            }
        }

        if (d[source.x][source.y - 1] == expectedDistance) {
            return new Point(source.x, source.y - 1, expectedDistance);
        } else if (d[source.x - 1][source.y] == expectedDistance) {
            return new Point(source.x - 1, source.y, expectedDistance);
        } else if (d[source.x + 1][source.y] == expectedDistance) {
            return new Point(source.x + 1, source.y, expectedDistance);
        } else if (d[source.x][source.y + 1] == expectedDistance) {
            return new Point(source.x, source.y + 1, expectedDistance);
        } else {
            throw new IllegalStateException("bug?");
        }

    }

    public void resolveUnitRound(Unit unit) {
//        System.out.println("resoulve for " + unit);
        NearestEnemies nearestEnemies = searchNearestEnemies(unit);
        if (nearestEnemies.enemies.size() > 0 && nearestEnemies.distance > 1) {
            Unit enemy = nearestEnemies.getFirstEnemy();
            Point pointToMove = findSquareToMoveFrom(unit, enemy, nearestEnemies.enemyApproachPoint);
            //move
            Character c = M[unit.x][unit.y];
            M[unit.x][unit.y] = '.';
            unit.x = pointToMove.x;
            unit.y = pointToMove.y;
            M[unit.x][unit.y] = c;

        }

        unit.findEnemyToShoot().ifPresent(Unit::takeDamage);

    }


    private void addInput() {
        Scanner scanner = new Scanner(Ac15.class.getResourceAsStream("/a15.txt"));
        int y = 0;
        while (scanner.hasNext()) {
            String line = scanner.nextLine();
            for (int x = 0; x < line.length(); x++) {
                M[x][y] = line.charAt(x);
            }
            y++;
        }

    }

    private void findUnits() {
        char goblin = 'a';
        char elve = 'F';

        for (int y = 0; y < M.length; y++) {
            for (int x = 0; x < M[y].length; x++) {
                if (M[x][y] == 'G') {
                    M[x][y] = goblin;
                    units.put(goblin++, new Unit(true, x, y));
                } else if (M[x][y] == 'E') {
                    M[x][y] = elve;
                    units.put(elve++, new Unit(false, x, y));
                }
            }
        }
    }

    private void printMap() {
        System.out.println("round " + round);
        for (int y = 0; y < M_Y; y++) {
            for (int x = 0; x < M_X; x++) {
                System.out.print(M[x][y]);
            }
            System.out.println();
        }
    }


    public static void main(String[] args) {
        new Ac15().solve();
    }

    private void solve() {
        boolean solved = false;

        while (!solved) {
            try {
                round = 0;
                M = new char[M_X][M_Y];
                units = new HashMap<>();

                addInput();
                findUnits();
                printMap();
                for (int i = 0; i < 10000; i++) {
                    resolveRound();
                    long goblinsCount = units.values().stream().filter(u -> u.isGoblin).count();
                    long elvesCount = units.values().stream().filter(u -> !u.isGoblin).count();
                    if (goblinsCount == 0 || elvesCount == 0) {
                        break;
                    }
                }
                solved = true;
            } catch (ElveDiedException e) {
                elveHandicap++;
            }
        }

        printMap();
        int sum = units.values().stream().mapToInt(u -> u.hp).sum();
        System.out.println(sum);
        System.out.println(sum * (round));
    }
}
