#include <bits/stdc++.h>
#include <string>
using namespace std;

int main ()
{
    int d;
    vector<int> P;
    vector<double> V;
    cin >> d;
    string line;
    while (d--)
    {
        P.clear();
        V.clear();
        getline(cin, line);
        getline(cin, line);

        cout << "a line: " << line << endl;
        int n = 0;
        for (auto c : line)
        {
            if (c==' ') {
                P.push_back(n);
                n = 0;
            }
            else
            {
                n = 10*n + (c - '0');
            }
        }
        P.push_back(n);
        for (auto i : P) cout << i << " ";
        cout << endl;


        cout << endl;
        getline(cin, line);
        cout << line << endl;
    }
    return 0;
}
