def solution(arr, divisor) : # solution�̶�� �Լ� ����
    answer = [] # answer�̶�� list����
    for i in arr : # �ݺ��� for -> arr�̶�� list�� ���Ҹ� ���ʴ�� i�� �����ϸ� �ݺ�
        if i % divisor == 0 : # ���ǹ� if -> �������� 0�� ���
            answer.append(i) # append�� ����Ͽ� answer��� list�� ���ҷ� i�� ����
    if len(answer) == 0 : # ���ǹ� if, else -> len(answer)�� ���� 0�� ���
        return [-1] # [-1]��ȯ
    else : # len(answer)�� ���� 0�� �ƴ� ���
        return sorted(answer) # sorted(answer)��ȯ