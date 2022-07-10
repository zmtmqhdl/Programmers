def solution(n) : # solution이라는 함수 생성
    answer = 0 # 결과값을 저장할 answer변수 초기화
    for i in str(n) : # 반복문 for -> str(n)의 문자를 차례대로 i에 대입하며 반복
        answer += int(i) # answer = answer + int(i)
    return answer # answer반환