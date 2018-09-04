#include <iostream>
#include <string>
#include <cmath>

using namespace std;


int max_factor(long long n){
    double lim = sqrt(n);
    int i = 2;
    while (i<=lim){
        if (n%i==0){
            return max_factor(int(n/i));
        }
        i++;
    }
    return n;
}

int main(){
    long long N = 600851475143;
    cout << max_factor(N);
    return 0;
}