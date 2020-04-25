import sys
import serial
import serial
from PyQt5 import uic,QtWidgets,QtCore
import pyautogui
import time
from pynput import keyboard
from pynput import mouse
from pynput.keyboard import Key, Listener
pyautogui.FAILSAFE = False
def on_functionf8(key):                                                                  #function that handles keystrokes
    handle = open("log.klep" , 'a')
    handle.write("press: " + str(key) + '\n')

    handle.close()
def on_scroll(x, y, dx, dy):                                                            #function to monitor scroll events and store it
    handle = open('log.klep', 'a')
    handle.write("scroll: " + str(dx) + ' ' + str(dy) + '\n')
    time.sleep(0.009)
    handle.close()


def on_click(x, y, button, pressed):                                                   #function to handle mouse click event and store it

    if (pressed):
        handle = open("log.klep", "a")
        handle.write("click: " + str(x) + ' ' + str(y) + '\n')
        handle.close()



#Main window class
class main(QtWidgets.QMainWindow):                                                      #MainWindow class
    sig = QtCore.pyqtSignal()
    inf = QtCore.pyqtSignal()
    tm = QtCore.pyqtSignal()
    re = QtCore.pyqtSignal()
    strt = QtCore.pyqtSignal()    
    def __init__(self):
        super(main,self).__init__()
        uic.loadUi('/home/klepsydra/Python_projects/Rapper/src/main/python/pillow.ui',self)
        self.btn.clicked.connect(self.change)
        self.info.clicked.connect(self.to_info)
        self.btn_3.clicked.connect(self.to_rep)
        self.btn_4.clicked.connect(self.to_strt)

        self.show()
#repeter function
    def to_rep(self):
        self.re.emit()
    def to_strt(self):
        self.strt.emit()
#info function
    def to_info(self):
        self.inf.emit()
#arduino function
    def change(self):
        self.sig.emit()
#repeter class
class rep(QtWidgets.QMainWindow):
    bck_r = QtCore.pyqtSignal()
    def __init__(self):
        super(rep,self).__init__()
        uic.loadUi('/home/klepsydra/Python_projects/Rapper/src/main/python/rep.ui',self)
        self.rec1.clicked.connect(self.repeter_f) 
        self.rp.clicked.connect(self.bck_rf)



    def repeter_f(self):                                                    #Recorder class
   
        f = open("log.klep",'+w')
        f.close()
        key_listener = keyboard.Listener(on_release=on_functionf8)
        key_listener.start()
        listener = mouse.Listener(on_click=on_click, on_scroll=on_scroll)
        listener.start()
        listener.join()

 
        
    def bck_rf(self):
        self.bck_r.emit()

#arduino class
class second(QtWidgets.QMainWindow):
    bk = QtCore.pyqtSignal()
    def __init__(self):
        super(second,self).__init__()
        uic.loadUi('/home/klepsydra/Python_projects/Rapper/src/main/python/sec.ui',self)
        self.ardb.clicked.connect(self.to_main)
        self.run.clicked.connect(self.arduino_code)
        self.show()
    def arduino_code(self):
     pass

    def to_main(self):
        self.bk.emit()
#help class
class hel(QtWidgets.QMainWindow):
    def __init__(self):
        super(hel,self).__init__()
        uic.loadUi('/home/klepsydra/Python_projects/Rapper/src/main/python/help.ui',self)
        self.show()

class start(QtWidgets.QMainWindow):
    bck4 = QtCore.pyqtSignal()
    def __init__(self):
        super(start,self).__init__()
        uic.loadUi('/home/klepsydra/Python_projects/Rapper/src/main/python/start.ui',self)
        self.rp2_2.clicked.connect(self.back4)
        self.rep_s.clicked.connect(self.l_start)
        self.show()
    def back4 (self):
        self.bck4.emit()
    def l_start(self):
        handle = open("log.klep","r")
        it = self.it.text()
        it = int(it)
        k1=0
        while(k1<it):
            for line in handle:
                key_1=""
                if(line.startswith('press:')):
                    key = line.strip().split()
                    for k_ in key[-1]:
                        if(k_ != '\''):
                            key_1 = key_1+k_
    
                    pyautogui.press(key_1)
                    time.sleep(0.5)
                    print(key_1)
                    
                if (line.startswith('click:')):
                    click = line.strip().split()
                    pyautogui.click(int(click[-2]),int(click[-1]))
                    print(int(click[-2]), int(click[-1]))
                    time.sleep(0.5)
                if (line.startswith('scroll:')):
                    scroll = line.strip().split()
                    pyautogui.click(int(click[-2]),int(click[-1]))
                    print(int(scroll[-2]), int(scroll[-1]))
                    time.sleep(0.05)
            k1 = k1+1
            print("k1",k1)
            handle = open("log.klep","r")

            
        print(k1,it)
        handle.close()
        if(it == k1):
            sys.exit()

#info class        
class info(QtWidgets.QMainWindow):
    inr = QtCore.pyqtSignal()
    her = QtCore.pyqtSignal()
    def __init__(self):
        super(info,self).__init__()
        uic.loadUi('/home/klepsydra/Python_projects/Rapper/src/main/python/info.ui',self)
        self.inb.clicked.connect(self.on)
        self.help.clicked.connect(self.hell)
        self.show()
    def hell(self):
        self.her.emit()
    def on(self):
        self.inr.emit()
     
class ctr:
    def __init__(self):
        pass
    def show_main(self):
        self.window = main()
        self.window.show()
        self.window.sig.connect(self.next)
        self.window.strt.connect(self.s_start)

        self.window.inf.connect(self.infop)
        self.window.re.connect(self.show_rep)
        self.window.setWindowTitle("MAPPER")
    def s_start(self):
        self.start_1=start()
        self.start_1.bck4.connect(self.back5)
        self.start_1.show()
        self.window.hide()

    def back5(self):
        self.start_1.close()
        self.window.show()
    def show_rep(self):
        self.repp = rep()

        self.repp.show()
        self.window.hide()
        self.repp.bck_r.connect(self.bck_r)
        self.repp.setWindowTitle("REPEATER")
    def bck_r(self):
        self.window.show()
        self.repp.close()

    def back(self,x):
            self.window.show()
            self.win2.hide()
    def back3(self):
        self.inp.close()
        self.window.show()
        
    def back2(self):
        self.window.show()
        self.win2.hide()
    def infop(self):
        self.inp = info()
        self.inp.show()
        self.window.hide()
        x=5
        self.inp.her.connect(self.help1)
    
        self.inp.inr.connect(self.back3)
        self.inp.setWindowTitle("INFO")
    def help1(self):
        self.hel2 = hel()
        self.hel2.show()
        self.help1.setWindowTitle("HELP")
        
    def next(self):
        self.win2 = second()
        self.win2.show()
        self.win2.bk.connect(self.back2)
        self.window.hide()
        self.win2.setWindowTitle("ARD MAPPER")
def ma():
    app = QtWidgets.QApplication(sys.argv)
    ctrl = ctr()
    ctrl.show_main()
    sys.exit(app.exec_() )
if(__name__ == '__main__'):
    ma()
