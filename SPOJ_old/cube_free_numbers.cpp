#include <cstdio>

const int MAX_SIZE = 1e6;
int A[MAX_SIZE] = {0};

void sieve()
{
	for (int i = 2; i*i*i <= MAX_SIZE; ++i)
	{
		int x = i * i * i;
		for (int j = x; j <= MAX_SIZE; j += x)
		{
			A[j] = -1;
		}
	}
	int c = 1;
	for (int i = 1; i <= MAX_SIZE; ++i)
	{
		if (A[i] == 0)
		{
			A[i] = c++;
		}
	}
}

int main(void)
{
	sieve();
	int t;
	
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i)
	{
		int x;
		
		scanf("%d", &x);
		printf("Case %d:", i);
		if (A[x] == -1)
		{
			puts("Not Cube Free");
		}
		else
		{
			printf("%d\n", A[x]);
		}
	}
	return 0;	
}


