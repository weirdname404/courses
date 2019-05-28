// The goal of this problem is to represent a given positive integer n as a sum of as many pairwise
// distinct positive integers as possible.

#include <iostream>
#include <vector>

std::vector<int64_t> find_numbers(int64_t n) {
    std::vector<int64_t> nums;
    int i = 1;
    
    while (n > 2*i) {
        n -= i;
        nums.push_back(i);
        i++;
    }

    nums.push_back(n);

    return nums;
}

int main() {
    int64_t n;
    std::vector<int64_t> numbers;
    std::cin >> n;
    numbers = find_numbers(n);

    std::cout << numbers.size() << std::endl;
    
    for (int i = 0; i < numbers.size(); i++) {
        std::cout << numbers[i] << " ";
    }

    return 0;
}
