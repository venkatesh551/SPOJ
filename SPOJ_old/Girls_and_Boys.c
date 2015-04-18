#include <stdio.h>

int main(void)
{
	while (1)
	{
		int g, b, ans;
		
		scanf("%d%d", &g, &b);
		if (g == -1 && b == -1)
			break;
		if (g > b)
		{
			ans = (g + b)/(b+1);
		}
		else
		{
			ans = (b + g)/(g+1);
		}
		printf("%d\n", ans);
	}
	
	return 0;
}
