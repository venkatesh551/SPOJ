#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void read_vector_and_sort(vector<int> &v, int n)
{
    for (int i = 0; i < n; ++i)
    {
        cin >> v[i];
    }
    sort(v.begin(), v.end());
}

int no_of_triples(vector<int> &v, int n)
{
    int result = 0;
    
    for (int i = n-1; i  > 1; --i)
    {
        int j = 0, k = i -1;
        while (j < k)
        {
            int sum = v[j] + v[k];
            if (v[i] > sum)
            {
                result += k-j;
                ++j;
            }
            else
            {
                k--;
            }
        }
    }
    return result;
}

int main()
{
    while (true)
    {
        int n;
        cin >> n;
        if (n == 0)
            return 0;
        vector<int> v(n);
        read_vector_and_sort(v, n);
        cout << no_of_triples(v, n) << endl;
    }
    
    return 0;
}