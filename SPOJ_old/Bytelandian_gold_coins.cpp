#include <iostream>

using namespace std;

int sum(int n)
{
	int x = n/2 + n/3 + n/4;
	if (x > n)
	{
		return sum(n/2) + sum(n/3) + sum(n/4);
	}
	else
	{
		return n;
	}
}

int main(void)
{
	int n;
	while (cin >> n)
	{
		cout << sum(n) << endl;
	}
	return 0;
}
