def solution(dartResult) :  # solution이라는 함수 생성
    answer = [] # answer라는 list생성
    dartResult = dartResult.replace('10', 't') # replace를 사용하여 10을 k로 변경
    bonus = { 'S':1, 'D':2, 'T':3 } # bonus라는 dictionary생성
    for n in dartResult : # 반복문 for -> dartResult의 문자를 한 개씩 n에 대입하며 반복
        if n in bonus : # 조건문 if, elif, else -> 조건문 if, elif, else -> n이 S, D, T인 경우
            answer[-1] **= bonus[n] # answer[-1] = answer[-1] ** bonus[n]
        elif n == '#' : # n이 #인 경우
            answer[-1] *= -1 # answer[-1] = answer[-1] * -1
        elif n == '*' : # n이 *인 경우
            answer[-1] *= 2 # answer[-1] = answer[=1] * 2
            if len(answer) > 1 : # 조건문 if -> len(answer)가 2이상인 경우
                answer[-2] *= 2 # answer[-2] = answer[-2] * 2 
        elif n == 't' : # n이 t인 경우
            answer.append(10) # append를 사용하여 answer라는 list에 10을 원소로 추가
        else : # n이 숫자인 경우
            answer.append(int(n)) # append를 사용하여 answer라는 list에 int(n)을 원소로 추가
    return sum(answer) # sum(answer)반환