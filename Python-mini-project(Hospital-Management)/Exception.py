class UnexepectedNum(Exception):
    def __init__(self):
        super().__init__('유효하지 않은 입력입니다 제대로된 숫자를 입력하세요.')

class UnexepectedTime(Exception):
    def __init__(self):
        super().__init__('유효하지 않은 입력입니다 제대로된 시간대(오전/오후)를 입력하세요.')

class UnexistPrescription(Exception):
    def __init__(self):
        super().__init__('해당 환자의 처방전이 존재하지 않습니다.')


class UnexistUser(Exception):
    def __init__(self):
        super().__init__('존재하지않는 회원입니다. 이름과 비밀번호를 다시 입력하세요')

class UnexistPatient(Exception):
    def __init__(self):
        super().__init__('존재하지않는 환자입니다. 환자정보 페이지에서 신규등록을 해주세요.')

class UnexistDoctor(Exception):
    def __init__(self):
        super().__init__('현재 해당분야의 의사를 찾을 수 없습니다. 죄송합니다.')