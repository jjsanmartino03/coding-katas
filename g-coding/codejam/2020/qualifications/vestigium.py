t = int(input())

for t_case in range(1, t+1):
    n = int(input())

    rows = []
    columns = [[] for _ in range(n)]
    for row in range(n):
        nums = list(map(lambda num: int(num), input().split()))
        rows.append(nums)

        for idx, num in enumerate(nums):
            columns[idx].append(num)

    trace = 0
    rows_repeat = 0
    cols_repeat = 0

    for index in range(n):
        trace += rows[index][index]

        if len(set(rows[index])) != len(rows[index]):
            rows_repeat += 1

        if len(set(columns[index])) != len(columns[index]):
            cols_repeat += 1






    print(f'#{t_case}: {trace} {rows_repeat} {cols_repeat}')
