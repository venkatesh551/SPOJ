#include <iostream>

using namespace std;

void reverse(string &s, int i, int j)
{
	while (i < j)
	{
		char c = s[i];
		s[i] = s[j];
		s[j ] = c;
		i++; j--;
	}
}

int main(void)
{
	int n;
	string s;
	
	cin >> n;
	while (n)
	{
		cin >> s;
		for (size_t i = n; i < s.size(); i += 2 * n)
		{
			reverse(s, i, i+n-1);
		}
		for (int i = 0; i < n; ++i)
		{
			for (size_t j = i; j < s.size(); j += n)
			{
				cout << s[j];
			}
		}
		cout << endl;
		cin >> n;
	}
	return 0;
}
