def solution(dartResult) :  # solution�̶�� �Լ� ����
    answer = [] # answer��� list����
    dartResult = dartResult.replace('10', 't') # replace�� ����Ͽ� 10�� k�� ����
    bonus = { 'S':1, 'D':2, 'T':3 } # bonus��� dictionary����
    for n in dartResult : # �ݺ��� for -> dartResult�� ���ڸ� �� ���� n�� �����ϸ� �ݺ�
        if n in bonus : # ���ǹ� if, elif, else -> ���ǹ� if, elif, else -> n�� S, D, T�� ���
            answer[-1] **= bonus[n] # answer[-1] = answer[-1] ** bonus[n]
        elif n == '#' : # n�� #�� ���
            answer[-1] *= -1 # answer[-1] = answer[-1] * -1
        elif n == '*' : # n�� *�� ���
            answer[-1] *= 2 # answer[-1] = answer[=1] * 2
            if len(answer) > 1 : # ���ǹ� if -> len(answer)�� 2�̻��� ���
                answer[-2] *= 2 # answer[-2] = answer[-2] * 2 
        elif n == 't' : # n�� t�� ���
            answer.append(10) # append�� ����Ͽ� answer��� list�� 10�� ���ҷ� �߰�
        else : # n�� ������ ���
            answer.append(int(n)) # append�� ����Ͽ� answer��� list�� int(n)�� ���ҷ� �߰�
    return sum(answer) # sum(answer)��ȯ