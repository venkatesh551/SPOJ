#include <iostream>

using namespace std;

int main(void)
{
	int d;
	cin >> d;
	while (d-- > 0)
	{
		int n, m;
		cin >> n >> m;
		cout << (((n-m) & ((m-1)/2)) == 0) << endl;
	}
	return 0;
}
