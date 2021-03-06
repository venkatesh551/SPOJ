#include <iostream>
#include <vector>
#include <set>

using namespace std;
const int MAX = 5e5;
int main(void)
{
	vector<int> seq(MAX);
	set<int> s;
	seq[0] = 0;
	s.insert(0);
	for (int i = 1; i <= MAX; ++i)
	{
		seq[i] = seq[i-1] - i;
		if (seq[i] <= 0 || s.count(seq[i]) > 0)
		{
			seq[i] = seq[i-1] + i;
		}
		s.insert(seq[i]);
	}
	int k;
	while ((cin >> k) && k != -1)
	{
		cout << seq[k] << endl;
	}
	return 0;
}
