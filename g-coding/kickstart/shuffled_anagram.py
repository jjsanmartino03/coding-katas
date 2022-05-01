from collections import defaultdict as dd

t = int(input())

for test_case in range(t):
    letters_count = dd(int)
    
    s = input()
    
    for letter in s:
        letters_count[letter] += 1

    maximum_count = max(letters_count.values())

    others = sum(letters_count.values()) - maximum_count

    if (maximum_count > others):
        print(f'Case #{test_case+1}: IMPOSSIBLE')
    else:
        result = ['0' for i in range(len(s))]

        sorted_counts = sorted(letters_count.items(), key=lambda x: x[1],reverse=True)

        contadora = 0
        for letter, count in sorted_counts:
            for i in range(count):
                for index, space in enumerate(result):
                    if space == '0' and (s[index] != letter):
                        result[index] = letter
                        break
                    elif space == '0' and (contadora == len(sorted_counts)-1):
                        interval = 1

                        while True:
                            new_index = index - interval

                            if(s[new_index] != letter and result[new_index] != letter):
                                result[index] = result[new_index]

                                result[new_index] = letter
                                break
                            
                            interval += 1
            contadora += 1
                        

        print(f'Case #{test_case+1}: {"".join(result)}')