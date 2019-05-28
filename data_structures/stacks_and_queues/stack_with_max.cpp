#include <iostream>
#include <vector>
#include <string>
#include <cassert>
#include <algorithm>

using std::cin;
using std::string;
using std::vector;
using std::cout;
using std::max_element;

class StackWithMax {
    vector<int> stack;
    vector<int> auxiliary_stack;

  public:

    void Push(int value) {
        stack.push_back(value);
        int a_stack_size = auxiliary_stack.size();

        if (a_stack_size > 0) {
            int last_symbol = auxiliary_stack[a_stack_size - 1];

            if (value > last_symbol) {
              auxiliary_stack.push_back(value);
            } else {
              auxiliary_stack.push_back(last_symbol);
            }
          } else {
            auxiliary_stack.push_back(value);
          }
    }

    void Pop() {
        assert(stack.size());
        stack.pop_back();
        auxiliary_stack.pop_back();
    }

    int Max() const {
        int stack_size = stack.size();
        assert(stack_size > 0);
        return auxiliary_stack[stack_size - 1];
    }
};

int main() {
    int num_queries = 0;
    cin >> num_queries;

    string query;
    string value;

    StackWithMax stack;

    for (int i = 0; i < num_queries; ++i) {
        cin >> query;
        if (query == "push") {
            cin >> value;
            stack.Push(std::stoi(value));
        }
        else if (query == "pop") {
            stack.Pop();
        }
        else if (query == "max") {
            cout << stack.Max() << "\n";
        }
        else {
            assert(0);
        }
    }
    return 0;
}
