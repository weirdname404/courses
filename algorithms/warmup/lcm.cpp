// Given two integers a and b, find their least common multiple.

#include <iostream>

using namespace std;

int gcd_euclid(long a, long b) {
    if (a % b == 0) {
        return b;
    }
    int gcd = gcd_euclid(b, a % b);
    return gcd;
}

long long lcm(long a, long b) {
    long long mult = a * b;
    return (long long) mult / gcd_euclid(a, b);
}

int main() {
    long a, b;
    cin >> a >> b;
    cout << lcm(a, b) << endl;
    return 0;
}
