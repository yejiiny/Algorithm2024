def solution(participant, completion):
    answer = ''
    hash = {}
    cnt = 1
    
    for i in participant:
        if i in hash:
            cnt = hash.get(i) + 1
        
        hash[i] = cnt
        cnt = 1
        
        
    for i in completion:
        if hash.get(i) == 1:
            del hash[i]
            
        else:
            cnt = hash.get(i) - 1
            hash[i] = cnt
            
    answer = str(*hash)
    
    return answer