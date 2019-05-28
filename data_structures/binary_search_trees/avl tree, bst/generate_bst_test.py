import random


def generate_append_data(n: int) -> (str, list):
    append_query = ""
    nums = []
    for _ in range(n):
        num = random.randint(MIN_NUM, MAX_NUM)
        nums.append(num)
        append_query += f"a {str(num)}\n"

    return append_query, nums


def generate_find_data(n: int, nums: list) -> (str, str):
    find_query = ""
    find_answ = ""
    nums = set(nums)

    for _ in range(n):
        num = random.randint(MIN_NUM, MAX_NUM)
        find_query += f"f {num}\n"
        if num in nums:
            find_answ += "FOUND\n"
        else:
            find_answ += "NOT FOUND\n"

    return find_query, find_answ


def generate_del_data(n: int, nums: list) -> str:
    del_query = ""
    for _ in range(n):
        del_num = random.choice(nums)
        del_query += f"del {del_num}\n"
        nums.remove(del_num)

    return del_query


def get_sorted_nums(nums: list) -> list:
    return sorted(nums)


def main():
    line = f"{APPEND_N + FIND_N + DEL_N + EXTRA_N}\n"

    append_query, nums = generate_append_data(APPEND_N)
    del_query = generate_del_data(DEL_N, nums)
    find_query, find_answ = generate_find_data(FIND_N, nums)

    line = line + append_query + del_query + find_query + EXTRA_CMD
    right_answ = find_answ + f"{get_sorted_nums(nums)}"

    with open("test", "w") as f:
        f.write(line)

    with open("answ", "w") as f:
        f.write(right_answ)


if __name__ == "__main__":
    MIN_NUM = -1000000
    MAX_NUM = 1000000

    APPEND_N = 300000
    DEL_N = 1000
    FIND_N = 30000
    EXTRA_N = 2
    EXTRA_CMD = "t\nb\n"
    assert len(EXTRA_CMD.strip().split("\n")) == EXTRA_N
    main()
