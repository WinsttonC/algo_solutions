for _ in range(int(input())):
    n = int(input())
    if n < 31:
        print('NO')
    else:
        num = [6, 10, 14]
        if n-sum(num) in num:
            num[-1] = 15
        num.append(n-sum(num))
        print('YES')
        print(' '.join([str(i) for i in num]))




