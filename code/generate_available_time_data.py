import csv
import random
from datetime import datetime, timedelta

# 더미 데이터 수
data_count = 5000000

# 고정 repair_shop_id
repair_shop_id = 1

def generate_datetime_range():
    # 시작 날짜와 시간 설정
    start_date = datetime.now().date() - timedelta(days=365 * 10)  # 오늘부터 10년 전까지의 범위
    start_time = datetime.strptime('06:00:00', '%H:%M:%S').time()

    # 종료 날짜와 시간 설정
    end_date = datetime.now().date() + timedelta(days=365 * 2)  # 오늘부터 2년 후까지의 범위
    end_time = datetime.strptime('22:00:00', '%H:%M:%S').time()

    # 모든 날짜와 시간 조합 생성
    datetime_range = []
    current_date = start_date
    while current_date <= end_date:
        current_time = start_time
        while current_time <= end_time:
            datetime_range.append(datetime.combine(current_date, current_time))
            current_time = (datetime.combine(datetime.min, current_time) + timedelta(hours=1)).time()  # 1시간씩 증가
        current_date += timedelta(days=1)  # 1일씩 증가

    return datetime_range

if __name__ == "__main__":
    # 날짜와 시간 조합 생성
    datetime_range = generate_datetime_range()

    # CSV 파일 저장
    with open('./data/available_time.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['id', 'repair_shop_id', 'reservation_date', 'reservation_time', 'reservation_count', 'create_datetime', 'update_datetime']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()

        id = 1

        create_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        update_datetime = create_datetime
        
        for idx, datetime_value in enumerate(datetime_range):
            reservation_date = datetime_value.date()
            reservation_time = datetime_value.time()
            reservation_count = random.randint(0, 5) 
            writer.writerow({'id': id, 'repair_shop_id': repair_shop_id, 'reservation_date': reservation_date, 'reservation_time': reservation_time, 'reservation_count': reservation_count,
            'create_datetime': create_datetime, 'update_datetime': update_datetime})
            id += 1

    print(f"{len(datetime_range)}개의 날짜와 시간 데이터가 random_available_times.csv 파일에 저장되었습니다.")
