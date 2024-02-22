import csv
from faker import Faker
import random
from datetime import datetime
import os

fake = Faker('ko_KR')

def generate_fake_data(num_records):
    data = []
    for _ in range(num_records):
        serial_number = fake.uuid4().replace('-', '')[:30]  # UUID를 이용하여 랜덤한 시리얼 넘버 생성
        expired_date = fake.date_between(start_date='today', end_date='+10y')  # 오늘부터 10년 이내의 날짜 생성
        is_used = random.choice([0, 1])  # 0 또는 1 중에서 랜덤으로 선택
        create_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 현재 시간을 생성 일시로 사용
        update_datetime = create_datetime  # 생성된 일시와 동일하게 설정
        data.append([serial_number, expired_date, is_used, create_datetime, update_datetime])
    return data

if __name__ == "__main__":
    num_records = 10000
    current_directory = os.path.dirname(__file__)
    filename = os.path.join(current_directory, '..', 'data', 'coupon.csv')
    data = generate_fake_data(num_records)

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # 헤더 추가
        writer.writerow(['serial_number', 'expired_date', 'is_used', 'create_datetime', 'update_datetime'])
        # 데이터 추가
        writer.writerows(data)

    print(f'{num_records}개의 데이터가 생성되어 {filename}에 저장되었습니다.')