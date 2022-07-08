def solution(arr1, arr2) : # solution이라는 함수 생성
    for i in range(len(arr1)) : # 반복문 for -> 0부터 len(arr1) - 1까지 차례대로 i에 대입하며 반복
        for j in range(len(arr1[0])) : # 반복문 for -> 0부터 len(arr1[0]) - 1까지 차례대로 j에 대입하며 반복
            arr1[i][j] += arr2[i][j] # arr1[i][j] = arr1[i][j] +arr2[i][j]
    return arr1 # arr1반환