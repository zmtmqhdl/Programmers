def solution(arr) : # solution�̶�� �Լ� ����
    answer = [] # answer�̶�� list����
    for i in range(len(arr)) : # �ݺ��� for -> 0���� len(arr) - 1���� ���ʴ�� i�� �����ϸ� ����
        if i == 0: # ���ǹ� if, elif -> ó������ �ݺ��� �����ϴ� ���
            answer.append(arr[i]) # append�� ����Ͽ� arr[i]�� answer�̶�� list�� ���ҷ� �߰�
        elif arr[i] != arr[i - 1] : # ���������� ���ڰ� ��Ÿ���� �ʴ� ���
            answer.append(arr[i]) # append�� ����Ͽ� arr[i]�� answer�̶�� list�� ���ҷ� �߰�
    return answer # answer��ȯ