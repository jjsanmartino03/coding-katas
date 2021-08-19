from pprint import pprint as pp

def makeFigure(n: int) -> list[list[int]]:
    result = [[0 for i in range(n)] for j in range(n)]
    posible_directions = ['r', 'b', 'l', 't']

    interval = 0
    next_pos = 0

    for i in range(n):
        quantity = n - interval

        direction = posible_directions[i % 4]

        for j in range(quantity):
            line = int(next_pos / n)
            col = next_pos % n

            result[line][col] = 1

            if j < (quantity-1):

                if(direction == 'r'):
                    next_pos += 1
                elif direction == 'b':
                    next_pos += n
                elif direction == 'l':
                    next_pos -= 1
                else:
                    next_pos -= n
            else:
                if(direction == 'r'):
                    next_pos += n
                elif direction == 'b':
                    next_pos -= 1
                elif direction == 'l':
                    next_pos -= n
                else:
                    next_pos += 1

        if (not (i % 2)) and i != 0:
            interval += 2
        elif i == 0:
            interval = 1
    # 5 4 4 2 2
    # 10 9 9 7 7 5 5 3 3 1


makeFigure(20)
