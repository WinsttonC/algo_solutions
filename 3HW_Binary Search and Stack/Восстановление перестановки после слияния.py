def restore_permutation():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split())) 
        seen = set()
        p = []
        for num in a:
            if num not in seen:
                seen.add(num)
                p.append(num)
        
        print(' '.join(map(str, p)))

restore_permutation()

