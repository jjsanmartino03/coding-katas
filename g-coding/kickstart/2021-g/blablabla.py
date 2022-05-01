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
  sums = []
  objects = []

  for k in range(int(input())):
    
    x1, y1, x2, y2 = list(map(int, input().split()))

    objects.append(Object(x1,y1,x2,y2))

  min_x = -100
  min_y = -100
  max_x = 100
  max_y = 100

  room = Object(min_x, min_y, max_x, max_y)

  for bottle_position in room.get_all_coordinates():
    steps = 0

    for item in objects:
      steps_to_item = []

      for coordinate in item.get_border_coordinates():
        steps_to_item.append(coordinate - bottle_position)
      
      steps += (min(steps_to_item))
    #print(steps)

    sums += [ [steps, bottle_position] ]
  
  min_result = sums[0][0]
  min_position = sums[0][1]

  for result in sums:
    if result[0] < min_result:
      print(result[1])
      min_result = result[0]
      min_position = result[1]
    elif result[0] == min_result:
      if min_position.x > result[1].x:
        min_position = result[1]
      elif min_position.x == result[1].x and min_position.y > result[1].y:
        min_position = result[1]  

  print(f"Case #{t_case}: {min_position.x} {min_position.y}")
  



