for t_case in range(int(input())):
    s = input()
    f = input()

    count = 0

    for letter in s:
        if not (letter in f):
            min_ops = False

            for favorite in f:
                ops = min([
                    abs(ord(letter) - ord(favorite)),
                    (122 - ord(letter)) + (ord(favorite) - 97) + 1,
                    (122 - ord(favorite)) + (ord(letter) - 97) + 1
                ])

                if min_ops is False:
                    min_ops = ops
                elif ops < min_ops:
                    min_ops = ops

            count += min_ops

    print(f'Case #{t_case+1}: {count}')
