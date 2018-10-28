#include<iostream>
#include<cmath>
#include<string>
#include "euler.hpp"

using namespace std;



int main(){
    int count=0;
    int num=2;
    while (count<10001){
        if (PrimeUtils::isPrime(num)){
            count+=1;
        }
        num+=1;
    }
    cout << num-1 <<endl;
    return 0;
}