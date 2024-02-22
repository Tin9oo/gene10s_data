import csv
import random
from datetime import datetime, timedelta
import os

# 차종 목록
car_models = ['G70', 'G80', 'G90', 'GV70', 'GV80']

# 다양한 고객 요청 문구
customer_requests = [
    '',
    '특별한 요청사항이 없습니다.',
    '차량 내부 청소 부탁드립니다.',
    '차량 정비 이외에 추가 작업 필요합니다.',
    '타이어 교체 요청합니다.',
    '브레이크 점검 부탁드립니다.',
    '에어컨 점검 요청합니다.',
    '엔진 체크 필요합니다.',
    '브레이크 오일 교체 요청합니다.',
    '배터리 교체 필요합니다.',
    '차량 시동이 이상합니다.'
]

# 다양한 검사 결과 문구
inspection_results = [
    '',
    '엔진 오일 교체 필요',
    '브레이크 패드 교체 요망',
    '타이어 교체 필요',
    '차량 내부 청소 필요',
    '에어컨 필터 교체 필요',
    '엔진 체크 필요',
    '브레이크 오일 교체 요청',
    '배터리 교체 필요',
    '시동 불가능',
    '조수석 에어백 체크 필요'
]

# 데이터 폴더 경로
data_folder = 'data'
if not os.path.exists(data_folder):
    os.makedirs(data_folder)

# 기존에 생성된 번호를 저장할 집합
existing_plate_numbers = set()
existing_contact_numbers = set()
existing_coupon_ids = set()

# CSV 파일에 데이터 작성
def write_csv(filename, data, header):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)

# 차량 번호 생성하는 함수
def generate_plate_number():
    while True:
        plate_number = f"{random.randint(1, 99):02}{''.join(random.choice('가나다라마바사아자차카타파하') for _ in range(1))} {''.join(random.choice('0123456789') for _ in range(4))}"
        if plate_number not in existing_plate_numbers:
            existing_plate_numbers.add(plate_number)
            return plate_number
        
# 전화번호 생성하는 함수
def generate_contact_number():
    while True:
        contact_number = ''.join(str(random.randint(0, 9)) for _ in range(10))
        if contact_number not in existing_contact_numbers:
            existing_contact_numbers.add(contact_number)
            return contact_number

# 쿠폰 아이디 생성하는 함수
def generate_coupon_id():
    while True:
        coupon_id = random.randint(1, 500)
        if coupon_id not in existing_coupon_ids:
            existing_coupon_ids.add(coupon_id)
            return coupon_id
        
# 랜덤 데이터를 생성하기 위한 함수
def generate_random_reservation(i):
    if (i % 100000) == 0:
        print(f"{i}-th record is created")
    id_ = i
    customer_id = random.randint(1, 100)
    coupon_id = generate_coupon_id()
    repair_shop_id = 1
    departure_time = datetime.now() - timedelta(days=random.randint(1, 365), hours=random.randint(0, 23), minutes=random.randint(0, 59))
    arrival_time = departure_time + timedelta(hours=random.randint(1, 24))

    contact_number = generate_contact_number()

    # 랜덤으로 차종 선택
    sell_name = f"Genesis {random.choice(car_models)}"

    plate_number = generate_plate_number()
    service_type = generate_service_type()

    # 고객 요청
    customer_request = random.choice(customer_requests)

    # 검사 결과
    inspection_result = random.choice(inspection_results)

    progress_stage = random.choice(['예약완료', '차량인계', '정비중', '완료됨', '취소됨'])

    create_datetime = datetime.now()
    update_datetime = datetime.now()
    
    return (id_, customer_id, coupon_id, repair_shop_id, departure_time, arrival_time, contact_number,
            sell_name, plate_number, service_type, customer_request, inspection_result, progress_stage,
            create_datetime, update_datetime)

# 서비스 유형을 랜덤으로 생성하는 함수
def generate_service_type():
    services = {
        'oil': random.choice(['true', 'false']),
        'battery': random.choice(['true', 'false']),
        'engine-run': random.choice(['true', 'false']),
        'engine-cooler': random.choice(['true', 'false']),
        'air-cleaner': random.choice(['true', 'false']),
        'bottom': random.choice(['true', 'false']),
        'breakpad': random.choice(['true', 'false']),
        'lamp': random.choice(['true', 'false']),
        'engine-mount': random.choice(['true', 'false']),
        'suspension': random.choice(['true', 'false']),
        'shaft': random.choice(['true', 'false']),
        'scanner': random.choice(['true', 'false']),
        'heater': random.choice(['true', 'false']),
        'tire': random.choice(['true', 'false']),
        'filter': random.choice(['true', 'false'])
    }
    service_type = '{' + ', '.join(f"{key}={value}" for key, value in services.items()) + '}'
    return service_type

# 300만 건의 랜덤 데이터 생성
num_records = 3000000
data = [generate_random_reservation(i) for i in range(num_records)]

# 헤더 정보
header = ['id', 'customer_id', 'coupon_id', 'repair_shop_id', 'departure_time', 'arrival_time',
          'contact_number', 'sell_name', 'plate_number', 'service_type', 'customer_request',
          'inspection_result', 'progress_stage', 'create_datetime', 'update_datetime']

# CSV 파일로 작성
csv_filename = os.path.join(data_folder, 'reservation.csv')
write_csv(csv_filename, data, header)

print("CSV 파일이 성공적으로 생성되었습니다.")
