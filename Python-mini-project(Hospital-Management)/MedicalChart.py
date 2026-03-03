from Exception import UnexistMedicalChart
class MedicalChart:
    def __init__(self):
        pass

    def chartRegister(self,name,date,disease):
        ## MedicalChart.json 파일에 딕셔너리 형태로 객체를 추가하는 함수
    #     {
    #     "name":"백승우",
    #     "date":"2026-01-16",
    #     "disease":"감기 몸살"
    #     }
        pass

    def findByName(self, name):
        ##name을 이용해서 MedicalChart.json 파일에서 해당 환자의 진료기록 딕셔너리를 찾아서 모두 리스트로 반환하는 함수
        ## 해당환자의 진료기록이 없으면 UnexistMedicalChart(예외)를 raise시킴
        pass