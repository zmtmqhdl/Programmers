def solution(n) : # solution�̶�� �Լ� ����
    for i in range(1, n) : # �ݺ��� for -> 1���� n - 1���� ���ʴ�� i�� �����ϸ� �ݺ�
        if n % i == 1 : # ���ǹ� if -> n�� i�� ������ �� �������� 1�� ���
            answer = i # i�� ���� answer������ ����
            break # ����
    return answer # answer��ȯ