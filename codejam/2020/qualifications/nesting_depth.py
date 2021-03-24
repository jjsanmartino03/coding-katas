t = int(input())

for t_case in range(1, t + 1):
    s = input()

    s_digits = list(map(int, s))
    lat_num = 0
    current_parenthesis_num = 0
    result = ""

    for digit in s_digits:
        if digit:
            if not result or result[-1] == '0':
                result += '(' + str(digit)
            else:
                result += str(digit)
        else:
            if (not result) or (result[-1] == '0'):
                result += str(digit)
            else:
                result += ')' + str(digit)

    if result[-1] != '0' and result[-1] != ')':
        result += ')'

    print(f'Case #{t_case}: {result}')

