#include <stdio.h>

int main(void)
{
	int T;
	
	scanf("%d", &T);
	while (T--)
	{
		int x, y;
		
		scanf("%d%d", &x, &y);
		if (x == y)
		{
			if ((x & 1) == 0)
			{
				printf("%d\n", x * 2);
			}
			else
			{
				printf("%d\n", x * 2 - 1);
			}
		}
		else if (x == y + 2)
		{
			if ((x & 1) == 0)
			{
				printf("%d\n", x + y);
			}
			else
			{
				printf("%d\n", x + y - 1);
			}
		}
		else
		{
			puts("No Number");
		}
	
	
	}
	
	return 0;
}
