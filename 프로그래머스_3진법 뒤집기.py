def solution(n) : # solution이라는 함수 생성
    answer = '' # answer변수 초기화
    while(n >= 1) : # 반복문 while -> n이 1이상일 경우 반복
        rest = n % 3 # n% 3의 값을 rest변수에 저장
        n //= 3 # n = n // 3
        answer += str(rest) # answer = answer += str(rest)
    return int(answer, 3)  # int를 사용하여 3진법 수를 10진법 수로 바꾸어 반환