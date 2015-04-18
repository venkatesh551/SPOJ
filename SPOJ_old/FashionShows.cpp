#include <iostream>
#include <algorithm>

using namespace std;

void read_andSort(int *a, int n)
{
	for (int i = 0; i < n; ++i)
	{
		cin >> a[i];
	}
	sort(a, a+n);
}

int main()
{
	int T;
	
	cin >> T;
	while (T--)
	{
		int n;
		const int SIZE = 1e3;
		int a[SIZE], b[SIZE];
		cin >> n;
		read_andSort(a, n);
		read_andSort(b, n);
		int sum = 0;
		for (int i = 0; i < n; ++i)
		{
			sum += a[i] * b[i];
		}
		cout << sum << endl;
	}
	return 0;
}
