#include <iostream>
#include "euler.hpp"

using namespace std;

int main()
{
    long ans = 2;
    const int N = 2000000;
    for(int i = 3; i <= N; i+=2)
    {
        if (PrimeUtils::isPrime(i)) {
             ans += i;
        }
    }
    cout<< ans << endl;
    return 0;
}