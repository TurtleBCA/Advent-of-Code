#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

struct Patch {
    int x, y, width, length;
};

int main() {
    freopen("input.in", "r", stdin);

    enum class Status : int { FREE, COVERED, OVERLAPPED };

    vector< vector<int> > space(1000, vector<int>(1000));
    vector<Patch> patches;

    while (!cin.eof()) {
        string line;
        getline(cin, line);

        int x, y, width, length;
        string delimiter = "#", token;
        line.erase(0, line.find(delimiter) + delimiter.length());
        delimiter = " @ ";
        line.erase(0, line.find(delimiter) + delimiter.length());

        delimiter = ",";
        token = line.substr(0, line.find(delimiter));
        x = stoi(token);
        line.erase(0, line.find(delimiter) + delimiter.length());

        delimiter = ": ";
        token = line.substr(0, line.find(delimiter));
        y = stoi(token);
        line.erase(0, line.find(delimiter) + delimiter.length());

        delimiter = "x";
        token = line.substr(0, line.find(delimiter));
        width = stoi(token);
        line.erase(0, line.find(delimiter) + delimiter.length());

        length = stoi(line);

        patches.push_back({x, y, width, length});

        for (int i = y; i < y + length; i++) {
            for (int j = x; j < x + width; j++) {
                if (space[i][j] == (int)Status::FREE) {
                    space[i][j] = (int)Status::COVERED;
                } else if (space[i][j] == (int)Status::COVERED) {
                    space[i][j] = (int)Status::OVERLAPPED;
                }
            }
        }
    }

    int ans1 = 0;
    for (int i = 0; i < space.size(); i++) {
        for (int j = 0; j < space[i].size(); j++) {
            if (space[i][j] == (int)Status::OVERLAPPED) {
                ans1++;
            }
        }
    }

    cout << ans1 << endl;

    int ans2;
    for (int i = 0; i < patches.size(); i++) {
        bool isOnly = true;
        for (int j = patches[i].y; j < patches[i].y + patches[i].length; j++) {
            for (int k = patches[i].x; k < patches[i].x + patches[i].width; k++) {
                if (space[j][k] == (int)Status::OVERLAPPED) {
                    isOnly = false;
                    break;
                }
            }
            if (!isOnly) break;
        }

        if (isOnly) {
            ans2 = i + 1;
            break;
        }
    }

    cout << ans2 << endl;
}
