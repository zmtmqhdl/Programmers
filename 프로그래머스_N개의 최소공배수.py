def solution(arr) : # solution�̶�� �Լ� ����
    answer = 0 # answer���� �ʱ�ȭ
    n = 1 # n������ 1����  
    while True : # �ݺ��� while -> False�� ��ȯ�� ������ �ݺ�
        answer = max(arr) * n # answer������ max(arr) * n����
        result = True # result������ True����
        for i in arr : # �ݺ��� for -> arr��� list�� ���Ҹ� ���ʴ�� i�� �����ϸ� �ݺ�
            if answer % i != 0 : # ���ǹ� if -> answer�� i�� ������ �� �������� 0�� �ƴ� ���
                result = False # result������ False����
                break # ����
        if result == True: # ���ǹ� if -> result������ True�� ���
            break # ����
        n += 1 # n = n + 1
    return answer # answer��ȯ