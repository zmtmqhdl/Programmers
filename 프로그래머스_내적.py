def solution(a, b) : # solution�̶�� �Լ� ����
    answer = 0 # answer���� �ʱ�ȭ
    for i in range(len(a)) : # �ݺ��� for -> 0���� len(a) - 1���� ���ʴ�� i�� �����ϸ� �ݺ�
        answer += a[i] * b[i] # answer = answer + (a[i] * b[i])
    return answer # answer��ȯ