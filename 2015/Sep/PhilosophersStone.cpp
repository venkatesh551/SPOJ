#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int R = 105;
const int C = 105;

int mat[R][C];

int get_max_sum(int h, int w)
{
    for (int i = 1; i < h ; ++i)
    {
        for (int j = 1; j <= w; ++j)
        {
            mat[i][j] += max(max(mat[i-1][j], mat[i-1][j-1]), mat[i-1][j+1]);
        }
    }
    int result = 0;
    for (int i = 0; i <= w; ++i)
    {
        result = max(result, mat[h-1][i]);
    }
    return result;
}


int main()
{
    int tc;
    scanf("%d", &tc);
    while (tc--)
    {
        int h, w;
        scanf("%d%d", &h, &w);
        memset(mat, 0, sizeof(mat));
        for (int i = 0; i < h; i++)
        {
            for (int j = 1; j <= w; ++j)
            {
                scanf("%d", &mat[i][j]);
            }
        }
        printf("%d\n", get_max_sum(h, w));
    }
    
    return 0;
}
