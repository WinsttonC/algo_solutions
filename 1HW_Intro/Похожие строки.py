for _ in range(int(input())):
    len_str = int(input())
    in_str = input()

    #символ, который точно есть во всех подстроках
    symb = in_str[len_str-1]
    out_str = symb * len_str

    print(out_str)