#include <iostream>
#include <set>
using namespace std;

int square_sum(int n)
{
	int sum = 0;
	
	while (n > 0)
	{
		int d = n % 10;
		sum += d * d;
		n /= 10;
	}
	return sum;
}


int main(void)
{
	int n;
	
	cin >> n;
	int cnt = 0;
	set<int> s;
	while (n != 1)
	{
		int x = square_sum(n);
		if (s.count(x) == 1)
		{
			cnt = -1; 
			break;
		}
		else
		{
			++cnt;
			s.insert(x);
		}
		n = x;
	}
	cout << cnt << endl;

	return 0;
}
