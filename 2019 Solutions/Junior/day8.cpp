#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    freopen("input.in", "r", stdin);

//    Part 1
    string input;
    cin >> input;

//    int fewest0 = 150;
//    int ans = 0;
//
//    for (int i = 0; i < input.size(); i += 150) {
//        vector<int> count(3);
//        for (int j = 0; j < 150; j++) {
//            count[input[i+j]-'0']++;
//        }
//
//        if (count[0] < fewest0) {
//            fewest0 = count[0];
//            ans = count[1] * count[2];
//        }
//    }
//
//    cout << ans;

//    Part 2

    for (int y = 0; y < 6; y++) {
        for (int x = 0; x < 25; x++) {
            for (int i = x + 25 * y; i < input.size(); i += 150) {
                if (input[i] != '2') {
                    cout << input[i];
                    break;
                }
            }
        }
        cout << endl;
    }

    return 0;
}