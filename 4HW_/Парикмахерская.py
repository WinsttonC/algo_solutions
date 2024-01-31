
queue_end_time = 0
results = []

for i in range(1, int(input()) + 1):
    lines = input()
    h, m, impatience = map(int, lines.split())
    arrival_time = h * 60 + m
    
    if queue_end_time < arrival_time:
        queue_end_time = arrival_time
    
    if queue_end_time - arrival_time <= impatience * 20:
        queue_end_time += 20 
        exit_hour = queue_end_time // 60
        exit_minute = queue_end_time % 60
        results.append(f"{exit_hour} {exit_minute}")
        
    else:
        results.append(f"{h} {m}")

print('\n'.join(results))

