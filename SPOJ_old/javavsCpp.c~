#include <stdio.h>
#include <ctype.h>

#define MAX_SIZE 109
typedef enum lang_type{
	CPP,
	JAVA,
	UNKNOWN
}lang_type;

lang_type get_langType(char *s)
{
	lang_type type = CPP;
	int i, U = 0, _ = 0, prev = -1;
	
	if (isupper(s[0]) || (s[0] == '_'))
	{
		return UNKNOWN;
	}
	for (i = 0; s[i]; ++i)
	{
		if (isupper(s[i]))
		{
			U = 1;
			type = JAVA;
		}
		if (s[i] == '_')
		{
			_ = 1;
		}
		if ((_ == 1 && U == 1) || (prev == s[i] && s[i] == '_'))
		{
			return UNKNOWN;
		}
		prev = s[i];
	}
	return type;
}

int main(void)
{
	char s[MAX_SIZE];
	
	while (scanf("%s", s) != EOF)
	{
		lang_type type = get_langType(s);
		int i;
		
		if (type == CPP)
		{
			for (i = 0; s[i]; ++i)
			{
				if (s[i] == '_')
				{
					s[i+1] = toupper(s[i+1]);
				}
				else
				{
					putchar(s[i]);
				}
			}
		}
		else if (type == JAVA)
		{
			for (i = 0; s[i]; ++i)
			{
				if (isupper(s[i]))
				{
					putchar('_');
					putchar(tolower(s[i]));
				}
				else
				{
					putchar(s[i]);
				}
			}
		}
		else
		{
			printf("Error!");
		}
		putchar('\n');
	}
	
	return 0;
}
