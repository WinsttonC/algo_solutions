for _ in range(int(input())):
    list_len, k = [int(i) for i in input().split()]
    list_in = [int(i) for i in input().split()]

    #так как значения повторяются каждый 2 шаг,
    #можно уменьшить количество итераций
    if k % 2 == 0:
        k = 2
    else:
        k = 1

    for _ in range(k):
        if _ == 0:
            updated_list = list_in
        d = max(updated_list)
        updated_list = [d - elem for elem in updated_list]
    
    print(' '.join(map(str, updated_list)))