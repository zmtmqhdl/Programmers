def solution(n, arr1, arr2) : # solution이라는 함수 생성
    answer = [] # answer라는 list생성
    for x, y in zip(arr1, arr2) : # 반복문 for -> arr1, arr2라는 list의 원소를 차례대로 x, y에 대입하며 반복
        x, y = (bin(x)[2:]), (bin(y)[2:]) # bin을 사용하여 x와 y를 2진수로 변환하여 x, y변수에 저장
        if len(x) < n : # # 조건문 if -> len(x)가 n보다 작을 경우
            x = '0' * (n - len(x)) + x # x에 0을 붙혀 자리수를 n으로 맞춰줌
        if len(y) < n : # 조건문 if -> len(y)가 n보다 작을 경우
            y = '0' * (n - len(y)) + y # y에 0을 붙혀 자리수를 n으로 맞춰줌
        data = '' # data변수 초기화
        for a, b in zip(x, y) : # 반복문 for -> x, y라는 문자를 한 문자씩 차례대로 a, b에 대입하며 반복
            temp = bin(int(a) | int(b))[2:] # bin을 사용하여 int(a)와 int(b)를 2진수로 변환하여 temp변수에 저장
                                            # or(|)을 사용하여 int(a)와 int(b)중 하나라도 1일 경우 1반환
            if temp == '1' : # 조건문 if, else -> temp가 1일 경우
                data += '#' # data = data + '#'
            else : # temp가 0일 경우
                data += ' ' # data = data + ' '
        answer.append(data) # append를 사용하여 answer라는 list에 data를 원소를 추가
    return answer # answer반환