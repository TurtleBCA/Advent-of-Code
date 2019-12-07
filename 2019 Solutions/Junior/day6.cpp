#include <iostream>
#include <unordered_map>
#include <vector>
#include <queue>

using namespace std;

void bfs (int& ans, unordered_map<string, vector<string> >& tree) {
    queue< pair<string, int> > q;
    q.push({"COM", 0});

    while (!q.empty()) {
        pair<string, int> next = q.front();
        ans += next.second;
        q.pop();

        for (string i: tree[next.first]) {
            q.push({i, next.second+1});
        }
    }
}

void bfs2 (int& ans, unordered_map<string, vector<string> >& tree, unordered_map<string, bool>& visited) {
    queue< pair<string, int> > q;
    q.push({"YOU", 0});
    visited["YOU"] = true;

    while (!q.empty()) {
        pair<string, int> next = q.front();
        q.pop();

        if (next.first == "SAN") {
            ans = next.second - 2;

        }

        for (string i: tree[next.first]) {
            if (visited[i]) {
                continue;
            }

            q.push({i, next.second+1});
            visited[i] = true;
        }
    }
}

int main() {
    freopen("input.in", "r", stdin);

//    Part 1

    unordered_map<string, vector<string> > tree;
    tree.insert({"COM", vector<string>()});

    string delimiter = ")";

//    int ans = 0;
//    while (!cin.eof()) {
//        string orbit;
//        cin >> orbit;
//
//        auto pos = orbit.find(delimiter);
//        string center = orbit.substr(0, pos);
//        orbit.erase(0, pos + delimiter.length());
//        string orbitee = orbit;
//
//        if (tree.find(center) == tree.end()) {
//            tree.insert({center, {orbitee}});
//        } else {
//            vector<string> newVal = tree[center];
//            newVal.push_back(orbitee);
//            tree[center] = newVal;
//        }
//    }
//
//    bfs(ans, tree);
//
//    cout << ans << endl;


//    Part 2

    int ans = 0;
    while (!cin.eof()) {
        string orbit;
        cin >> orbit;

        auto pos = orbit.find(delimiter);
        string center = orbit.substr(0, pos);
        orbit.erase(0, pos + delimiter.length());
        string orbitee = orbit;

        if (tree.find(center) == tree.end()) {
            tree.insert({center, {orbitee}});
        } else {
            vector<string> newVal = tree[center];
            newVal.push_back(orbitee);
            tree[center] = newVal;
        }

        if (tree.find(orbitee) == tree.end()) {
            tree.insert({orbitee, {center}});
        } else {
            vector<string> newVal = tree[orbitee];
            newVal.push_back(center);
            tree[orbitee] = newVal;
        }
    }

    unordered_map<string, bool> visited;

    bfs2(ans, tree, visited);
    cout << ans << endl;

    return 0;
}