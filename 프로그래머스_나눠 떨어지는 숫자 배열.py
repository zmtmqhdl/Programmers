def solution(arr, divisor) : # solution�̶�� �Լ� ����
    answer = [] # answer��� list����
    for i in arr : # �ݺ��� for -> arr��� list�� ���Ҹ� ���ʴ�� i�� �����ϸ� �ݺ�
        if i % divisor == 0 : # ���ǹ� if -> i�� divisor�� ������ �� �������� 0�� ���
            answer.append(i) # append�� ����Ͽ� i�� answer��� list�� ���ҷ� �߰� 
    if len(answer) == 0 : # ���ǹ� if, else -> answer��� list�� ���Ұ� 0���� ���
        return [-1] # [-1]��ȯ
    else : # answer��� list�� ���Ұ� 1�� �̻��� ���
        return sorted(answer) # sorted�� ����Ͽ� answer��� list�� ���Ҹ� ������������ �����Ͽ� ��ȯ