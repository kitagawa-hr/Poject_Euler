#include<iostream>
#include<cmath>
#include<string>

using namespace std;


int is_prime(unsigned int n){
    float lim=sqrt(n);
    if (n==2){
        return true;
    }
    if (n%2==0){
        return false;
    }
    for (int i=3; i<=lim; i+=2){
        if (n%i==0){
            return false;
        }
    }
    return true;
}

int main(){
    int count=0;
    int num=2;
    while (count<10001){
        if (is_prime(num)){
            count+=1;
        }
        num+=1;
    }
    cout << num-1 <<endl;
    return 0;
}