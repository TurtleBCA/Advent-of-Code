#include <iostream>
#include <vector>

using namespace std;

int power(int b, int p) {
    if (p == 0) return 1;

    int halfResult = power(b, p/2);
    if (p % 2 == 0) {
        return (halfResult * halfResult);
    } else {
        return ((halfResult * halfResult) * b);
    }
}

// Part 1
//int checkNumber(int n) {
//    bool hasTwoSame = false;
//    for (int i = 1; i <= 5; i++) {
//        int currentDigit = n % 10;
//        n /= 10;
//        int previous = n % 10;
//        if (previous > currentDigit) return 0;
//        if (previous == currentDigit) hasTwoSame = true;
//    }
//    return hasTwoSame;
//}

// Part 2
int checkNumber(int n) {
    bool notPartOfGreater = false;
    int inRow = 1;
    for (int i = 1; i <= 5; i++) {
        int currentDigit = n % 10;
        n /= 10;
        int previous = n % 10;
        if (previous > currentDigit) return 0;
        if (previous == currentDigit) {
            inRow++;
        } else if (inRow == 2) {
            notPartOfGreater = true;
        } else {
            inRow = 1;
        }
    }
    return (notPartOfGreater || inRow == 2);
}

int main() {
    int ans = 0;

    for (int i = 402328; i <= 864247; i++) {
        ans += checkNumber(i);
    }

    cout << ans << endl;

}