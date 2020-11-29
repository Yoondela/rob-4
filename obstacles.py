obs = [(34,78), (7,90), (1,9)]

y_change = False
ocupied = []
def is_position_blocked(y,x):
    pos =(y,x)
    for i in range(3):
        obstacle = obs[i]
        helper(obstacle)
    if pos in ocupied:
        return True
    else:
        return False

def is_path_blocked(x1,y1,x2,y2):
    start = (x1,y1)
    end = (x2, y2)
    start_x = start[0]
    end_x = end[0]
    start_y = start[1]
    end_y = end[1]
    blocked = False
    if start_x <= end_x:
        for i in range(start_x, end_x+1):
            if start_y <= end_y:
                for j in range(start_y, end_y):
                    if start_y < end_y:
                        start_y = start_y + 1
                    else:
                        start_y = start_y - 1
                    if (start_x,start_y) in ocupied:
                        blocked = True

            elif start_y > end_y:
                for j in range(end_y, start_y):
                    if start_y < end_y:
                        start_y = start_y + 1
                    else:
                        start_y = start_y - 1
                    if (start_x,start_y) in ocupied:
                        blocked = True

            if start_x < end_x:
                start_x = start_x + 1
            elif start_x > end_x:
                start_x = start_x - 1

    elif start_x > end_x:
        for i in range(end_x, start_x+1):
            if start_y <= end_y:
                for j in range(start_y, end_y):
                    if start_y < end_y:
                        start_y = start_y + 1
                    else:
                        start_y = start_y - 1
                    if (start_x,start_y) in ocupied:
                        blocked = True

            elif start_y > end_y:
                for j in range(end_y, start_y):
                    if start_y < end_y:
                        start_y = start_y + 1
                    else:
                        start_y = start_y - 1
                    if (start_x,start_y) in ocupied:
                        blocked = True

            if start_x < end_x:
                start_x = start_x + 1
            elif start_x > end_x:
                start_x = start_x - 1
    return blocked
        

def is_blocked():
    for i in range(3):
        obstacle = obs[i]
        helper(obstacle)


def helper(obstacle):
    global ocupied, y_change
    (y,x) = obstacle
    x_marker = x
  
    for i in range(6):
        for j in range(5):
            ocupied.append((y,x))              
            
            if y_change:
                x = x_marker
                ocupied.append((y,x))
                y_change = False
            x = x + 1
        y = y - 1
        y_change = True

print(is_position_blocked(32,78))
print(ocupied)
print(is_path_blocked(6,12,-3, 13))

    