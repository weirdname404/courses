//Given two integers a and b, find their greatest common divisor

#include <iostream>
#include <cassert>

using namespace std;

int gcd_euclid(int a, int b) {
    assert(a > 0 && b > 0);
    if (a % b == 0) {
        return b;
    }
    int gcd = gcd_euclid(b, a % b);
    return gcd;
}

int main() {
    int a, b;
    cin >> a >> b;
    cout << gcd_euclid(a, b) << endl;
    return 0;
}
