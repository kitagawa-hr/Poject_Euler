#include <iostream>
#include <string>
using namespace std;

int fibo(int n){
    if (n==1 or n==2){
        return n;
    }
    return fibo(n-1)+fibo(n-2);
}

int main(){
    int i=1;
    int ans=0;
    while (fibo(i)<4000000){
        ans += fibo(i);
        i++;
    }
    cout << ans << endl;
    return 0;
}
