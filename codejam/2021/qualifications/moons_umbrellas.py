for t_case in range(1, int(input()) + 1):
    [x, y, s] = input().split()
    x, y = int(x), int(y)

    for idx, char in enumerate(s):
        if char == '?':
            before = s[idx - 1]
            after = s[idx - 1]
