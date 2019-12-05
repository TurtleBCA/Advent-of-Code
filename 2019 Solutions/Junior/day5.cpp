#include <iostream>
#include <vector>
#include <string>

using namespace std;

int runProgram(vector<int> nums) {
    int current = 0;
    while (nums[current] != 99) {
        if (nums[current] == 1) {
            int result = nums[nums[current+1]] + nums[nums[current+2]];
            nums[nums[current+3]] = result;
        } else {
            int result = nums[nums[current+1]] * nums[nums[current+2]];
            nums[nums[current+3]] = result;
        }
        current += 4;
    }
    return nums[0];
}

int main() {
    freopen("input.in", "r", stdin);

//    Part 1
    string line;
    getline(cin, line);

    vector<int> nums;
    string delimiter = ",";
    auto pos = line.find(delimiter);
    while (pos != -1) {
        int num = stoi(line.substr(0, pos));
        nums.push_back(num);
        line.erase(0, pos + delimiter.length());
        pos = line.find(delimiter);
    }

    int num = stoi(line);
    nums.push_back(num);

    int current = 0;
    int opcode = nums[current] % 100;
    while (opcode != 99) {
        int parameters = nums[current] / 100;

        vector<int> p(3);
        for (int i = 0; i < 3; i++) {
            p[i] = parameters % 10;
            parameters /= 10;
        }

        if (opcode == 1) {
            int p1 = (p[0] ? nums[current+1] : nums[nums[current+1]]);
            int p2 = (p[1] ? nums[current+2] : nums[nums[current+2]]);

            nums[nums[current+3]] = p1+p2;

            current += 4;
        } else if (opcode == 2) {
            int p1 = (p[0] ? nums[current+1] : nums[nums[current+1]]);
            int p2 = (p[1] ? nums[current+2] : nums[nums[current+2]]);

            nums[nums[current+3]] = p1*p2;

            current += 4;
        } else if (opcode == 3) {
            int p1;
            cin >> p1;
            nums[nums[current+1]] = p1;

            current += 2;
        } else if (opcode == 4) {
            int p1 = (p[0] ? nums[current+1] : nums[nums[current+1]]);
            cout << p1 << endl;

            current += 2;
        } else if (opcode == 5) { // Part 2
            int p1 = (p[0] ? nums[current+1] : nums[nums[current+1]]);
            if (p1) {
                current = (p[1] ? nums[current+2] : nums[nums[current+2]]);
            } else {
                current += 3;
            }
        } else if (opcode == 6) {
            int p1 = (p[0] ? nums[current+1] : nums[nums[current+1]]);
            if (!p1) {
                current = (p[1] ? nums[current+2] : nums[nums[current+2]]);
            } else {
                current += 3;
            }
        } else if (opcode == 7) {
            int p1 = (p[0] ? nums[current+1] : nums[nums[current+1]]);
            int p2 = (p[1] ? nums[current+2] : nums[nums[current+2]]);

            nums[nums[current+3]] = (p1 < p2);

            current += 4;
        } else if (opcode == 8) {
            int p1 = (p[0] ? nums[current+1] : nums[nums[current+1]]);
            int p2 = (p[1] ? nums[current+2] : nums[nums[current+2]]);

            nums[nums[current+3]] = (p1 == p2);

            current += 4;
        }
        opcode = nums[current] % 100;
    }
    
    return 0;
}

