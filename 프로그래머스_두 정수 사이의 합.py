def solution(a, b) : # solution�̶�� �Լ� ����
    answer = 0 # answer���� �ʱ�ȭ
    for i in range(min(a, b), max(a, b) + 1) : # �ݺ��� for -> min(a, b)���� max(a, b)���� ���ʴ�� i�� �����ϸ� �ݺ�
        answer += i # answer = answer + i
    return answer # answer��ȯ