#include <iostream>
#include <vector>
#include <numeric> 

using namespace std;

 bool erPrimtall(int N){
     for(int i = 2; i < N;i++){
         bool tester = true;
         if(N%i == 0){
             tester = false;
             break;
         }
         
         return tester;
     }
     return 0;
 }
 
 
 int largest_prime_factor(int N,long int F){
     vector<int> faktor_liste;
     for(int i = 0; i < N;i++){
         int K = 2*i +1 ;
         if(F%K == 0 && erPrimtall(K) == true){
             faktor_liste.push_back(K);
         }
     }
     //int result = accumulate(faktor_liste.begin(), faktor_liste.end(),1, multiplies<int>());
     return  faktor_liste[faktor_liste.size()-1];
     
 }
 
int main() {
    
    cout<<(largest_prime_factor(10000,600851475143));
    
    return 0;
}
