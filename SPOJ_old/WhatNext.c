#include <stdio.h>

int main(void)
{
	while (1)
	{
		int a, b, c, d, r;
		
		scanf("%d%d%d", &a, &b, &c);
		if (a == 0 && b == 0 && c == 0)
		{
			break;
		}
		d = b - a;
		if (d == c - b)
		{
			printf("AP %d\n", c + d);
		}
		else
		{
			r = b / a;
			printf("GP %d\n", r * c);
		}
	}
	
	return 0;
}
