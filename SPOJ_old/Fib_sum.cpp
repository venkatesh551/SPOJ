#include <iostream>
#include <utility>

using namespace std;
const int ROW = 2;
const int COL = 2;
const int P = 1e9 + 7;
typedef long long LL;
typedef pair<int, int> pii;

void copy_matrix(int src[][COL], int dest[][COL])
{
	for (int i = 0; i < ROW; ++i)
	{
		for (int j = 0; j < COL; ++j)
		{
			dest[i][j] = src[i][j];
		}
	}
}

void mat_mul(int A[][COL], int B[][COL], int C[][COL])
{
	int result[ROW][COL];
	
	for (int i = 0; i < ROW; ++i)
	{
		for (int j = 0; j < ROW; ++j)
		{
			result[i][j] = 0;
			for (int k = 0; k < COL; ++k)
			{
				result[i][j] = (result[i][j] + (LL) A[i][k] * B[k][j]) % P;
			}
		}
	}
	copy_matrix(result, C);	
}

void mat_exp(int A[][COL], int power)
{
	int result[ROW][COL] = {{1, 0}, 
							{0, 1}
							};
	LL n = power;
	while (n > 0)
	{
		if (n & 1)
		{
			mat_mul(result, A, result);
		}
		mat_mul(A, A, A);
		n >>= 1;
	}	
	copy_matrix(result, A);
}

pii get_nth_fibonacci(int n)
{
	if (n == 0)
	{
		return make_pair(0, 1);
	}
	int m[ROW][COL] = { {1, 1}, 
						{1, 0}
					  };
	mat_exp(m, n);
	return make_pair(m[1][0], m[0][0]);	
}

int main(void)
{
	int t;
	
	cin >> t;
	while (t-- > 0)
	{
		int n, m;
		
		cin >> n >> m;
		pii num = get_nth_fibonacci(n);
		if (n == m)
		{
			cout << num.first << endl;
			continue;
		}
		int a = num.first;
		int b = num.second;
		int sum = ((LL)a + b) % P;
		for (int i = n+2; i <= m; ++i)
		{
			int c = ((LL)a + b) % P;
			a = b;
			b = c;
			sum = ((LL)sum + c) % P;
		}
		cout << sum << endl;
	}
	return 0;
}
