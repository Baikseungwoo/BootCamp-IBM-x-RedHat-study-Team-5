from Exception import UnexistUser
from Exception import UnexistDoctor
class User:

    def __init__(self, name, password):
        self.name = name
        self.password=password

    def userLogin(self):
        ##이름과 비밀번호를 가지고 User.json파일 안에서 해당 인물의 정보를 찾아 확인해서 존재하면 아무것도 안함.
        ##만약 회원이 존재하지 않는다면 정의해놓은 예외인 UnexistUser를 raise.
        pass

    def userRegister(self, author, field):
    # {
    # "name":"승우", 
    # "password": 1234, 
    # "author": "0" , 
    # "field": "1"
    # } 이런식으로 User.json파일에 객체를 추가하는 함수
        pass

    def findDoctor(self, field):
        ## 해당 filed(분야)의 의사 즉, author가 "super"이며 field가 매개변수값과 같은 사람을 User.json에서 찾아서 이름을 return하는 함수
        ##만약 찾을 수 없으면 UnexistDoctor(예외)를 raise
        pass

    

    