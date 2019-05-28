// In this task your goal is to implement a simple phone book manager.
// It should be able to process the following types of user’s queries:
//  - add num name
//  - del num
//  - find num
//
// Use the direct addressing scheme.
// Tel. num. has no more than 7 digits

#include <iostream>
#include <vector>

int main() {
    std::vector<std::string> arr(10000000);
    std::string value, command;
    int n, key;
    std::cin >> n;

    for (int i = 0; i < n; i++) {
        std::cin >> command;
        if (command == "add") {
            std::cin >> key >> value;
            arr[key] = value;

        } else {
            std::cin >> key;
            if (command == "find") {
                auto res = arr[key].empty() ? "not found" : arr[key];
                std::cout << res << std::endl;

            } else {
                arr[key].clear();
            }
        }
    }
    return 0;
}
