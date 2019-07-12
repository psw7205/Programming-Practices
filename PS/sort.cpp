#include <bits/stdc++.h>

using namespace std;

int main()
{
    vector<int> arr = {4, 2, 5, 3, 5, 8, 3};

    for (int i = 0; i < arr.size(); ++i)
        cout << arr[i] << " ";

    cout << " origin" << endl;

    sort(arr.begin(), arr.end());

    for (int i = 0; i < arr.size(); ++i)
        cout << arr[i] << " ";

    cout << " sorted" << endl << "--------------" << endl;


    vector<int> arr2 = {4, 2, 5, 3, 5, 8, 3};

    for (int i = 0; i < arr2.size(); ++i)
        cout << arr2[i] << " ";

    cout << " origin" << endl;

    sort(arr2.rbegin(), arr2.rend());

    for (int i = 0; i < arr2.size(); ++i)
        cout << arr2[i] << " ";

    cout << " sorted" << endl << "--------------" << endl;
    string s = "apple";

    for (int i = 0; i < s.size(); ++i)
        cout << s[i] << " ";

    cout << " origin" << endl;

    sort(s.begin(), s.end());

    for (int i = 0; i < s.size(); ++i)
        cout << s[i] << " ";

    cout << " sorted" << endl << "--------------" << endl;

    vector<pair<int, int>> v;
    v.push_back({1, 5});
    v.push_back({2, 3});
    v.push_back({1, 2});
    v.push_back({2, 4});

    for (int i = 0; i < v.size(); ++i)
        cout << "{" << v[i].first << " " << v[i].second << "} ";

    cout << " origin" << endl;
    sort(v.begin(), v.end());

    for (int i = 0; i < v.size(); ++i)
        cout << "{" << v[i].first << " " << v[i].second << "} ";

    cout << " sorted" << endl << "--------------" << endl;
    return 0;
}