def solution(a, b) : # solution�̶�� �Լ� ����
    month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # �� ������ ��¥�� ������ month��� list����
    day = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED'] # ������ ������ day��� list����
    date = sum(month[:a]) + b # ��¥ ����
    return day[date % 7] # day[date % y])��ȯ