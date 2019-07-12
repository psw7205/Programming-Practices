#include <bits/stdc++.h>

using namespace std;

int n = 8;

int cnt;

vector<int> col(n * n);

vector<int> diag1(n * n);

vector<int> diag2(n * n);

void nQueen(int y)
{
    if (y == n)
    {
        cnt++;
        return;
    }

    for (int x = 0; x < n; ++x)
    {
        if (col[x] || diag1[x + y] || diag2[x - y + n - 1])
            continue;

        col[x] = diag1[x + y] = diag2[x - y + n - 1] = 1;
        nQueen(y + 1);
        col[x] = diag1[x + y] = diag2[x - y + n - 1] = 0;

    }
}

int main()
{
    nQueen(0);
    cout << cnt << endl;

    return 0;
}