from PyQt5 import QtCore, QtWidgets
import sys, os, time, datetime
from core.QuadrantFunctions import runAnalysis
from core.GUI_Utils import background, Worker, Communicate, center, project_name, raise_window
from core.default_parameters import default_filename, default_arena_shape, default_ppm
from core.addSessions import RepeatAddSessions
from core.settingsWindow import SettingsWindow
import json


class MainWindow(QtWidgets.QWidget):  # defines the window class (main window)

    def __init__(self):  # initializes the main window
        """
        The init method will set some of the background window information (window size, window title, etc)
        """
        super(MainWindow, self).__init__()

        self.settings_window = None
        self.child_data_taken = False
        self.top_level_taken = False
        self.modifying_list = False
        self.current_subdirectory = ''
        self.current_session = ''
        self.analyzing = False

        # initialize attributes/widgets
        self.LogError = None
        self.LogAppend = None
        self.choice = None
        self.Log = None
        self.directory_queue = None
        self.arena = None
        self.directory = None
        self.choose_directory = None
        self.arena_shape = None
        self.run_btn = None
        self.RepeatAddSessionsWorker = None

        self.RemoveSessionData = Communicate()
        self.RemoveSessionData.myGUI_signal.connect(self.takeChildData)

        self.RemoveQueueItem = Communicate()
        self.RemoveQueueItem.myGUI_signal.connect(self.takeTopLevel)

        # initializing the repeat addSessions parameters
        self.current_session = None
        self.directory_changed = None

        self.RepeatAddSessionsThread = QtCore.QThread(self)
        self.reset_add_thread = False
        self.repeat_thread_active = False

        self.analyze_thread = QtCore.QThread()

        background(self)  # acquires some features from the background function we defined earlier

        self.setWindowTitle("%s - Main Window" % project_name)

        self.home()  # runs the home function

    def takeChildData(self, child_count):
        self.child_session = self.directory_item.takeChild(int(child_count)).data(0, 0)
        self.child_data_taken = True

    def takeTopLevel(self, item_count):
        item_count = int(item_count)
        self.directory_queue.takeTopLevelItem(item_count)
        self.top_level_taken = True

    def home(self):  # defines the home function (the main window)
        """
        Method that populates the QWidget with all the Widgets/layouts
        """

        self.LogError = Communicate()
        self.LogError.myGUI_signal.connect(self.raiseError)

        self.LogAppend = Communicate()
        self.LogAppend.myGUI_signal.connect(self.AppendLog)

        # ---------- directory layout --------------------------------
        directory_layout = QtWidgets.QHBoxLayout()

        directory_label = QtWidgets.QLabel("Current Set Directory:")

        self.directory = QtWidgets.QLineEdit()
        self.directory.setText(default_filename)
        self.directory.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.directory.textChanged.connect(self.changeDirectory)

        directory_with_label = QtWidgets.QHBoxLayout()
        directory_with_label.addWidget(directory_label)
        directory_with_label.addWidget(self.directory)

        self.choose_directory = QtWidgets.QPushButton("Choose Directory")
        self.choose_directory.clicked.connect(self.ChooseDir)

        directory_layout.addWidget(self.choose_directory)
        directory_layout.addLayout(directory_with_label)

        # ---------- queue widget

        self.directory_queue = QtWidgets.QTreeWidget()
        self.directory_queue.headerItem().setText(0, "Axona Sessions:")
        self.directory_queue.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        directory_queue_label = QtWidgets.QLabel('Queue: ')

        queue_layout = QtWidgets.QVBoxLayout()
        queue_layout.addWidget(directory_queue_label)
        queue_layout.addWidget(self.directory_queue)

        # --------parameter layout-----------
        '''
        self.arena = QtWidgets.QComboBox()
        arena_options = ['BehaviorRoom', 'DarkRoom', 'Room4']

        for arena in arena_options:
            self.arena.addItem(arena)

        arena_label = QtWidgets.QLabel("Arena:")
        arena_layout = QtWidgets.QHBoxLayout()
        arena_layout.addWidget(arena_label)
        arena_layout.addWidget(self.arena)
        '''
        ppm_layout = QtWidgets.QHBoxLayout()
        self.ppm = QtWidgets.QLineEdit()
        self.ppm.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.ppm.setText(default_ppm)
        ppm_label = QtWidgets.QLabel("Pixels Per Meter:")
        ppm_layout.addWidget(ppm_label)
        ppm_layout.addWidget(self.ppm)

        self.arena_shape = QtWidgets.QComboBox()
        arena_shape_options = ['Auto', 'Circle', 'Rectangular']

        for shape in arena_shape_options:
            self.arena_shape.addItem(shape)

        self.arena_shape.setCurrentIndex(self.arena_shape.findText(default_arena_shape))

        arena_shape_label = QtWidgets.QLabel("Arena Shape:")
        arena_shape_layout = QtWidgets.QHBoxLayout()
        arena_shape_layout.addWidget(arena_shape_label)
        arena_shape_layout.addWidget(self.arena_shape)

        parameter_layout = QtWidgets.QHBoxLayout()

        parameter_layout.addStretch(1)
        for widget in [ppm_layout, arena_shape_layout]:
            parameter_layout.addLayout(widget)
            parameter_layout.addStretch(1)

        # ------- log widget -------------------
        self.Log = QtWidgets.QTextEdit()
        log_label = QtWidgets.QLabel('Log:')

        log_lay = QtWidgets.QVBoxLayout()
        log_lay.addWidget(log_label, 0, QtCore.Qt.AlignTop)
        log_lay.addWidget(self.Log)

        # ------ buttons -----------------------------
        self.run_btn = QtWidgets.QPushButton("Run", self)
        self.run_btn.setToolTip("Click to run the analysis (or press Ctrl+R)!")
        self.run_btn.setShortcut("Ctrl+R")
        self.run_btn.clicked.connect(self.analyze)  # connect the run button with the analyze() function

        self.settings_btn = QtWidgets.QPushButton("Settings")

        quit_btn = QtWidgets.QPushButton("Quit", self)
        quit_btn.clicked.connect(self.close_app)
        quit_btn.setShortcut("Ctrl+Q")
        quit_btn.setToolTip('Click to quit (or press Ctrl+Q)')

        btn_layout = QtWidgets.QHBoxLayout()

        button_order = [self.run_btn, self.settings_btn, quit_btn]
        for button in button_order:
            btn_layout.addWidget(button)

        # ---------------- Version information ----------------------------------
        vers_label = QtWidgets.QLabel(project_name + " V1.0.3")

        # ------------- layout ------------------------------

        layout = QtWidgets.QVBoxLayout()

        layout_order = [directory_layout, parameter_layout, queue_layout, log_lay, btn_layout, vers_label]
        add_stretch = [False, False, False, False, False, False]
        align_center = [False, False, False, False, False, False]
        for order, stretch, align_c in zip(layout_order, add_stretch, align_center):
            if 'Layout' in order.__str__():
                layout.addLayout(order)
                if stretch:
                    layout.addStretch(1)
            else:
                if align_c:
                    layout.addWidget(order, 0, QtCore.Qt.AlignCenter)
                else:
                    layout.addWidget(order)

                if stretch:
                    layout.addStretch(1)

        self.setLayout(layout)

        self.setParameters()

        center(self)

        self.RepeatAddSessionsThread.start()
        self.RepeatAddSessionsWorker = Worker(RepeatAddSessions, self)
        self.RepeatAddSessionsWorker.moveToThread(self.RepeatAddSessionsThread)
        self.RepeatAddSessionsWorker.start.emit("start")

        self.show()

    def loadSettings(self):
        if os.path.exists(self.settings_fname):
            with open(self.settings_fname, 'r') as f:
                settings = json.load(f)
        else:
            settings = {'directory': default_filename,
                        'ppm': default_ppm,
                        'arena_shape': default_arena_shape
                        }

        return settings

    def setParameters(self):
        settings = self.loadSettings()

        self.directory.setText(settings['directory'])
        self.arena_shape.setCurrentIndex(self.arena_shape.findText(settings['arena_shape']))
        self.ppm.setText(settings['ppm'])

    def getSettings(self):
        settings = {}
        settings['directory'] = self.directory.text()
        settings['ppm'] = self.ppm.text()
        settings['arena_shape'] = self.arena_shape.currentText()
        return settings

    def raiseError(self, error_val):
        """raises an error window given certain errors from an emitted signal"""
        if 'ChooseDir' in error_val:
            self.choice = QtWidgets.QMessageBox.question(self, "Error: Choose Directory!",
                                                      "You have not chosen a directory yet to analyze!\n" +
                                                      "Please make sure to choose a directory before pressing 'Run'!\n",
                                                         QtWidgets.QMessageBox.Ok)

        elif 'DirExistsError' in error_val:
            self.choice = QtWidgets.QMessageBox.question(self, "Error: Directory Doesn't Exist!",
                                                     "You have a directory that doesn't exist!\n" +
                                                     "Please make sure to choose an existing directory before pressing 'Run'!\n",
                                                     QtWidgets.QMessageBox.Ok)

    def AppendLog(self, message):
        """
        A function that will append the Log field of the main window (mainly
        used as a slot for a custom pyqt signal)
        """
        if '#' in message:
            message = message.split('#')
            color = message[-1].lower()
            message = message[0]
            message = '<span style="color:%s">%s</span>' % (color, message)

        self.Log.append(message)

    def analyze(self):

        current_directory = self.directory.text()
        if 'Choose a Set' in current_directory:
            self.choice = None
            self.LogAppend.myGUI_signal.emit(
                '[%s %s]: Error: Choose a directory!#Red' % (str(datetime.datetime.now().date()),
                                                             str(datetime.datetime.now().time())[:8]))

            self.LogError.myGUI_signal.emit('ChooseDir')
            while self.choice is None:
                time.sleep(0.1)
            return

        if not os.path.exists(current_directory):
            self.choice = None
            self.LogAppend.myGUI_signal.emit(
                '[%s %s]: Error: Directory doesn\'t exist!#Red' % (str(datetime.datetime.now().date()),
                                                                   str(datetime.datetime.now().time())[:8]))
            self.LogError.myGUI_signal.emit('DirExistError')
            while self.choice is None:
                time.sleep(0.1)
            return

        self.disableParameters()

        self.run_btn.setText('Stop')
        self.run_btn.setToolTip('Click to stop analysis.')  # defining the tool tip for the start button
        self.run_btn.clicked.disconnect()
        self.run_btn.clicked.connect(self.stop_analysis)

        self.analyzing = True
        self.analyze_thread.start()
        self.analyze_thread_worker = Worker(Analyze, self)
        self.analyze_thread_worker.moveToThread(self.analyze_thread)
        self.analyze_thread_worker.start.emit(1)

    def stop_analysis(self):

        self.enableParameters()

        self.analyzing = False
        self.run_btn.setText('Run')
        self.analyze_thread.terminate()

        self.LogAppend.myGUI_signal.emit(
            '[%s %s]: Terminated analysis!' % (str(datetime.datetime.now().date()),
                                                     str(datetime.datetime.now().time())[:8]))

        self.run_btn.setToolTip('Click to start analysis.')  # defining the tool tip for the start button
        self.run_btn.clicked.disconnect()
        self.run_btn.clicked.connect(self.analyze)

    def close_app(self):
        """Function that will close the app if the close button is pressed"""
        # pop up window that asks if you really want to exit the app ------------------------------------------------

        choice = QtWidgets.QMessageBox.question(self, "Quitting ",
                                                "Do you really want to exit?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if choice == QtWidgets.QMessageBox.Yes:
            sys.exit()  # tells the app to quit
        else:
            pass

    def ChooseDir(self):
        """
        This method will be run when the choose directory button is pressed.

        :return:
        """

        settings = self.getSettings()
        if 'directory' not in settings.keys():
            current_directory = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory"))

        else:
            if os.path.exists(settings['directory']):
                current_directory = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory",
                                                                                   settings['directory']))
            else:
                current_directory = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory"))

        if current_directory != '':
            self.directory.setText(current_directory)

    def disableParameters(self):
        self.choose_directory.setEnabled(0)
        self.directory.setEnabled(0)
        self.ppm.setEnabled(0)
        self.arena_shape.setEnabled(0)

        self.settings_window.disableParameters()
        pass

    def enableParameters(self):
        self.choose_directory.setEnabled(1)
        self.directory.setEnabled(1)
        self.ppm.setEnabled(1)
        self.arena_shape.setEnabled(1)

        self.settings_window.enableParameters()

    def changeDirectory(self):
        """

        :return:
        """
        self.directory_changed = True
        self.change_directory_time = time.time()


def getSetFileChildNumber(self, set_file):
    """
    This function will find the position within the Queue that the Session is located in.
    :param self:
    :param set_file:
    :return:
    """

    for i in range(self.directory_item.childCount()):
        session_item = self.directory_item.child(i)
        current_setfile = os.path.realpath(os.path.join(self.directory.text(), session_item.data(0, 0)))
        if os.path.realpath(set_file) == os.path.realpath(current_setfile):
            return i

    return None


def Analyze(self):

    # validate analysis
    if self.directory_queue.topLevelItemCount() == 0:
        pass

    settings = self.getSettings()
    sw_settings = self.settings_window.getSettings()
    settings = {**settings, **sw_settings}
    with open(self.settings_fname, 'w') as f:
        json.dump(settings, f)

    directory = settings['directory']

    # puts a QuadrantAnalysis directory in the directory
    save_directory = os.path.join(directory, 'QuadrantAnalysis')

    # adds a figures directory to that QuadrantAnalysis directory to save the figures
    save_figures_directory = os.path.join(save_directory, 'Figures')

    # make the figure if it doesn't exist already
    if not os.path.exists(save_figures_directory):
        os.makedirs(save_figures_directory)

    while self.analyzing:

        self.directory_item = self.directory_queue.topLevelItem(0)

        if self.directory_item is None:
            # then there are no topLevelItems
            time.sleep(0.1)
            continue

        while self.directory_item.childCount() != 0:

            session = self.directory_item.child(0).data(0, 0)

            session_path = os.path.join(directory, session)  # name of the directory that the set file exists in

            runAnalysis(session_path, save_directory, ppm=float(self.ppm.text()), center=None, self=self)

            childNum = getSetFileChildNumber(self, session_path)

            # removes session from list
            self.child_data_taken = False
            self.modifying_list = True
            self.RemoveSessionData.myGUI_signal.emit(str(childNum))
            while not self.child_data_taken:
                time.sleep(0.1)
            self.modifying_list = False

        if self.directory_item.childCount() == 0:
            # deletes sub-directory if there are no sessions left
            self.top_level_taken = False
            self.modifying_list = True
            self.RemoveQueueItem.myGUI_signal.emit(str(0))
            while not self.top_level_taken:
                time.sleep(0.1)
            self.modifying_list = False

            self.current_subdirectory = ''
            self.current_session = ''

        time.sleep(0.1)


def launch_gui():
    app = QtWidgets.QApplication(sys.argv)

    # the main window
    window = MainWindow()

    # the settings window
    settings = SettingsWindow()

    window.settings_btn.clicked.connect(lambda: raise_window(settings, window))

    window.settings_window = settings

    sys.exit(app.exec_())  # prevents the window from immediately exiting out


if __name__ == '__main__':
    launch_gui()  # the command that calls run()
