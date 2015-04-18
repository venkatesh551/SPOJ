#include <iostream>
using namespace std;

class Test
{
	public:
		virtual int add(int x) = 0;
		void print(int n)
		{
			cout << n + add(n) << endl;
		}
};

class B : public Test
{
	public:
		int add(int x)
		{
			return 10;
		}
};

int main()
{
	Test *a = new B();
	a->print(10);
	return 0;
}
