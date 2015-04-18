#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <cstdlib>

using namespace std;
int longest_contiguous_seq_words(const vector<int> &v)
{
	int cnt = 1, result = 0;
	
	for (size_t i = 1; i < v.size(); ++i)
	{
		if (v[i] == v[i-1])
		{
			++cnt;
		}
		else
		{
			result = max(result, cnt);	
			cnt = 1;
		}
	}
	return max(result, cnt);
}

int main()
{
	stringstream ss;
	string word, line;
	getline(cin, line);
	int t = atoi(line.c_str());
	while (t-- > 0)
	{
		getline(cin, line);
		ss.clear();
		ss << line;
		vector<int> v;
		while (ss >> word)
		{
			v.push_back(word.length());
		}
		cout << longest_contiguous_seq_words(v) << endl;
	}
	return 0;
}
