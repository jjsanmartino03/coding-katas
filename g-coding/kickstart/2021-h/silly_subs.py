for t_case in range(int(input())):
    input()
    s = input()

    previous_length = len(s) - 1

    while previous_length != len(s):
        previous_length = len(s)

        for i in range(1, 11):
            substring = f'{i-1}{i%10}'

            s = s.replace(substring, str((i+1) % 10))

    print(f'Case #{t_case+1}: {s}')
