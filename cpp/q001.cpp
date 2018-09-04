#include <iostream>
#include <string>
using namespace std;

int main(){
    int ans = 0;
    for (unsigned int n=0; n<1000; n++){
        if (n % 3 == 0 or n% 5 == 0){
            ans += n;
        }
    }
    cout << ans << endl;
    return 0;
}