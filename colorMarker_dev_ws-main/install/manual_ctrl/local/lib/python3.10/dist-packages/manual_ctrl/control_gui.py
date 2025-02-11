import sys
import subprocess
import signal
from PyQt5 import QtCore, QtGui, QtWidgets
# from path_mapper import TurtleBot3PathDrawer

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1023, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 130, 981, 501))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        # Buttons
        self.Record_map_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Manjari")
        font.setPointSize(24)
        self.Record_map_button.setFont(font)
        self.Record_map_button.setObjectName("Record_map_button")
        self.horizontalLayout_2.addWidget(self.Record_map_button)

        self.Map_choose_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Manjari")
        font.setPointSize(24)
        self.Map_choose_button.setFont(font)
        self.Map_choose_button.setObjectName("Map_choose_button")
        self.horizontalLayout_2.addWidget(self.Map_choose_button)

        self.Autonomous_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Manjari")
        font.setPointSize(24)
        self.Autonomous_button.setFont(font)
        self.Autonomous_button.setObjectName("Autonomous_button")
        self.horizontalLayout_2.addWidget(self.Autonomous_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.stackedWidget = QtWidgets.QStackedWidget(self.verticalLayoutWidget)

        # Stacked Widget with Pages
        self.stackedWidget.setObjectName("stackedWidget")

        # Page-1
        self.Record_Map_page = QtWidgets.QWidget()
        self.Record_Map_page.setObjectName("Record_Map_page")
        self.Record_map_title_label = QtWidgets.QLabel(self.Record_Map_page)
        self.Record_map_title_label.setGeometry(QtCore.QRect(260, 0, 471, 61))
        font = QtGui.QFont()
        font.setFamily("Manjari")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.Record_map_title_label.setFont(font)
        self.Record_map_title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Record_map_title_label.setObjectName("Record_map_title_label")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.Record_Map_page)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(29, 83, 361, 261))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Map_Record_Start_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Manjari")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.Map_Record_Start_button.setFont(font)
        self.Map_Record_Start_button.setObjectName("Map_Record_Start_button")
        self.verticalLayout_2.addWidget(self.Map_Record_Start_button)
        self.Map_recording_stop_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Manjari")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.Map_recording_stop_button.setFont(font)
        self.Map_recording_stop_button.setObjectName("Map_recording_stop_button")
        self.verticalLayout_2.addWidget(self.Map_recording_stop_button)
        self.Map_image_label = QtWidgets.QLabel(self.Record_Map_page)
        self.Map_image_label.setGeometry(QtCore.QRect(620, 70, 271, 271))
        self.Map_image_label.setText("")
        self.Map_image_label.setPixmap(QtGui.QPixmap("manual_ctrl/manual_ctrl/gui/whitw_bg.png"))
        self.Map_image_label.setObjectName("Map_image_label")
        self.stackedWidget.addWidget(self.Record_Map_page)

        # Page-2 
        self.Choose_map_page = QtWidgets.QWidget()
        self.Choose_map_page.setObjectName("Choose_map_page")
        self.Map_selection_title = QtWidgets.QLabel(self.Choose_map_page)
        self.Map_selection_title.setGeometry(QtCore.QRect(260, 0, 471, 61))
        font = QtGui.QFont()
        font.setFamily("Manjari")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.Map_selection_title.setFont(font)
        self.Map_selection_title.setAlignment(QtCore.Qt.AlignCenter)
        self.Map_selection_title.setObjectName("Map_selection_title")
        self.maps_comboBox = QtWidgets.QComboBox(self.Choose_map_page)
        self.maps_comboBox.setGeometry(QtCore.QRect(130, 100, 721, 51))
        self.maps_comboBox.setObjectName("maps_comboBox")
        self.Confirm_map_button = QtWidgets.QPushButton(self.Choose_map_page)
        self.Confirm_map_button.setGeometry(QtCore.QRect(400, 290, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Manjari")
        font.setPointSize(20)
        self.Confirm_map_button.setFont(font)
        self.Confirm_map_button.setObjectName("Confirm_map_button")
        self.stackedWidget.addWidget(self.Choose_map_page)

        # Page-3
        self.Autonomous_page = QtWidgets.QWidget()
        self.Autonomous_page.setObjectName("Autonomous_page")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.Autonomous_page)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(210, 100, 561, 251))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Start_autonoous_button = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Manjari")
        font.setPointSize(26)
        self.Start_autonoous_button.setFont(font)
        self.Start_autonoous_button.setObjectName("Start_autonoous_button")
        self.verticalLayout_3.addWidget(self.Start_autonoous_button)
        self.Stop_autonomous_button = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Manjari")
        font.setPointSize(26)
        self.Stop_autonomous_button.setFont(font)
        self.Stop_autonomous_button.setObjectName("Stop_autonomous_button")
        self.verticalLayout_3.addWidget(self.Stop_autonomous_button)
        self.Map_selection_title_2 = QtWidgets.QLabel(self.Autonomous_page)
        self.Map_selection_title_2.setGeometry(QtCore.QRect(10, 0, 961, 61))
        font = QtGui.QFont()
        font.setFamily("Manjari")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.Map_selection_title_2.setFont(font)
        self.Map_selection_title_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Map_selection_title_2.setObjectName("Map_selection_title_2")
        self.stackedWidget.addWidget(self.Autonomous_page)
        self.verticalLayout.addWidget(self.stackedWidget)

        # Main Page Title
        self.Title_label = QtWidgets.QLabel(self.centralwidget)
        self.Title_label.setGeometry(QtCore.QRect(290, 30, 431, 71))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(48)
        self.Title_label.setFont(font)
        self.Title_label.setObjectName("Title_label")
        MainWindow.setCentralWidget(self.centralwidget)

        # Set Initial Page
        self.stackedWidget.setCurrentIndex(0)  # Set the default page to Record_Map_page

        # Connect buttons to pages
        self.Record_map_button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.Map_choose_button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.Autonomous_button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))

        # Connect buttons to functions
        self.Map_Record_Start_button.clicked.connect(self.start_recording)
        self.Map_recording_stop_button.clicked.connect(self.stop_recording)

        self.running_processes = {}

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Record_map_button.setText(_translate("MainWindow", "Record New Map"))
        self.Map_choose_button.setText(_translate("MainWindow", "Choose The Map"))
        self.Autonomous_button.setText(_translate("MainWindow", "Autonomous Mode"))
        self.Record_map_title_label.setText(_translate("MainWindow", "Record A New Map"))
        self.Map_Record_Start_button.setText(_translate("MainWindow", "Start Recording"))
        self.Map_recording_stop_button.setText(_translate("MainWindow", "Stop Recording"))
        self.Map_selection_title.setText(_translate("MainWindow", "Select the Map"))
        self.Confirm_map_button.setText(_translate("MainWindow", "Confirm"))
        self.Start_autonoous_button.setText(_translate("MainWindow", "Start Action"))
        self.Stop_autonomous_button.setText(_translate("MainWindow", "Stop Action"))
        self.Map_selection_title_2.setText(_translate("MainWindow", "Start Autonomous Grass Cutting"))
        self.Title_label.setText(_translate("MainWindow", "colorMarker"))

    def start_recording(self):
        command = 'ros2 launch bringup path_mapper.launch.xml'
        self.run_command_with_check(command)

    def stop_recording(self):
        # Terminate the running ROS2 process by sending SIGINT
        for command, process in self.running_processes.items():
            process.send_signal(signal.SIGINT)  # Send Ctrl+C to the process
            process.wait()  # Wait for the process to terminate
        self.running_processes.clear()  # Clear the process dictionary

    def run_command_in_terminal(self, command):

        subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', command])

    def run_command_with_check(self, command):
        # Check if the command is already running
        if command in self.running_processes:
            # Terminate the existing process
            self.running_processes[command].terminate()
            self.running_processes[command].wait()
        
        # Run the command
        process = subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.running_processes[command] = process

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
