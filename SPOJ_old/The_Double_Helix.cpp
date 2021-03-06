#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int get_maxSum(const vector<int> &a, const vector<int> &b) 
{
	int sum(0), a_sum(0), b_sum(0);
	int n = a.size(), m = b.size();
	int i = 0, j = 0;
	while (i < n && j < m)
	{
		if (a[i] < b[j])
		{
			a_sum += a[i];
			++i;
		}
		else if (a[i] > b[j])
		{
			b_sum += b[j];
			++j;
		}
		else
		{
			a_sum += a[i];
			b_sum += b[j];
			sum += max(a_sum, b_sum);
			a_sum = b_sum = 0;
			++i, ++j;
		}
	}
	while (i < n)
	{
		a_sum += a[i];
		++i;
	}
	while (j < m)
	{
		b_sum += b[j];
		++j;
	}
	return sum + max(a_sum, b_sum);
}

void read(vector<int> &v)
{
	int n;
	
	cin >> n;
	for (int i = 0; i < n; ++i)
	{
		int x;
		cin >> x;
		v.push_back(x);
	}
}

int main(void)
{
	while (true)
	{
		vector<int> seq_a, seq_b;
		read(seq_a);
		if (seq_a.size() == 0)
			break;
		read(seq_b);
		cout << get_maxSum(seq_a, seq_b) << endl;
	}
	return 0;
}
