# python3
"""
Find optimal minimum number of coins 1, 3, 4 that could change M
"""


# count optimal changes from 1 up to m
def get_change(m):
    change_arr = [0]
    coins = [1, 3, 4]

    def count_change(money):
        if money >= len(change_arr):
            for m in range(1, money + 1):
                change_arr.append(float("inf"))

                for c in coins:
                    if m >= c:
                        coins_num = count_change(m - c) + 1
                        if coins_num < change_arr[m]:
                            change_arr[m] = coins_num
        return change_arr[money]

    return count_change(m)


def main():
    m = int(input())
    print(get_change(m))


if __name__ == "__main__":
    main()
