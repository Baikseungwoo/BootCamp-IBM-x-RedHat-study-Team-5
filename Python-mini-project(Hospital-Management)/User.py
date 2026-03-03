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

    def doctorLogin(self):
    ##이름을 가지고 User.json에서 해당인물을 찾아서 의사인지 아닌지 판단하고 없으면 UnexistDoctor raise
    ##비밀번호를 통해서 json파일에 적힌 pasword와 일치하는지 확인후 없으면 UnexistDoctor raise
    ##최종적으로 만족하는 인물을 확인했으면 True를 반환
        return True
    

    