// Online C++ compiler to run C++ program online
#include <iostream>
using namespace std;
int Multiples_3_5(int N){
    int svaret = 0;
    for(int i = 0; i<N;i++){
        if(i%3 == 0){
            svaret+=i;
        }
        if(i%5 == 0){
            svaret+=i;
        }
        if(i%15 == 0){
            svaret-=i;
        }
    }
    return svaret;
}

int main() {
    // Write C++ code here
    cout<<Multiples_3_5(1000);

    return 0;
}
