import random


def generate_str():
    return ('%06x' % random.randrange(16**6)).upper() + ('%06x' % random.randrange(16**6)).upper()


def is_used():
    return random.choice((True, False))


def generate_value(arr):
    if is_used():
        return random.choice(arr)
    return generate_str()


def main():
    n = random.randint(1, 10**5)
    m = random.randint(n//5, n)
    data = f"{m}\n{n}\n"
    cmds = tuple(range(4))
    used_words = [generate_str()]

    with open("test", "w") as f:
        f.writelines(data)
        for _ in range(n):
            cmd = random.choice(cmds)
            if cmd == 0:
                line = f"add {generate_value(used_words)}\n"

            elif cmd == 1:
                line = f"del {generate_value(used_words)}\n"
            
            elif cmd == 2:
                line = f"find {generate_value(used_words)}\n"
            
            else:
                line = f"check {random.randrange(m)}\n"
            
            f.write(line)
            

if __name__ == "__main__":
    main()

