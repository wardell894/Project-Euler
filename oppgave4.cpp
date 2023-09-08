
#include <iostream>
#include <iostream>
#include <vector>
#include <string>
using namespace std;

string reverseStr(string& str, int n, int i)
{
    if (n <= i) {
        return str;
    }
    swap(str[i], str[n]);
    return reverseStr(str, n - 1, i + 1);
}

int palindrome_finder(int N) { // Endre returtype til int
    vector<int> palindrome_list;
    for (int i = 1; i < N + 1; i++) {
        for (int j = N + 1; j > 1; j--) { // Rett opp skrivefeilen her
            int L = i * j;
            string L_string = to_string(L);
            string L_string_ekte = L_string;
            string L_string_reversed = reverseStr(L_string, L_string.length() - 1, 0);
            if (L_string_reversed == L_string_ekte) {
                int W = stoi(L_string);
                palindrome_list.push_back(W);
            }
        }
    }
    if (!palindrome_list.empty()) {
        auto svaret = max_element(begin(palindrome_list), end(palindrome_list));
        return *svaret;
    }
    return -1; // Returner -1 hvis ingen palindromer blir funnet
}

int main()
{
    cout << "Hello World!" << endl;
    cout << palindrome_finder(999);

    return 0; // Legg til en returnsetning for main-funksjonen
}
