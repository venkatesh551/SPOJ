#include <stdio.h>
#include <string.h>
#define MAX_SIZE 10001

void sum(char *s, char *t)
{	
	int i, c = 0, sum;
	for (i = 0; s[i] && t[i]; i++)
	{
		int x = s[i] - '0';
		int y = t[i] - '0';
		sum = (x + y + c);
		s[i] = '0' + sum % 10;
		c = sum / 10;
	}
	if (s[i] == 0)
	{
		strcpy(s + i, t + i);
	}
	for ( ; c && s[i]; i++)
	{
		sum = (s[i] - '0')+ c;
		s[i] = '0' + sum % 10;
		c = sum / 10;
	}
	if (c)
	{
		s[i] = '1';
		s[i+1] = 0;
	}
	
}

int main(void)
{
	int T;
	
	scanf("%d", &T);
	while (T--)
	{
		char s[MAX_SIZE];
		char t[MAX_SIZE];
		int i;
		
		scanf("%s%s", s, t);
		sum(s, t);
		for (i = 0; s[i] == '0'; i++)
			;
		puts(s+i);
	}
	
	return 0;
}
