for _ in range(int(input())):
    str_num, col_num = [int(i) for i in input().split()]
    changes_num = 0

    for i in range(str_num):
        stroke = input()
        for j in range(col_num):
            if i == str_num-1 and stroke[j] == 'D':
                changes_num += 1
            if j == col_num-1 and stroke[j] == 'R':
                changes_num += 1

    print(changes_num)
