#include <iostream>
#include <algorithm>

using namespace std;

int edit_dist(string &a, string &b)
{
	int m = a.length();
	int ascii_map[128] = {0};
	
	for (int i = 0; i < m; ++i)
	{
		int x = a[i];
		++ascii_map[x];
	}
	int cnt = 0, n = b.length();
	for (int i = 0; i < n; ++i)
	{
		int x = b[i];
		if (ascii_map[x])
		{
			--ascii_map[x];
			++cnt;
		}
	}
	return max(m - cnt, n - cnt);
}

int main(void)
{
	int t;
	
	cin >> t;
	string A, B;
	while (t-- > 0)
	{
		cin >> A >> B;
		cout << edit_dist(A, B) << endl;
	}
	return 0;
}

