len_pass =[]
passwords = []
for _ in range(int(input())):
        len_pass.append(int(input()))
        passwords.append([int(i) for i in input().split()])

def min_password_length(password):
    if len(set(password)) > 1:
        return 1
    else:
        return len(password)
a = [min_password_length(password) for password in passwords]

for elem in a:
    print(elem)
    
