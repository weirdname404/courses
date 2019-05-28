#include <iostream>
#include <vector>

int fib_mod(int64_t &n) {
    // the length of pisano_period(10) is 60
    int pp = 60;
    int fib_n = n % pp;

    std::vector<int> mod_seq = {0, 1};

    for (int i = 1; i < fib_n; i++) {
        int size = mod_seq.size();
        int res = (mod_seq.back() + mod_seq[size - 2]) % 10;
        mod_seq.push_back(res);
    }

    int sum = 0;

    for (int i = 0; i <= fib_n; i++) {
        sum += mod_seq[i] * mod_seq[i];
    }

    return sum % 10;
}

int main() {
    int64_t n;
    std::cin >> n;
    std::cout << fib_mod(n);

    return 0;
}
