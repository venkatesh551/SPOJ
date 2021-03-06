#include <iostream>
#include <cstdio>

using namespace std;
const int MAX_SIZE = 1e6 + 7;

int get_probable_major(const int *v, int n)
{
	int cnt = 1, maj_element = v[0];
	for (int i = 1; i < n; ++i) 
	{
		if (cnt == 0)
		{
			cnt = 1;
			maj_element = v[i];
		}
		else if (v[i] == maj_element)
		{
			++cnt;
		}
		else
		{
			--cnt;
		}
	}
	return maj_element;
}

bool is_major(const int *v, int n, int m)
{
	int cnt = 0;
	for (int i = 0; i < n; ++i)
	{
		if (v[i] == m)
		{
			++cnt;
		}
	}
	return cnt > (n/2);
}

int main(void)
{
	int t, v[MAX_SIZE];
	
	cin >> t;
	while (t-- > 0)
	{
		int n;
		cin >> n;
		for (int i = 0; i < n; ++i)
		{
			scanf("%d", &v[i]);
		}
		int m = get_probable_major(v, n);
		if (is_major(v, n, m))
		{
			printf("YES %d\n", m);
		}
		else
		{
			puts("NO");
		}
	}
	return 0;
}
