import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.Set;
import java.util.function.ToIntFunction;

import static java.util.Set.of;

public class Ac24 {

    public static final int IMMUNE = 0;
    public static final int INFECTION = 1;

    public static final String RADIATION = "r";
    public static final String BLUDGEONING = "b";
    public static final String FIRE = "f";
    public static final String COLD = "c";
    public static final String SLASHING = "s";
    public static final String NO_SPECIAL = "n";

    List<Unit> allUnits = new ArrayList<>();
    List<Unit> infectionList = new ArrayList<>();
    List<Unit> immuneList = new ArrayList<>();
    int immuneGroup = 0;
    int infectionGroup = 0;
    int round = 1;


    class Unit {
        int type;
        int count;
        int hitpoints;
        Set<String> immunes;
        Set<String> weakness;
        int damage;
        String damageType;
        int initiative;


        Unit target = null;
        int group;

        boolean isATarget = false;

        public Unit(int type, int count, int hitpoints, Set<String> immunes, Set<String> weakness,
                    int damage, String damageType,
                    int initiative) {
            this.type = type;
            this.count = count;
            this.hitpoints = hitpoints;
            this.immunes = immunes;
            this.weakness = weakness;
            this.damage = damage;
            this.damageType = damageType;
            this.initiative = initiative;
            if (type == IMMUNE) {
                group = ++immuneGroup;
                immuneList.add(this);
            } else {
                group = ++infectionGroup;
                infectionList.add(this);
            }
            allUnits.add(this);
        }

        void selectTarget() {

            Optional<Unit> first = getEnemies().stream().filter(u -> !u.isATarget).min((o1, o2) -> {
                int hd = Integer.compare(o2.countDmg(damageType, getEffectivePower()), o1.countDmg(damageType,
                        getEffectivePower()));
                if (hd != 0) return hd;
                int ep = Integer.compare(o2.getEffectivePower(), o1.getEffectivePower());
                if (ep != 0) return ep;
                return Integer.compare(o2.initiative, o1.initiative);
            });
            first.ifPresent(unit -> {
                if (unit.countDmg(damageType, getEffectivePower()) > 0) {
//                    System.out.printf("%distance group %distance selected target group %distance\n", type, group, unit.group);
                    unit.isATarget = true;
                    target = unit;
                }
            });
        }

        List<Unit> getEnemies() {
            return type == IMMUNE ? infectionList : immuneList;
        }

        List<Unit> getFriends() {
            return type == IMMUNE ? immuneList : infectionList;
        }


        int getEffectivePower() {
            return count * damage;
        }

        int countDmg(String damageType, int dmg) {
            if (immunes.contains(damageType)) {
                return 0;
            } else if (weakness.contains(damageType)) {
                return dmg * 2;
            } else return dmg;
        }

        void receiveDamage(String damageType, int dmg) {
            int kills = countDmg(damageType, dmg) / hitpoints;
            if (kills >= count) {
//                System.out.println("killing ALL " + count + " units " + this.group + " of type " + this.type);
                count = 0;
                getFriends().remove(this);
                //allUnits.remove(this);
            } else {
//                System.out.println("killing " + kills + " units " + this.group + " of type " + this.type);
                count -= kills;
            }
        }

        void dealDamage() {
            if (target != null) {
//                System.out.printf("%distance group %distance dealing damage to %distance type %s power %distance\n", type, group, target.group,
//                        damageType, getEffectivePower());
                target.receiveDamage(damageType, getEffectivePower());
            }
        }

        @Override public String toString() {
            return "Unit{" +
                    "type=" + type +
                    ", count=" + count +
                    ", hitpoints=" + hitpoints +
                    ", immunes=" + immunes +
                    ", weakness=" + weakness +
                    ", damage=" + damage +
                    ", damageType='" + damageType + '\'' +
                    ", initiative=" + initiative +
                    ", target=" + (target != null ? target.group : null) +
                    ", group=" + group +
                    ", isATarget=" + isATarget +
                    '}';
        }
    }

    private void doRound() {
        round++;
        allUnits.forEach(unit -> unit.target = null);
        allUnits.forEach(unit -> unit.isATarget = false);
        allUnits.sort((o1, o2) -> {
                    int ep = Integer.compare(o2.getEffectivePower(), o1.getEffectivePower());
                    if (ep != 0) return ep;
                    return Integer.compare(o2.initiative, o1.initiative);
                }
        );
        for (Unit allUnit : allUnits) {
            allUnit.selectTarget();
        }

        allUnits.sort((o1, o2) -> Integer.compare(o2.initiative, o1.initiative));

        for (Unit allUnit : allUnits) {
            if (allUnit.count > 0) {
                allUnit.dealDamage();
            }
        }

        /*for (Unit allUnit : allUnits) {
            System.out.println(allUnit);
        }*/
    }


    private void solve() {
        for (int i = 0 ; i< 1000; i++) {
            System.out.println("boost " + i);
            parseInput(i);
            while (!infectionList.isEmpty() && !immuneList.isEmpty() && round < 100000) {
                doRound();
            }
            if (infectionList.isEmpty()) {
                System.out.println(allUnits.stream().mapToInt(value -> value.count).sum());
                return;
            }
        }
    }


    private void parseInput(int immuneBoost) {

        allUnits = new ArrayList<>();
        infectionList = new ArrayList<>();
        immuneList = new ArrayList<>();
        immuneGroup = 0;
        infectionGroup = 0;
        round = 1;


//        new Unit(IMMUNE, 17, 5390, of(), of(RADIATION, BLUDGEONING), 4507, FIRE, 2);
//        new Unit(IMMUNE, 989, 1274, of(FIRE), of(BLUDGEONING, SLASHING), 25, SLASHING, 3);

//        new Unit(INFECTION, 801, 4706, of(FIRE), of(RADIATION), 116, BLUDGEONING, 1);
//        new Unit(INFECTION, 4485, 2961, of(RADIATION), of(FIRE, COLD), 12, SLASHING, 4);
        new Unit(IMMUNE, 1614, 8016, of(SLASHING), of(RADIATION), 48 + immuneBoost, FIRE, 9);
        new Unit(IMMUNE, 3730, 5611, of(BLUDGEONING), of(FIRE), 14 + immuneBoost, RADIATION, 16);
        new Unit(IMMUNE, 1627, 9770, of(), of(COLD), 55 + immuneBoost, FIRE, 3);
        new Unit(IMMUNE, 4665, 9782, of(), of(FIRE), 18 + immuneBoost, RADIATION, 10);
        new Unit(IMMUNE, 281, 5764, of(FIRE), of(RADIATION), 187 + immuneBoost, SLASHING, 19);
        new Unit(IMMUNE, 524, 9344, of(), of(), 158 + immuneBoost, COLD, 15);
        new Unit(IMMUNE, 5013, 9768, of(), of(), 15 + immuneBoost, COLD, 14);
        new Unit(IMMUNE, 1143, 1822, of(), of(RADIATION), 15 + immuneBoost, FIRE, 18);
        new Unit(IMMUNE, 136, 6830, of(), of(RADIATION), 420 + immuneBoost, SLASHING, 7);
        new Unit(IMMUNE, 665, 7973, of(SLASHING), of(BLUDGEONING), 119 + immuneBoost, FIRE, 11);
        new Unit(INFECTION, 515, 8712, of(RADIATION), of(SLASHING, FIRE), 30, COLD, 1);
        new Unit(INFECTION, 5542, 56769, of(), of(), 16, BLUDGEONING, 4);
        new Unit(INFECTION, 1663, 10437, of(SLASHING, FIRE, RADIATION), of(), 12, RADIATION, 12);
        new Unit(INFECTION, 574, 50124, of(), of(SLASHING, RADIATION), 171, FIRE, 8);
        new Unit(INFECTION, 1190, 10652, of(), of(), 16, COLD, 17);
        new Unit(INFECTION, 3446, 23450, of(), of(), 12, FIRE, 5);
        new Unit(INFECTION, 5887, 14556, of(), of(SLASHING), 4, RADIATION, 2);
        new Unit(INFECTION, 1761, 41839, of(), of(COLD), 35, COLD, 20);
        new Unit(INFECTION, 4194, 16090, of(FIRE), of(SLASHING), 6, FIRE, 6);
        new Unit(INFECTION, 2127, 27065, of(), of(COLD, SLASHING), 24, SLASHING, 13);


    }


    public static void main(String[] args) {
        new Ac24().solve();
    }
}
