#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
typedef long long LL;

void read_vector_and_sort(vector<int> &v, int n)
{
    for (int i = 0; i < n; ++i)
    {
        cin >> v[i];
    }
    sort(v.begin(), v.end());
}

int main()
{
    while (true)
    {
        int n;
        cin >> n;
        if (n == 0)
        {
            return 0;
        }
        vector<int> a(n), b(n);
        read_vector_and_sort(a, n);
        read_vector_and_sort(b, n);
        LL sum = 0;
        for (int i = 0, j = n - 1; i < n; ++i, --j)
        {
            sum += ((LL) a[i]) * b[j];
        }
        cout << sum << endl;
    }
    return 0;
}
