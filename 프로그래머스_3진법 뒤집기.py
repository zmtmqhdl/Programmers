def solution(n) : # solution�̶�� �Լ� ����
    answer = '' # answer���� �ʱ�ȭ
    while(n >= 1) : # �ݺ��� while -> n�� 1�̻��� ��� �ݺ�
        rest = n % 3 # n% 3�� ���� rest������ ����
        n //= 3 # n = n // 3
        answer += str(rest) # answer = answer += str(rest)
    return int(answer, 3)  # int�� ����Ͽ� 3���� ���� 10���� ���� �ٲپ� ��ȯ