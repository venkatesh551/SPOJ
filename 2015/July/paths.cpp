#include <iostream>
using namespace std;
const int MAX = 15;
int dp[MAX][MAX] = {0};
void pre_calculate(){
    for (int i = 0; i < MAX; ++i){
        for (int j = 0; j < MAX; ++j){
            if (i == 0 || j == 0)
            {
                dp[i][j] = 1;
            }
            else
            {
                dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
    }
}
int main()
{
    int tc;
    cin >> tc;
    pre_calculate();
    while (tc--)
    {
        int n;
        cin >> n;
        cout << dp[n][n] << endl;
    }
    return 0;
}