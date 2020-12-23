#include <iostream>
#include <string>
#include <vector>

using namespace std;

/*

lines = [x.strip() for x in fileinput.input()]
for line in lines:
    print(line)
    if ":" in line:
        ll, r = line.split(": ")
        ll = int(ll)
        if r == '"a"':
            M[ll] = 'a'
        elif r == '"b"':
            M[ll] = 'b'
        else:
            x = r.split("|")
            print(x)
            if (len(x)) == 2:
                a, b = x
                a = [int(s) for s in a.split()]
                b = [int(s) for s in b.split()]
                assert len(a) <= 3
                assert len(b) <= 3
                E[ll].append(a)
                E[ll].append(b)

            elif (len(x) == 1):
                a = [int(s) for s in x[0].split()]
                assert len(a) <= 3
                E[ll].append(a)
    else:
        if line:
            words.append(line)
# 0: 4 1 5
# 1: 2 3 | 3 2
# 2: 4 4 | 5 5
# 3: 4 5 | 5 4
# 4: "a"
# 5: "b"
*/

int main() {
    ios::sync_with_stdio(false);
    string line;
    int l;
    bool second = false;
    vector<string> words;
    vector<vector<vector<int>>> E(200, vector<vector<int>>());

    while (getline(cin, line)) {
        if (line == "") {
            second = true;
        } else if (second) {

            words.push_back(line);
        } else {
            int dw = line.find(':');
            int l = stoi(line.substr(0, dw));

            cout << l << line.substr(dw+2 , line.size()) << endl;

        }
    }
}
