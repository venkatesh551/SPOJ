#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
#include <cstdio>

using namespace std;
typedef long long LL;
typedef pair<LL, LL> PLL;

const int MAX_SIZE = 1e5 + 7;

class SegmentTree
{
	private:
		vector<PLL> v;
		int n;
	private:
		PLL merge(PLL a, PLL b)
		{
			LL values[4] = {a.first, a.second, b.first, b.second};
			sort(values, values+4);
			return make_pair(values[2], values[3]);
		};
		void build_tree(int ind, const int A[], int s, int e)
		{
			if (s == e)
			{
				v[ind] = make_pair(A[s], 0);
			}
			else
			{
				int m = (s + e)/2;
				build_tree(2*ind + 1, A, s, m);
				build_tree(2*ind + 2, A, m+1, e);
				v[ind] = merge(v[2*ind+1], v[2*ind+2]);
			}
		};
		PLL __query(int ind, int s, int e, int l, int r)
		{
			if (l > e || r < s)
			{
				return make_pair(0, 0);
			}
			else if (s >= l && e <= r)
			{
				return v[ind];
			}
			else
			{
				int m = (s + e)/2;
				return merge(
					__query(2*ind+1, s, m, l, r),
					__query(2*ind+2, m+1, e, l, r)
				);
			}
		};
		void __update(int ind, int s, int e, int pos, int ele)
		{
			if (pos < s || pos > e)
				return;
			if (s == e && s == pos)
			{
				v[ind] = make_pair(ele, 0);
			}
			else
			{
				int m = (s + e)/2;
				if (pos <= m)
					__update(2*ind + 1,  s, m, pos, ele);
				if (pos > m)
					__update(2*ind + 2, m+1, e, pos, ele);
				v[ind] = merge(v[2*ind+1], v[2*ind+2]);
			}
		}
	public:
		SegmentTree(const int A[], int n)
		{
			v.resize(4 * n);
			this->n = n;
			build_tree(0, A, 0, n-1);
		};
		PLL query(int l, int r)
		{
			return __query(0, 0, this->n-1, l, r);
		};
		void update(int i, LL x)		
		{
			__update(0, 0, this->n-1, i, x);
		}
};

int main(void)
{
	int n;
	scanf("%d", &n);
	int A[MAX_SIZE];
	for (int i = 0; i < n; ++i)
	{
		scanf("%d", &A[i]);
	}
	SegmentTree tree(A, n);		
	int q;
	scanf("%d", &q);
	while (q--)
	{
		int x, y;
		char c;
		cin >> c;
		scanf("%d%d", &x, &y);
		if (c == 'Q')
		{
			PLL result = tree.query(x-1, y-1);
			printf("%lld\n", result.first + result.second);
		}
		else
		{
			tree.update(x-1, y);
		}
		//cout << c << " " << x << " "<< y << endl;
	}
	return 0;
}




