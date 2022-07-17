def solution(arr) : # solution이라는 함수 생성
    answer = [] # answer이라는 list생성
    for i in range(len(arr)) : # 반복문 for -> 0부터 len(arr) - 1까지 차례대로 i에 대입하며 만복
        if i == 0: # 조건문 if, elif -> 처음으로 반복을 실행하는 경우
            answer.append(arr[i]) # append를 사용하여 arr[i]를 answer이라는 list의 원소로 추가
        elif arr[i] != arr[i - 1] : # 연속적으로 숫자가 나타나지 않는 경우
            answer.append(arr[i]) # append를 사용하여 arr[i]를 answer이라는 list의 원소로 추가
    return answer # answer반환