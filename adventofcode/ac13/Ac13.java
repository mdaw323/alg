import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

public class Ac13 {

    static final int R = 0;
    static final int U = 1;
    static final int L = 2;
    static final int D = 3;

    private int cornerDirection(int directionFrom, char corner) {
        int r = directionFrom;
        if (directionFrom == R && corner == '\\') r--;
        if (directionFrom == R && corner == '/') r++;

        if (directionFrom == L && corner == '\\') r--;
        if (directionFrom == L && corner == '/') r++;

        if (directionFrom == U && corner == '\\') r++;
        if (directionFrom == U && corner == '/') r--;

        if (directionFrom == D && corner == '\\') r++;
        if (directionFrom == D && corner == '/') r--;
        if (directionFrom == r) throw new IllegalArgumentException("" + directionFrom + " " + corner);
        return (r + 4) % 4;
    }

    private boolean isCorner(char c) {
        return c == '\\' || c == '/';
    }

    private boolean isIntersection(char c) {
        return c == '+';
    }

    private boolean isCrash(char c) {
        return c == 'X';
    }

    private boolean isNormal(char c) {
        return c == '-' || c == '|';
    }

    private int intersection(int directionFrom, int d) {
        return (directionFrom - (d - 1) + 4) % 4;
    }



    class Mine {
        public Mine(int x, int y, int direction) {
            this.x = x;
            this.y = y;
            this.direction = direction;
            pos = direction == L || direction == R ? '-' : '|';

        }

        int x, y;
        int direction;
        char pos;
        int intersection = 0;
        boolean removed = false;

        private String dir() {
            if (direction == U) return "^";
            if (direction == D) return "v";
            if (direction == L ) return "<";
            return ">";
         }

        public int nx() {
            return direction == L || direction == R ? x : direction == U ? x - 1 : x + 1;
        }

        public int ny() {
            return direction == U || direction == D ? y : direction == L ? y - 1 : y + 1;
        }

        @Override public String toString() {
            return "Mine{" +
                    "x=" + x +
                    ", y=" + y +
                    ", direction=" + dir() +" "+ direction +
                    ", pos=" + pos +
                    ", intersection=" + intersection +
                    '}';
        }
    }

    private void solve() {

        Scanner scanner = new Scanner(Ac13.class.getResourceAsStream("/input.txt"));
        char[][] chars = new char[150][150];

        List<Mine> mines = new ArrayList<>();

        int x = 0;
        while (scanner.hasNext()) {
            chars[x++] = scanner.nextLine().toCharArray();
        }

        for (int i = 0; i < chars.length; i++) {
            for (int j = 0; j < chars[i].length; j++) {
                switch (chars[i][j]) {
                    case '<':
                        mines.add(new Mine(i, j, L));
                        chars[i][j] = 'X';
                        break;
                    case '>':
                        mines.add(new Mine(i, j, R));
                        chars[i][j] = 'X';
                        break;
                    case '^':
                        mines.add(new Mine(i, j, U));
                        chars[i][j] = 'X';
                        break;
                    case 'v':
                        mines.add(new Mine(i, j, D));
                        chars[i][j] = 'X';
                        break;

                }

            }

        }


        while (mines.size() > 1) {

            mines.sort((a, b) -> a.x == b.x ? Integer.compare(a.y, b.y) : Integer.compare(a.x, b.x));
//        Mine mine = mines.get(0);
            for (Mine mine : mines) {
//        for (int i = 0; i <= 50; i++) {
//                System.out.println(mine);
//                print(chars);
                if (mine.removed) continue;
                int nx = mine.nx();
                int ny = mine.ny();
                char nc = chars[nx][ny];
                if (isCrash(nc)) {
//                    System.out.println(ny + "," + nx);
                    for (Mine mine1 : mines) {
                        if (mine1.x == nx && mine1.y == ny) {
                            mine1.removed = true;
                            chars[mine1.x][mine1.y] = mine1.pos;
                        }
                    }
                    chars[mine.x][mine.y] = mine.pos;
                    mine.pos = chars[nx][ny];
                    mine.removed = true;
                    continue;

                } else if (isCorner(nc)) {
                    mine.direction = cornerDirection(mine.direction, nc);
                } else if (isNormal(nc)) {

                } else if (isIntersection(nc)) {
                    mine.direction = intersection(mine.direction, mine.intersection);
                    mine.intersection = (mine.intersection + 1) % 3;
                } else {
                    System.out.println("invalid");
                    return;
                }
                if (!mine.removed) {
                    chars[mine.x][mine.y] = mine.pos;
                    mine.pos = chars[nx][ny];
                    chars[nx][ny] = 'X';
                    mine.x = nx;
                    mine.y = ny;
                }
            }
            mines = mines.stream().filter(m -> !m.removed).collect(Collectors.toList());

        }


//        System.out.println(mines.size());

        System.out.println(mines);


    }

    private void print(char[][] c) {
        for (char[] chars : c) {
            for (char aChar : chars) {
                System.out.print(aChar);
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        try {
            new Ac13().solve();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
