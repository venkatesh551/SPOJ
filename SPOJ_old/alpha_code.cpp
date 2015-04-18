#include <iostream>

using namespace std;

bool check_in_range(int num)
{
	return 9 < num && num < 27;
}

int main()
{
	string s;
	const int MAX_LEN = 5007;
	while (true)
	{
		cin >> s;
		if (s == "0")
			break;
		int len = s.length();
		if (len == 1)
		{
			cout << "1" << endl;
			continue;
		}
		int two[MAX_LEN];
		s[0] -= '0';
		for (int i = 1; i < len; ++i)
		{
			s[i] -= '0';
			two[i] = s[i-1] * 10 + s[i];
		}
		int  ways[MAX_LEN] = {0};
		ways[0] = 1;
		if (s[1] == 0)
			ways[1] = 0;
		else
			ways[1] = 1;
		if (check_in_range(two[1]))
		{
			ways[1]++;
		}
		for (int i = 2; i < len; ++i)
		{
			if (s[i] == 0)
			{
				ways[i] = 0;
			}
			else
			{
				ways[i] = ways[i-1];
			}
			if (check_in_range(two[i]))
			{
				ways[i] += ways[i-2];
			}
		}
		cout << ways[len-1] << endl;
	}
	return 0;



}
