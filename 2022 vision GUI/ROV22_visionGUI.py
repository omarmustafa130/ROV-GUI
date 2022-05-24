# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vision_ROV22GUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import subprocess

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(721, 465)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 721, 421))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("../../Downloads/background.png"))
        self.background.setScaledContents(True)
        self.background.setWordWrap(False)
        self.background.setObjectName("background")
        self.front_camera_button = QtWidgets.QPushButton(self.centralwidget)
        self.front_camera_button.setGeometry(QtCore.QRect(525, 111, 61, 16))
        self.front_camera_button.setText("")
        self.front_camera_button.setFlat(True)
        self.front_camera_button.setObjectName("front_camera_button")
        self.front_camera_button.clicked.connect(self.front_camera_stream)
        self.down_camera_button = QtWidgets.QPushButton(self.centralwidget)
        self.down_camera_button.setGeometry(QtCore.QRect(526, 146, 61, 16))
        self.down_camera_button.setText("")
        self.down_camera_button.setFlat(True)
        self.down_camera_button.setObjectName("down_camera_button")
        self.down_camera_button.clicked.connect(self.down_camera_stream)
        self.gripper_camera_button = QtWidgets.QPushButton(self.centralwidget)
        self.gripper_camera_button.setGeometry(QtCore.QRect(527, 182, 61, 16))
        self.gripper_camera_button.setText("")
        self.gripper_camera_button.setFlat(True)
        self.gripper_camera_button.setObjectName("gripper_camera_button")
        self.gripper_camera_button.clicked.connect(self.gripper_camera_stream)
        self.redline_button = QtWidgets.QPushButton(self.centralwidget)
        self.redline_button.setGeometry(QtCore.QRect(88, 262, 111, 31))
        self.redline_button.setText("")
        self.redline_button.setFlat(True)
        self.redline_button.setObjectName("redline_button")
        self.redline_button.clicked.connect(self.redline)
        self.photomosaic_button = QtWidgets.QPushButton(self.centralwidget)
        self.photomosaic_button.setGeometry(QtCore.QRect(204, 262, 111, 31))
        self.photomosaic_button.setText("")
        self.photomosaic_button.setFlat(True)
        self.photomosaic_button.setObjectName("photomosaic_button")
        self.photomosaic_button.clicked.connect(self.photomosaic)
        self.map_button = QtWidgets.QPushButton(self.centralwidget)
        self.map_button.setGeometry(QtCore.QRect(320, 260, 111, 31))
        self.map_button.setText("")
        self.map_button.setFlat(True)
        self.map_button.setObjectName("map_button")
        self.map_button.clicked.connect(self.map)
        self.fishsize_button = QtWidgets.QPushButton(self.centralwidget)
        self.fishsize_button.setGeometry(QtCore.QRect(433, 260, 111, 31))
        self.fishsize_button.setText("")
        self.fishsize_button.setFlat(True)
        self.fishsize_button.setObjectName("fishsize_button")
        self.drift_button = QtWidgets.QPushButton(self.centralwidget)
        self.drift_button.setGeometry(QtCore.QRect(384, 297, 111, 31))
        self.drift_button.setText("")
        self.drift_button.setFlat(True)
        self.drift_button.setObjectName("drift_button")
        self.drift_button.clicked.connect(self.drift)
        self.shipsize_button = QtWidgets.QPushButton(self.centralwidget)
        self.shipsize_button.setGeometry(QtCore.QRect(550, 260, 111, 31))
        self.shipsize_button.setText("")
        self.shipsize_button.setFlat(True)
        self.shipsize_button.setObjectName("shipsize_button")
        self.shipsize_button.clicked.connect(self.shipsize)
        self.ai_button = QtWidgets.QPushButton(self.centralwidget)
        self.ai_button.setGeometry(QtCore.QRect(260, 300, 111, 31))
        self.ai_button.setText("")
        self.ai_button.setFlat(True)
        self.ai_button.setObjectName("ai_button")
        self.all_button = QtWidgets.QPushButton(self.centralwidget)
        self.all_button.setGeometry(QtCore.QRect(465, 206, 71, 21))
        self.all_button.setAutoDefault(False)
        self.all_button.setDefault(True)
        self.all_button.setFlat(False)
        self.all_button.setObjectName("all_button")
        self.all_button.clicked.connect(self.all_stream)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 721, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.all_button.setText(_translate("MainWindow", "ALL"))
        
    def front_camera_stream(self):
        self.command = subprocess.Popen(['cd && cd Desktop && python3 Streaming/frontcam_lap.py'], shell = True)
        self.command = subprocess.Popen(["ssh -t pi@192.168.0.101 'source ros_catkin_ws/devel/setup.bash && cd && python3 Desktop/frontcam_rasp.py' "], shell = True)
        
    def down_camera_stream(self):
        #remove pass and uncomment downcam_lap.py when it works
    	pass
    	#self.command = subprocess.Popen(['cd && cd Desktop && python3 Streaming/downcam_lap.py'], shell = True)
    	
    def gripper_camera_stream(self):
        self.command = subprocess.Popen(['cd && cd Desktop && python3 Streaming/gripcam_lap.py'], shell = True)
        self.command = subprocess.Popen(["ssh -t pi@192.168.0.101 'source ros_catkin_ws/devel/setup.bash && cd && python3 Desktop/gripcam_rasp.py' "], shell = True)
        
        
    def all_stream(self):
        self.command = subprocess.Popen(['cd && cd Desktop && python3 Streaming/frontcam_lap.py'], shell = True)
        self.command = subprocess.Popen(["ssh -t pi@192.168.0.101 'source ros_catkin_ws/devel/setup.bash && cd && python3 Desktop/frontcam_rasp.py' "], shell = True)
        self.command = subprocess.Popen(['cd && cd Desktop && python3 Streaming/gripcam_lap.py'], shell = True)
        self.command = subprocess.Popen(["ssh -t pi@192.168.0.101 'source ros_catkin_ws/devel/setup.bash && cd && python3 Desktop/gripcam_rasp.py' "], shell = True)
        #self.command = subprocess.Popen(['cd && cd Desktop && python3 Streaming/downcam_lap.py'], shell = True) #uncomment when it works
    
    
    def photomosaic(self):
        self.command = subprocess.Popen(['cd && cd Desktop && python3 Streaming/photo_mosaic.py'], shell = True)
	
    def map(self):
        self.command = subprocess.Popen(['cd && cd Desktop && python3 Map2022.py'], shell = True)
        
    def shipsize(self):
        pass
#self.command = subprocess.Popen(['cd && cd Desktop && python3 Map2022.py'], shell = True)     
    def redline(self):
        self.command = subprocess.Popen(['cd && cd Desktop && python3 Abdo_Red_Line0.py'], shell = True)
        self.command = subprocess.Popen(["ssh -t pi@192.168.0.101 'source ros_catkin_ws/devel/setup.bash && cd && python3 Desktop/frontcam_rasp.py' "], shell = True)
    def drift(self):
        self.command = subprocess.Popen(['cd && cd Desktop && python3 drift.py'], shell = True)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_MainWindow()
    w = QtWidgets.QMainWindow()
    ex.setupUi(w)
    w.show()
    
    sys.exit(app.exec_())
