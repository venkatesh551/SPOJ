#include <iostream>
#include <cstdio>

using namespace std;

int main(void)
{
	int n;
	scanf("%d", &n);
	int result = 0;
	for (int i = 0; i < n; ++i)
	{
		int x;
		scanf("%d", &x);
		result ^= x;
	}
	printf("%d\n", result);
	return 0;
}
