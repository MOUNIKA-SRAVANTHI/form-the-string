def simulate_office_attendance(num_employees, num_friendships, friendships, target_attendance):
    
    daily_attendance = [1] * num_employees
    friendship_network = [[] for _ in range(num_employees)]

    for a, b in friendships:
        friendship_network[a-1].append(b-1)
        friendship_network[b-1].append(a-1)

    total_attendance = 0
    days = 0

    while total_attendance < target_attendance:
        days += 1
        
        current_day_attendance = sum(daily_attendance)
        total_attendance += current_day_attendance

        if total_attendance >= target_attendance:
            break

        next_day_attendance = [0] * num_employees

        for i in range(num_employees):
            if daily_attendance[i] == 1:
                office_friends = sum(1 for friend in friendship_network[i] if daily_attendance[friend] == 1)
                if office_friends == 3:
                    next_day_attendance[i] = 1
                else:
                    next_day_attendance[i] = 0
            else:
                office_friends = sum(1 for friend in friendship_network[i] if daily_attendance[friend] == 1)
                if office_friends < 3:
                    next_day_attendance[i] = 1
                else:
                    next_day_attendance[i] = 0

        daily_attendance = next_day_attendance

    return days

num_employees, num_friendships = map(int, input().split())
friendships = [tuple(map(int, input().split())) for _ in range(num_friendships)]
target_attendance = int(input())

print(simulate_office_attendance(num_employees, num_friendships, friendships, target_attendance), end="")
