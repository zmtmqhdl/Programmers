def solution(arr, divisor) : # solution이라는 함수 생성
    answer = [] # answer이라는 list생성
    for i in arr : # 반복문 for -> arr이라는 list의 원소를 차례대로 i에 대입하며 반복
        if i % divisor == 0 : # 조건문 if -> 나머지가 0인 경우
            answer.append(i) # append를 사용하여 answer라는 list의 원소로 i를 대입
    if len(answer) == 0 : # 조건문 if, else -> len(answer)의 값이 0인 경우
        return [-1] # [-1]반환
    else : # len(answer)의 값이 0이 아닌 경우
        return sorted(answer) # sorted(answer)반환