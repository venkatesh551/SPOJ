#include <iostream>
#include <stack>

using namespace std;

int min_changes_make_stable(const string &s)
{
	stack<char> ch_stk;
	int cnt = 0;
	int n = s.size();
	for (int i = 0; i < n; ++i)
	{
		if (s[i] == '{')
		{
			ch_stk.push('{');
		}
		else
		{
			if (ch_stk.empty())
			{
				ch_stk.push('{');	
				++cnt;
			}
			else
			{
				ch_stk.pop();
			}
		}
	}
	return cnt + ch_stk.size()/2;
}

int main(void)
{
	string s;
	for (int i = 1; (cin >> s) && s[0] != '-'; ++i)
	{
		cout << i << ". " << min_changes_make_stable(s) << endl;
	}
	return 0;
}
