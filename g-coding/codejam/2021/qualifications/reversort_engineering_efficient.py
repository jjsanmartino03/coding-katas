for t_case in range(1, int(input())+1):
    [n, c] = input().split()
    n, c = int(n), int(c)

    if c < n - 1:
        print(f'Case #{t_case}: IMPOSSIBLE')
    elif c == n - 1:
        print(f'Case #{t_case}: {" ".join([str(i) for i in range(1, n + 1)])}')
    else:
        pass
