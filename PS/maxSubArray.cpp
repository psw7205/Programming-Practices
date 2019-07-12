#include <bits/stdc++.h>

using namespace std;

vector<int> arr;

int maxSubArrayNSquare()
{
    int sum = 0, best = 0;
    for (int i = 0; i < arr.size(); ++i)
    {
        sum = 0;
        for (int j = i; j < arr.size(); ++j)
        {
            sum += arr[j];
            best = max(best, sum);
        }
    }

    return best;
}

int maxSubArrayN()
{
    int best = 0;
    int sum = 0;
    for (int i = 0; i < arr.size(); ++i)
    {
        sum = max(arr[i], sum + arr[i]);
        best = max(best, sum);
    }

    return best;
}

int main()
{
    arr = {-1, 2, 4, -3, 5, 2, -5, 2};

    cout << maxSubArrayNSquare() << endl;
    cout << maxSubArrayN() << endl;
    return 0;
}