from Exception import UnexistPatient

class Patient:

    def __init__ (self):
        pass

    def findByName(self,name):
        ## Patient.json 파일에서 name을 이용해서 파일 리스트에 등록되어 있는 해당 환자를 조회하여 
        ## 그 환자의 개인정보를 print(출력)하는 함수
        ##만약에 환자가 존재하지 않으면 UnexistPatient(예외) raise 하기
        pass

    def register(self, name,resident_id, address, phonenum):
        ## 받은 이름, 주민번호, 주소, 연락처를 Patient.json 파일에 딕셔너리형태로 추가하는 함수
        pass