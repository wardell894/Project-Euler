// Online C++ compiler to run C++ program online
#include <iostream>
using namespace std;

int fibbonaci(int N){
    if(N < 2){
        return N;
    }
    return fibbonaci(N-1) + fibbonaci(N-2);
}
int svaretFibbo(int iterasjoner){
     int svaret = 0;
    for(int i = 2; i < 34;i++){
        if( fibbonaci(i) %2 ==0){
            svaret+=fibbonaci(i);
        }
    }
    return svaret;
}

int main() {
    // Write C++ code here
    cout<<svaretFibbo(34);
    return 0;
}
