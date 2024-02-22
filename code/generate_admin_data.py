import csv
import random
import hashlib
from datetime import datetime

# 랜덤한 한글 이름 생성
def generate_random_korean_name():
    # 성씨 리스트
    surnames = ["김", "이", "박", "최", "정", "강", "조", "윤", "장", "임", "한", "오", "서", "신", "권", "황", 
    "안", "송", "전", "홍", "유", "고", "문", "양", "손", "배", "조", "백", "허", "유", "남", "심", "노", "정", 
    "하", "곽", "성", "차", "주", "우", "구", "신", "임", "전", "민", "유", "류", "나", "진", "지", "엄", "채", 
    "원", "천", "방", "공", "강", "현", "함", "변", "염", "양", "변", "여", "추", "노", "도", "소", "신", "석", 
    "선", "설", "마", "길", "주", "연", "위", "라", "왕", "금", "옥", "육", "인", "맹", "제", "모", "장", "남궁", 
    "탁", "국", "여", "진", "어", "은", "편", "구", "용", "유", "예", "경"]

    # 이름 리스트
    names = ["준호", "성우", "민준", "준영", "지훈", "도현", "재원", "시우", "유준", "건우", "지호", "지원", "영호", 
    "영준", "성민", "준성", "재현", "도영", "정우", "시훈", "서윤", "예은", "지윤", "서연", "하은", "예원", "지민", 
    "수빈", "윤서", "시은", "다은", "시현", "유진", "수민", "서현", "채원", "서진", "수연", "지현", "지우", "서연", 
    "지민", "현우", "지훈", "서현", "예은", "현아", "민준", "민지", "지원", "지안", "서영", "준호", "은지", "승민", 
    "지연", "현지", "민성", "민서", "현우", "예린", "지현", "유진", "혜진", "주원", "은영", "세은", "은서", "예지", 
    "동현", "수빈", "세진", "민규", "민아", "은주", "혜원", "예림", "세아", "민주", "지선", "예나", "준영", "서진", 
    "지호", "혜정", "현주", "예빈", "민혁", "민경", "세희", "예은", "민찬", "혜린", "세연", "은경", "민지", "민수", 
    "예서", "민영", "혜수", "은찬", "지수", "세정", "서윤", "예진", "혜진", "준영", "민우", "민주", "세윤", "민정", 
    "예린", "현수", "은우", "지우", "지윤", "은수", "혜림", "민경", "현우", "은채", "서우", "현준", "예나", "민아", 
    "현호", "민호", "은호", "혜민", "서하", "예림", "세영", "예지", "민규", "혜은", "민지", "혜선", "은정", "현우"]
    
    # 랜덤한 성씨와 이름 선택
    surname = random.choice(surnames)
    name = random.choice(names)

    return surname + name

# 비밀번호를 SHA-256으로 암호화하는 함수
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# CSV 파일 생성
def generate_random_admin_csv(filename, num_admins):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['admin_id', 'admin_password', 'phone_number', 'create_datetime', 'update_datetime', 'admin_name']
        writer = csv.writer(csvfile)
        writer.writerow(fieldnames)
        
        for _ in range(num_admins):
            admin_id = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=10))
            admin_password = hash_password(''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=10)))  # 비밀번호를 SHA-256으로 암호화
            phone_number = '010' + ''.join(random.choices('0123456789', k=8))
            create_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            update_datetime = create_datetime
            admin_name = generate_random_korean_name()
            writer.writerow([admin_id, admin_password, phone_number, create_datetime, update_datetime, admin_name])

if __name__ == "__main__":
    # 200 건의 랜덤 데이터를 가진 CSV 파일 생성
    generate_random_admin_csv('./data/admin.csv', 200)
    print("랜덤한 관리자 데이터가 random_admin_data.csv 파일에 생성되었습니다.")
