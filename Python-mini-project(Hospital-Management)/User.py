from Exception import UnexistUser
from Exception import UnexistDoctor
import json

add='./User.json'

class User:
    

    def __init__(self, name, password):
        self.name = name
        self.password=password
        

    def userLogin(self):
        ##이름과 비밀번호를 가지고 User.json파일 안에서 해당 인물의 정보를 찾아 확인해서 존재하면 아무것도 안함.
        ##만약 회원이 존재하지 않는다면 정의해놓은 예외인 UnexistUser를 raise.
        with open(add,'r',encoding='utf-8') as f:
            line=json.load(f)

            for i in line:
                name,pw,author,field=i
                if i[name]==self.name and i[pw]==self.password:
                    return
                
            raise UnexistUser()


        pass

    def userRegister(self, author, field):

        data = {
        "name": self.name,
        "password": self.password,
        "author": author,
        "field": field
        }
        #이런식으로 User.json파일에 객체를 추가하는 함수
        
        with open(add,'r',encoding='utf-8') as f:
            user=json.load(f)

        user.append(data)    

        with open(add, 'w', encoding='utf-8') as f:
            json.dump(user, f, indent=4, ensure_ascii=False)

        pass

    def doctorLogin(self):
    ##이름을 가지고 User.json에서 해당인물을 찾아서 의사인지 아닌지 판단하고 없으면 UnexistDoctor raise
    ##비밀번호를 통해서 json파일에 적힌 pasword와 일치하는지 확인후 없으면 UnexistDoctor raise
    ##최종적으로 만족하는 인물을 확인했으면 True를 반환
        with open(add,'r',encoding='utf-8') as f:
            line=json.load(f)

            for i in line:
                name,pw,author,field=i

                if i[name]==self.name and i[author]=='0':
                    if i[pw]==self.password:    
                        return True
                else:
                    raise UnexistDoctor()

if __name__=='__main__':
    u=User('백승우','1234')
    u.userLogin()
    #u.userRegister('0','0')
    #u.doctorLogin()
