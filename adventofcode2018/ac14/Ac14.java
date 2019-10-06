public class Ac14 {

    public static void main(String[] args) {
        StringBuilder recipes = new StringBuilder();
        int k = 0, l = 1;
        recipes.append(3);
        recipes.append(7);
        int q = 990941;
        for (int j = 0; j < 30000000; j++) {
            int s = (recipes.charAt(k) - '0') + (recipes.charAt(l) - '0');
            if (s >= 10) {
                recipes.append(1);
            }
            recipes.append(s % 10);

            k = (k + recipes.charAt(k) - '0' + 1) % recipes.length();
            l = (l + recipes.charAt(l) - '0' + 1) % recipes.length();
        }
        System.out.println(recipes.indexOf(Integer.toString(q)));
    }
}
