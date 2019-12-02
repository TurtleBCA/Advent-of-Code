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
//    string line;
//    getline(cin, line);
//
//    vector<int> nums;
//    string delimiter = ",";
//    auto pos = line.find(delimiter);
//    while (pos != -1) {
//        int num = stoi(line.substr(0, pos));
//        nums.push_back(num);
//        line.erase(0, pos + delimiter.length());
//        pos = line.find(delimiter);
//    }
//
//    int num = stoi(line);
//    nums.push_back(num);
//
//    nums[1] = 12;
//    nums[2] = 2;
//
//    int current = 0;
//    while (nums[current] != 99) {
//        if (nums[current] == 1) {
//            int result = nums[nums[current+1]] + nums[nums[current+2]];
//            nums[nums[current+3]] = result;
//        } else {
//            int result = nums[nums[current+1]] * nums[nums[current+2]];
//            nums[nums[current+3]] = result;
//        }
//        current += 4;
//    }
//    cout << nums[0];

//    Part 2
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


    for (int i = 0; i < 100; i++) {
        nums[1] = i;
        for (int j = 0; j < 100; j++) {
            nums[2] = j;
            if (runProgram(nums) == 19690720) {
                cout << 100 * i + j;
                break;
            }
        }
    }
    return 0;
}

