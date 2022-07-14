def solution(a, b) : # solution이라는 함수 생성
    month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # 각 월마다 날짜를 저장한 month라는 list생성
    day = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED'] # 요일을 저장한 day라는 list생성
    date = sum(month[:a]) + b # 날짜 연산
    return day[date % 7] # day[date % y])반환