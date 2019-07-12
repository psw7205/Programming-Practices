#include <bits/stdc++.h>

using namespace std;

vector<int> permutation;

bool chosen[100];

int n;

void createPermutation()
{
    if (permutation.size() == n)
    {
        for (int i = 0; i < permutation.size(); ++i)
        {
            cout << permutation[i] << " ";
        }
        cout << endl;
    }
    else
    {
        for (int i = 1; i <= n; ++i)
        {
            if (chosen[i])
            {
                continue;
            }

            chosen[i] = true;
            permutation.push_back(i);
            createPermutation();
            chosen[i] = false;
            permutation.pop_back();
        }
    }
}

int main()
{
    cin >> n;

    createPermutation();


    cout << "--------------------------" << endl;
    permutation.clear();

    for (int i = 1; i <= n; i++)
    {
        permutation.push_back(i);
    }

    do
    {
        for (int i = 0; i < permutation.size(); ++i)
        {
            cout << permutation[i] << " ";
        }

        cout << endl;
    }
    while (next_permutation(permutation.begin(), permutation.end()));


    return 0;
}