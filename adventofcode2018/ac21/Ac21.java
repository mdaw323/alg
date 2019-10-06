import java.util.Scanner;

public class Ac21 {
    private char[][] map = new char[52][52];


    private void solve() {

        int sum = 0;
        for (int i = 1; i<= 10551340; i++) {
            if (10551340 % i  == 0) {
                sum += i;
            }
        }
        System.out.println(sum);
    }




    public static void main(String[] args) {
        new Ac21().solve();
    }

}
