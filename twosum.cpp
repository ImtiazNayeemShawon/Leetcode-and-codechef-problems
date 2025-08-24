#include <iostream>
#include <vector>
using namespace std;

int main()
{
    vector<int> nums = {2, 3, 4, 6};
    int target = 5;
    for (int i = 0; i < nums.size(); i++)
    {
        for (int j = i + 1; j < nums.size(); j++)
        {
            if (nums[i] + nums[j] == target)
            {
                cout << i <<","<< j;
                return 0; // Return early if a solution is found
            }
        }
    }
    cout << "No solution found." << endl;
    return 0;
}