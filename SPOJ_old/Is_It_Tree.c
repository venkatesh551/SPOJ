#include <stdio.h>
#define MAX_SIZE 10009

int main(void)
{
	int n, m, i, cnt, loop ,A[MAX_SIZE] = {0} ;
	
	scanf("%d%d", &n, &m);
	loop = 0;
	for (i = 0; i < m; ++i)
	{
		int x, y;
		
		scanf("%d%d", &x, &y);
		if (A[x] == 1 && A[y] == 1)
		{
			loop = 1;
		}
		else
		{
			A[x] = A[y] = 1;
		}
	}
	cnt = 0;
	for (i = 1; i <= n; ++i)
	{
		cnt += A[i];
	}
	if (loop == 0 && ((n == 1 && m == 0) || (n == m+1 && cnt == n)))
	{
		puts("YES");
	}
	else
	{
		puts("NO");
	}
	
	return 0;
}
