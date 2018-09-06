#include <iostream>
#include <string>
#include <cmath>
using namespace std;
int palindrome(int number){
    int n = number;
    int reversed = 0;
    int digit;
    while (n > 0) {
        digit = n % 10;
        reversed = reversed * 10 + digit;
        n /= 10;
    }
    return reversed;
}

int main(){
    int ans=0;
    for (int i=100; i<1000; i++){
        for (int j = 100; j<1000;j++){
            if (i*j == palindrome(i*j)){
                ans = max(ans, i*j);
            }
        }
    }
    cout << ans << endl;
    return 0;
}