from Exception import UnexistUser
class User:

    def __init__(self, name, password):
        self.name = name
        self.password=password

    def userLogin(self):
        ##이름과 비밀번호를 가지고 json파일 안에서 해당 인물의 정보를 찾아 인스턴스의 author과 field를 추가 (self.author, self.field)
        ##만약 회원이 존재하지 않는다면 정의해놓은 예외인 UnexistUser를 raise.
        pass

    def userRegister(self, author, field):
    # {
    # "name":"승우", 
    # "password": 1234, 
    # "author": "0" , 
    # "field": "1"
    # } 이런식으로 json파일에 객체를 추가하는 함수
        pass

    