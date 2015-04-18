#include <iostream>
#include <cstdlib>

using namespace std;

bool is_num(const string &s)
{
	size_t i;
	for (i = 0; i < s.length() && isdigit(s[i]); ++i)
		;
	return i == s.length();
}

int main()
{
	int t;
	
	cin >> t;
	string a, b, c, x;
	while (t-- > 0)
	{
		cin >> a >> x >> b >> x >> c;
		if (is_num(a))
		{
			if (is_num(b))
				cout << a << " + " << b << " = " << atoi(a.c_str()) + atoi(b.c_str()) << endl;
			else
				cout << a << " + " << atoi(c.c_str()) - atoi(a.c_str()) << " = " << c << endl;
		}
		else
		{
			cout << atoi(c.c_str()) - atoi(b.c_str()) + " + " << b << " = " << c << endl;
		}
	}
	return 0;
}
