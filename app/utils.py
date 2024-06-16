import re

def normalize_phone_number(phone: str) -> str:
    # 모든 숫자를 추출
    numbers = re.sub(r'\D', '', phone)
    
    # 전화번호가 11자리인 경우에만 포맷 변경 (한국 휴대폰 번호 기준)
    if len(numbers) == 11:
        return f'{numbers[:3]}-{numbers[3:7]}-{numbers[7:]}'
    return phone
