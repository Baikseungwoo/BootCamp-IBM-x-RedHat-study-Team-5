from Exception import UnexistPrescription
class Prescription:

    def __init__(self):
        pass

    def prescriptionRegister(self, name, disease, medicine):
        ##환자의 처방전을 입력해서 등록하는 함수
    #     {
    #     "name": "백승우",
    #     "disease": "감기",
    #     "medicine": "감기약, 몸살약, 해열제"
    #     }
        ##이런 형식으로 처방전을 입력해서 json형식으로 Perscription.json 파일에 딕셔너리로 추가하는 함수
        pass

    def findByName(self, name):
        ##name을 이용해서 Perscription.json 파일에서 해당 환자의 처방전 딕셔너리를 찾아서 제일 최근 처방전을 반환하는 함수
        ## 해당환자 없으면 UnexistPrescription(예외)를 raise시킴
        pass