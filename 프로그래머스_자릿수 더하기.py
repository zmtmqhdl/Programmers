def solution(n) : # solution�̶�� �Լ� ����
    answer = 0 # ������� ������ answer���� �ʱ�ȭ
    for i in str(n) : # �ݺ��� for -> str(n)�� ���ڸ� ���ʴ�� i�� �����ϸ� �ݺ�
        answer += int(i) # answer = answer + int(i)
    return answer # answer��ȯ