for t_case in range(int(input())):
    input()
    s = input()

    order = ['01', '12', '23', '34', '45', '56', '67', '78', '89', '90']

    index = 0
    while index < (len(s) - 1):
        a, b = int(s[index]), int(s[index+1])

        if (a + 1) % 10 == b:
            replacer = str((b+1) % 10)
            if index < (len(s)-2):
                d = int(s[index+2])

                if ((b + 1) % 10 == d) and (order.index(f'{b}{d}') < order.index(f'{a}{b}')):
                    index += 1
                else:
                    s = s[:index] + replacer + s[index+2:]
            else:
            	s = s[:index] + replacer + s[index+2:]
        else:
            index += 1

    print(f'Case #{t_case+1}: {s}')
