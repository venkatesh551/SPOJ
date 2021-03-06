#include <cstdio>

int gcd(int a, int b)
{
	while (b > 0)
	{
		int r = a%b;
		a = b;
		b = r;
	}
	return a;
}

int no_of_factors(int n)
{
	int init_n = n;
	int num_factors = 1;
	for (int i = 2; i * i <= init_n && n > 1; ++i)
	{
		int pwr = 0;
		while (n % i == 0)
		{
			n /= i;
			++pwr;	
		}
		num_factors *= (pwr + 1);
	}
	if (n > 1)
	{
		num_factors *= 2;	
	}
	return num_factors;
}

int main(void)
{
	int t;
	
	scanf("%d", &t);
	while (t-- > 0)
	{
		int a, b;
		scanf("%d%d", &a, &b);
		printf("%d\n", no_of_factors(gcd(a, b)));
	}
	return 0;	
}

