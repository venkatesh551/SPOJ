#include <iostream>

using namespace std;
typedef unsigned long long LL;

int last_digit(LL a, LL b)
{
	int result = 1;
	while (b > 0 && result > 0)
	{
		if (b & 1)	
			result = (result * a) % 10;
		a = (a * a) % 10;
		b >>= 1;
	}
	return result;
}

int main()
{
	int t;
	
	cin >> t;
	while (t-- > 0)
	{
		string a;
		LL b;
		
		cin >> a >> b;
		int d = a[a.length()-1] - '0';
		cout << last_digit(d, b) << endl;
	}
	return 0;
}
