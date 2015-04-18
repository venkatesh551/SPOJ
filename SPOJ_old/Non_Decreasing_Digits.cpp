#include <iostream>
#include <vector>

using namespace std;
typedef long long LL;

void calculate(vector<LL> &v)
{
	int n= v.size();
	LL d[10], sum = 0;
	for (int i = 0; i < 10; ++i)
	{
		d[i] = 1;
		sum += d[i];
	}
	v[1] = sum;
	for (int i = 2; i < n; ++i)
	{
		sum = d[9];
		for (int j = 8; j >= 0; --j)
		{
			d[j] += d[j+1];
			sum += d[j];
		}
		v[i] = sum;
	}
}
int main()
{
	const int MAX = 65;
	vector<LL> v(MAX);
	calculate(v);
	int t;
	cin >> t;
	while (t--)
	{
		int x, y;
		cin >> x >> y;
		cout << x << " " << v[y] << endl;
	}
	return 0;
}
