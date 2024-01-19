def solution(board, moves):
    answer = 0
    
    stack = []
    
    for value in (moves):
        for i in range(len(board)):
            if board[i][value-1] != 0:
                if stack and stack[-1] == board[i][value-1]:
                    answer += 2
                    stack.pop()
                else:
                    stack.append(board[i][value-1])
                
                board[i][value-1] = 0
                
                break
    
    return answer