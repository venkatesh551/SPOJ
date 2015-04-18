#include <iostream>

using namespace std;

int main()
{
	
	while (1)
	{
		int n;
		
		cin >> n;
		if (n == -1)
		{
			break;
		}
		int x;
		
		for (x = 0; 3 * x * (x + 1) < (n - 1); x++)
			;
		if (x * (x + 1) * 3 == (n - 1))
		{
			cout << "Y" << endl;
		}
		else
		{
			cout << "N" << endl;
		}
	}


	return 0;
}
