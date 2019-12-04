#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <climits>

using namespace std;

struct Point {
    int x, y;
};

struct Line {
    Point l, r;
};

Point operator* (Point p, int a) {
    return {p.x * a, p.y * a};
}

Point operator+ (Point a, Point b) {
    return {a.x + b.x, a.y + b.y};
}

bool operator< (Point a, Point b) {
    if (a.x == b.x) {
        return a.y < b.y;
    }
    return a.x < b.x;
}

// If there is an intersection, return its distance, else INT_MAX
// a = horizontal, b = vertical
int intersectionDistance(Line a, Line b) {
    if (a.l.x <= b.l.x && b.l.x <= a.r.x && b.l.y <= a.l.y && a.l.y <= b.r.y) {
        if (abs(b.l.x) + abs(a.l.y) == 0) return INT_MAX;
        return abs(b.l.x) + abs(a.l.y);
    } else return INT_MAX;
}

int stepDistance(Line a, int aSteps, Line b, int bSteps) {
    if (a.l.x <= b.l.x && b.l.x <= a.r.x && b.l.y <= a.l.y && a.l.y <= b.r.y) {
        int result = 0;
        if (aSteps >= 0) {
            result += aSteps + (b.l.x - a.l.x);
        } else {
            result += -aSteps + (a.r.x - b.l.x);
        }

        if (bSteps >= 0) {
            result += bSteps + (a.l.y - b.l.y);
        } else {
            result += -bSteps + (b.r.y - a.l.y);
        }

        if (result == 0) return INT_MAX;
        return result;
    } else return INT_MAX;
}

/*void parseFirstWireSegments(string& wire, unordered_map<char, Point>& unitVector, Point& current, auto& pos,
        vector< pair<Line, int> >& vertical, vector< pair<Line, int> >& horizontal, int& cumulativeSteps) {
    string segmentString = wire.substr(0, pos);
    char direction = segmentString[0];
    int steps = stoi(wire.substr(1, pos));
    Point delta = unitVector[direction] * steps;
    Line segment = {min(current, current+delta), max(current, current+delta)};
    if (direction == 'R') {
        horizontal.push_back({segment, cumulativeSteps});
    } else if (direction == 'L') {
        horizontal.push_back({segment, -cumulativeSteps});
    } else if (direction == 'U') {
        vertical.push_back({segment, cumulativeSteps});
    } else {
        vertical.push_back({segment, -cumulativeSteps});
    }
    current = current + delta;
    cumulativeSteps += steps;

    wire.erase(0, pos + delimiter.length());
    pos = wire.find(delimiter);
}*/

int main() {
    freopen("input.in", "r", stdin);

    string wire;
    getline(cin, wire);

    unordered_map<char, Point> unitVector = {
            {'R', {1, 0}},
            {'U', {0, 1}},
            {'L', {-1, 0}},
            {'D', {0, -1}}};

    vector< pair<Line, int> > vertical;
    vector< pair<Line, int> > horizontal;

    Point current = {0, 0};
    string delimiter = ",";
    auto pos = wire.find(delimiter);
    int cumulativeSteps = 0;
    while (pos != -1) {
        string segmentString = wire.substr(0, pos);
        char direction = segmentString[0];
        int steps = stoi(wire.substr(1, pos));
        Point delta = unitVector[direction] * steps;
        Line segment = {min(current, current+delta), max(current, current+delta)};
        if (direction == 'R') {
            horizontal.push_back({segment, cumulativeSteps});
        } else if (direction == 'L') {
            horizontal.push_back({segment, -cumulativeSteps});
        } else if (direction == 'U') {
            vertical.push_back({segment, cumulativeSteps});
        } else {
            vertical.push_back({segment, -cumulativeSteps});
        }
        current = current + delta;
        cumulativeSteps += steps;

        wire.erase(0, pos + delimiter.length());
        pos = wire.find(delimiter);
    }

    char direction = wire[0];
    int steps = stoi(wire.substr(1, pos));
    Point delta = unitVector[direction] * steps;
    Line segment = {min(current, current+delta), max(current, current+delta)};
    if (direction == 'R') {
        horizontal.push_back({segment, cumulativeSteps});
    } else if (direction == 'L') {
        horizontal.push_back({segment, -cumulativeSteps});
    } else if (direction == 'U') {
        vertical.push_back({segment, cumulativeSteps});
    } else {
        vertical.push_back({segment, -cumulativeSteps});
    }
    current = current + delta;
    cumulativeSteps += steps;

    getline(cin, wire);

    int ans = INT_MAX;
    current = {0, 0};
    delimiter = ",";
    pos = wire.find(delimiter);

//    Part 1

//    while (pos != -1) {
//        string segmentString = wire.substr(0, pos);
//        direction = segmentString[0];
//        steps = stoi(wire.substr(1, pos));
//        delta = unitVector[direction] * steps;
//        segment = {min(current, current+delta), max(current, current+delta)};
//        if (direction == 'R' || direction == 'L') {
//            for (int i = 0; i < vertical.size(); i++) {
//                ans = min(ans, intersectionDistance(segment, vertical[i].first));
//            }
//        } else {
//            for (int i = 0; i < horizontal.size(); i++) {
//                ans = min(ans, intersectionDistance(horizontal[i].first, segment));
//            }
//        }
//        current = current + delta;
//
//        wire.erase(0, pos + delimiter.length());
//        pos = wire.find(delimiter);
//    }
//
//    direction = wire[0];
//    steps = stoi(wire.substr(1, pos));
//    delta = unitVector[direction] * steps;
//    segment = {min(current, current+delta), max(current, current+delta)};
//    if (direction == 'R' || direction == 'L') {
//        for (int i = 0; i < vertical.size(); i++) {
//            ans = min(ans, intersectionDistance(segment, vertical[i].first));
//        }
//    } else {
//        for (int i = 0; i < horizontal.size(); i++) {
//            ans = min(ans, intersectionDistance(horizontal[i].first, segment));
//        }
//    }
//    current = current + delta;

//    cout << ans;

//    Part 2

    cumulativeSteps = 0;
    while (pos != -1) {
        string segmentString = wire.substr(0, pos);
        direction = segmentString[0];
        steps = stoi(wire.substr(1, pos));
        delta = unitVector[direction] * steps;
        segment = {min(current, current+delta), max(current, current+delta)};
        if (direction == 'R') {
            for (int i = 0; i < vertical.size(); i++) {
                ans = min(ans, stepDistance(segment, cumulativeSteps, vertical[i].first, vertical[i].second));
            }
        } else if (direction == 'L') {
            for (int i = 0; i < vertical.size(); i++) {
                ans = min(ans, stepDistance(segment, -cumulativeSteps, vertical[i].first, vertical[i].second));
            }
        } else if (direction == 'U') {
            for (int i = 0; i < horizontal.size(); i++) {
                ans = min(ans, stepDistance(horizontal[i].first, horizontal[i].second, segment, cumulativeSteps));
            }
        } else {
            for (int i = 0; i < horizontal.size(); i++) {
                ans = min(ans, stepDistance(horizontal[i].first, horizontal[i].second, segment, -cumulativeSteps));
            }
        }
        current = current + delta;
        cumulativeSteps += steps;

        wire.erase(0, pos + delimiter.length());
        pos = wire.find(delimiter);
    }

    direction = wire[0];
    steps = stoi(wire.substr(1, pos));
    delta = unitVector[direction] * steps;
    segment = {min(current, current+delta), max(current, current+delta)};
    if (direction == 'R') {
        for (int i = 0; i < vertical.size(); i++) {
            ans = min(ans, stepDistance(segment, cumulativeSteps, vertical[i].first, vertical[i].second));
        }
    } else if (direction == 'L') {
        for (int i = 0; i < vertical.size(); i++) {
            ans = min(ans, stepDistance(segment, -cumulativeSteps, vertical[i].first, vertical[i].second));
        }
    } else if (direction == 'U') {
        for (int i = 0; i < horizontal.size(); i++) {
            ans = min(ans, stepDistance(horizontal[i].first, horizontal[i].second, segment, cumulativeSteps));
        }
    } else {
        for (int i = 0; i < horizontal.size(); i++) {
            ans = min(ans, stepDistance(horizontal[i].first, horizontal[i].second, segment, -cumulativeSteps));
        }
    }
    current = current + delta;
    cumulativeSteps += steps;
    cout << ans << endl;
    return 0;
}

