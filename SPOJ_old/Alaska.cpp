#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

bool is_reachable(vector<int> &v)
{
	const int distance = 1422;
	sort(v.begin(), v.end());
	int d = 0;
	int n = v.size();
	for (int i = 0; i < n; ++i)
	{
		if (v[i] <= d)
		{
			d = v[i] + 200;
		}
		else
		{
			return false;
		}
	}
	if (d < distance || (distance - v[n-1]) * 2 > 200)
	{
		return false;
	}
	return true;
}

int main(void)
{
	while (true)
	{
		int n;
		cin >> n;
		if (n == 0)
		{
			break;
		}
		vector<int> v(n);
		for (int i = 0; i < n; ++i)
		{
			cin >> v[i];	
		}
		if (is_reachable(v))
		{
			cout << "POSSIBLE" << endl;	
		}
		else
		{
			cout << "IMPOSSIBLE" << endl;	
		}
	}
	return 0;
}



