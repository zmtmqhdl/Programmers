def solution(arr1, arr2) : # solution�̶�� �Լ� ����
    for i in range(len(arr1)) : # �ݺ��� for -> 0���� len(arr1) - 1���� ���ʴ�� i�� �����ϸ� �ݺ�
        for j in range(len(arr1[0])) : # �ݺ��� for -> 0���� len(arr1[0]) - 1���� ���ʴ�� j�� �����ϸ� �ݺ�
            arr1[i][j] += arr2[i][j] # arr1[i][j] = arr1[i][j] +arr2[i][j]
    return arr1 # arr1��ȯ