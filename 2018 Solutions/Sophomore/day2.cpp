#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int main() {
    freopen("input.in", "r", stdin);

    char letter;
    int totalTwo = 0, totalThree = 0;

    vector< vector<char> > seen;
    int ind = 0;

    while (!cin.eof()) {
        vector<int> count('z' + 1);
        vector<char> current;

        string line;
        getline(cin, line);
        for (char c: line) {
            count[c]++;

            current.push_back(c);
        }
        seen.push_back(current);

        bool hasTwo = false, hasThree = false;
        for (int i = 0; i < 'z' + 1; i++) {
            if (count[i] == 2) hasTwo = true;
            else if (count[i] == 3) hasThree = true;
        }

        if (hasTwo) totalTwo++;
        if (hasThree) totalThree++;

        for (int i = 0; i < seen.size() - 1; i++) {
            bool differing = false, isAns2 = true;
            int diffInd;
            for (int j = 0; j < seen[i].size(); j++) {
                if (seen[i][j] != current[j]) {
                    if (differing) {
                        isAns2 = false;
                        break;
                    } else {
                        differing = true;
                        diffInd = j;
                    }
                }
            }

            if (isAns2) {
                for (int j = 0; j < current.size(); j++) {
                    if (j != diffInd) cout << current[j];
                }
            }
        }

        ind++;
    }

    int ans1 = totalTwo * totalThree;
    cout << endl;
    cout << ans1 << endl;
    return 0;
}

// not 165
// not 12