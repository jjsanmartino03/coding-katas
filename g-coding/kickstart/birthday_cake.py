def get_cuts(num, k):
  if num < k:
    return 1
  else:
    return (num // k) + (num % k)

for t_case in range(int(input())):
  r,c,k = list(map(int, input().split()))

  r1, c1, r2, c2 = list(map(int, input().split()))

  rows = (r2 - r1 + 1)
  cols = (c2 - c1 + 1)

  if (total_cells > 1):
    common_borders = ( (cols - 1) * get_cuts(rows,k) ) + ( (rows - 1) * get_cuts(cols, k) )

    delicious_cuts = common_borders + get_cuts(cols, k) * 2 + get_cuts(rows, k) 
    * 2
  else:
    delicious_cuts = get_cuts(4, k)

  min_distance = min([r - r2, c - c2, r1 - 1, c1 -1])
  min_distance = get_cuts(min_distance, k)

  delicious_cuts += min_distance

  if r1 == 1:
    delicious_cuts -= get_cuts(cols, k)

  if r2 == r:
    delicious_cuts -= get_cuts(cols, k)

  if c1 == 1:
    delicious_cuts -= get_cuts(rows, k)

  if c2 == c:
    delicious_cuts -= get_cuts(rows, k)

  print(f"Case #{t_case + 1}: {delicious_cuts}")


