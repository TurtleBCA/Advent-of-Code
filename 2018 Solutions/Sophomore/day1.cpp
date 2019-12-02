#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int main() {
    int num, ans1, ans2;
    vector<int> nums;
    vector<int> frequency;

    freopen("input.in", "r", stdin);

    frequency.push_back(0);

    while (!cin.eof()) {
        cin >> num;
        nums.push_back(num);
    }

    for (int i = 0; i < nums.size(); i++) {
        ans1 += nums[i];
    }

    cout << ans1 << endl;

    int i = 0, sum = 0;
    while (true) {
        sum += nums[i];

        if (find(frequency.begin(), frequency.end(), sum) != frequency.end()) {
            ans2 = sum;
            break;
        } else {
            frequency.push_back(sum);
        }

        i = (i + 1) % nums.size();
    }
    cout << ans2 << endl;
    return 0;
}