
for t_case in range(1, int(input())+1):
  n,d,c,m = list(map(int, input().split()))
  dogs_full = False
  s = input()

  for index, animal in enumerate(s):
    if animal == 'D' and d:
      d -= 1
      c += m
    elif animal == 'D' and not d:
      break
    elif animal == 'C' and c:
      c -= 1
    elif animal == 'C' and not c:
      if s[index:].find('D') == -1:
        dogs_full = True
      break
  else:
    dogs_full = True

  print(f"Case #{t_case}: {'YES' if dogs_full else 'NO'}")
  



