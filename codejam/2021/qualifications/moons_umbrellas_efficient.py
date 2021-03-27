def get_cost(s, x, y):
    x_cost = x * s.count('CJ')
    y_cost = y * s.count('JC')
    return x_cost + y_cost


for t_case in range(1, int(input())+1):
    [x, y, s] = input().split()
    x, y = int(x), int(y)
    s = list(s)
    prices = {'CJ': x, 'JC': y, 'JJ': 0, 'CC': 0}
    # CJ -> x, JC -> y
    # ??J???

    for index, letter in enumerate(s):
        if letter == '?':
            before = s[index - 1] if index > 0 else None
            after = s[index + 1] if index < len(s) - 1 else None

            if before and after:
                if after != '?':
                    s[index] = 'C' if get_cost(before + 'C' + after, x, y) <= get_cost(before + 'J' + after, x, y) else 'J'
                else:
                    s[index] = before
            elif before and not after:
                s[index] = before
            elif after and not before:
                if after != '?':
                    s[index] = after
                else:
                    counting = index + 1
                    while counting < len(s) and s[counting] == '?':
                        counting += 1
                    if counting == len(s):
                        s = ''
                        break
                    s[index] = s[counting]
        else:
            s[index] = letter
    best_cost = get_cost(''.join(s), x, y)
    print(f'Case #{t_case}: {best_cost}')

