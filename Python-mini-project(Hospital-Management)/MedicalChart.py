from Exception import UnexistMedicalChart
import json
class MedicalChart:
    def __init__(self):
        self.chart='MedicalChart.json'

    def chartRegister(self,name,date,disease):
        ## MedicalChart.json 파일에 딕셔너리 형태로 객체를 추가하는 함수
    #     {
    #     "name":"백승우",
    #     "date":"2026-01-16",
    #     "disease":"감기 몸살"
    #     }
        with open('MedicalChart.json','r',encoding='utf-8')as f:
            data=json.load(f)

        newdata={
            'name':name,
            'date':date,
            'disease':disease
        }

        data.append(newdata)
        
        with open('MedicalChart.json','w',encoding='utf-8')as f:
            json.dump(data,f,ensure_ascii=False,indent=2)
        
        

    def findByName(self, name):
        ##name을 이용해서 MedicalChart.json 파일에서 해당 환자의 진료기록 딕셔너리를 찾아서 모두 리스트로 반환하는 함수
        ## 해당환자의 진료기록이 없으면 UnexistMedicalChart(예외)를 raise시킴

        with open('MedicalChart.json','r',encoding='utf-8')as f:
            data1=json.load(f)
            match=[]
            for i in data1:
                if i['name']==name:
                    match.append(i)
                if len(match)==0:
                    raise UnexistMedicalChart()            
      
            return match
                    