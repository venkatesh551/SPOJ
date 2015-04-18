#include <iostream>
#include <vector>

using namespace std;
typedef long long LL;

LL __abs(LL x)
{
	return x < 0 ? -x : x;
}

int main(void)
{
	int t;
	cin >> t;
	while (t-- > 0)
	{
		int n;
		cin >> n;
		vector<int> v(n);
		LL x, sum = 0, p = 0, q = 0;
		for (int i = 0; i < n; ++i)
		{
			cin >> x;
			sum += x;
			p += (LL)(n-1-i) * x;
			q += (LL)(n-i) * x;
		}
		LL temp = sum * n - q;
		cout << __abs(p-temp) << endl;
	}
	return 0;
}
