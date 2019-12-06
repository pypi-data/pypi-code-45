from PyQt5 import QtWidgets, QtCore
from core.GUI_Utils import background, project_name, center
from core.default_parameters import default_rectangle_cols, default_rectangle_rows, default_bin_label_array, \
    default_num_inner, default_num_outer, default_inner_rad, default_rectangle_length, default_rectangle_width, \
    default_circle_radius
from core.plot_utils import CustomViewBox, RectangleItem
from core.QuadrantFunctions import new_atan2
import numpy as np
import pyqtgraph as pg
import os
import json
from functools import partial
pg.setConfigOptions(antialias=True)


class SettingsWindow(QtWidgets.QWidget):  # defines the window class (Settings Window)
    def __init__(self):  # initializes the Settings Window
        super(SettingsWindow, self).__init__()
        background(self)

        self.setWindowTitle("%s - Settings" % project_name)

        self.rectangle_labels = None
        self.circular_labels = None

        # parameter layout
        parameter_tabs = QtWidgets.QTabWidget()

        rectangle_tab = QtWidgets.QWidget()
        self.setRectangleLayout(rectangle_tab)
        circle_tab = QtWidgets.QWidget()
        self.setCircularLayout(circle_tab)

        parameter_tabs.addTab(rectangle_tab, 'Rectangle')
        parameter_tabs.addTab(circle_tab, 'Circle')

        # button layout
        self.hide_btn = QtWidgets.QPushButton("Hide")
        self.hide_btn.clicked.connect(self.hide_callback)

        btn_layout = QtWidgets.QHBoxLayout()
        for btn in [self.hide_btn]:
            btn_layout.addWidget(btn)

        # setting the layout
        layout = QtWidgets.QVBoxLayout()

        layout_order = [parameter_tabs, btn_layout]
        add_stretch = [False, False]
        align_center = [False, False]
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

        self.setSettings()

        self.setLayout(layout)

        center(self)

        self.hide()

    def setRectangleLayout(self, tab):
        """
        set the widgets for the rectangle tab

        :param tab:
        :return:
        """
        # parameter layout

        parameter_layout = QtWidgets.QHBoxLayout()

        num_rows_layout = QtWidgets.QHBoxLayout()
        num_rows_label = QtWidgets.QLabel("Num Rows:")
        self.num_rows = QtWidgets.QLineEdit()
        self.num_rows.setAlignment(QtCore.Qt.AlignHCenter)  # centers the text
        num_rows_layout.addWidget(num_rows_label)
        num_rows_layout.addWidget(self.num_rows)
        self.num_rows.setText(default_rectangle_rows)
        self.num_rows.textChanged.connect(self.rectangularParamsChanged)

        num_cols_layout = QtWidgets.QHBoxLayout()
        num_cols_label = QtWidgets.QLabel("Num Cols:")
        self.num_cols = QtWidgets.QLineEdit()
        self.num_cols.setAlignment(QtCore.Qt.AlignHCenter)  # centers the text
        num_cols_layout.addWidget(num_cols_label)
        num_cols_layout.addWidget(self.num_cols)
        self.num_cols.setText(default_rectangle_cols)
        self.num_cols.textChanged.connect(self.rectangularParamsChanged)

        rect_length_layout = QtWidgets.QHBoxLayout()
        rect_length_label = QtWidgets.QLabel("Arena Length(cm):")
        self.rect_length = QtWidgets.QLineEdit()
        self.rect_length.setAlignment(QtCore.Qt.AlignHCenter)  # centers the text
        rect_length_layout.addWidget(rect_length_label)
        rect_length_layout.addWidget(self.rect_length)
        self.rect_length.setText(default_rectangle_length)

        rect_width_layout = QtWidgets.QHBoxLayout()
        rect_width_label = QtWidgets.QLabel("Arena Width(cm):")
        self.rect_width = QtWidgets.QLineEdit()
        self.rect_width.setAlignment(QtCore.Qt.AlignHCenter)  # centers the text
        rect_width_layout.addWidget(rect_width_label)
        rect_width_layout.addWidget(self.rect_width)
        self.rect_width.setText(default_rectangle_width)

        parameter_layout.addStretch(1)
        for widget in [num_rows_layout, num_cols_layout, rect_length_layout, rect_width_layout]:
            if 'Layout' in widget.__str__():
                parameter_layout.addLayout(widget)
            else:
                parameter_layout.addWidget(widget, 0, QtCore.Qt.AlignCenter)
            parameter_layout.addStretch(1)

        # graph layout
        self.rectangle_win = pg.GraphicsWindow()
        self.rectangle_plot = self.rectangle_win.addPlot(row=0, col=0, viewBox=CustomViewBox(self, self.rectangle_win))
        self.rectangle_plot.hideAxis('left')  # remove the y-axis
        self.rectangle_plot.hideAxis('bottom')  # remove the x axis
        self.rectangle_plot.hideButtons()  # hide the auto-resize button
        self.rectangle_plot.setMouseEnabled(x=False, y=False)  # disables the mouse interactions
        self.rectangle_plot.enableAutoRange(False, False)
        # tab layout

        self.rectangle_plot.vb.mouseClickEvent = partial(mouse_click_event, self, "rect")

        self.rectanglePlot()

        tab_layout = QtWidgets.QVBoxLayout()
        layout_order = [parameter_layout, self.rectangle_win]
        add_stretch = [False, False]
        align_center = [False, False]
        for order, stretch, align_c in zip(layout_order, add_stretch, align_center):
            if 'Layout' in order.__str__():
                tab_layout.addLayout(order)
                if stretch:
                    tab_layout.addStretch(1)
            else:
                if align_c:
                    tab_layout.addWidget(order, 0, QtCore.Qt.AlignCenter)
                else:
                    tab_layout.addWidget(order)

                if stretch:
                    tab_layout.addStretch(1)

        tab.setLayout(tab_layout)

    def rectanglePlot(self):
        """
        This method will plot on the self.rectangle_plot

        :return:
        """

        self.rectangle_plot.clear()

        if self.rectangle_labels is None:
            self.rectangle_labels = {}

        self.rectangle_labels_plot = {}

        try:
            num_cols = int(self.num_cols.text())
            num_rows = int(self.num_rows.text())
        except:
            return

        self.col_edges = np.linspace(0, 1, num=num_cols+1)
        self.row_edges = np.linspace(0, 1, num=num_rows+1)

        for row in self.row_edges:
            self.rectangle_plot.plot([row, row], [0, 1])

        for col in self.col_edges:
            self.rectangle_plot.plot([0, 1], [col, col])

        for row in self.row_edges[:-1]:
            for col in self.col_edges[:-1]:
                col_lab = np.sum([col >= x for x in self.col_edges], 0)
                row_lab = np.sum([row >= y for y in self.row_edges], 0)

                label = 1. * col_lab + row_lab / 100

                if label not in self.rectangle_labels.keys():
                    rectangle_item = RectangleItem([col, row], [1/num_cols, 1/num_rows],
                                                   brush=pg.mkBrush(*self.getColor(2)), pen_color='k')
                    self.rectangle_labels[label] = 2
                else:
                    rectangle_item = RectangleItem([col, row], [1 / num_cols, 1 / num_rows],
                                                   brush=pg.mkBrush(*self.getColor(self.rectangle_labels[label])), pen_color='k')
                self.rectangle_plot.addItem(rectangle_item)
                self.rectangle_labels_plot[label] = rectangle_item

    def rectangularParamsChanged(self):

        # get num_rows
        num_rows = int(self.num_rows.text())
        num_cols = int(self.num_cols.text())

        if num_rows <= 0 or num_cols <= 0:
            self.rectangle_plot.clear()

        key = ('Rectangular', num_rows, num_cols)
        self.rectangle_labels = {}

        if key in default_bin_label_array.keys():
            bin_label_array = default_bin_label_array[key]
            for row_i, row in enumerate(bin_label_array):
                for col_i, value in enumerate(row):
                    label = 1. * (col_i + 1) + (row_i + 1) / 100
                    self.rectangle_labels[label] = value
        else:
            # we will assume only boxes directly touching the edge are the outer
            for row_i in range(num_rows):
                for col_i in range(num_cols):
                    label = 1. * (col_i + 1) + (row_i + 1) / 100
                    if row_i == 0 or col_i == 0 or row_i == num_rows-1 or col_i == num_cols-1:
                        value = 0
                    else:
                        value = 1
                    self.rectangle_labels[label] = value

        self.rectanglePlot()

    def getColor(self, state):
        """
        :param state: 0 = edge, 1 = inner, 2 = discard
        :return:
        """

        if state == 0:
            return (0, 0, 255, 255)
        elif state == 1:
            return (255, 0, 0, 255)
        elif state == 2:
            return (255, 255, 255, 255)

    def setCircularLayout(self, tab):
        parameter_layout = QtWidgets.QHBoxLayout()

        num_inner_layout = QtWidgets.QHBoxLayout()
        num_inner_label = QtWidgets.QLabel("Num Inner Bins:")
        self.num_inner = QtWidgets.QLineEdit()
        self.num_inner.setAlignment(QtCore.Qt.AlignHCenter)  # centers the text
        num_inner_layout.addWidget(num_inner_label)
        num_inner_layout.addWidget(self.num_inner)
        self.num_inner.setText(default_num_inner)
        self.num_inner.textChanged.connect(self.circularParmsChanged)

        num_outer_layout = QtWidgets.QHBoxLayout()
        num_outer_label = QtWidgets.QLabel("Num Outer Bins:")
        self.num_outer = QtWidgets.QLineEdit()
        self.num_outer.setAlignment(QtCore.Qt.AlignHCenter)  # centers the text
        num_outer_layout.addWidget(num_outer_label)
        num_outer_layout.addWidget(self.num_outer)
        self.num_outer.setText(default_num_outer)
        self.num_outer.textChanged.connect(self.circularParmsChanged)

        inner_rad_layout = QtWidgets.QHBoxLayout()
        inner_label = QtWidgets.QLabel("Inner Radius(%):")
        self.inner_rad = QtWidgets.QLineEdit()
        self.inner_rad.setAlignment(QtCore.Qt.AlignHCenter)  # centers the text
        inner_rad_layout.addWidget(inner_label)
        inner_rad_layout.addWidget(self.inner_rad)
        self.inner_rad.setText(default_inner_rad)
        self.inner_rad.textChanged.connect(self.circularParmsChanged)

        circle_radius_layout = QtWidgets.QHBoxLayout()
        circle_radius_label = QtWidgets.QLabel("Arena Radius(cm):")
        self.circle_radius = QtWidgets.QLineEdit()
        self.circle_radius.setAlignment(QtCore.Qt.AlignHCenter)  # centers the text
        circle_radius_layout.addWidget(circle_radius_label)
        circle_radius_layout.addWidget(self.circle_radius)
        self.circle_radius.setText(default_circle_radius)

        parameter_layout.addStretch(1)
        for widget in [num_inner_layout, num_outer_layout, inner_rad_layout, circle_radius_layout]:
            if 'Layout' in widget.__str__():
                parameter_layout.addLayout(widget)
            else:
                parameter_layout.addWidget(widget, 0, QtCore.Qt.AlignCenter)
            parameter_layout.addStretch(1)

        # graph layout
        self.circular_win = pg.GraphicsWindow()
        self.circular_plot = self.circular_win.addPlot(row=0, col=0, viewBox=CustomViewBox(self, self.circular_win))
        self.circular_plot.hideAxis('left')  # remove the y-axis
        self.circular_plot.hideAxis('bottom')  # remove the x axis
        self.circular_plot.hideButtons()  # hide the auto-resize button
        self.circular_plot.setMouseEnabled(x=False, y=False)  # disables the mouse interactions
        self.circular_plot.enableAutoRange(False, False)
        # tab layout

        self.circular_plot.vb.mouseClickEvent = partial(mouse_click_event, self, "circle")

        self.circularPlot()

        tab_layout = QtWidgets.QVBoxLayout()
        layout_order = [parameter_layout, self.circular_win]
        add_stretch = [False, False]
        align_center = [False, False]
        for order, stretch, align_c in zip(layout_order, add_stretch, align_center):
            if 'Layout' in order.__str__():
                tab_layout.addLayout(order)
                if stretch:
                    tab_layout.addStretch(1)
            else:
                if align_c:
                    tab_layout.addWidget(order, 0, QtCore.Qt.AlignCenter)
                else:
                    tab_layout.addWidget(order)

                if stretch:
                    tab_layout.addStretch(1)

        tab.setLayout(tab_layout)

    def circularPlot(self):
        """
        This method will plot on the self.circular_plot

        :return:
        """

        self.circular_plot.clear()

        if self.circular_labels is None:
            self.circular_labels = {}

        self.circular_labels_plot = {}

        rad_limits = np.array([0, float(self.inner_rad.text()), 1])

        geometry = (int(self.num_inner.text()), int(self.num_outer.text()))

        for i in range(len(geometry)):
            rad_lab = i + 1
            angle_limits = np.linspace(0, 2*np.pi, num=geometry[i] + 1)

            rad_start = rad_limits[i]
            rad_stop = rad_limits[i + 1]

            for x in range(len(angle_limits) - 1):
                angle_lab = x + 1
                label = 1. * rad_lab + angle_lab / 100

                start_theta = angle_limits[x]
                stop_theta = angle_limits[x+1]

                theta = np.linspace(start_theta, stop_theta, num=100)
                theta2 = np.linspace(stop_theta, start_theta, num=100)

                if stop_theta - start_theta == 2*np.pi:
                    # circle

                    if rad_start != 0:
                        x_values_out = rad_stop * np.cos(theta)
                        y_values_out = rad_stop * np.sin(theta)
                        plot1 = self.circular_plot.plot(x_values_out, y_values_out)

                        x_values_in = rad_start * np.cos(theta)
                        y_values_in = rad_start * np.sin(theta)
                        plot2 = self.circular_plot.plot(x_values_in, y_values_in)

                    else:
                        # draw a circle
                        half_ind = int(len(theta)/2)

                        x_values_top = rad_stop * np.cos(theta[:half_ind])
                        y_values_top = rad_stop * np.sin(theta[:half_ind])
                        plot1 = self.circular_plot.plot(x_values_top, y_values_top)

                        x_values_bottom = rad_stop * np.cos(theta[half_ind-1:])
                        y_values_bottom = rad_stop * np.sin(theta[half_ind-1:])
                        plot2 = self.circular_plot.plot(x_values_bottom, y_values_bottom)

                else:
                    # circular sector
                    x_values = np.hstack(
                        (rad_stop * np.cos(theta),  # outer radius
                         rad_stop * np.cos(stop_theta),  # connect outer to inner
                         rad_start * np.cos(stop_theta)
                         ))

                    x_values2 = np.hstack(
                        (rad_start * np.cos(theta2),  # inner radius
                         rad_start * np.cos(start_theta),
                         rad_stop * np.cos(start_theta),
                         ))

                    y_values = np.hstack(
                        (rad_stop * np.sin(theta),  # outer radius
                         rad_stop * np.sin(stop_theta),  # connect outer to inner
                         rad_start * np.sin(stop_theta)
                         ))

                    y_values2 = np.hstack(
                        (rad_start * np.sin(theta2),  # inner radius
                         rad_start * np.sin(start_theta),
                         rad_stop * np.sin(start_theta),
                         ))

                    plot1 = self.circular_plot.plot(x_values, y_values)
                    plot2 = self.circular_plot.plot(x_values2, y_values2)

                if label not in self.circular_labels.keys():
                    fill = pg.FillBetweenItem(plot1, plot2, pg.mkBrush(*self.getColor(2)))
                    self.circular_labels[label] = 2
                else:
                    fill = pg.FillBetweenItem(plot1, plot2, pg.mkBrush(*self.getColor(self.circular_labels[label])))

                self.circular_plot.addItem(fill)
                self.circular_labels_plot[label] = [plot1, plot2, fill]

                self.circular_plot.setXRange(-1, 1)
                self.circular_plot.setYRange(-1, 1)

    def circularParmsChanged(self):
        # get num_rows
        try:
            n_inner = int(self.num_inner.text())
            n_outer = int(self.num_outer.text())
            inner_rad = float(self.inner_rad.text())
        except ValueError:
            self.circular_plot.clear()
            return

        if inner_rad >= 1 or inner_rad <= 0:
            self.circular_plot.clear()
            return

        key = ('Circle', n_inner, n_outer)
        self.circular_labels = {}

        if key in default_bin_label_array.keys():
            bin_label_array = default_bin_label_array[key]
            for rad_i, rad in enumerate(bin_label_array):
                for angle_i, value in enumerate(rad):
                    label = 1. * (rad_i + 1) + (angle_i + 1) / 100
                    self.circular_labels[label] = value
        else:
            # if it has a rad_i > 1 assume it's outer
            for angle_i in range(n_outer):
                label = 1. * (1 + 1) + (angle_i + 1) / 100
                self.circular_labels[label] = 0

            # inner
            for angle_i in range(n_inner):
                label = 1. * (1) + (angle_i + 1) / 100
                self.circular_labels[label] = 1

        self.circularPlot()

    def disableParameters(self):
        self.num_rows.setEnabled(0)
        self.num_cols.setEnabled(0)
        self.rect_length.setEnabled(0)
        self.rect_width.setEnabled(0)

        self.num_inner.setEnabled(0)
        self.num_outer.setEnabled(0)
        self.inner_rad.setEnabled(0)
        self.circle_radius.setEnabled(0)

    def enableParameters(self):
        self.num_rows.setEnabled(1)
        self.num_cols.setEnabled(1)
        self.rect_length.setEnabled(1)
        self.rect_width.setEnabled(1)

        self.num_inner.setEnabled(1)
        self.num_outer.setEnabled(1)
        self.inner_rad.setEnabled(1)
        self.circle_radius.setEnabled(1)

    def hide_callback(self):
        self.hide()

    def loadSettings(self):
        if os.path.exists(self.settings_fname):
            with open(self.settings_fname, 'r') as f:
                settings = json.load(f)
        else:
            settings = {
                # rectangle arena
                'num_rows': default_rectangle_cols,
                'num_cols': default_rectangle_cols,
                'rect_length': default_rectangle_length,
                'rect_width': default_rectangle_width,
                # circle arena
                'num_inner': default_num_inner,
                'num_outer': default_num_outer,
                'inner_rad': default_inner_rad,
                'circle_radius': default_circle_radius
            }

        return settings

    def setSettings(self):

        settings = self.loadSettings()
        self.num_rows.setText(str(settings['num_rows']))
        self.num_cols.setText(str(settings['num_cols']))
        if 'rect_length' in settings.keys():
            self.rect_length.setText(str(settings['rect_length']))
        if 'rect_width' in settings.keys():
            self.rect_width.setText(str(settings['rect_width']))

        rect_key = ('Rectangular', int(settings['num_rows']), int(settings['num_cols']))

        if 'rectangle_labels' not in settings.keys():
            if rect_key in default_bin_label_array.keys():
                bin_label_array = default_bin_label_array[rect_key]
                self.rectangle_labels = {}
                for row_i, row in enumerate(bin_label_array):
                    for col_i, value in enumerate(row):
                        label = 1. * (col_i + 1) + (row_i + 1) / 100
                        self.rectangle_labels[label] = value

                self.rectanglePlot()
        else:
            self.rectangle_labels = {}
            for key, value in settings['rectangle_labels'].items():
                self.rectangle_labels[float(key)] = value
            self.rectanglePlot()

        # circle settings
        self.num_inner.setText(str(settings['num_inner']))
        self.num_outer.setText(str(settings['num_outer']))
        self.inner_rad.setText(str(settings['inner_rad']))
        if 'circle_rad' in settings.keys():
            self.circle_radius.setText(str(settings['circle_rad']))

        if 'circular_labels' not in settings.keys():
            circle_key = ('Circle', int(settings['num_inner']), int(settings['num_outer']))
            if circle_key in default_bin_label_array.keys():
                bin_label_array = default_bin_label_array[circle_key]
                self.circular_labels = {}
                for row_i, row in enumerate(bin_label_array):
                    for col_i, value in enumerate(row):
                        label = 1. * (row_i + 1) + (col_i + 1) / 100
                        self.circular_labels[label] = value

                self.circularPlot()
        else:

            self.circular_labels = {}
            for key, value in settings['circular_labels'].items():
                self.circular_labels[float(key)] = value
            self.circularPlot()

    def getSettings(self):
        settings = {}
        # rectangle settings
        settings['num_rows'] = int(self.num_rows.text())
        settings['num_cols'] = int(self.num_cols.text())
        settings['rect_length'] = self.rect_length.text()
        settings['rect_width'] = self.rect_width.text()
        settings['rectangle_labels'] = self.rectangle_labels

        settings['num_inner'] = int(self.num_inner.text())
        settings['num_outer'] = int(self.num_outer.text())
        settings['inner_rad'] = float(self.inner_rad.text())
        settings['circle_rad'] = self.circle_radius.text()
        settings['circular_labels'] = self.circular_labels

        return settings


def mouse_click_event(self, mode, ev=None):
    """
    This function will override the mouse click event.

    :param self: the settings window so we can grab any attributes that we need.
    :param index: the index of the plots, essentially the order of which the plots were created
    :param ev: the event that caused this function to run
    :return: None
    """

    # determine if the user used any modifiers (shift, ctrl, etc).
    # modifiers = QtGui.QApplication.keyboardModifiers()

    if ev.button() == QtCore.Qt.LeftButton:

        # acquire the position where you clicked

        if mode == "rect":
            clickPoint = [self.rectangle_plot.vb.mapToView(ev.pos()).x(),
                          self.rectangle_plot.vb.mapToView(ev.pos()).y()]

            row_lab = np.sum([clickPoint[1] >= col for col in self.row_edges], 0)
            col_lab = np.sum([clickPoint[0] >= row for row in self.col_edges], 0)

            label = 1. * col_lab + row_lab / 100

            if label not in self.rectangle_labels.keys():
                return
            else:
                # remove the item from the plot
                self.rectangle_plot.removeItem(self.rectangle_labels_plot[label])

                label_value = self.rectangle_labels[label]
                label_value += 1

                if label_value > 2:
                    label_value = 0

                rectangle_item = RectangleItem([self.col_edges[col_lab-1], self.row_edges[row_lab-1]],
                                               [1 / (len(self.col_edges)-1), 1 / (len(self.row_edges)-1)],
                                               brush=pg.mkBrush(*self.getColor(label_value)), pen_color='k')

                self.rectangle_plot.addItem(rectangle_item)
                self.rectangle_labels_plot[label] = rectangle_item
                self.rectangle_labels[label] = label_value

        elif mode == 'circle':
            clickPoint = [self.circular_plot.vb.mapToView(ev.pos()).x(),
                          self.circular_plot.vb.mapToView(ev.pos()).y()]

            # 1 = outer radius
            rad_limits = np.array([0, float(self.inner_rad.text()), 1])

            radius = np.sqrt((clickPoint[0])**2 + (clickPoint[1])**2)

            rad_lab = np.sum([radius >= r for r in rad_limits[:-1]], 0)

            geometry = (int(self.num_inner.text()), int(self.num_outer.text()))

            angle_limits = np.linspace(0, 360, num=geometry[int(rad_lab)-1] + 1)

            angle_pos = new_atan2(clickPoint[1], clickPoint[0])

            angle_lab = np.sum([angle_pos >= theta for theta in angle_limits], 0)

            label = 1. * rad_lab + angle_lab / 100

            if label not in self.circular_labels.keys():
                return
            else:
                # remove the item from the plot

                for item in self.circular_labels_plot[label]:
                    self.circular_plot.removeItem(item)

                label_value = self.circular_labels[label]
                label_value += 1

                if label_value > 2:
                    label_value = 0

                self.circular_labels[label] = label_value

                rad_start = rad_limits[int(rad_lab)-1]
                rad_stop = rad_limits[int(rad_lab)]

                start_theta = angle_limits[int(angle_lab)-1]
                stop_theta = angle_limits[int(angle_lab)]

                start_theta *= np.pi/180
                stop_theta *= np.pi/180

                theta = np.linspace(start_theta, stop_theta, num=100)
                theta2 = np.linspace(stop_theta, start_theta, num=100)

                if stop_theta - start_theta == 2 * np.pi:
                    # circle

                    if rad_start != 0:
                        x_values_out = rad_stop * np.cos(theta)
                        y_values_out = rad_stop * np.sin(theta)
                        plot1 = self.circular_plot.plot(x_values_out, y_values_out)

                        x_values_in = rad_start * np.cos(theta)
                        y_values_in = rad_start * np.sin(theta)
                        plot2 = self.circular_plot.plot(x_values_in, y_values_in)

                    else:
                        # draw a circle
                        half_ind = int(len(theta) / 2)

                        x_values_top = rad_stop * np.cos(theta[:half_ind])
                        y_values_top = rad_stop * np.sin(theta[:half_ind])
                        plot1 = self.circular_plot.plot(x_values_top, y_values_top)

                        x_values_bottom = rad_stop * np.cos(theta[half_ind - 1:])
                        y_values_bottom = rad_stop * np.sin(theta[half_ind - 1:])
                        plot2 = self.circular_plot.plot(x_values_bottom, y_values_bottom)

                else:
                    # circular sector
                    x_values = np.hstack(
                        (rad_stop * np.cos(theta),  # outer radius
                         rad_stop * np.cos(stop_theta),  # connect outer to inner
                         rad_start * np.cos(stop_theta)
                         ))

                    x_values2 = np.hstack(
                        (rad_start * np.cos(theta2),  # inner radius
                         rad_start * np.cos(start_theta),
                         rad_stop * np.cos(start_theta),
                         ))

                    y_values = np.hstack(
                        (rad_stop * np.sin(theta),  # outer radius
                         rad_stop * np.sin(stop_theta),  # connect outer to inner
                         rad_start * np.sin(stop_theta)
                         ))

                    y_values2 = np.hstack(
                        (rad_start * np.sin(theta2),  # inner radius
                         rad_start * np.sin(start_theta),
                         rad_stop * np.sin(start_theta),
                         ))

                    plot1 = self.circular_plot.plot(x_values, y_values)
                    plot2 = self.circular_plot.plot(x_values2, y_values2)

                fill = pg.FillBetweenItem(plot1, plot2, pg.mkBrush(*self.getColor(label_value)))
                self.circular_plot.addItem(fill)
                self.circular_labels_plot[label] = [plot1, plot2, fill]

        ev.accept()

    else:
        if mode == "rect":
            pg.ViewBox.mouseClickEvent(self.rectangle_plot.vb, ev)
        elif mode == "circle":
            pg.ViewBox.mouseClickEvent(self.circular_plot.vb, ev)
