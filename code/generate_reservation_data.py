import csv
from faker import Faker
import random
import datetime
import os

from modules.write_to_csv import write_to_csv

fake = Faker('ko_KR')

def generate_fake_reservation():
    reservation_id = fake.random_int(1, 1000000)
    car_id = fake.random_int(1, 100)
    customer_id = fake.random_int(1000, 9999)
    status = random.choice(['예약완료', '차량인수', '점검중', '완료됨', '취소됨'])
    created_at = fake.date_time_between(start_date='-10y', end_date='now')
    updated_at = fake.date_time_between(start_date=created_at, end_date='now')
    phone_number = fake.phone_number()
    car_model = fake.random_element(elements=('Genesis G70', 'Genesis G80', 'Genesis GV80', 'Genesis G90'))
    license_plate = fake.random_element(elements=('00가 0000', '11나 1111', '22다 2222'))
    issues = fake.sentence()
    comment = fake.sentence() if random.random() > 0.5 else None
    return [reservation_id, car_id, customer_id, 1, created_at, updated_at, phone_number, car_model, license_plate, issues, comment, status, created_at, updated_at]

def generate_fake_data(num_records):
    print('generate_fake_data() ...')
    records = []
    for _ in range(num_records):
        records.append(generate_fake_reservation())
    return records

if __name__ == "__main__":
    num_records = 1
    current_directory = os.path.dirname(__file__)
    filename = os.path.join(current_directory, '../data/fake_reservation_data.csv')
    data = generate_fake_data(num_records)
    write_to_csv(data, filename)
    print(f'{num_records}개의 데이터가 생성되어 {filename}에 저장되었습니다.')
