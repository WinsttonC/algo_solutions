for _ in range(int(input())):
    
    str_num = int(input())
    list_ = []
    #объединить строки
    str_ = ''
    for i in range(str_num):
        str_ += input()
    #написать счетчик для каждой буквы
    w_counter = dict()
    for elem in str_:
        if elem in list_:
            w_counter[elem] += 1
        else:
            w_counter[elem] = 1
            list_.append(elem)

    checker = sum([elem % str_num for elem in w_counter.values()])

    if checker == 0:
        print("YES")
    else:
        print("NO")