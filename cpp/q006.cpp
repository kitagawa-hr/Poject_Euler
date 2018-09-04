#include <iostream>
#include <string>
#include <cmath>
#include <vector>

using namespace std;

int main(){
    int sum1,sum2, ans;
    for (int i=1; i<=100; i++){
        sum1 += i;
        sum2 += pow(i,2);
    }
    ans = pow(sum1,2)-sum2;
    cout << ans << endl;
    return 0;
}