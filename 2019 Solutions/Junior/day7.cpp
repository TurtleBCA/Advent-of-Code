#include <iostream>
#include <vector>
#include <string>

using namespace std;

int runProgram(vector<int> nums, int phase, int input) {
    int current = 0;
    int opcode = nums[current] % 100;
    bool gotSetting = false;
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
            if (gotSetting) {
                p1 = input;
            } else {
                p1 = phase;
                gotSetting = true;
            }

            nums[nums[current+1]] = p1;

            current += 2;
        } else if (opcode == 4) {
            int p1 = (p[0] ? nums[current+1] : nums[nums[current+1]]);
            return p1;
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
}

int runProgram2(vector<int> nums, vector<int> setting) {
    vector< vector<int> > instructions(5, vector<int>(nums.begin(), nums.end()));
    vector<int> instructionPointer(5);
    int currentAmp = 0;
    int opcode = instructions[currentAmp][instructionPointer[currentAmp]] % 100;
    vector<bool> gotSetting(5);
    int input = 0;
    while (!(currentAmp == 4 && instructions[currentAmp][instructionPointer[4]] % 100 == 99) ) {
        opcode = instructions[currentAmp][instructionPointer[currentAmp]] % 100;

        if (opcode == 99) {
            currentAmp = (currentAmp + 1) % 5;
            continue;
        }

        int parameters = instructions[currentAmp][instructionPointer[currentAmp]] / 100;

        vector<int> p(3);
        for (int i = 0; i < 3; i++) {
            p[i] = parameters % 10;
            parameters /= 10;
        }

        if (opcode == 1) {
            int p1 = (p[0] ? instructions[currentAmp][instructionPointer[currentAmp]+1] : instructions[currentAmp][instructions[currentAmp][instructionPointer[currentAmp]+1]]);
            int p2 = (p[1] ? instructions[currentAmp][instructionPointer[currentAmp]+2] : instructions[currentAmp][instructions[currentAmp][instructionPointer[currentAmp]+2]]);

            instructions[currentAmp][instructions[currentAmp][instructionPointer[currentAmp]+3]] = p1+p2;

            instructionPointer[currentAmp] += 4;
        } else if (opcode == 2) {
            int p1 = (p[0] ? instructions[currentAmp][instructionPointer[currentAmp]+1] : instructions[currentAmp][instructions[currentAmp][instructionPointer[currentAmp]+1]]);
            int p2 = (p[1] ? instructions[currentAmp][instructionPointer[currentAmp]+2] : instructions[currentAmp][instructions[currentAmp][instructionPointer[currentAmp]+2]]);

            instructions[currentAmp][instructions[currentAmp][instructionPointer[currentAmp]+3]] = p1*p2;

            instructionPointer[currentAmp] += 4;
        } else if (opcode == 3) {
            int p1;
            if (gotSetting[currentAmp]) {
                p1 = input;
            } else {
                p1 = setting[currentAmp];
                gotSetting[currentAmp] = true;
            }

            instructions[currentAmp][instructions[currentAmp][instructionPointer[currentAmp]+1]] = p1;

            instructionPointer[currentAmp] += 2;
        } else if (opcode == 4) {
            int p1 = (p[0] ? instructions[currentAmp][instructionPointer[currentAmp]+1] : instructions[currentAmp][instructions[currentAmp][instructionPointer[currentAmp]+1]]);
            input = p1;
            instructionPointer[currentAmp] += 2;

            currentAmp = (currentAmp + 1) % 5;
        } else if (opcode == 5) { // Part 2
            int p1 = (p[0] ? instructions[currentAmp][instructionPointer[currentAmp]+1] : instructions[currentAmp][instructions[currentAmp][instructionPointer[currentAmp]+1]]);
            if (p1) {
                instructionPointer[currentAmp] = (p[1] ? instructions[currentAmp][instructionPointer[currentAmp]+2] : instructions[currentAmp][instructions[currentAmp][instructionPointer[currentAmp]+2]]);
            } else {
                instructionPointer[currentAmp] += 3;
            }
        } else if (opcode == 6) {
            int p1 = (p[0] ? instructions[currentAmp][instructionPointer[currentAmp]+1] : instructions[currentAmp][instructions[currentAmp][instructionPointer[currentAmp]+1]]);
            if (!p1) {
                instructionPointer[currentAmp] = (p[1] ? instructions[currentAmp][instructionPointer[currentAmp]+2] : instructions[currentAmp][instructions[currentAmp][instructionPointer[currentAmp]+2]]);
            } else {
                instructionPointer[currentAmp] += 3;
            }
        } else if (opcode == 7) {
            int p1 = (p[0] ? instructions[currentAmp][instructionPointer[currentAmp]+1] : instructions[currentAmp][instructions[currentAmp][instructionPointer[currentAmp]+1]]);
            int p2 = (p[1] ? instructions[currentAmp][instructionPointer[currentAmp]+2] : instructions[currentAmp][instructions[currentAmp][instructionPointer[currentAmp]+2]]);

            instructions[currentAmp][instructions[currentAmp][instructionPointer[currentAmp]+3]] = (p1 < p2);

            instructionPointer[currentAmp] += 4;
        } else if (opcode == 8) {
            int p1 = (p[0] ? instructions[currentAmp][instructionPointer[currentAmp]+1] : instructions[currentAmp][instructions[currentAmp][instructionPointer[currentAmp]+1]]);
            int p2 = (p[1] ? instructions[currentAmp][instructionPointer[currentAmp]+2] : instructions[currentAmp][instructions[currentAmp][instructionPointer[currentAmp]+2]]);

            instructions[currentAmp][instructions[currentAmp][instructionPointer[currentAmp]+3]] = (p1 == p2);

            instructionPointer[currentAmp] += 4;
        }
    }

    return input;
}



int main() {
    freopen("input.in", "r", stdin);

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

//    Part 1
//    int ans = 0;
//    vector<bool> taken(5);
//    for (int a = 0; a < 5; a++) {
//        taken[a] = true;
//        for (int b = 0; b < 5; b++) {
//            if (taken[b]) continue;
//            taken[b] = true;
//            for (int c = 0; c < 5; c++) {
//                if (taken[c]) continue;
//                taken[c] = true;
//                for (int d = 0; d < 5; d++) {
//                    if (taken[d]) continue;
//                    taken[d] = true;
//                    for (int e = 0; e < 5; e++) {
//                        if (taken[e]) continue;
//                        int aRes = runProgram(nums, a, 0);
//                        int bRes = runProgram(nums, b, aRes);
//                        int cRes = runProgram(nums, c, bRes);
//                        int dRes = runProgram(nums, d, cRes);
//                        ans = max(ans, runProgram(nums, e, dRes));
//                    }
//                    taken[d] = false;
//                }
//                taken[c] = false;
//            }
//            taken[b] = false;
//        }
//        taken[a] = false;
//    }
//
//    cout << ans << endl;

//    Part 2
    int ans = 0;
    vector<bool> taken(5);
    for (int a = 5; a < 10; a++) {
        taken[a] = true;
        for (int b = 5; b < 10; b++) {
            if (taken[b]) continue;
            taken[b] = true;
            for (int c = 5; c < 10; c++) {
                if (taken[c]) continue;
                taken[c] = true;
                for (int d = 5; d < 10; d++) {
                    if (taken[d]) continue;
                    taken[d] = true;
                    for (int e = 5; e < 10; e++) {
                        if (taken[e]) continue;
                        ans = max(ans, runProgram2(nums, {a, b, c, d, e}));
                    }
                    taken[d] = false;
                }
                taken[c] = false;
            }
            taken[b] = false;
        }
        taken[a] = false;
    }

    cout << ans << endl;


    return 0;
}

