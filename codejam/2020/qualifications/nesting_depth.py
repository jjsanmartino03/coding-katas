"""
4
021
312
4
221
"""
t = int(input())

for t_case in range(1, t + 1):
    s = input()

    s_digits = list(map(int, s))
    lat_num = 0
    current_nesting = 0
    result = ""

    for index, digit in enumerate(s_digits):
        if current_nesting > digit:
            result += ')' * (current_nesting - digit)
            result += str(digit)
            current_nesting -= current_nesting - digit
        elif current_nesting == digit:
            result += str(digit)
        elif current_nesting < digit:
            result += '(' * (digit - current_nesting)
            current_nesting += digit-current_nesting
            result += str(digit)

        if index == len(s_digits)-1:
            result += ')' * current_nesting


    print(f'Case #{t_case}: {result}')
