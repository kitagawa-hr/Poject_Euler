#include <iostream>
#include <string>
#include <cmath>
#include <map>
#include <vector>
#include "euler.hpp"

using namespace std;

// 約数の個数が500以上の最初の三角数

map<int, int> divisor_num(int num)
{
    map<int, int> mPower;
    while (num > 1)
    {
        FOR(i, 2, num+1)
        {
            if (num % i == 0)
            {
                num /= i;
                mPower[i] += 1;
                break;
            }
        }
    }
    return mPower;
}

int div_sum(int num)
{
    int div_sum = 1;
    map<int,int> mp = divisor_num(num);
    for(auto itr = mp.begin(); itr != mp.end(); ++itr)
    {
        div_sum *= (itr->second +1 );
    }
    return div_sum;
}

int main(){
    int ans=0, n=1, m=0;
    while(true)
    {
        m = n*(n+1)/2;
        if (div_sum(m)>=500)
        {
            cout << m << endl;
            return 0;
        }
        n+=1;
    }
}