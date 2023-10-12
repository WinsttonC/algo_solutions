#input_numbers = [int(i) for i in input().split()]
num_datasets = int(input())

for num in range(num_datasets):
    len_a = int(input())
    a = [int(i) for i in input().split()]
    if a[0] + a[1] <= a[len_a-1]:
        print(1, 2, len_a)
    else:
        print(-1)