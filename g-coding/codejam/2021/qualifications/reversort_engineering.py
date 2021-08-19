from itertools import permutations


def get_reversort_cost(numbers):
    count = 0
    for i in range(len(numbers) - 1):
        min_num = min(numbers[i:])
        min_position = numbers.index(min_num, i)

        numbers[i:min_position + 1] = reversed(numbers[i:min_position + 1])
        count += (min_position + 1) - i
    return count


for t_case in range(1, int(input()) + 1):
    n, c = input().split()
    n, c = int(n), int(c)

    possibles = permutations([i for i in range(1, n + 1)])

    for possible in possibles:
        if get_reversort_cost(list(possible)) == c:
            print(f'Case #{t_case}: {" ".join(list(map(str, possible)))}')
            break
    else:
        print(f'Case #{t_case}: IMPOSSIBLE')
