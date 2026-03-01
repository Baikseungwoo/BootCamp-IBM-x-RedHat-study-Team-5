class UnexepectedNum(Exception):
    def __init__(self):
        super().__init__('희망하는 메뉴에 해당하는 숫자만을 입력하세요.')


class UnexistUser(Exception):
    def __init__(self):
        super().__init__('존재하지않는 회원입니다. 이름과 비밀번호를 다시 입력하세요')