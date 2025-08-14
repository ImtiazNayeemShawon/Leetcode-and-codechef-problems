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
    // your code goes here
    int t;
    cin >> t;

    for (int i = 0; i < t; i++)
    {
        int N;
        cin >> N;
        int arr[N];

        for (int num = 0; num < N; num++)
        {
            cin >> arr[num];
        }
        int onHand = arr[0];
        int result = 1;
        for (int j = 1; j < N; j++)
        {
            if (arr[j] > onHand)
            {
                onHand = arr[j];
                result = j + 1;
            }
        }

        cout << result << endl;
    }
}