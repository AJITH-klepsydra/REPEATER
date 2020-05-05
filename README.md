# REPEATER
Helps you to automate repetitive computational tasks which utilises mouse and Keyboard.
Made with Python3(pyautogui,pynput,pyqt5). currently it can monitor events like mouse clicks, 
button presses and mouse scrolling. Key holding and mouse dragging aren't yet implemented
import sys

from PyQt5 import QtWidgets,uic,QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal,QUrl
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import cv2
from PyQt5.QtGui import QIcon, QPixmap
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from PyQt5 import QtGui
import requests
from PyQt5.QtWebEngineWidgets import QWebEngineSettings, QWebEngineView, QWebEnginePage
import url1
import pyautogui
import numpy as np
import random


from bs4 import BeautifulSoup
class Web(QWebEngineView):

    def load(self, url):
        self.setUrl(QUrl(url))

    def adjustTitle(self):
        self.setWindowTitle(self.title())

    def disableJS(self):
        settings = QWebEngineSettings.globalSettings()
        settings.setAttribute(QWebEngineSettings.JavascriptEnabled, False)

def draw_circle(event,x,y,flags,param):
	if event == cv2.EVENT_LBUTTONDOWN:
		img = cv2.imread('/home/klepsydra/Python_projects/covid19/Covid-19-Tracker-master/world_map.jpg')

		cv2.circle(img,(x,y),10,(255,0,0),-1)
		if(x<1079 and x>1068 and y<358 and y>348):
                        f=open('m.txt','w')
                        f.write('China')
                        print('China')
                        f.close()
                        pyautogui.press('esc')
		elif(x<1001 and x>991 and y<423 and y>415):
			f=open('m.txt','w')
			f.write('India')
			print('India')
			f.close()
			pyautogui.press('esc')
			
		elif(x<264 and x>254 and y<323 and y>313):
			f=open('m.txt','w')
			f.write('USA')
			print('USA')
			f.close()
			pyautogui.press('esc')

		elif(x<1208 and x>1196 and y<494 and y>483):
			f=open('m.txt','w')
			f.write('Indonesia')
			print('Indonesia')
			f.close()
			pyautogui.press('esc')

		elif(x<959 and x>946 and y<382 and y>369):
			f=open('m.txt','w')
			f.write('Paskistan')
			print('Pakistan')
			f.close()
			pyautogui.press('esc')
			
		elif(x<491 and x>479 and y<536 and y>524):
			f=open('m.txt','w')
			f.write('Brazil')
			print('Brazil')
			f.close()
			pyautogui.press('esc')

		elif(x>681 and x<696 and y>442 and y<455):
			f=open('m.txt','w')
			f.write('Nigeria')
			print('Nigeria')
			f.close()
			pyautogui.press('esc')
			
		elif(x>1042 and x<1057 and y>172 and y<187):
			f=open('m.txt','w')
			f.write('Russia')
			print('Russia')
			f.close()
			pyautogui.press('esc')

		elif(x>286 and x<301 and y>398 and y<411):
			f=open('m.txt','w')
			f.write('Mexico')
			print('Mexico')
			f.close()
			pyautogui.press('esc')

		elif(x>1180 and x<1194 and y>370 and y<384):
			f=open('m.txt','w')
			f.write('Japan')
			print('Japan')
			f.close()
			pyautogui.press('esc')

		elif(x>834 and x<849 and y>486 and y<501):
			f=open('m.txt','w')
			f.write('Ethiopiia')
			print('Ethiopia')
			f.close()
			pyautogui.press('esc')

		elif(x>726 and x<742 and y>377 and y<391):
			f=open('m.txt','w')
			f.write('Egypt')
			print('Egypt')
			f.close()
			pyautogui.press('esc')

		elif(x>742 and x<757 and y>512 and y<525):
			f=open('m.txt','w')
			f.write('DR Congo')
			print('Dr Congo')
			f.close()
			pyautogui.press('esc')

		elif(x>782 and x<796 and y>333 and y<349):
			f=open('m.txt','w')
			f.write('Turkey')
			print('Turkey')
			f.close()
			pyautogui.press('esc')

		elif(x>866 and x<883 and y>329 and y<345):
			f=open('m.txt','w')
			f.write('Iran')
			print('Iran')
			f.close()
			pyautogui.press('esc')

		elif(x>699 and x<714 and y>238 and y<250):
			f=open('m.txt','w')
			f.write('Germany')
			print('Germany')
			f.close()
			pyautogui.press('esc')

		elif(x>648 and x<661 and y>228 and y<241):
			f=open('m.txt','w')
			f.write('UK')
			print('UK')
			f.close()
			pyautogui.press('esc')

		elif(x>665 and x<678 and y>266 and y<280):
			f=open('m.txt','w')
			f.write('France')
			print('France')
			f.close()
			pyautogui.press('esc')

		elif(x>729 and x<745 and y>288 and y<302):
			f=open('m.txt','w')
			f.write('Italy')
			print('Italy')
			f.close()
			pyautogui.press('esc')

		elif(x>750 and x<764 and y>483 and y<499):
			f=open('m.txt','w')
			f.write('Tanzania')
			print('Tanzania')
			f.close()
			pyautogui.press('esc')

		elif(x>774 and x<787 and y>635 and y<649):
			f=open('m.txt','w')
			f.write('South Africa')
			print('South Africa')
			f.close()
			pyautogui.press('esc')

		elif(x>824 and x<839 and y>532 and y<548):
			f=open('m.txt','w')
			f.write('Kenya')
			print('Kenya')
			f.close()
			pyautogui.press('esc')

		elif(x>1151 and x<1168 and y>397 and y<412):
			f=open('m.txt','w')
			f.write('South Korea')
			print('South Korea')
			f.close()
			pyautogui.press('esc')

		elif(x>357 and x<389 and y>480 and y<493):
			f=open('m.txt','w')
			f.write('Colombia')
			print('Colombia')
			f.close()
			pyautogui.press('esc')

		elif(x>606 and x<622 and y>282 and y<297):
			f=open('m.txt','w')
			f.write('Spain')
			print('Spain')
			f.close()
			pyautogui.press('esc')

		elif(x>426 and x<441 and y>646 and y<661):
			f=open('m.txt','w')
			f.write('Argentina')
			print('Argentina')
			f.close()
			pyautogui.press('esc')

		elif(x>652 and x<670 and y>362 and y<377):
			f=open('m.txt','w')
			f.write('Algeria')
			print('Algeria')
			f.close()
			pyautogui.press('esc')

		elif(x>810 and x<825 and y>448 and y<463):
			f=open('m.txt','w')
			f.write('Sudan')
			print('Sudan')
			f.close()
			pyautogui.press('esc')

		elif(x>722 and x<734 and y>251 and y<264):
			f=open('m.txt','w')
			f.write('Ukraine')
			print('Ukraine')
			f.close()
			pyautogui.press('esc')

		elif(x>832 and x<847 and y>359 and y<373):
			f=open('m.txt','w')
			f.write('Iraq')
			print('Iraq')
			f.close()
			pyautogui.press('esc')

		elif(x>922 and x<935 and y>331 and y<344):
			f=open('m.txt','w')
			f.write('Afghanisthan')
			print('Afghanisthan')
			f.close()
			pyautogui.press('esc')

		elif(x>728 and x<743 and y>208 and y<222):
			f=open('m.txt','w')
			f.write('Poland')
			print('Poland')
			f.close()
			pyautogui.press('esc')

		elif(x>237 and x<252 and y>192 and y<210):
			f=open('m.txt','w')
			f.write('Canada')
			print('Canada')
			f.close()
			pyautogui.press('esc')

		elif(x>679 and x<694 and y>312 and y<326):
			f=open('m.txt','w')
			f.write('Morocco')
			print('Morocco')
			f.close()
			pyautogui.press('esc')

		elif(x>861 and x<877 and y>411 and y<425):
			f=open('m.txt','w')
			f.write('Saudi Arabia')
			print('Saudi Arabia')
			f.close()
			pyautogui.press('esc')

		elif(x>912 and x<929 and y>281 and y<296):
			f=open('m.txt','w')
			f.write('Uzbekistan')
			print('Uzbekistan')
			f.close()
			pyautogui.press('esc')

		elif(x>448 and x<463 and y>462 and y<481):
			f=open('m.txt','w')
			f.write('Peru')
			print('Peru')
			f.close()
			pyautogui.press('esc')

		elif(x>720 and x<736 and y>552 and y<566):
			f=open('m.txt','w')
			f.write('Angola')
			print('Angola')
			f.close()
			pyautogui.press('esc')

		elif(x>865 and x<880 and y>432 and y<446):
			f=open('m.txt','w')
			f.write('Yemen')
			print('Yemen')
			f.close()
			pyautogui.press('esc')
			
		elif(x>324 and x<342 and y>510 and y<528):
			f=open('m.txt','w')
			f.write('Venezuela')
			print('Venezuela')
			f.close()
			pyautogui.press('esc')

		elif(x>862 and x<876 and y>560 and y<575):
			f=open('m.txt','w')
			f.write('Madagascar')
			print('Madagascar')
			f.close()
			pyautogui.press('esc')

		elif(x>1174 and x<1190 and y>574 and y<594):
			f=open('m.txt','w')
			f.write('Australia')
			print('Australia')
			f.close()
			pyautogui.press('esc')

		elif(x>675 and x<690 and y>414 and y<429):
			f=open('m.txt','w')
			f.write('Niger')
			print('Niger')
			f.close()
			pyautogui.press('esc')

		elif(x>1008 and x<1026 and y>458 and y<474):
			f=open('m.txt','w')
			f.write('Sri Lanka')
			print('Sri Lanka')
			f.close()
			pyautogui.press('esc')

		elif(x>627 and x<644 and y>413 and y<428):
			f=open('m.txt','w')
			f.write('Mali')
			print('Mali')
			f.close()
			pyautogui.press('esc')

		elif(x>785 and x<828 and y>255 and y<264):
			f=open('m.txt','w')
			f.write('Romania')
			print('Romania')
			f.close()
			pyautogui.press('esc')

		elif(x>408 and x<424 and y>610 and y<623):
			f=open('m.txt','w')
			f.write('Chile')
			print('Chile')
			f.close()
			pyautogui.press('esc')

		elif(x>915 and x<930 and y>247 and y<266):
			f=open('m.txt','w')
			f.write('Kazakhstan')
			print('Kazakhstan')
			f.close()
			pyautogui.press('esc')

		elif(x>774 and x<788 and y>565 and y<581):
			f=open('m.txt','w')
			f.write('Zambia')
			print('Zambia')
			f.close()
			pyautogui.press('esc')

		elif(x>794 and x<810 and y>373 and y<386):
			f=open('m.txt','w')
			f.write('Syria')
			print('Syria')
			f.close()
			pyautogui.press('esc')

		elif(x>777 and x<791 and y>437 and y<452):
			f=open('m.txt','w')
			f.write('Chad')
			print('Chad')
			f.close()
			pyautogui.press('esc')

		elif(x>823 and x<837 and y>508 and y<522):
			f=open('m.txt','w')
			f.write('Somalia')
			print('Somalia')
			f.close()
			pyautogui.press('esc')

		elif(x>662 and x<677 and y>335 and y<348):
			f=open('m.txt','w')
			f.write('Tunisia')
			print('Tunisia')
			f.close()
			pyautogui.press('esc')

		elif(x>417 and x<434 and y>574 and y<591):
			f=open('m.txt','w')
			f.write('Bolivia')
			print('Bolivia')
			f.close()
			pyautogui.press('esc')

		elif(x>801 and x<818 and y>288 and y<306):
			f=open('m.txt','w')
			f.write('Greece')
			print('Greece')
			f.close()
			pyautogui.press('esc')
			
		elif(x>603 and x<621 and y>309 and y<327):
			f=open('m.txt','w')
			f.write('Portugal')
			print('Portugal')
			f.close()
			pyautogui.press('esc')

		elif(x>677 and x<693 and y>180 and y<196):
			f=open('m.txt','w')
			f.write('Belarus')
			print('Belarus')
			f.close()
			pyautogui.press('esc')

		elif(x>771 and x<811 and y>230 and y<238):
			f=open('m.txt','w')
			f.write('Austria')
			print('Austria')
			f.close()
			pyautogui.press('esc')

		elif(x>900 and x<914 and y>305 and y<322):
			f=open('m.txt','w')
			f.write('Turkmenistan')
			print('Turkmenistan')
			f.close()
			pyautogui.press('esc')

		elif(x>750 and x<764 and y>402 and y<418):
			f=open('m.txt','w')
			f.write('Libya')
			print('Libya')
			f.close()
			pyautogui.press('esc')

		elif(x>688 and x<702 and y>221 and y<234):
			f=open('m.txt','w')
			f.write('Denmark')
			print('Denmark')
			f.close()
			pyautogui.press('esc')

		elif(x>788 and x<805 and y>138 and y<151):
			f=open('m.txt','w')
			f.write('Finland')
			print('Finland')
			f.close()
			pyautogui.press('esc')

		elif(x>722 and x<738 and y>134 and y<148):
			f=open('m.txt','w')
			f.write('Norway')
			print('Norway')
			f.close()
			pyautogui.press('esc')

		elif(x>891 and x<908 and y>449 and y<465):
			f=open('m.txt','w')
			f.write('Oman')
			print('Oman')
			f.close()
			pyautogui.press('esc')

		elif(x>593 and x<611 and y>244 and y<260):
			f=open('m.txt','w')
			f.write('Ireland')
			print('Ireland')
			f.close()
			pyautogui.press('esc')

		elif(x>1090 and x<1104 and y>282 and y<298):
			f=open('m.txt','w')
			f.write('Mongolia')
			print('Mongolia')
			f.close()
			pyautogui.press('esc')

		elif(x>743 and x<758 and y>591 and y<607):
			f=open('m.txt','w')
			f.write('Namibia')
			print('Namibia')
			f.close()
			pyautogui.press('esc')

		elif(x>1279 and x<1295 and y>676 and y<691411):
			f=open('m.txt','w')
			f.write('Newzealand')
			print('Newzealand')
			f.close()
			pyautogui.press('esc')

		elif(x>771 and x<787 and y>616 and y<631):
			f=open('m.txt','w')
			f.write('Botswana')
			print('Botswana')
			f.close()
			pyautogui.press('esc')

		elif(x>615 and x<633 and y>113 and y<132):
			f=open('m.txt','w')
			f.write('Iceland')
			print('Iceland')
			f.close()
			pyautogui.press('esc')

		elif(x>511 and x<528 and y>54 and y<71):
			f=open('m.txt','w')
			f.write('Greenland')
			print('Greenland')
			f.close()
			pyautogui.press('esc')

		elif(x>714 and x<730 and y>103 and y<117):
			f=open('m.txt','w')
			f.write('Sweden')
			print('Sweden')
			f.close()
			pyautogui.press('esc')

		elif(x>1066 and x<1080 and y>420 and y<433):
			f=open('m.txt','w')
			f.write('Thailand')
			print('Thailand')
			f.close()
			pyautogui.press('esc')

		elif(x>993 and x<1005 and y>306 and y<322):
			f=open('m.txt','w')
			f.write('Kyrgyzstan')
			print('Kyrgyzstan')
			f.close()
			pyautogui.press('esc')

		elif(x>121 and x<139 and y>108 and y<126):
			f=open('m.txt','w')
			f.write('Alaska')
			print('Alaska')
			f.close()
			pyautogui.press('esc')
		else:
			print("not valid")
class MplCanvas(FigureCanvasQTAgg):
	def __init__(self, parent=None, width=5, height=4, dpi=100):
		f, ax = plt.subplots(figsize=(18,5)) 
		plt.bar([1,2,3], [global1.confirmed,global1.death,global1.recovered],label='', color=(1,0.274509804,0.466666667,1))
		f.set_facecolor(color=(0.156862745,0.129411765,0.250980392,0.588235294))
		ax.set_facecolor(color=(0.156862745,0.129411765,0.250980392,0.588235294))
		ax.tick_params(axis='x', colors=(0.301960784,0.301960784,0.392156863,1))
		ax.tick_params(axis='y', colors=(0.301960784,0.301960784,0.392156863,1))

	
		ax.legend(fontsize = 14)
		ax.set_xticklabels(('','','confirmed Cases','','Deaths','','Recovered Cases'))
		super(MplCanvas,self).__init__(f)
class dash_board(QtWidgets.QMainWindow):
	sig2g = QtCore.pyqtSignal()
	sig2c = QtCore.pyqtSignal()
	sig2ck = QtCore.pyqtSignal()
	sig2i = QtCore.pyqtSignal()
	def __init__(self):
		super(dash_board,self).__init__()
		uic.loadUi("dash.ui",self)
		StyleSheet = '''
		QPushButton{
		border-width: 2px;
		border-radius:6px;
		font: 57 16pt "Ubuntu";
		background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(235, 137, 39, 255));

		}
		QPushButton:hover {
    	background-color: #64b5f6;
    	color: #fff;
		}
		'''
		StyleSheet2 = '''
		QPushButton{
		color: rgb(255,255,255);
		font: 75 20pt "Ubuntu";

		}
		QPushButton:hover {
    	color: rgb(0,255,0);
		font: 75 20pt "Ubuntu";

		}
		'''
		StyleSheet3 = '''
		QPushButton{
		color: rgb(255,255,255);
		font: 30pt "Webdings";


		}
		QPushButton:hover {
		color: rgb(0,255,0);
		font: 30pt "Webdings";
		}
		'''
		StyleSheet4 = '''
		QPushButton{
		color: rgb(255,255,255);
		font: 30pt "Webdings";


		}
		QPushButton:hover {
		color: rgb(255,0,0);
		font: 30pt "Webdings";
		}
		'''
		StyleSheet5 = '''
		QLabel{
		background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(0, 0, 0, 0));
		font: 75 10pt "Ubuntu";
		color:rgb(255, 255, 255);

		}
		QLabel:hover {
		background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(0, 0, 0, 0));
		font: 75 10pt "Ubuntu";
		color: rgb(150, 150, 150);
		}
		'''
		StyleSheet6 = '''
		QTextBrowser{
		background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(0, 0, 0, 0)););

		}
		QLabel:hover {
		background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(0, 0, 0, 0));
		font: 75 10pt "Ubuntu";
		color: rgb(150, 150, 150);
		}
		'''

		self.p1.setStyleSheet(StyleSheet)
		self.p2.setStyleSheet(StyleSheet)
		self.p3.setStyleSheet(StyleSheet)
		self.p4.setStyleSheet(StyleSheet)
		self.p11.setStyleSheet(StyleSheet2)
		self.p22.setStyleSheet(StyleSheet3)
		self.p33.setStyleSheet(StyleSheet3)
		self.p44.setStyleSheet(StyleSheet3)
		self.quit.setStyleSheet(StyleSheet4)

		self.l1.setStyleSheet(StyleSheet5)
		self.l2.setStyleSheet(StyleSheet5)
		self.l3.setStyleSheet(StyleSheet5)
		self.l4.setStyleSheet(StyleSheet5)
		self.l5.setStyleSheet(StyleSheet5)
		self.l6.setStyleSheet(StyleSheet5)
		self.l7.setStyleSheet(StyleSheet5)
		self.l8.setStyleSheet(StyleSheet5)
		self.l9.setStyleSheet(StyleSheet5)
		self.l10.setStyleSheet(StyleSheet5)
		self.l11.setStyleSheet(StyleSheet5)
		self.l12.setStyleSheet(StyleSheet5)
		
		self.p1.clicked.connect(self.toglob)
		self.p11.clicked.connect(self.toglob)
		self.p2.clicked.connect(self.tocnt)
		self.p22.clicked.connect(self.tocnt)
		self.p3.clicked.connect(self.tocheck)
		self.p33.clicked.connect(self.tocheck)
		self.p4.clicked.connect(self.toinf)
		self.p44.clicked.connect(self.toinf)
		self.quit.clicked.connect(self.quit1)
		self.show()
	def quit1(self):
		sys.exit()
	def toinf(self):
		self.sig2i.emit()
	def toglob(self):
		self.sig2g.emit()
	def tocnt(self):
		self.sig2c.emit()
	def tocheck(self):
		self.sig2ck.emit()
import global1
class main_window(QtWidgets.QMainWindow):

	sigc=QtCore.pyqtSignal()
	sigi = QtCore.pyqtSignal()
	sigcc = QtCore.pyqtSignal()
	map =QtCore.pyqtSignal()
	def __init__(self):
		super(main_window,self).__init__()
		uic.loadUi('main_window1.ui',self)
		StyleSheet = '''
		QPushButton{
		color: rgb(255, 255, 255);
		border-width: 2px;
		border-radius:15px;
		font: 75 15pt "Ubuntu";
		background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(77, 70, 100, 255));

		}
		QPushButton:hover {
    	background-color: #64b5f6;
    	color: #fff;
		}
		'''
		StyleSheet2 = '''
		QPushButton{
		color: rgb(255,255,255);
		font: 75 20pt "Ubuntu";

		}
		QPushButton:hover {
    	color: rgb(0,255,0);
		font: 75 20pt "Ubuntu";

		}
		'''
		StyleSheet3 = '''
		QPushButton{
		color: rgb(255,255,255);
		font: 30pt "Webdings";


		}
		QPushButton:hover {
		color: rgb(0,255,0);
		font: 30pt "Webdings";
		}
		'''
		StyleSheet4 = '''
		QLabel{
		font: 57 26pt "Ubuntu";
		color: rgb(150, 22, 41);;


		}
		QLabel:hover {
		font: 57 37pt "Ubuntu";
		color: rgb(150, 150, 41);;

		}



		'''
		self.cc.setStyleSheet(StyleSheet)
		self.cp.setStyleSheet(StyleSheet)
		self.cp_2.setStyleSheet(StyleSheet)
		self.hmb.setStyleSheet(StyleSheet2)
		self.bt.setStyleSheet(StyleSheet3)
		self.inn.setStyleSheet(StyleSheet3)
		self.cn.setStyleSheet(StyleSheet3)
		self.confirmed.setStyleSheet(StyleSheet4)
		self.death.setStyleSheet(StyleSheet4)
		self.recovered.setStyleSheet(StyleSheet4)
		


		layout = QtWidgets.QVBoxLayout(self.widget)


		if(url1.k==0):
			self.confirmed.setText("NETWORK ERROR")
			self.death.setText(str("NETWORK ERROR"))
			self.recovered.setText(str("NETWORK ERROR"))
		else:
			self.confirmed.setText(str(global1.confirmed))
			self.death.setText(str(global1.death))
			self.recovered.setText(str(global1.recovered))
			self.cc.clicked.connect(self.tocc)
			sc = MplCanvas(self)
            
			layout.addWidget(sc)
			self.cp.clicked.connect(self.tocountry)
			#self.inb.clicked.connect(self.toinfo)
			self.show()




	def tocc(self):

		self.sigcc.emit()
	def toinfo(self):
		self.sigi.emit()

	def tocountry(self):
		self.sigc.emit()
		self.map.emit()

class c_window(QtWidgets.QMainWindow):
	def __init__(self):
		super(c_window,self).__init__()
		uic.loadUi('c_window1.ui',self)
		self.figure = plt.figure()
		self.canvas = FigureCanvas(self.figure)
		self.toolbar = NavigationToolbar(self.canvas, self)
		layout1 =QtWidgets.QVBoxLayout(self.wid1)
		layout1.addWidget(self.canvas)
		layout1.addWidget(self.toolbar)
		self.mp.clicked.connect(self.tomp)
		


		#f = open("country.txt","rb")
		#for line in f:
		#	cstr=str(line.strip())
		#	self.cb.addItem(str(cstr[2:-1]))
		#f.close()
		

		self.show()


	def tomp(self):
		img = cv2.imread('/home/klepsydra/Python_projects/covid19/Covid-19-Tracker-master/world_map.jpg')
		cv2.namedWindow('select_country', cv2.WINDOW_NORMAL)
		cv2.setMouseCallback('select_country',draw_circle)
		cv2.setWindowProperty ('select_country', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
		while(1):
			cv2.imshow('select_country',img)
			k = cv2.waitKey(20) & 0xFF
			if k == 27:
				break
		cv2.destroyAllWindows()
		QtWidgets.QApplication.setOverrideCursor(Qt.WaitCursor)
		f= open("m.txt","r")
		cnt=str(f.read())
		print(cnt)
		f.close()
		self.tag.setText(cnt)
		country=cnt
    	
		url = r'https://www.worldometers.info/coronavirus/'
		resource = requests.get(url).text
		souped_resource = BeautifulSoup(resource, "html.parser")
		all_tr = souped_resource.find_all('tr')
		flag = 0
		count = 0
		rdata = []
		for tr in all_tr:
			all_td = tr.find_all('td')
			for td in all_td:
				if flag == 1:
					rdata.append(td.string)
					count += 1
					if count > 10:
						break
				try:
					if td.string.startswith(country):
						flag = 1
				except:
					continue
			if count > 10:
				break
		datar = [str(x) for x in rdata]


		#info = requests.get(request_url)
		#dataq = info.json()
		#data = info.json()[-1]
		#for case in dataq:
			#x.append(case['Date'][:10])
			#y.append(case['Confirmed'])
			#z.append(case['Deaths'])
			#r.append(case['Recovered'])
		#coordinates = dict(lat = data['Lat'],lon = data['Lon'])
		#recovered = data['Recovered']
		#active = data['Active']
		#country_code = data['CountryCode']
		#last_updated = data['Date'][:10]
		
		self.det.setText(str(datar[2]))
		self.con.setText(str(datar[0]))
		self.reco.setText(str(datar[4]))
		#self.cc.setText(str(country_code))
		#self.ac.setText(str(active))
		self.nc.setText(str(datar[1]))
		self.nd.setText(str(datar[3]))
		self.tt.setText(str(datar[9]))
		self.cpm.setText(str(datar[7]))
		self.dpm.setText(str(datar[8]))
		self.tpm.setText(str(datar[10]))

		url = None
		with open('countryurl.txt') as file:
			for line in file:
				if line.startswith(country):
					url = line.strip().split()[-1]
		if url is None:
			print("Invalid Name")
			quit()
		try:
			info = requests.get('https://www.worldometers.info/coronavirus/' + url).text
		except:
			print("BAD Connection")




		lines = info.split('\n')
		for line in lines:
			if line.strip().startswith('categories: ['):
				dates = line.split(',')
				break
		dates[0] = dates[0].strip()[13:]
		del(dates[-1])
		dates[-1] = dates[-1][:8]
		new_dates=[]
		for date in dates:
			new_date = ''
			for c in date:
				if c.isalnum():
					new_date += c
			new_dates.append(new_date)



		flag = 0
		for line in lines:
			if flag == 1:
				if line.strip().startswith("data:"):
					confirmed_y = line.split(',')
					break
			if line.strip().startswith("text: 'Total Coronavirus Cases'"):
				flag = 1
		confirmed_y[0] = confirmed_y[0].strip()[7:]
		del(confirmed_y[-1])

		new_y=[]
		for value in confirmed_y:
			new_value = ''
			for c in value:
				if c.isalnum():
					new_value += c
			new_y.append(new_value)

		confirmed_y = [int(x) for x in new_y]
		print(confirmed_y)

		flag = 0
		for line in lines:
			if flag == 1:
				if line.strip().startswith("data:"):
					death_y = line.split(',')
					break
			if line.strip().startswith("text: 'Total Coronavirus Deaths'"):
				flag = 1
		death_y[0] = death_y[0].strip()[7:]
		del(death_y[-1])

		new_death_y=[]
		for value in death_y:
			new_value = ''
			for c in value:
				if c.isalnum():
					new_value += c
			new_death_y.append(new_value)

		death_y = [int(x) for x in new_death_y]
		self.figure.clear()
		ax = self.figure.add_subplot(111)
		#datam = y
		#data1 = x
		#self.figure.clear()
		#ax = self.figure.add_subplot(111)
		#ax1=self.figure.add_subplot()
	#	ax2=self.figure.add_subplot()
		plt.xlabel("Date")
		plt.ylabel("Number of people")
		for tick in ax.xaxis.get_major_ticks():
			tick.label.set_rotation('vertical')
			tick.label.set_fontsize(5)
		ax.tick_params(axis='x', colors='white')
		ax.tick_params(axis='y', colors='white')
		ax.xaxis.label.set_color('white')
		ax.xaxis.label.set_color('white')
	#	ax1.plot(x,z,'*-',label="Deaths")
		ax.plot(new_dates,death_y,label="Death Toll")
		ax.plot(new_dates,confirmed_y,label="Confirmed Cases")
		ax.set_facecolor(color=(0.101960784,0.101960784,0.109803922,1))
		self.figure.set_facecolor(color=(0.101960784,0.101960784,0.109803922,1))
	#	ax2.plot(x,r,'*-',label="Recovered cases")
	#	ax2.legend()
		ax.legend()
	#	ax1.legend()


		self.canvas.draw()
		QtWidgets.QApplication.restoreOverrideCursor()


			
class info(QtWidgets.QMainWindow):
	backh=QtCore.pyqtSignal()
	def __init__(self):
		super(info,self).__init__()
		uic.loadUi("info1.ui",self)

		self.bh.clicked.connect(self.back)
		self.layout3 =QtWidgets.QVBoxLayout(self.wid5)
		self.web = Web()
		self.layout3.addWidget(self.web)
		self.web.load("https://meenakshi2604.github.io/Covid-tracker/")
		self.count=0
		self.web.show()
		self.n.clicked.connect(self.next)
		self.n_2.clicked.connect(self.back1)
		self.ur=["https://meenakshi2604.github.io/Covid-tracker/","https://www.youtube.com/embed/BtN-goy9VOY","https://www.who.int/","https://github.com/Niranjanprof/Covid-19-Tracker"]
		self.show()
		ur2 = ["WEBSITE","AWARNESS VIDEO","WHO WEBSITE","GITHUB PAGE"]
	def change(self):
		if(self.ind== 0):
			self.l2.setText("WEBSITE")
			self.l3.setText("AWARNESS VIDEO")
			self.l4.setText("WHO WEBSITE")
			self.l1.setText("GITHUB PAGE")
		if(self.ind== 1):
			self.l2.setText("AWARNESS VIDEO")
			self.l3.setText("WHO WEBSITE")
			self.l4.setText("GITHUB PAGE")
			self.l1.setText("WEBSITE")
		if(self.ind == 2):
			self.l2.setText("WHO WEBSITE")
			self.l3.setText("GITHUB PAGE")
			self.l4.setText("WEBSITE")
			self.l1.setText("AWARNESS VIDEO")
		if(self.ind ==3):
			self.l2.setText("GITHUB PAGE")
			self.l3.setText("WEBSITE")
			self.l4.setText("AWARNESS VIDEO")
			self.l1.setText("WHO WEBSITE")
	def back1(self):
		if(self.count == 0):
			self.count = 4
		self.ind = self.count-1	
		self.web.load(self.ur[self.ind])
		self.change()
		self.count -= 1

	def next(self):
		if(self.count == 3):
			self.count = -1
		self.ind = self.count+1
		self.web.load(self.ur[self.ind])
		self.change()
		self.count += 1


	

	def  back(self):
		self.backh.emit()
class c_checker(QtWidgets.QMainWindow):
	def __init__(self):
		super(c_checker,self).__init__()
		uic.loadUi("c_check.ui",self)
		self.show()
		layout = QtWidgets.QVBoxLayout(self.widget_5)
		web = Web()
		layout.addWidget(web)
		web.load("https://evgeny-nadymov.github.io/telegram-react/")
		
class controller():
	def __init__(self):
		pass
	def dash(self):
		self.dwin = dash_board()
		self.dwin.show()
		self.dwin.sig2g.connect(self.show_main_window)
		self.dwin.sig2c.connect(self.toc)
		self.dwin.sig2ck.connect(self.checker)
		self.dwin.sig2i.connect(self.infop)
		self.dwin.setWindowTitle("Welcome To Viscot")


	def show_main_window(self):
		self.win1 = main_window()
		self.win1.setWindowTitle("COVID TRACKER")
		self.win1.show()
		self.dwin.hide()
		self.win1.sigi.connect(self.infop)
		self.win1.sigc.connect(self.mapper)
		self.win1.sigcc.connect(self.checker)
		self.win1.map.connect(self.mapper)
	def toc(self):
		self.c_win=c_window()
		try:
			self.dwin.hide()
		except:
			self.win1.hide()
		self.c_win.setWindowTitle("Country_Wise Results")
		self.c_win.show()
		print

	def mapper(self):
		
		self.c_win.tomp()
	def checker(self):
		self.checkw = c_checker()
		self.checkw.show()
		try:
			self.win1.hide()
		except:
			self.dwin.hide()
		self.checkw.setWindowTitle("Viscot-bot")
	def infop(self):
		self.win2=info()
		self.win2.show()
		self.win2.setWindowTitle("INFO PAGE")
		self.win2.backh.connect(self.backhm)
		try:
			self.win1.hide()
		except:
			self.dwin.hide()
		
	def backhm(self):
		self.win2.close()
		
		self.win1.show()
	def toc(self):
		self.c_win=c_window()
		self.c_win.setWindowTitle("Country_Wise Results")
		self.c_win.show()
		print

app= QtWidgets.QApplication(sys.argv)
ctr = controller()
ctr.dash()
sys.exit(app.exec_())



