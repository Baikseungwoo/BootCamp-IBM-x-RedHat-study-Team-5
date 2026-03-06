from Exception import UnexistPatient
import json
import os

class Patient:

    def __init__ (self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.file = os.path.join(base_dir, "Patient.json")

    def findByName(self,name):
        with open(self.file, "r", encoding="utf-8") as f:
            data = json.load(f)

        for patient in data:
            if patient["name"] == name:
                print("이름:", patient["name"])
                print("주민번호:", patient["주민번호"])
                print("주소:", patient["address"])
                print("연락처:", patient["phoneNum"])
                return

        raise UnexistPatient("존재하지 않는 환자입니다.")
        ## Patient.json 파일에서 name을 이용해서 파일 리스트에 등록되어 있는 해당 환자를 조회하여 
        ## 그 환자의 개인정보를 print(출력)하는 함수
        ##만약에 환자가 존재하지 않으면 UnexistPatient(예외) raise 하기
        

    def register(self, name, resident_id, address, phonenum):

        with open(self.file, "r", encoding="utf-8") as f:
            data = json.load(f)

            new_patient = {
                "name": name,
                "주민번호": resident_id,
                "address": address,
                "phoneNum": phonenum
            }

            data.append(new_patient)

        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        ## 받은 이름, 주민번호, 주소, 연락처를 Patient.json 파일에 딕셔너리형태로 추가하는 함수