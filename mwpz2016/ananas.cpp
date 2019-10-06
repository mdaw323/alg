#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

string build_palindrome(string s, unsigned int length) {
     string palindrome_half = s.substr(0, length);
     reverse(palindrome_half.begin(), palindrome_half.end());
     return s + palindrome_half;
}

int main() {
    int D;    
    cin >> D;
    string s;
    while (D--) {
        cin >> s;
        
        unsigned int hl = (s.length()+1)/2; //dlugosc polowki (123)45 , (12)34
        unsigned int pl = s.length()/2;  //dlugosc czesci palindromu do powtorzenia (12)345, (12)34 
        string half = s.substr(0, hl);        
        string palindrome = build_palindrome(half, pl);
        
        //jesli trzeba zwiekszyc palindorm
        if (stoull(palindrome) <=  stoull(s)) {
            unsigned long long halfll = stoull(half);            
            half = to_string(++halfll); 
            //jesli nowy palindrom bedzie mial wiecej cyfr i poczatkowa wartosc miala nieparzysta ilosc cyfr
            if (half.length() > hl && pl != hl) {
                halfll /= 10;
                half = to_string(halfll);                
                pl++;
            }
            palindrome = build_palindrome(half, pl);       
        }
        cout << palindrome << endl;    
    }
    return 0;
}