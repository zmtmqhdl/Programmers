def solution(arr, divisor) : # solution이라는 함수 생성
    answer = [] # answer라는 list생성
    for i in arr : # 반복문 for -> arr라는 list의 원소를 차례대로 i에 대입하며 반복
        if i % divisor == 0 : # 조건문 if -> i를 divisor로 나눴을 때 나머지가 0인 경우
            answer.append(i) # append를 사용하여 i를 answer라는 list의 원소로 추가 
    if len(answer) == 0 : # 조건문 if, else -> answer라는 list의 원소가 0개인 경우
        return [-1] # [-1]반환
    else : # answer라는 list의 원소가 1개 이상인 경우
        return sorted(answer) # sorted를 사용하여 answer라는 list의 원소를 오름차순으로 정렬하여 반환