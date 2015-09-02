#include <iostream>
#include <cstdio>

using namespace std;

int read_int()
{
    int c, val = 0;
    while ((c = getchar()) != EOF  && (c != '\n'))
    {
        val = val * 10 + c - '0' ;
    }
    return val;  
}

void read_pattern(char *pat)
{
    int c;
    while ((c = getchar()) != '\n')
    {
        *pat++ = c;
    }
}


int main()
{
    int pat_len;
    while ((pat_len = read_int()) > 0)
    {
        char *pat = new char[pat_len+1];
        read_pattern(pat);
        char c;
        for (int i = 0; (c = getchar()) != '\n'; ++i)
        {
        }
        delete [] pat;
    }
    return 0;
}
