/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

* File Name : Distinct_Substrings.cpp

* Purpose :

* Creation Date : 24-02-2015

* Last Modified : Tuesday 24 February 2015 09:33:27 PM IST

* Created By : Venkatesh

_._._._._._._._._._._._._._._._._._._._._.*/

#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <utility>
#include <algorithm>
#include <cmath>
#include <set>
using namespace std;
typedef long long LL;

int count_distinct_substr(const string &s)
{
	int n = s.length();
	set<string> distinct_str;
	for (int i = 0; i < n; ++i)
	{
		for (int len = 1; len <= n; ++len)
		{
			distinct_str.insert(s.substr(i, len));
		}
	}
	return distinct_str.size();
}

int main()
{
	int t;
	cin >> t;
	string s;
	while (t-- > 0)
	{
		cin >> s;
		cout << count_distinct_substr(s) << endl;
	}
	return 0;
}
