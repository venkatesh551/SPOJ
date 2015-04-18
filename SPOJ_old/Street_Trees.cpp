#include <iostream>
#include <algorithm>

using namespace std;
int main()
{
	int n, a, b;
	cin >> n >> a;
	int g = 0, first = a;
	for (int i = 1; i < n; ++i)
	{
		cin >> b;
		g = __gcd(g, b-a);
		a = b;
	}
	int p = 1 + (b - first)/g;
	cout << p-n << endl;
	return 0;
}
