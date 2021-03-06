#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void)
{
	int n;
	
	cin >> n;
	vector <pair <int, int> > v;
	for (int i = 1; i < n; ++i)
	{
		int x, y;
		
		cin >> x >> y;
		v.push_back(make_pair(x, y));
	}
	sort(v.begin(), v.end());
	int ans = 1;
	for (int i = 1; i < n; ++i)
	{
		if (v[i].first == v[i-1].second)
		{
			++ans;
		}
		else
		{
			ans = 1;
		}
	}
	cout << ans << endl;
	return 0;
}

