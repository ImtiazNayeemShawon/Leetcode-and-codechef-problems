#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <stack>
#include <bitset>
#include <iomanip>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for (int l = 0; l < t; l++)
    {
        int N;
        cin >> N;
        int A[N];
        int count[N + 1];
        for (int i = 0; i < N; i++)
        {
            cin >> A[i];
            count[A[i]]++;
        }

        int maxFreq = 0;
        for (int i = 1; i <= N; i++)
        {
            if (count[i] > maxFreq)
                maxFreq = count[i];
        }

        cout << 1 + (N - maxFreq) << "\n";
    }
    return 0;
}