import os
from PyQt5 import QtGui, QtCore, QtWidgets
import sys


def print_msg(self, msg):
    if self is not None:
        self.LogAppend.myGUI_signal.emit(msg)
    else:
        print(msg)


@QtCore.pyqtSlot()
def raise_window(new_window, old_window):
    """ raise the current window"""
    new_window.raise_()
    new_window.show()


class Worker(QtCore.QObject):
    '''This worker object will act to ensure that the QThreads are not within the Main Thread'''
    # def __init__(self, main_window, thread):
    def __init__(self, function, *args, **kwargs):
        '''takes in a function, and the arguments and keyword arguments for that function'''
        super(Worker, self).__init__()
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.start.connect(self.run)

    start = QtCore.pyqtSignal(int)

    @QtCore.pyqtSlot()
    def run(self):
        self.function(*self.args, **self.kwargs)


project_name = "QuadrantAnalysis"


def background(self):  # defines the background for each window
    """providing the background info for each window"""
    # Acquiring information about geometry

    project_dir = os.path.dirname(os.path.abspath("__file__"))
    if os.path.basename(project_dir) != project_name:
        project_dir = os.path.dirname(sys.argv[0])

    self.PROJECT_DIR = project_dir

    self.CORE_DIR = os.path.join(self.PROJECT_DIR, 'core')
    self.SETTINGS_DIR = os.path.join(self.PROJECT_DIR, 'settings')
    if not os.path.exists(self.SETTINGS_DIR):
        os.mkdir(self.SETTINGS_DIR)
    self.IMG_DIR = os.path.join(self.PROJECT_DIR, 'img')
    self.setWindowIcon(QtGui.QIcon(os.path.join(self.IMG_DIR, 'GEBA_Logo.png')))  # declaring the icon image
    self.deskW, self.deskH = QtWidgets.QDesktopWidget().availableGeometry().getRect()[2:]  # gets the window resolution
    # self.setWindowState(QtCore.Qt.WindowMaximized) # will maximize the GUI
    self.setGeometry(0, 0, self.deskW/2, self.deskH/1.75)  # Sets the window size

    self.settings_fname = os.path.join(self.SETTINGS_DIR, 'settings.json')

    QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('GTK+'))


def center(self):
    """centers the window on the screen"""
    frameGm = self.frameGeometry()
    screen = QtWidgets.QApplication.desktop().screenNumber(QtWidgets.QApplication.desktop().cursor().pos())
    centerPoint = QtWidgets.QApplication.desktop().screenGeometry(screen).center()
    frameGm.moveCenter(centerPoint)
    self.move(frameGm.topLeft())


class Communicate(QtCore.QObject):
    """A custom pyqtsignal so that errors and popups can be called from the threads
    to the main window"""
    myGUI_signal = QtCore.pyqtSignal(str)
    myGUI_signal_QTreeWidgetItem = QtCore.pyqtSignal(QtWidgets.QTreeWidgetItem)


def find_consec(data):
    '''finds the consecutive numbers and outputs as a list'''
    consecutive_values = []  # a list for the output
    current_consecutive = [data[0]]

    if len(data) == 1:
        return [[data[0]]]

    for index in range(1, len(data)):

        if data[index] == data[index - 1] + 1:
            current_consecutive.append(data[index])

            if index == len(data) - 1:
                consecutive_values.append(current_consecutive)

        else:
            consecutive_values.append(current_consecutive)
            current_consecutive = [data[index]]

            if index == len(data) - 1:
                consecutive_values.append(current_consecutive)
    return consecutive_values
