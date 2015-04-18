#include <iostream>

using namespace std;
typedef long long LL;

int main(void)
{
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		int n;
		cin >> n;
		LL init = 0, sum = 0;
		while (n--)
		{
			int x;
			cin >> x;
			
			sum += x;
			if (sum <= 0)
			{
				init += 1-sum;
				sum = 1;
			}
		}
		LL ans = (init == 0) ? 1 : init;
		cout << "Scenario #" << i << ": " << ans << endl;
	}
	return 0;
}
