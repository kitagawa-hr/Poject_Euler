#include <iostream>
#include "euler.hpp"

using namespace std;

// find (a,b,c) such as a+b+c=1000, a^2+b^2=c^2
// ans: a*b*c

namespace
{
const int N = 1000;
}

int main()
{

    for (size_t i = 1; i < N; i++)
    {
        for (size_t j = 1; j < i; j++)
        {
            if (pow(1000 - i - j, 2) == pow(i, 2) + pow(j, 2))
            {
                cout << i * j * (1000 - i - j) << endl;
            }
        }
    }
}