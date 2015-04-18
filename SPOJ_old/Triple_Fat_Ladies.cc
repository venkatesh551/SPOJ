#include <iostream>

using namespace std;
typedef long long LL;

int main(void)
{
	int t;
	
	cin >> t;
	while (t-- > 0)
	{
		LL k;
		cin >> k;
		cout << (k-1) * 1000 + 192 << endl;
	}
	return 0;
}
