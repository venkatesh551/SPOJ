#include <cstdio>
#include <algorithm>

using namespace std;
const int MAX = 1e6;
int a[MAX];

int main()
{
    int  tc;
    scanf("%d", &tc);
   
    while (tc--)
    {
        int n;
        scanf("%d", &n);
        for (int i = 0; i < n; ++i)
        {
            scanf("%d", &a[i]);
        }
        for (int i = 1; i < n; ++i)
        {
            if (a[i] < a[i-1])
            {
                swap(a[i], a[i-1]);
                ++i;
            }
        }
        bool ans = true;
        for (int i = 1; i < n; ++i)
        {
            if (a[i] < a[i-1])
            {
                ans = false;
                break;
            }
        }
        printf("%s\n", ans ? "YES" : "NO");
    }
    return 0;
}