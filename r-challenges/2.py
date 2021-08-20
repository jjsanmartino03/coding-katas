"""
Validate if a battleship game's field is correctly set up. Should have:
- 4 submarinos
- 3 destructores
- 2 cruceros
- 1 acorazado
Ships can't touch each other, not even with the corners.
"""

def get_size_and_validate(coords, field, direction=None):
    positions_with_ones = []
  
    x = coords[0]
    y = coords[1]

    if (x+1 <= 9) and (field[y][x+1]):
        if direction == 'y':
            return False
        direction = 'x'
        positions_with_ones.append([x+1, y])

    if (y+1 <= 9) and (field[y+1][x]):
        if direction == 'x':
            return False
        direction = 'y'
        positions_with_ones.append([x, y+1])

    if (x+1 <= 9) and (y+1 <= 9) and (field[y+1][x+1]):
        return False
    elif (x-1 >= 0) and (y+1 <= 9) and (field[y+1][x-1]):
        return False
    

    if len(positions_with_ones) > 1:
        return False
    elif len(positions_with_ones) == 1:
        other_positions = get_size_and_validate(
            positions_with_ones[0],
            field,
            direction
        )

        if(other_positions != False):
            return [
                *positions_with_ones,
                *other_positions
            ]
        else:
            return False
    else:
        return [coords]

def already_registered(coords, registered):
    for x,y in registered:
        if (x == coords[0]) and (y==coords[1]):
            return True
    
    return False

def validate(field: list[list[int]]) -> bool:
    registered = []
    ships = {
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
    }

    for y in range(10):
        for x in range(10):
            if field[y][x] == 1 and (not already_registered([x,y], registered)):
                current_ship = get_size_and_validate([x,y], field)

                if current_ship == False:
                    return False
                else:
                    registered += current_ship
                    size = len(current_ship)

                    if (size > 4):
                        return False                    

                    ships[ str(size) ] += 1

    correct_submarines = ships['1'] != 4
    correct_destr = ships['2'] != 3
    correct_cruises = ships['3'] != 2
    correct_acor = ships['4'] != 1 

    if correct_submarines or correct_destr or correct_cruises or correct_acor:
        return False
    else:
        return True
        
                    


def tests():
    validField = [
        [1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
        [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    invalidField = [
        [1, 0, 0, 1, 0, 1, 1, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
        [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    if (validate(validField) == False):
        print("The program fails to recognize a valid field")
    elif (validate(invalidField)):
        print("The program fails to recognize an invalid battle field")
    else:
        print("The program validates the initial test cases correctly")


tests()
