#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)
print(sys.argv)  ##sys.argv가 무엇인지 궁금해서 쳐보면, 고유주소임. 이걸 생성자로 넣어줘야함
label = QLabel("Hi sohheon")
label.show()
app.exec_()


# In[1]:


import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)
label = QPushButton("Quit")  ##새로운 클래스를 사용해봄
label.show()
app.exec_()


# In[1]:


import sys
from PyQt5.QtWidgets import *  #sys모듈 불러오기, PyQt5모듈 불러오기

class MyWindow(QMainWindow):  #MyWindow Class생성하는데, 이건 QMainWindow클래스의 기능을 상속받겠다
    def __init__(self):  ##__init__메서드로 초깃값 설정
        super().__init__()  ##Q. super함수? - A. 부모클래스에 정의된 __init__()를 호출함. 내장함수
        self.setWindowTitle("PyStock")  ##setWindowTitle함수 사용 - Q. 'PyStock'이라고 뜨나? A. 타이틀 창의 텍스트를 바꾸는 메서드
        self.setGeometry(300, 300, 
                         300, 400)  ##setGeometry함수 사용 - Q. 각각의 값이 부여되나? A. 창의 위치 및 크기를 조절하는 메서드
        
if __name__ == "__main__":  ##직접 이 파일을 실행시키면 아랫값들을 수행하지만, 다른 곳에서 모듈을 불러쓰면 수행하지 말아라. 이걸 안 쓰면 MyWindow 클래스를 다른 데서 실행할 때, 아래 해당값이 뜸
    app = QApplication(sys.)  ##QApplication이라는 클래스를 사용하겠다
    mywindow = MyWindow()  ##mywindow는 이제 MyWindow클래스의 인스턴스가 됨. 클래스 사용 가능
    mywindow.show()  ##show라는 함수를 씀 - 띄워주나?
    app.exec_()


# In[1]:


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pystock")
        self.setGeometry(300, 300, 300, 400)
        
        btn1 = QPushButton("Click me", self)  #btn1이라는 변수로 QPushButton클래스 사용. Click me라고 뜨게 하기
        btn1.move(20, 20)  #Q. 버튼의 크기, 길이 설정? A. 버튼 출력 위치를 move메서드를 사용해 조절
        btn1.clicked.connect(self.btn1_clicked)  #Q. clicekd.connect함수 사용? A. 이벤트와 이벤트를 처리할 메서드를 connect라는 메서드로 연결
        
    def btn1_clicked(self):
        QMessageBox.about(self, "message", "clicked")  #이것도 메서드 사용? 'clicked'라는 메세지가 뜨는 메세지박스를 띄워라.
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()


# In[1]:


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QAxContainer import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyStock")
        self.setGeometry(300, 300, 300, 150)
        
        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")  #고유의 값을 가짐(CLSID, ProgID)
        
        btn1 = QPushButton("Login", self)
        btn1.move(20, 20)
        btn1.clicked.connect(self.btn1_clicked)  #사용자의 이벤트 행동을 아래에 있는 이벤트처리함수와 연결
        
        btn2 = QPushButton("Check state", self)
        btn2.move(20, 70)
        btn2.clicked.connect(self.btn2_clicked)
        
    def btn1_clicked(self):
        ret = self.kiwoom.dynamicCall("CommConnect()")  #ret이라는 변수에 self.kiwoom을 dynamicCall함수에 적용한 결과 할당. 로그인버튼 누르면 이렇게 뜨라고
        #A. 인스턴스를 통해 CommConnect메서드를 호추라면 로그인을 위한 윈도우가 자동으로 실행. 인자를 받지 않으며, 반환 값을 통해 로그인 성공 여부를 확인할 수 있음
        
    def btn2_clicked(self):
        if self.kiwoom.dynamicCall("GetConnecState()") == 0:  #check state눌렀을 때, 뭔가가 0이면 연결 안 됐다고 뜨게 해라.
            #dynamicCall 메서드로 원하는 메서드를 호출할 수 있음
            self.statusBar().showMessage("Not connected")
        else:
            self.statusBar().showMessage("Connected")
            
if __name__=="__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()


# In[ ]:


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5. QAxContainer import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyStock")
        self.setGeometry(300, 300, 300, 150)
        
        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.kiwoom.dynamicCall("CommConnect()")
        
        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(10, 60, 280, 80)
        self.text_edit.setEnabled(False)
        
        self.kiwoom.OnEventConnect.connect(self.event_connect)  #둘을 연결
        
    def event_connect(self, err_code):
        if err_code == 0:
            self.text_edit.append("로그인 성공")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()


# In[1]:


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QAxContainer import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.kiwoom.dynamicCall("CommConnect()")
        
        self.kiwoom.OnEventConnect.connect(self.event_connect)
        self.kiwoom.OnReceiveTrData.connect(self.receive_trdata)
        
        self.setWindowTitle("PyStock")
        self.setGeometry(300, 300, 300, 150)  #창의 제목과 크기, 위치
        
        label = QLabel('종목코드: ', self) #Q.두 번째 인자에는 부모 위젯을 지정라하라는 게 무슨 뜻?
        label.move(20, 20)  #QLabel 클래스를 사용해서 종목코드 출력. 위치는 move함수 사용
        
        self.code_edit = QLineEdit(self)
        self.code_edit.move(80, 20)
        self.code_edit.setText("039490")  #QLineEdit 클래스 사용해서 넣는 칸 만들기 Q. 왜 숫자를 미리 써놓지? 그러면 모든 정보를 다 써놓아야하나?
        #A. 아니야, 다른 종목코드 써도 정보가 출력이 됨. 그러면 굳이 "039490"을 안 써도 되는 거지?
        
        btn1 = QPushButton("조회", self)
        btn1.move(190, 20)
        btn1.clicked.connect(self.btn1_clicked) #이벤트행동(조회 누르면)과 이벤트 처리(종목코드와 코드가 떠라) 연결
        
        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(10, 60, 280, 80)
        self.text_edit.setEnabled(False) #읽기쓰기가능여부. 읽기만 가능으로!
        
    def event_connect(self, err_code):
        if err_code == 0:
            self.text_edit.append("로그인 성공")
            
    def btn1_clicked(self):
        code = self.code_edit.text()
        self.text_edit.append("종목코드: " + code)
        
        self.kiwoom.dynamicCall("SetInputValue(Qstring, Qstring)", "종목코드", code)  #문자 두 개, 종목코드, 코드 뜨는 듯
        
        self.kiwoom.dynamicCall("CommRqData(Qstring, Qstring, int, Qstring)", "opt10001_req", "opt10001", 0, "0101") #10001기능 가져와서 출력?
        
    def receive_trdata(self, screen_no, rqname, trcode, recordname, prev_next, data_len, err_code, msg1, msg2):
        if rqname == "opt10001_req":
            name = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "종목명")
            volume = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "거래량")
            
            self.text_edit.append("종목명: " + name.strip())
            self.text_edit.append("거래량: " + volume.strip())
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()


# In[1]:


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QAxContainer import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.kiwoom.dynamicCall("CommConnect()")
        
        self.kiwoom.OnEventConnect.connect(self.event_connect)
        
        self.setWindowTitle("계좌 정보")
        self.setGeometry(300, 300, 300, 150)
        
        btn1 = QPushButton("계좌 얻기", self)
        btn1.move(190, 20)
        btn1.clicked.connect(self.btn1_clicked)
        
        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(10, 60, 280, 80)
        
    def btn1_clicked(self):
        account_num = self.kiwoom.dynamicCall("GetLoginInfo(QString)", ["ACCNO"])
        self.text_edit.append("계좌번호: " + account_num.rstrip(';'))
        
    def event_connect(self, err_code):
        if err_code == 0:
            self.text_edit.append("로그인 성공")
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()


# In[1]:


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QAxContainer import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.kiwoom.dynamicCall("CommConnect()")
        
        self.setWindowTitle("종목 코드")
        self.setGeometry(300, 300, 300, 150)
        
        btn1 = QPushButton("종목코드 얻기", self)
        btn1.move(190, 10)
        btn1.clicked.connect(self.btn1_clicked)
        
        self.listWidget = QListWidget(self)
        self.listWidget.setGeometry(10, 10, 170, 130)
        
    def btn1_clicked(self):
        ret = self.kiwoom.dynamicCall("GetCodeListByMarket(QString)", ["0"])
        kospi_code_list = ret.split(';')
        kospi_code_name_list = []
        
        for x in kospi_code_list:  #코스피 코드 리스트 안에 x를 반복 출력해라!
            name = self.kiwoom.dynamicCall("GetMasterCodeName(Qstring)", [x])
            kospi_code_name_list.append(x + " : " + name)  #x : 이름 형식으로
            
        self.listWidget.addItems(kospi_code_name_list)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    sys.exit(app.exec_())  #여기가 달라졌네. 왜...?


# In[ ]:




