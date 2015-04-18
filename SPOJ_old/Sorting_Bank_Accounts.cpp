#include <iostream>
#include <map>
#include <algorithm>
#include <string>

using namespace std;

int main(void)
{
	int t;
	string s;
	getline(cin, s);
	t = atoi(s.c_str());
	while (t-- > 0)
	{
		int n;
		getline(cin, s);
		n = atoi(s.c_str());
		
		map<string, int> m;
		for (int i = 0; i < n; ++i)
		{
			string s;
			getline(cin, s);
			m[s]++;
		}
		// Read Empty Line
		if (t > 0)
		{
			getline(cin, s);
		}
		for (map<string,int>::iterator it = m.begin(); it!=m.end(); ++it)
		{
			cout << it->first << " " << it->second << endl;
		}
		cout << endl;
	}
	return 0;
}
