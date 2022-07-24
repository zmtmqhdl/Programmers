def solution(arr) : # solution이라는 함수 생성
    answer = 0 # answer변수 초기화
    n = 1 # n변수에 1저장  
    while True : # 반복문 while -> False가 반환될 때까지 반복
        answer = max(arr) * n # answer변수에 max(arr) * n저장
        result = True # result변수에 True저장
        for i in arr : # 반복문 for -> arr라는 list의 원소를 차례대로 i에 대입하며 반복
            if answer % i != 0 : # 조건문 if -> answer를 i로 나눴을 때 나머지가 0이 아닌 경우
                result = False # result변수에 False저장
                break # 중지
        if result == True: # 조건문 if -> result변수가 True인 경우
            break # 중지
        n += 1 # n = n + 1
    return answer # answer반환