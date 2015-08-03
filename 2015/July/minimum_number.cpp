#include <iostream>
#include <vector>
using namespace std;

int main() {
	
	while (true)
	{
		string s;
		cin >> s;
		if (s == "-1")
		{
			return 0;
		}
		if (s == "0")
		{
			cout << "0" << endl;
			continue;
		}
		vector<int> v;
		int num = 0;
		for (int i = 0; i < s.length(); ++i)
		{
			int digit = s[i] - '0';
			num = num * 10 + digit;
			if (num >= 9)
			{
				v.push_back(num/9);
				num %= 9;
			}
			else if(v.size() > 0)
			{
				v.push_back(0);
			}
		}
		string ans = "";
		if (num > 0)
		{
			int carry = 1;
			for (int i = v.size()-1; i >= 0; --i)
			{
				int sum = v[i] + carry;
				carry = sum/10;
				v[i] = sum % 10;
			}
			if (carry)
				ans += carry + '0';
		}
		for (int i = 0; i < v.size(); ++i)
		{
			ans += v[i] + '0';
		}
		cout << ans << endl;
	}

	return 0;
}