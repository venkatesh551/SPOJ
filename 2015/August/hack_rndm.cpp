#include <algorithm>
#include <iostream>
#include <set>

using namespace std;

int main()
{
    int n, k;
    cin >> n >> k;
    set<int> myset;
    for(int i=0;i < n;i++)
    {
        int x;
        cin >> x;
        myset.insert(x);
    }
    int cnt = 0;
    for (set<int>::iterator it = myset.begin(); it != myset.end(); ++it)  
    {
        int ele = *it + k;
        if (myset.count(ele) != 0)
        {
            cnt++;
        }
    }
    cout << cnt << endl;
    return 0;
} 