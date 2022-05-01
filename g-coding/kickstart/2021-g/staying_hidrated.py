class Object:
  def __init__(self, x1, y1, x2, y2):
    self.x1 = x1
    self.y1 = y1
    self.x2 = x2
    self.y2 = y2

  def get_all_coordinates(self):
    for x in range(self.x1, self.x2+1):
      for y in range(self.y1, self.y2+1):
        yield Coordinate(x, y)

  def get_nearest_border_coordinates(self, position):
    x_left_distance = abs(position.x - self.x1)
    x_right_distance = abs(position.x - self.x2)
    y_left_distance = abs(position.y - self.y1)
    y_right_distance = abs(position.y - self.y1)

    
    x_distance = min(x_left_distance, x_right_distance)
    y_distance = min(y_left_distance, y_right_distance)

    


  def get_border_coordinates(self):
    for y in range(self.y1, self.y2+1):
      yield Coordinate(self.x1, y)
      yield Coordinate(self.x2, y)

    for x in range(self.x1, self.x2+1):
      yield Coordinate(x, self.y1)
      yield Coordinate(x, self.y2)

  def bottom_left_corner(self):
    return Coordinate(self.x1, self.y1)

  def top_left_corner(self):
    return Coordinate(self.x1, self.y2)

  def top_right_corner(self):
    return Coordinate(self.x2, self.y2)

  def bottom_right_corner(self):
    return Coordinate(self.x2, self.y1)
  
  def __str__(self):
    matrix = []

    for y in range(self.y1, self.y2+1):
      row = []
      for x in range(self.x1, self.x2+1):
        row.append("0")

      matrix.append(", ".join(row))

    return "\n".join(matrix)
  
class Coordinate:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __sub__(self, other):
    x_steps = abs(self.x - other.x)
    y_steps = abs(self.y - other.y)

    return x_steps + y_steps

  def __str__(self):
    return f"({self.x}, {self.y})"
  


for t_case in range(1, int(input())+1):
  objects = []

  for k in range(int(input())):
    
    x1, y1, x2, y2 = list(map(int, input().split()))

    objects.append(Object(x1,y1,x2,y2))

  min_x = -100
  min_y = -100
  max_x = 100
  max_y = 100

  room = Object(min_x, min_y, max_x, max_y)
  min_sum = False
  min_position = False

  for bottle_position in room.get_all_coordinates():
    steps = 0

    for item in objects:
      min_steps_to_item = False

      # don't get all border coordinates, but the one that is nearest to the bottle
      for coordinate in item.get_border_coordinates():
        
        steps_to_item = coordinate - bottle_position

        if (min_steps_to_item is False) or (steps_to_item < min_steps_to_item):
          min_steps_to_item = steps_to_item        

      steps += min_steps_to_item

    if (min_sum is False) or (steps < min_sum):
      
      min_sum = steps
      min_position = bottle_position
    elif (steps == min_sum):
      if (min_position.x > bottle_position.x):
        min_position = bottle_position
      elif (min_position.x == bottle_position.x) and (min_position.y > bottle_position.y):
        min_position = bottle_position

  print(f"Case #{t_case}: {min_position.x} {min_position.y}")
  



