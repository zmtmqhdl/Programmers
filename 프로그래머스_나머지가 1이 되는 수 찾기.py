def solution(n) : # solution이라는 함수 생성
    for i in range(1, n) : # 반복문 for -> 1부터 n - 1까지 차례대로 i에 대입하며 반복
        if n % i == 1 : # 조건문 if -> n을 i로 나눴을 때 나머지가 1인 경우
            answer = i # i의 값을 answer변수에 저장
            break # 중지
    return answer # answer반환