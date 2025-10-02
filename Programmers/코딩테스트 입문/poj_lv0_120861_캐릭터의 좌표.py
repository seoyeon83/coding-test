def solution(keyinput, board):
    # up-down = y, right-left = x
    x_max = board[0]//2
    y_max = board[1]//2
    
    answer = [0, 0]
    
    for key in keyinput:
        if (key == "up") and (answer[1] < y_max):
            answer[1] += 1
        elif (key == "down") and (answer[1] > -y_max):
            answer[1] -= 1
        elif (key == "right") and (answer[0] < x_max):
            answer[0] += 1
        elif (key == "left") and (answer[0] > -x_max):
            answer[0] -= 1
    
    return answer