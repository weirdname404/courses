#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>

using namespace std;


int64_t MaxPairwiseProductFast(const vector<int>& numbers) {
  int n = numbers.size();
  int max_value_i1 = (numbers[0] > numbers[1] ? 0 : 1);
  int max_value_i2 = (max_value_i1 == 0 ? 1 : 0);

  for (int i = 2; i < n; ++i) {
    if (numbers[i] > numbers[max_value_i1] && numbers[i] > numbers[max_value_i2]) {
        max_value_i2 = max_value_i1;
        max_value_i1 = i;
    } else if (numbers[i] > numbers[max_value_i2] && numbers[i] <= numbers[max_value_i1]) {
        max_value_i2 = i;
    }
  }

  return (int64_t)numbers[max_value_i1] * numbers[max_value_i2];
}


int64_t MaxPairwiseProduct(const vector<int>& numbers) {
  int64_t max_product = 0;
  int n = numbers.size();

  for (int first = 0; first < n; ++first) {
    for (int second = first + 1; second < n; ++second) {
        int64_t res = numbers[first] * numbers[second];
        max_product = (res >= max_product ? res : max_product);

    }
  }

  return max_product;
}


int main() {
  int n;
  cin >> n;
  vector<int> numbers(n);
  for (int i = 0; i < n; ++i) {
      cin >> numbers[i];
  }

  int64_t result = MaxPairwiseProductFast(numbers);
  cout << result << "\n";
  return 0;
}
