def vacuum_world():
    goal_state = {'A': '0', 'B': '0'}
    cost = 0

    location = input("Enter Location A/B: ")
    status = input("Enter status of " + location + ": ")
    other_status = input("Enter status of other room: ")

    if location == 'A':
        if status == '1':          # Clean A
            goal_state['A'] = '0'
            cost += 1
            if other_status == '1':  # Move to B
                cost += 1
                goal_state['B'] = '0'
                cost += 1
        else:                       # A already clean
            if other_status == '1':  # Move to B
                cost += 1
                goal_state['B'] = '0'
                cost += 1
    else:  # Location == 'B'
        if status == '1':          # Clean B
            goal_state['B'] = '0'
            cost += 1
            if other_status == '1':  # Move to A
                cost += 1
                goal_state['A'] = '0'
                cost += 1
        else:                       # B already clean
            if other_status == '1':
                cost += 1
                goal_state['A'] = '0'
                cost += 1

    print("GOAL STATE:", goal_state)
    print("Performance Cost:", cost)

vacuum_world()
