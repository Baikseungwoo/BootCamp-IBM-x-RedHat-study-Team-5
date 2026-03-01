from Exception import UnexepectedNum
from Exception import UnexistUser
from User import User

def logIn():
    while True:
        try:
            print("=======================================")
            print("로그인 페이지에 접속하셨습니다.")
            print("=======================================")
            name = input("이름을 입력하세요: ")
            password = input("비밀번호를 입력하세요: ")
            user = User(name, password)
            user.userLogin()
            print("로그인에 성공하였습니다!!!!")
            mainMenu()
            

        
        except UnexistUser as e:
            print(e)

def register():
    while True:
        try:
            print("=======================================")
            print("회원가입 페이지에 접속하셨습니다.")
            print("=======================================")
            name = input("이름을 입력하세요: ")
            password = input("비밀번호를 입력하세요: ")
            author = input("권한을 입력하세요.(의사: 0, 그외: 1)")
            if author not in ["1", "2"]:
                raise UnexepectedNum()
            user = User(name, password)
            user.userRegister(author, )
            print("로그인에 성공하였습니다!!!!")
            main()
        except UnexepectedNum as e:
            print(e)

    
def mainMenu():
    while True:
        try:
            print("=======================================")
            print("메인메뉴 페이지에 접속하셨습니다.")
            print("=======================================")
            print("**접속을 원하는 서비스의 메뉴번호를 입력하세요.**")
            n=input("1. 환자 정보\n2. 진료접수\n3. 예약\n4.수납\n5. 진료기록/처방전(의사만 접근가능)\n6. 로그아웃(처음부터 다시 시작)\n")
            if(n=="1"):
                
            elif(n=="2"):
                pass
            elif(n=="3"):
                pass
            elif(n=="4"):
                pass
            elif(n=="5"):
                pass
            elif(n=="6"):
                m=input("정말 나가겠습니까??\nyes -> 0\n")
                if(m=="0"):
                    main()
            else:
                raise UnexepectedNum()

        except UnexepectedNum as e:
            print(e)


def main():
    while True:
        try:
            print("=======================================")
            print("병원 운영 관리 시스템에 접속하셨습니다.")
            print("=======================================")
            print("**로그인을 원하시면 \"1\"을 입력하시고, 회원가입을 원하시면 \"2\"을 입력하세요.**\n")

            sign = input("1. 로그인\n2. 회원가입\n")
            
            if(sign=="1"):
                logIn()
            elif(sign=="2"):
                register()
            else:
                raise UnexepectedNum()

        except UnexepectedNum as e:
            print(e)

main()
