#include <iostream>

using namespace std;
typedef long long LL;

int main()
{

	int t;
	cin >> t;
	while (t-- > 0)
	{	
		LL x, y, s;
		
		cin >> x >> y >> s;
		LL n = 2 * s/(x + y);
		LL d = (y - x)/(n - 5);
		LL a = x - 2 * d;
		cout << n << endl;
		for (int i = 0; i < n; ++i, a += d)
		{
			cout << a << " " ;
		}
		cout << endl;
	}
	return 0;
}
