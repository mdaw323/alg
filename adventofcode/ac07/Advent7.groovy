import com.sun.corba.se.spi.orbutil.threadpool.Work

String input = '''Step X must be finished before step Q can begin.
Step Y must be finished before step P can begin.
Step U must be finished before step F can begin.
Step V must be finished before step S can begin.
Step G must be finished before step R can begin.
Step T must be finished before step P can begin.
Step O must be finished before step D can begin.
Step R must be finished before step I can begin.
Step M must be finished before step F can begin.
Step L must be finished before step C can begin.
Step K must be finished before step H can begin.
Step D must be finished before step H can begin.
Step I must be finished before step W can begin.
Step S must be finished before step C can begin.
Step J must be finished before step Z can begin.
Step B must be finished before step A can begin.
Step A must be finished before step W can begin.
Step W must be finished before step F can begin.
Step P must be finished before step E can begin.
Step C must be finished before step Q can begin.
Step E must be finished before step Z can begin.
Step Q must be finished before step F can begin.
Step Z must be finished before step F can begin.
Step N must be finished before step H can begin.
Step H must be finished before step F can begin.
Step N must be finished before step F can begin.
Step K must be finished before step D can begin.
Step P must be finished before step F can begin.
Step Q must be finished before step Z can begin.
Step G must be finished before step W can begin.
Step E must be finished before step N can begin.
Step R must be finished before step Z can begin.
Step V must be finished before step R can begin.
Step Q must be finished before step N can begin.
Step U must be finished before step L can begin.
Step P must be finished before step N can begin.
Step S must be finished before step Q can begin.
Step G must be finished before step S can begin.
Step U must be finished before step E can begin.
Step M must be finished before step I can begin.
Step A must be finished before step N can begin.
Step W must be finished before step H can begin.
Step J must be finished before step A can begin.
Step M must be finished before step S can begin.
Step T must be finished before step I can begin.
Step E must be finished before step Q can begin.
Step C must be finished before step Z can begin.
Step B must be finished before step H can begin.
Step J must be finished before step F can begin.
Step G must be finished before step E can begin.
Step Q must be finished before step H can begin.
Step T must be finished before step B can begin.
Step V must be finished before step B can begin.
Step R must be finished before step F can begin.
Step V must be finished before step H can begin.
Step K must be finished before step N can begin.
Step A must be finished before step H can begin.
Step S must be finished before step E can begin.
Step I must be finished before step N can begin.
Step V must be finished before step I can begin.
Step M must be finished before step E can begin.
Step U must be finished before step G can begin.
Step J must be finished before step N can begin.
Step T must be finished before step K can begin.
Step D must be finished before step N can begin.
Step L must be finished before step S can begin.
Step P must be finished before step Z can begin.
Step X must be finished before step S can begin.
Step B must be finished before step W can begin.
Step R must be finished before step M can begin.
Step W must be finished before step Q can begin.
Step A must be finished before step Z can begin.
Step A must be finished before step F can begin.
Step G must be finished before step T can begin.
Step S must be finished before step A can begin.
Step J must be finished before step E can begin.
Step Y must be finished before step N can begin.
Step D must be finished before step J can begin.
Step D must be finished before step S can begin.
Step M must be finished before step W can begin.
Step U must be finished before step T can begin.
Step E must be finished before step H can begin.
Step S must be finished before step W can begin.
Step T must be finished before step C can begin.
Step A must be finished before step P can begin.
Step U must be finished before step V can begin.
Step U must be finished before step J can begin.
Step L must be finished before step B can begin.
Step L must be finished before step N can begin.
Step J must be finished before step C can begin.
Step L must be finished before step Q can begin.
Step K must be finished before step B can begin.
Step G must be finished before step H can begin.
Step W must be finished before step Z can begin.
Step C must be finished before step E can begin.
Step B must be finished before step Q can begin.
Step O must be finished before step Z can begin.
Step L must be finished before step J can begin.
Step R must be finished before step N can begin.
Step J must be finished before step P can begin.
Step Y must be finished before step F can begin.
'''

Map<String, List<String>> graph = new HashMap<>()

input.split("\n").each {
    def split = it.split(" ")
    def a = split[1], b = split[7]
    graph.putIfAbsent(a, [])
    graph.putIfAbsent(b, [])
    graph.get(a).add(b)
}


//while (!graph.isEmpty()) {
int d = graph.size()
class Work {
    String name
    int time = 0

    @Override
    public String toString() {
        return "Work{" +
                "name='" + name + '\'' +
                ", time=" + time +
                '}';
    }
}


List<Work> tasks = []


int time = 0
while (graph.size()> 0) {
//    println graph
    Map<String, Integer> s = new HashMap<>()

    for (String keys : graph.keySet()) {
        s.put(keys, 0)
    }

    graph.values().flatten().each { a -> s.put(a as String, s.get(a) + 1) }
    def minkeys = s.findAll { k, v -> v == 0 && !tasks.find{it.name == k} }.collect { it.key }.sort {it}
    minkeys.take(5-tasks.size()).each {tasks.add(new Work(name: it, time: 61 + (it.toCharacter() - 'A'.toCharacter())))}
    tasks.sort {it.time}

    def elapsed = tasks.first().time
    time += elapsed
    tasks.each {it.time -= elapsed}

//    println tasks
    tasks.findAll{it.time == 0}.each {graph.remove(it.name)}
    tasks = tasks.findAll{it.time > 0}
    println tasks

}

println tasks
println time
//println graph

