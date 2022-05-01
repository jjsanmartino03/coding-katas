for t_case in range(int(input())):
    n = int(input())
    p = input()

    colors = {
        'U': '',
        'R': '',
        'Y': '',
        'B': '',
        'O': 'RY',
        'P': 'RB',
        'G': 'YB',
        'A': 'YBR'
    }

    count = 0

    for color in 'RYB':
        stroking = False
        for space in p:
            if space != color and not (color in colors[space]):
                if stroking:
                    stroking = False
                    count += 1
            elif space == color or (color in colors[space]):
                stroking = True
        
        if stroking:
            count += 1

    print(f'Case #{t_case+1}: {count}')
