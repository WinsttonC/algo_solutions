def find_indexes(p):
    results = []

    found = False
    for i in range(1, len(p) - 1):
        if p[i - 1] < p[i] and p[i] > p[i + 1]:
 
            print(f"YES\n{i} {i + 1} {i + 2}")
            found = True
            break
    if not found:

        print('NO')


for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    find_indexes(p)

