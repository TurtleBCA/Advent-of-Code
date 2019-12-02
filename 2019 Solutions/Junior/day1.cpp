#include <iostream>

using namespace std;

int main() {
    freopen("input.in", "r", stdin);

//    Part 1
//    int ans = 0;
//
//    while (!cin.eof()) {
//        int n;
//        cin >> n;
//        ans += (n / 3 - 2);
//    }
//
//    cout << ans << endl;


//    Part 2
    int ans = 0;

    while (!cin.eof()) {
        int n;
        cin >> n;
        n = n / 3 - 2;
        while (n > 0) {
            ans += n;
            n = n / 3 - 2;
        }
    }

    cout << ans << endl;
    return 0;
}