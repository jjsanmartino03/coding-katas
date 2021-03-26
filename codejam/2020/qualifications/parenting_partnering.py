def get_overlapping(past, interval):
    overlaps = []
    for idx, element in enumerate(past):
        if element[0] < interval[1] and element[1] > interval[0]:
            overlaps.append(idx)
    if len(overlaps) > 1:
        return overlaps
    elif len(overlaps) == 1:
        return overlaps[0]
    else:
        return False


for t_case in range(1, int(input())+1):
    activities = [list(map(int, input().split())) for _ in range(int(input()))]

    result = ''
    for index, activity in enumerate(activities):
        overlaps_with = get_overlapping(activity, activities[:index])
        if type(overlaps_with) == int:
            pass
        elif overlaps_with:
            print(f'Case #{t_case}: IMPOSSIBLE')
            break
        else:
            result += 'C'
    else:
        pass

