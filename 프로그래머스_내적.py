def solution(a, b) : # solution이라는 함수 생성
    answer = 0 # answer변수 초기화
    for i in range(len(a)) : # 반복문 for -> 0부터 len(a) - 1까지 차례대로 i에 대입하며 반복
        answer += a[i] * b[i] # answer = answer + (a[i] * b[i])
    return answer # answer반환