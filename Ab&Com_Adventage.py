from cmath import exp
import sys
from PyQt5 import uic, QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *


form_class = uic.loadUiType('AdComAdventage.ui')[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.ResultBtn.clicked.connect(self.result)


    def result(self):
        vax = self.axsb.value()
        vbx = self.bxsb.value()
        vay = self.aysb.value()
        vby = self.bysb.value()
        ch = self.combo.currentIndex()
        try:
            if ch == 0: #생산량
                if vax > vbx:
                    self.abx.setText(f"Product X에서 A가 유리")
                elif vax < vbx:
                    self.abx.setText(f"Product X에서 B가 유리")
                else:
                    self.abx.setText(f"같음")
#--------------------------------------------------------------------------------------------
                if vay > vby:
                    self.aby.setText(f"Product Y에서 A가 유리")
                elif vay < vby:
                    self.aby.setText(f"Product Y에서 B가 유리")
                else:
                    self.aby.setText(f"같음")
#--------------------------------------------------------------------------------------------
                if float(vax / vay) > float(vbx / vby):
                    self.comy.setText(f'Product Y에서 B가 유리. A : {round(vax / vay, 2)} B : {round(vbx / vby, 2)}')
                elif float(vax / vay) < float(vbx / vby):
                    self.comy.setText(f'Product Y에서 A가 유리. A : {round(vax / vay, 2)} B : {round(vbx / vby, 2)}')
                else:
                    self.comy.setText(f"같음")
#--------------------------------------------------------------------------------------------
                if float(vay / vax) > float(vby / vbx):
                    self.comx.setText(f'Product X에서 B가 유리. A : {round(vay / vax, 2)} B : {round(vby / vbx, 2)}')
                elif float(vay / vax) < float(vby / vbx):
                    self.comx.setText(f'Product X에서 A가 유리. A : {round(vay / vax, 2)} B : {round(vby / vbx, 2)}')
                else:
                    self.comx.setText(f"같음")
#--------------------------------------------------------------------------------------------
#-------------------------이 밑부터 생산비용---------------------------------------------------
#--------------------------------------------------------------------------------------------
            if ch == 1: #생산비용
                if vax > vbx:
                    self.abx.setText(f"Product X에서 B가 유리")
                elif vax < vbx:
                    self.abx.setText(f"Product X에서 A가 유리")
                else:
                    self.abx.setText(f"같음")
#--------------------------------------------------------------------------------------------
                if vay > vby:
                    self.aby.setText(f"Product Y에서 B가 유리")
                elif vay < vby:
                    self.aby.setText(f"Product Y에서 A가 유리")
                else:
                    self.aby.setText(f"같음")
#--------------------------------------------------------------------------------------------
                if float(vax / vay) > float(vbx / vby):
                    self.comx.setText(f'Product X에서 B가 유리. A : {round(vax / vay, 2)} B : {round(vbx / vby, 2)}')
                elif float(vax / vay) < float(vbx / vby):
                    self.comx.setText(f'Product X에서 A가 유리. A : {round(vax / vay, 2)} B : {round(vbx / vby, 2)}')
                else:
                    self.comx.setText(f"같음")
#--------------------------------------------------------------------------------------------
                if float(vay / vax) > float(vby / vbx):
                    self.comy.setText(f'Product Y에서 B가 유리. A : {round(vay / vax, 2)} B : {round(vby / vbx, 2)}')
                elif float(vay / vax) < float(vby / vbx):
                    self.comy.setText(f'Product Y에서 A가 유리. A : {round(vay / vax, 2)} B : {round(vby / vbx, 2)}')
                else:
                    self.comy.setText(f"같음")
#--------------------------------------------------------------------------------------------
        except ZeroDivisionError:
            self.abx.setText(f"값을 0으로 지정하지 마세요!")
            self.aby.setText(f"값을 0으로 지정하지 마세요!")
            self.comx.setText(f"값을 0으로 지정하지 마세요!")
            self.comy.setText(f"값을 0으로 지정하지 마세요!")
            



        

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
