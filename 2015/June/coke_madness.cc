#include <iostream>

using namespace std;
typedef long long LL;

int main()
{
	int tc;
	cin >> tc;
	for(int sc = 1; sc <= tc; ++sc)
	{
		int n;
		cin >> n;
		LL sum =  1, ans = 1;
		for (int i = 0; i < n;  ++i)
		{
			int val;
			cin >> val;
			sum += val;
			if (sum <= 0)
			{
				ans += 1-sum;
				sum = 1;
			}
		}
		cout << "Scenario #" << sc << ": " << ans << endl; 
	}
	return 0;
}