import csv
import random
import string
from datetime import datetime

# 더미 데이터 수
data_count = 100

# 가능한 sell_name 옵션
sell_name_options = ["Genesis G70", "Genesis G80", "Genesis G90", "Genesis GV70", "Genesis GV80"]

# CSV 파일에 쓰기
with open('./data/car.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['customer_id', 'vin', 'sell_name', 'plate_number', 'create_datetime', 'update_datetime']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for _ in range(data_count):
        customer_id = random.randint(1, 1000)  # 임의의 customer_id 선택
        vin = ''.join(random.choices(string.ascii_uppercase + string.digits, k=17))  # 랜덤한 VIN 생성
        sell_name = random.choice(sell_name_options)  # 가능한 옵션 중 하나 선택
        plate_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))  # 랜덤한 차 번호판 생성
        create_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        update_datetime = create_datetime
        writer.writerow({'customer_id': customer_id, 'vin': vin, 'sell_name': sell_name, 'plate_number': plate_number, 'create_datetime': create_datetime, 'update_datetime': update_datetime})

print(f"{data_count}개의 더미 데이터가 car.csv 파일에 생성되었습니다.")
