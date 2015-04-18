#include <iostream>
#include <algorithm>

using namespace std;
typedef long long LL;

int main(void)
{
	int t;
	cin >> t;
	while (t--)
	{
		LL a, b;
		cin >> a >> b;
		int g = __gcd(a, b);
		LL lcm = (a * b)/g;
		cout << lcm/a << " " << lcm/b << endl;
	}
	return 0;
}
