#include <bits/stdc++.h>

using namespace std;

int main()
{
    bitset<8> bit;
    bit[1] = bit[3] = bit[4] = bit[7] = 1;

    bitset<8> bit2;
    bit2[0] = bit2[3] = bit2[4] = bit[6] = 1;

    cout << bit << endl << bit2 << endl;
    cout << "--------------" << endl;
    cout << (bit & bit2) << " &" << endl;
    cout << (bit | bit2) << " |" <<endl;
    cout << (bit ^ bit2) << " ^" <<endl;
    cout << bit.count() << endl;

    return 0;
}