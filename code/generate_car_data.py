import csv
import random
import string
from datetime import datetime

def generate_random_plate_number():
    # '123가 1234'와 같은 형식의 번호판 생성
    middle_char = random.choice("가나다라마바사아자차카파타하")
    plate_number = f'{random.randint(100, 999)}{middle_char} {random.randint(1000, 9999)}'
    return plate_number

# 더미 데이터 수
data_count = 1000

# 가능한 sell_name 옵션
sell_name_options = ["Genesis G70", "Genesis G80", "Genesis G90", "Genesis GV70", "Genesis GV80"]

if __name__ == "__main__":
    # CSV 파일 저장
    with open('./data/car.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['id', 'customer_id', 'vin', 'sell_name', 'plate_number', 'create_datetime', 'update_datetime']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        id = 1
        
        for _ in range(data_count):
            vin = ''.join(random.choices(string.ascii_uppercase + string.digits, k=17))  # 랜덤한 VIN 생성
            sell_name = random.choice(sell_name_options)
            plate_number = generate_random_plate_number()
            create_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            update_datetime = create_datetime
            writer.writerow({'id' : id, 'customer_id': random.randint(1, 100), 'vin': vin, 'sell_name': sell_name, 'plate_number': plate_number,
            'create_datetime' : create_datetime, 'update_datetime' : update_datetime})
            id += 1

    print(f"{data_count}개의 랜덤한 차량 데이터가 car.csv 파일에 저장되었습니다.")
