#include <iostream>

using namespace std;
typedef long long LL;

int main()
{
	int T;
	
	cin >> T;
	while (T--)
	{
		int n;
		
		cin >> n;		
		const int MAX_SIZE = 2e5;
		int A[MAX_SIZE];
		
		for (int i = 0; i < n; ++i)
		{
			cin >> A[i];
		}
		LL ans = 0;
		for (int i = 0; i < n; ++i)
		{
			for (int j = i+1; j < n; ++j)
			{
				if (A[i] > A[j])
				{
					ans++;
				}
			}
		}
		cout << ans << endl;
	}
	return 0;
}
