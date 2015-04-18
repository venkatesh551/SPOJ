#include <iostream>
#include <vector>

using namespace std;

int get_minCount(const vector<int> &v, const int sum) 
{
	int n = v.size();
	if (sum % n != 0)
	{
		return -1;
	}
	else
	{
		int ans = 0, x = sum/n;
		for (int i = 0; i < n; ++i)
		{
			if (x > v[i])
			{
				ans += x - v[i];
			}
		}
		return ans;
	}
}

int main(void)
{
	int n;
	
	while (cin >> n && n > 0)
	{
		int sum = 0;
		vector<int> v(n);
		for (int i = 0; i < n; ++i)
		{
			cin >> v[i];
			
			sum += v[i];
		}
		cout << get_minCount(v, sum) << endl;
	}
	return 0;
}
