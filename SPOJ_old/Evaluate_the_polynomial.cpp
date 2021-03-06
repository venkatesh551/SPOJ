#include <cstdio>
typedef long long LL;

LL evaluate(int *coeff, int n, int x)
{
	LL result = 0;
	for (int i = 0; i <= n; ++i)
	{
		result = result * x + coeff[i];
	}
	return result;
}

int main(void)
{
	const int MAX = 1e3;
	int A[MAX], n;
	for (int i = 1; (scanf("%d", &n) && n != -1); ++i)
	{
		for (int j = 0; j <= n; ++j)
		{
			scanf("%d", &A[j]);
		}
		int k;
		scanf("%d", &k);
		printf("Case %d:\n", i);
		for (int j = 0; j < k; ++j)
		{
			int x;
			scanf("%d", &x);
			printf("%lld\n", evaluate(A, n, x));
		}
	}
	return 0;
}
