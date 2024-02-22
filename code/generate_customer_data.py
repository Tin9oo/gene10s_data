import csv
import random
import string

def generate_random_email():
    domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "icloud.com"]
    
    # 랜덤 사용자 이름 생성 (알파벳 대문자, 소문자, 숫자로 구성된 10자리 문자열)
    username = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    
    # 랜덤 도메인 선택
    domain = random.choice(domains)
    
    # 이메일 주소 생성
    email = username + "@" + domain
    return email

def generate_random_phone_number():
    # 핸드폰 번호 생성 (010으로 시작하는 숫자로 구성된 11자리 문자열)
    phone_number = '010' + ''.join(random.choices(string.digits, k=8))
    return phone_number

# 성씨 리스트
surnames = ["김", "이", "박", "최", "정", "강", "조", "윤", "장", "임", "한", "오", "서", "신", "권", "황", "안", "송", "전", "홍", "유", "고", "문", "양", "손", "배", "조", "백", "허", "유", "남", "심", "노", "정", "하", "곽", "성", "차", "주", "우", "구", "신", "임", "전", "민", "유", "류", "나", "진", "지", "엄", "채", "원", "천", "방", "공", "강", "현", "함", "변", "염", "양", "변", "여", "추", "노", "도", "소", "신", "석", "선", "설", "마", "길", "주", "연", "위", "라", "왕", "금", "옥", "육", "인", "맹", "제", "모", "장", "남궁", "탁", "국", "여", "진", "어", "은", "편", "구", "용", "유", "예", "경"]

# 이름 리스트
names = ["준호", "성우", "민준", "준영", "지훈", "도현", "재원", "시우", "유준", 
		"건우", "지호", "지원", "영호", "영준", "성민", "준성", "재현", "도영", "정우", 
		"시훈", "서윤", "예은", "지윤", "서연", "하은", "예원", "지민", "수빈", "윤서", 
		"시은", "다은", "시현", "유진", "수민", "서현", "채원", "서진", "수연", "지현", 
		"지우", "서연", "지민", "현우", "지훈", "서현", "예은", "현아", "민준", "민지",
    "지원", "지안", "서영", "준호", "은지", "승민", "지연", "현지", "민성", "민서",
    "현우", "예린", "지현", "유진", "혜진", "주원", "은영", "세은", "은서", "예지",
    "동현", "수빈", "세진", "민규", "민아", "은주", "혜원", "예림", "세아", "민주",
    "지선", "예나", "준영", "서진", "지호", "혜정", "현주", "예빈", "민혁", "민경",
    "세희", "예은", "민찬", "혜린", "세연", "은경", "민지", "민수", "예서", "민영",
    "혜수", "은찬", "지수", "세정", "서윤", "예진", "혜진", "준영", "민우", "민주",
    "세윤", "민정", "예린", "현수", "은우", "지우", "지윤", "은수", "혜림", "민경",
    "현우", "은채", "서우", "현준", "예나", "민아", "현호", "민호", "은호", "혜민",
    "서하", "예림", "세영", "예지", "민규", "혜은", "민지", "혜선", "은정", "현우"]

# 데이터 수
data_count = 2000000

# CSV 파일 저장
with open('random_users.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['이름', '이메일', '핸드폰번호']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    
    for _ in range(data_count):
        surname = random.choice(surnames)
        name = random.choice(names)
        email = generate_random_email()
        phone_number = generate_random_phone_number()
        writer.writerow({'이름': surname + name, '이메일': email, '핸드폰번호': phone_number})

print(f"{data_count}개의 랜덤한 이름, 이메일, 핸드폰 번호가 random_users.csv 파일에 저장되었습니다.")
