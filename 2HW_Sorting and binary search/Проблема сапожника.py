work_minutes, s_num = [int(i) for i in input().split()]
s_time = [int(i) for i in input().split()]
total_time = 0
s_num_done = 0


for i in range(len(s_time)):
    for j in range(i+1, len(s_time)):
        if s_time[i] > s_time[j]:
            s_time[i], s_time[j] = s_time[j], s_time[i]

for time in s_time:
    if work_minutes >= time:
        work_minutes -= time
        s_num_done += 1
    else:
        break

print(s_num_done)
