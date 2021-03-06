#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void print_common_chars(const string &a, const string &b)
{
	int m[26] = {0};
	for (size_t i = 0; i < a.length(); ++i)
	{
		int v = a[i] - 'a';
		++m[v];
	}
	vector<char> v;
	for (size_t i = 0; i < b.length(); ++i)
	{
		int c = b[i] - 'a';
		if (m[c] > 0)
		{
			v.push_back(b[i]);
			--m[c];
		}
	}
	sort(v.begin(), v.end());
	for (size_t i = 0; i < v.size(); ++i)
	{
		cout << v[i];
	}
	cout << endl;
}

int main(void)
{
	string a, b;
	while (cin >> a >> b)
	{
		print_common_chars(a, b);
	}
	return 0;
}
