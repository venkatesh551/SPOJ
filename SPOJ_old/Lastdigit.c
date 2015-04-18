#include <stdio.h>

int pow_mod(int a, unsigned long long b)
{
	int result = 1;
	
	while (b > 0)
	{
		if (b & 1)
			result = (result * a) % 10;
		a = (a * a)% 10;
		b >>= 1;
	}
	return result;
}

int main(void)
{
	int T;
	
	scanf("%d", &T);
	while (T--)
	{
		int a;
		unsigned long long b;
		
		scanf("%d%llu", &a, &b);
		printf("%d\n", pow_mod(a, b));
	}
	
	return 0;
}
