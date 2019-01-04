import java.util.*;

public class Ac23 {
    private List<Nanobot> nanobots = new ArrayList<>();

    private Long[][] R_EQ_3 = new Long[][]{
            {1L, 1L, 1L},
            {1L, 1L, -1L},
            {1L, -1L, 1L},
            {1L, -1L, -1L},
            {-1L, 1L, 1L},
            {-1L, 1L, -1L},
            {-1L, -1L, 1L},
            {-1L, -1L, -1L},
    };

    private Long[][] R_LESS_3 = new Long[][]{
            {0L, 0L, 0L},

            {1L, 0L, 0L},
            {0L, 1L, 0L},
            {0L, 0L, 1L},
            {-1L, 0L, 0L},
            {0L, -1L, 0L},
            {0L, 0L, -1L},

            {1L, 1L, 0L},
            {-1L, 1L, 0L},
            {1L, -1L, 0L},
            {0L, 1L, 1L},
            {0L, -1L, 1L},
            {0L, 1L, -1L},
            {1L, 0L, 1L},
            {-1L, 0L, 1L},
            {1L, 0L, -1L},
    };

    class Nanobot {
        long x, y, z, r;
        int intersects = 0;

        Nanobot(long x, long y, long z, long r) {
            this.x = x;
            this.y = y;
            this.z = z;
            this.r = r;
        }

        Long distanceToNanobot(Nanobot b) {
            return Math.abs(x - b.x) + Math.abs(y - b.y) + Math.abs(z - b.z);
        }

    }

    class Cube {
        Long x, y, z, r;
        Long inCubeRange = 0L;
        Long inRange = 0L;

        Cube(Long x, Long y, Long z, Long r) {
            this.x = x;
            this.y = y;
            this.z = z;
            this.r = r;
            countInside();
        }

        void countInside() {
            for (Nanobot b : nanobots) {
                long len = distanceToNanobot(b);
                if (len <= b.r) {
                    inRange++;
                }
                if (len <= 3 * r + b.r) {
                    inCubeRange++;
                }
            }
        }

        List<Cube> splitOctaTree() {
            long nr = r / 2;
            List<Cube> result = new ArrayList<>();
            if (nr > 0) {
                for (Long[] s : R_EQ_3) {
                    Cube e = new Cube(x + nr * s[0], y + nr * s[1], z + nr * s[2], nr);
                    result.add(e);
                }
            } else {
                for (Long[] s : R_LESS_3) {
                    Cube e = new Cube(x + s[0], y + s[1], z + s[2], nr);
                    result.add(e);
                }
            }
            return result;
        }

        Long distanceToZero() {
            return Math.abs(x) + Math.abs(y) + Math.abs(z);
        }
        Long distanceToNanobot(Nanobot b) {
            return Math.abs(x - b.x) + Math.abs(y - b.y) + Math.abs(z - b.z);
        }

        @Override public String toString() {
            return "Cube{" +
                    "x=" + x +
                    ", y=" + y +
                    ", z=" + z +
                    ", r=" + r +
                    ", inCubeRange=" + inCubeRange +
                    ", inRange=" + inRange +
                    '}';
        }
    }

    private void solve() {
        parseInput();
        solvePart2();
        solvePart1();
    }

    private void parseInput() {
        Scanner scanner = new Scanner(Ac13.class.getResourceAsStream("/a23.txt"));
        while (scanner.hasNext()) {
            nanobots.add(new Nanobot(scanner.nextInt(), scanner.nextInt(), scanner.nextInt(),
                    scanner.nextInt()));
        }
    }

    private void solvePart2() {
        int iter = 0;

        PriorityQueue<Cube> cubePriorityQueue = new PriorityQueue<>((o1, o2) -> {
            int inRangeCompare = Long.compare(o2.inRange, o1.inRange);
            int rCompare = Long.compare(o2.r, o1.r);
            return inRangeCompare != 0 ? inRangeCompare
                    : rCompare != 0 ? rCompare : Long.compare(o1.distanceToZero(), o2.distanceToZero());
        });

        Cube startingCube = new Cube(0L, 0L, 0L, 1L << 30);
        cubePriorityQueue.offer(startingCube);

        List<Cube> bestFounds = new ArrayList<>(Collections.singletonList(startingCube));
        Long bestRange = startingCube.inRange;

        while (!cubePriorityQueue.isEmpty()) {
            Cube cube = cubePriorityQueue.poll();
            while (cube.inCubeRange < bestRange && !cubePriorityQueue.isEmpty()) {
                cube = cubePriorityQueue.poll();
            }

            if (++iter % 100000 == 0) { //DEBUG jeśli zbyt długo trwa
                System.out.printf("it :%d\t queue_size: %d\t current cube r: %d\t inrange: %d\t inCubeRange:%d \tbestFounds was: %d\n",
                        iter, cubePriorityQueue.size(), cube.r, cube.inRange, cube.inCubeRange, bestRange);
            }

            if (cube.inCubeRange >= bestRange) {
                List<Cube> octaTree = cube.splitOctaTree();
                for (Cube splitCube : octaTree) {
                    if (splitCube.inRange <= splitCube.inCubeRange && cube.inCubeRange > bestRange) {
                        cubePriorityQueue.offer(splitCube);
                    }
                }
            }

            if (cube.inRange > bestRange) {
                bestFounds = new ArrayList<>(Collections.singletonList(cube));
                bestRange = cube.inRange;
                System.out.println("found better cube: " + bestFounds);
            } else if (cube.inRange.equals(bestRange)) {
                bestFounds.add(cube);
            }
        }

        System.out.println("bestFounds range was:" + bestRange);
        System.out.println("part2: " + bestFounds.stream().mapToLong(Cube::distanceToZero).min().orElse(-1L));
    }

    private void solvePart1() {
        nanobots.sort((o1, o2) -> -Long.compare(o1.r, o2.r));
        for (Nanobot largest : nanobots) {
            long count = nanobots.stream().filter(nanobot -> nanobot.distanceToNanobot(largest) <= largest.r).count();
            largest.intersects = (int) count;
        }

        System.out.println("part1: " +
                nanobots.stream().max(Comparator.comparingLong(o -> o.r)).map(n -> n.intersects).orElse(-1));
    }

    public static void main(String[] args) {
        new Ac23().solve();
    }
}
