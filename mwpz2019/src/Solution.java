import java.util.*;

class Solution {
    public static final int MAX = 25000;

    static int[] F = new int[2 * 5000000 + 5];

    static long[] GG = new long[25000];
    public static void solve(long b, int n, long m) {

        List<List<Integer>> G = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            G.add(new ArrayList<>());
        }

        F[0] = F[1] = 1;
        for (int i = 2; i <= 2 * m; i++) {
            F[i] = (int) ((F[i - 1] + F[i - 2] + b) % n);
        }

        for (int i = 1; i <= m; i++) {
            int aa = F[2 * i - 1];
            int bb = F[2 * i];
            if (aa != bb) {
                G.get(aa).add(bb);
                G.get(bb).add(aa);
            } else {
                G.get(aa).add(aa);
            }

        }




        for (int i = 0; i < n; i++) {
            for (int j = 0; j< n; j++) {
                GG[j] = 0;
            }
            for (Integer nb : G.get(i)) {
                GG[nb]++;
            }

            int k = 1;
            long s = 0;
            for (int j = 0; j<n; j++) {
                s += j * ((k + k + GG[j] - 1)* GG[j] / 2) ;
                k += GG[j];
            }

            System.out.print(s + " ");

        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int d = scanner.nextInt();
        for (int i = 0 ; i< d; i++) {
            long b = scanner.nextLong();
            int n = scanner.nextInt();
            long m = scanner.nextLong();
            solve(b, n, m);
            System.out.println();
        }
    }
}
