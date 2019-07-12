#include <bits/stdc++.h>

using namespace std;

vector<int> subset;

int n;

void findSubset(int k)
{
    if (k == n + 1)
    {
        for (int i = 0; i < subset.size(); ++i)
        {
            cout << subset[i] << " ";
        }
        cout << endl;
    }
    else
    {
        subset.push_back(k);
        findSubset(k + 1);
        subset.pop_back();
        findSubset(k + 1);
    }
}

int main()
{
    n = 3;

    findSubset(1);

    return 0;
}