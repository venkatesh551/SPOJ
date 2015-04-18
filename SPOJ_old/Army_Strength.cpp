#include <iostream>
#include <vector>

using namespace std;

int get_max(int n)
{
	int res = 0;
	for (int i = 0; i < n; ++i)
	{
		int x;
		cin >> x;
		res = max(x, res);
	}
	return res;
}

int main(void)
{
	int t;
	cin >> t;
	while (t-- > 0)
	{
		int ng, nm;
		cin >> ng >> nm;
		int f = get_max(ng);
		int s = get_max(nm);
		if (f >= s)
		{
			cout << "Godzilla" << endl;
		}
		else
		{
			cout << "MechaGodzilla"	<< endl;
		}
	}
	return 0;
}
