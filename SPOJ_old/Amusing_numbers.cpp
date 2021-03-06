#include <iostream>
#include <vector>

using namespace std;
typedef long long LL;

void print_kth_number(LL k)
{
	LL x = 0, bits = 1;
	while (((x << 1)|2) < k)
	{
		x = (x << 1)|2;
		++bits;
	}
	LL pos = k - (x + 1);
	vector<int> v(bits);
	while (bits--)
	{
		if(pos & 1)
		{
			v[bits] = 6;
		}
		else
		{
			v[bits] = 5;
		}
		pos >>= 1;
	}
	for (size_t i = 0; i < v.size(); ++i)
	{
		cout << v[i];	
	}
	cout << endl;
}

int main(void)
{
	int n;
	cin >> n;
	while (n--)
	{
		LL k;
		cin >> k;
		print_kth_number(k);
	}
	return 0;
}


