for t_case in range(1, int(input())+1):
    n = int(input())
    numbers = list(map(int, input().split()))
    count = 0
    for i in range(len(numbers)-1):
        min_num = min(numbers[i:])
        min_position = numbers.index(min_num, i)

        numbers[i:min_position+1] = reversed(numbers[i:min_position+1])
        count += (min_position+1)-i
    print(f'Case #{t_case}: {count}')
