def solution(array, commands):
    answer = []
    
    for value in commands:
        list = []
        i = value[0]
        j = value[1]
        k = value[2]
        
        for a in range(i-1,j):
            list.append(array[a])
            
        list.sort()
        answer.append(list[k-1])
    
    
    return answer