def solution(n, arr1, arr2) : # solution�̶�� �Լ� ����
    answer = [] # answer��� list����
    for x, y in zip(arr1, arr2) : # �ݺ��� for -> arr1, arr2��� list�� ���Ҹ� ���ʴ�� x, y�� �����ϸ� �ݺ�
        x, y = (bin(x)[2:]), (bin(y)[2:]) # bin�� ����Ͽ� x�� y�� 2������ ��ȯ�Ͽ� x, y������ ����
        if len(x) < n : # # ���ǹ� if -> len(x)�� n���� ���� ���
            x = '0' * (n - len(x)) + x # x�� 0�� ���� �ڸ����� n���� ������
        if len(y) < n : # ���ǹ� if -> len(y)�� n���� ���� ���
            y = '0' * (n - len(y)) + y # y�� 0�� ���� �ڸ����� n���� ������
        data = '' # data���� �ʱ�ȭ
        for a, b in zip(x, y) : # �ݺ��� for -> x, y��� ���ڸ� �� ���ھ� ���ʴ�� a, b�� �����ϸ� �ݺ�
            temp = bin(int(a) | int(b))[2:] # bin�� ����Ͽ� int(a)�� int(b)�� 2������ ��ȯ�Ͽ� temp������ ����
                                            # or(|)�� ����Ͽ� int(a)�� int(b)�� �ϳ��� 1�� ��� 1��ȯ
            if temp == '1' : # ���ǹ� if, else -> temp�� 1�� ���
                data += '#' # data = data + '#'
            else : # temp�� 0�� ���
                data += ' ' # data = data + ' '
        answer.append(data) # append�� ����Ͽ� answer��� list�� data�� ���Ҹ� �߰�
    return answer # answer��ȯ