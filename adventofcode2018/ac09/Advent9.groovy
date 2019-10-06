def players = 438
def last = 71626 * 100
def score = [0 as BigInteger] * players


class Node {
    Node next
    Node prev
    Integer value
}

Node game = new Node(value: 0)
game.next = game
game.prev = game

def m = 0

int p = 0
for (int i = 0; i < last; i++) {
//    println game
   /* if (i % 10000 == 0) {
        println i + " of " + last
    }*/
    m++
    p = (p + 1) % players
    if (m % 23 == 0) {
        7.times {
            game = game.prev
        }
        //pos = (pos - 7 + game.size()) % game.size()
        score[p] += m + game.value
        Node prev = game.prev
        Node next = game.next
        prev.next = next
        next.prev = prev
        game = next

    } else {
        game = game.next
        Node next = game.next
        Node n = new Node(value: m, prev: game, next: next)
        next.prev = n
        game.next = n
        game = n
    }
}
//println game
println score.max { it }