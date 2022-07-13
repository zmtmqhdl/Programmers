def solution(a, b) : # solution이라는 함수 생성
    answer = 0 # answer변수 초기화
    for i in range(min(a, b), max(a, b) + 1) : # 반복문 for -> min(a, b)부터 max(a, b)까지 차례대로 i에 대입하며 반복
        answer += i # answer = answer + i
    return answer # answer반환