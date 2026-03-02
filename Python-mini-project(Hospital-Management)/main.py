from Exception import UnexepectedNum
from Exception import UnexistUser
from Exception import UnexistPatient
from Exception import UnexistDoctor
from Exception import UnexepectedTime
from User import User
from Patient import Patient


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
            if author not in ["0", "1"]:
                raise UnexepectedNum()
            field = input("분야를 입력하세요. (\"0\"/\"1\"/\"2\"/\"3\" (없음/외과/내과/정신과))")
            if field not in ["0","1","2","3","4"]:
                raise UnexepectedNum()
            user = User(name, password)
            user.userRegister(author,field)
            print("회원가입을 완료했습니다! 로그인을 해주십시오!!")
            main()
        except UnexepectedNum as e:
            print(e)

    
def mainMenu():
    while True:
        try:
            print("=======================================")
            print("메인메뉴 페이지에 접속하셨습니다.")
            print("=======================================")
            print("**접속을 원하는 서비스의 메뉴번호를 입력하세요.**\n")
            n=input("1. 환자 정보\n2. 진료접수\n3. 예약\n4.수납\n5. 진료기록/처방전(의사만 접근가능)\n6. 로그아웃(처음부터 다시 시작)\n")
            if(n=="1"):
                patient()
            elif(n=="2"):
                checkIn()
            elif(n=="3"):
                booking()
            elif(n=="4"):
                billing()
            elif(n=="5"):
                medicalChart()
            elif(n=="6"):
                m=input("정말 나가시겠습니까?? \n나가시려면 \"yes\"를 입력하세요.\n")
                if(m=="yes"):
                    main()
            else:
                raise UnexepectedNum()

        except UnexepectedNum as e:
            print(e)

def patient():
    while True:
        try:
            print("=======================================")
            print("환자정보 페이지에 접속하셨습니다.")
            print("=======================================")
            print("**접속을 원하는 서비스의 메뉴번호를 입력하세요.**\n")
            n=input("1. 환자 정보 조회\n2. 신규환자 등록\n3. 뒤로가기\n")
            if n not in ["1", "2", "3"]:
                raise UnexepectedNum()
            p = Patient()
            if(n=="1"):
                print("=======================================")
                print("환자정보 조회 페이지에 접속하셨습니다.")
                print("=======================================")
                print()
                name=input("조회를 원하는 환자의 이름을 입력하세요.\n")
                p.findByName(name)
                ok=input("확인하셨으면 아무 문자나 입력해주세요.")
            elif(n=="2"):
                print("=======================================")
                print("신규환자 등록 페이지에 접속하셨습니다.")
                print("=======================================")
                print()
                name=input("신규등록을 원하는 환자의 이름을 입력하세요.\n")
                resident_id=input("신규등록을 원하는 환자의 주민번호를 입력하세요.\n")
                address=input("신규등록을 원하는 환자의 주소을 입력하세요.\n")
                phoneNum=input("신규등록을 원하는 환자의 연락처를 입력하세요.\n")
                p.register(name, resident_id, address, phoneNum)
                print("신규환자 등록이 완료되었습니다.")
                ok=input("확인하셨으면 아무 문자나 입력해주세요.")
            elif(n=="3"):
                mainMenu()

        except UnexepectedNum as e:
            print(e)
        except UnexistPatient as e:
            print(e)




def checkIn():
     while True:
        try:
            print("=======================================")
            print("진료접수 페이지에 접속하셨습니다.")
            print("=======================================")
            print()
            name=input("진료를 원하는 환자의 이름을 입력하세요.\n")
            p=Patient()
            p.findByName(name)
            field = input("환자가 필요한 진료 분야를 입력하세요.\n \"0\"/\"1\"/\"2\"/\"3\" (없음/외과/내과/정신과)\n")
            if field not in ["0", "1", "2", "3"]:
                raise UnexepectedNum()
            u = User()
            doctor=u.findDoctor(field)
            print(f"해당환자를 {doctor}선생님의 진료실로 배정 완료하였습니다.")
            ok=input("확인하셨으면 아무 문자나 입력해주세요. 메인메뉴로 돌아갑니다.\n")
            mainMenu()

        except UnexistPatient as e:
            print(e)
        except UnexepectedNum as e:
            print(e)
        except UnexistDoctor as e:
            print(e)

def booking():
    while True:
        try:
            print("=======================================")
            print("예약 페이지에 접속하셨습니다.")
            print("=======================================")
            print()
            date=int(input("예약을 원하는 날짜를 입력해주세요.\n예약은 해당 월만 가능합니다.\n따라서 예약을 원하는 날짜의 일수만 입력해주세요. ( 1 ~ 31 )\n"))
            if date not in range(1,32):
                raise UnexepectedNum()
            time=input("예약을 원하는 시간대를 입력하세요\n(오전/오후)중에 선택하여 입력하세요.\n")
            if time not in ["오전","오후"]:
                raise UnexepectedTime()
            yes=fingBookingValid(date,time)
            if(yes):
                name=input("예약을 원하는 환자의 이름을 입력하세요.\n")
                makeBooking(date,time,name)
                print("예약이 완료되었습니다.")
            ok=input("확인하셨으면 아무 문자나 입력해주세요. 메인메뉴로 돌아갑니다.\n")
        except UnexepectedNum as e:
            print(e)
        except UnexepectedTime as e:
            print(e)

def fingBookingValid(date, time):
    ##books라는 리스트에서 date에 해당되는 인덱스의 딕셔너리 안에 time(오전/오후)에 해당되는 value가 빈 문자열인지 확인하는 함수
    ##가능하면 가능하다고 print하고 True반환, 만약에 값이 이미 있는 상태면 불가능하다고 print하고 False 반환
    pass

def makeBooking(date,time, name):
    ##books라는 리스트속 해당되는 딕셔너리안에 이름을넣어서 예약추가하는 함수
    pass

def billing():
    pass

def medicalChart():
    pass




books=[]

for i in range(1,32):
    books.append({
        "오전": "",
        "오후": ""
    })

main()
