'''
COM - Component Object Model
여러 컴포넌트 객체를 이용해 프로그램을 개발하는 모델을 의미
컨테이너를 이용해 집을 지으면 쉽고 빨리 집을 짓는것처럼 프로그램을 개발할 때도 특정 기능을 위해
개발이 된 Component Object를 이용하면 더욱 빠르게 프로그램을 개발할 수 있다.

컴포넌트 객체한 각각의 프로그래밍 언어에서 언급하는 클래스로부터 만들어지는 객체라고 생각하면 된다.
다만 COM은 프로그래밍 언어에 국한된게 아닌 언어와 상관없이 개발된 객체를 사용할 수 있게 해준다.
EX : COM을 통해 c++같은 언어에서 생성된 객체도 파이썬 or Java에서 사용할 수 있다.

------------------------------------------------------------------------------------------------------------------------
파이썬에서 다른 프로그래밍 언어로 작성된 COM객체를 생성하려면 win32com.client라는 모듈의 Dispatch 메소드를 사용하면 된다.

'''

#EX
class CpStackCode:
    # 생성자
    def __init__(self):
        self.stocks = {'유한양행':'A000100'}

    # 주식의 종목수를 리턴하는 메소드
    def GetCount(self):
        return len(self.stocks)
    # 종목명을 입력하면 해당 종목에 관한 종목 코드를 리턴하는 메소드
    def NameToCode(self, name):
        return self.stocks[name]


instCpStockCode = CpStackCode()
print(instCpStockCode.GetCount())
print(instCpStockCode.NameToCode("유한양행"))

#EX - 마이크로소프트의 인터넷 익스플로러에 대한 객체를 생성하려면 다음과 같이 구현하면 됨

'''
win32com.client라는 모듈을 사용하기 위해 import를 진행
win32com내부의 Dispatch라는 함수를 호줄하면서, 함수의 인자로 "InternetExplorer.Application"라는 문자열을 사용
Dispatch라는 함수가 호출이 되면 객체가 생성이 되면서 explore라는 변수가 생성된 COM을 바인딩한다.
'''

import win32com.client

explore = win32com.client.Dispatch("InternetExplorer.Application")
explore.Visible = True  # True / False를 통해 익스플로러의 행동을 결정

word = win32com.client.Dispatch("Word.Application")
word.Visible = True

excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = True
