from itertools import product


def get_cost(s, x, y):
    x_cost = x * s.count('CJ')
    y_cost = y * s.count('JC')
    return x_cost + y_cost


for t_case in range(1, int(input()) + 1):
    [x, y, s] = input().split()
    x, y = int(x), int(y)
    # CJ -> x, JC -> y

    possible_locations = product('CJ', repeat=s.count('?'))
    best_cost = 0
    for idx, possible in enumerate(list(possible_locations)):
        possible_string = ''
        count = 0
        for letter in s:
            if letter == '?':
                possible_string += possible[count]
                count += 1
            else:
                possible_string += letter
        this_cost = get_cost(possible_string, x, y)
        if idx > 0 and this_cost < best_cost:
            best_cost = this_cost
        elif idx == 0:
            best_cost = this_cost
    print(f'Case #{t_case}: {best_cost}')
