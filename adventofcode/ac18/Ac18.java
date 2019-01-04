import java.util.Scanner;

public class Ac18 {
    private char[][] map = new char[52][52];

    private final char OPEN = '.';
    private final char TREE = '|';
    private final char LUMBERYARD = '#';

    int[] W = new int[]{177683, 176808, 176715, 177784, 182016, 182479, 188256, 194892, 199864, 206720, 210330, 212102, 212310,
            215306, 217260, 223468, 227744, 226338, 221697, 214775, 206150, 200326, 197380, 177364, 177834, 176960,
            176490, 174584};

    public static void main(String[] args) {

        new Ac18().solve();

    }

    private int count(int x, int y, char c) {
        int sum = 0;
        if (map[x + 1][y] == c) sum++;
        if (map[x + 1][y + 1] == c) sum++;
        if (map[x + 1][y - 1] == c) sum++;
        if (map[x][y - 1] == c) sum++;
        if (map[x][y + 1] == c) sum++;
        if (map[x - 1][y] == c) sum++;
        if (map[x - 1][y + 1] == c) sum++;
        if (map[x - 1][y - 1] == c) sum++;

        return sum;
    }

    private void transform() {
        char[][] nm = new char[52][52];
        for (int i = 0; i < map.length; i++) {
            for (int j = 0; j < map[i].length; j++) {
                if (map[i][j] == OPEN) {
                    nm[i][j] = count(i, j, TREE) >= 3 ? TREE : OPEN;
                } else if (map[i][j] == TREE) {
                    nm[i][j] = count(i, j, LUMBERYARD) >= 3 ? LUMBERYARD : TREE;
                } else if (map[i][j] == LUMBERYARD) {
                    nm[i][j] = count(i, j, LUMBERYARD) >= 1 && count(i, j, TREE) >= 1 ? LUMBERYARD : OPEN;
                }
            }
        }
        map = nm;
    }


    private void solve() {
        parseInput();
        int x = 1000000000;

        //for (int i = 0; i <x; i++) {
        //    transform();
        //}
        //countWoodValue();

        System.out.println(W[(x - 1000 - 1) % W.length]);


    }

    private void countWoodValue() {
        int lsum = 0, wsum = 0;
        for (int i = 0; i < map.length; i++) {
            for (int j = 0; j < map[i].length; j++) {
                if (map[i][j] == LUMBERYARD) lsum++;
                if (map[i][j] == TREE) wsum++;
            }
        }
        System.out.println(lsum * wsum);
    }


    private void parseInput() {

        Scanner scanner = new Scanner(Ac13.class.getResourceAsStream("/a18.txt"));
        int i = 0;
        while (scanner.hasNext()) {
            map[i++] = scanner.nextLine().toCharArray();
        }

    }


}
