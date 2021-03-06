#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>

using namespace std;
typedef long long LL;
const int MAX = 1e4 + 7;

int main(void)
{
	int t;
	cin >> t;
	for (int j = 1; j <= t; ++j)
	{
		int n;
		cin >> n;
		int v[MAX];
		for (int i = 0; i < n; ++i)
		{
			cin >> v[i];
		}
		LL B[MAX];
		B[0] = v[0];
		B[1] = max(v[0], v[1]);
		for (int i = 2; i < n; ++i)
		{
			B[i] = max(B[i-1], B[i-2] + v[i]);
		}
		printf("Case %d: %lld\n", j, B[n-1]);
	}
	return 0;
}

