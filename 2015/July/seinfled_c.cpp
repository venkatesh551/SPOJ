#include <iostream>

using namespace std;

int min_operations(const string &s)
{
    int cnt = 0, open_paren = 0;
    for (int i = 0; i < s.size(); ++i)
    {
        if (s[i] == '{')
        {
            open_paren++;
        }
        else if (open_paren > 0)
        {
            open_paren--;
        }
        else
        {
            open_paren++;
            cnt++;
        }
    }
    cnt += open_paren/2;
    return cnt;
}

int main()
{
    string s;
    for (int tc =1;  ;tc++)
    {
        cin >> s;
        if (s[0] == '-')
        {
            return 0;
        }
        cout << tc << ": " << min_operations(s) << endl;
    }

    return 0;
}
