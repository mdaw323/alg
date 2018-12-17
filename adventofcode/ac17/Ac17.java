import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Ac17 {
    private byte[][] S = new byte[5000][5000];
    private int minY = Integer.MAX_VALUE, maxY = Integer.MIN_VALUE;
    private int minX = Integer.MAX_VALUE, maxX = Integer.MIN_VALUE;
    private int sumOfWater = 0;
    private int sumOfRest = 0;

    private Map<Byte, String> map = Map.of(
            SPACE, ".",
            ROCK, "#",
            UNKNOWN, "?",
            FLOW, "|",
            REST, "~"
            );

    private static final byte SPACE = 0;
    private static final byte ROCK = 1;
    private static final byte UNKNOWN = 2;
    private static final byte FLOW = 3;
    private static final byte REST = 4;


    public static void main(String[] args) {

        new Ac17().solve();

    }

    private void add(int x, int y) {
        if (y < minY) minY = y;
        if (y > maxY) maxY = y;
        if (x < minX) minX = x;
        if (x > maxX) maxX = x;

        S[x][y] = 1;

    }

    private void solve() {
        parseInput();
        deepSearch();

        printALL();

        System.out.println(sumOfWater);
        System.out.println(sumOfRest);
    }

    private void printALL() {
        for (int y = minY; y<=maxY; y++) {
            for (int x = minX ; x<=maxX; x++) {
                printSquare(x, y);
            }
            System.out.println();
        }
    }


    class Square {
        int x, y;

        Square(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    private void deepSearch() {
        Stack<Square> stack = new Stack<>();
        visitSquare(stack, 500,0);
        while (!stack.isEmpty()) {
            Square square = stack.peek();

            // idziemy w dół
            if (visitSquare(stack, square.x, square.y + 1)) {
                continue;
            }

            // jeśli w dół woda stoi to w lewo i prawo
            if (!canFlow(square.x, square.y + 1)) {
                if (visitSquare(stack, square.x - 1, square.y)) continue;
                if (visitSquare(stack, square.x + 1, square.y)) continue;
            }

            // jeśli nadal nie wiemy czy woda będzie stać to wyliczamy granice
            stack.pop();
            if (S[square.x][square.y] == UNKNOWN && checkIfLineCanBeSolved(square.x, square.y)) {
                boolean boundaries = checkLineBoundaries(square.x, square.y);
                markLineAs(square.x, square.y, boundaries ? REST : FLOW);
            }


        }
    }

    private boolean visitSquare(Stack<Square> stack, int x, int y) {
        if (y <= maxY && S[x][y] == SPACE) {
            S[x][y] = UNKNOWN;
            if (y >= minY) sumOfWater++;
            stack.push(new Square(x, y));
            return true;
        } else {
            return false;
        }
    }

    private boolean canFlow(int x, int y) {
        return S[x][y] != REST && S[x][y] != ROCK;
    }

    private void markLineAs(int x, int y, byte value) {
        int l = x;
        int r = x + 1;
        while (S[l][y] == UNKNOWN) {
            if (value == REST) sumOfRest ++;
            S[l--][y] = value;
        }
        while (S[r][y] == UNKNOWN) {
            if (value == REST) sumOfRest ++;
            S[r++][y] = value;
        }
    }


    private boolean checkLineBoundaries(int x, int y) {
        int l = x;
        while (S[l][y] == UNKNOWN) {
            if (canFlow(l, y + 1)) return false;
            l--;
        }

        if (canFlow(l, y)) {
            return false;
        }

        int r = x + 1;
        while (S[r][y] == UNKNOWN) {
            if (canFlow(r, y + 1)) return false;
            r++;
        }

        if (canFlow(r, y)) {
            return false;
        }

        return true;
    }

    private boolean checkIfLineCanBeSolved(int x, int y) {
        int l = x;
        while (S[l][y] == UNKNOWN) {
            l--;
        }

        if (S[l][y] == SPACE) {
            return false;
        }

        int r = x + 1;
        while (S[r][y] == UNKNOWN) {
            r++;
        }

        if (S[r][y] == SPACE) {
            return false;
        }

        return true;
    }


    private void parseInput() {
        Pattern pattern = Pattern.compile("(\\w)=(\\d+), \\w=(\\d+)\\.\\.(\\d+)");
        Scanner scanner = new Scanner(Ac13.class.getResourceAsStream("/a17_2.txt"));
        while (scanner.hasNext()) {
            Matcher matcher = pattern.matcher(scanner.nextLine());
            if (matcher.matches()) {
                int a = Integer.parseInt(matcher.group(2));
                int b = Integer.parseInt(matcher.group(3));
                int c = Integer.parseInt(matcher.group(4));
                if (matcher.group(1).equals("x")) {
                    for (int i = b; i <= c; i++) {
                        add(a, i);
                    }
                } else {
                    for (int i = b; i <= c; i++) {
                        add(i, a);
                    }
                }
            }
        }
    }

    private void printSquare(int x, int y) {
        System.out.printf("%s", map.get(S[x][y]));
    }

}
