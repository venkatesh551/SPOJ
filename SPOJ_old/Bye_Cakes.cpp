#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
const int MAX = 4;

void read_input(vector<int> &v)
{
	for (int i = 0; i < MAX; ++i)
	{
		cin >> v[i];
	}
}

int main(void)
{
	vector<int> has(MAX), req(MAX);
	while (true)
	{
		read_input(has);
		read_input(req);
		if (has[0] == -1)
		{
			break;
		}
		int m = 0;
		for (int i = 0; i < MAX; ++i)
		{
			int x = (has[i] + req[i] - 1)/req[i];
			m = max(m, x);
		}
		for (int i = 0; i < MAX; ++i)
		{
			cout << req[i] * m - has[i] << " ";
		}
		cout << endl;
	}
	return 0;
}
