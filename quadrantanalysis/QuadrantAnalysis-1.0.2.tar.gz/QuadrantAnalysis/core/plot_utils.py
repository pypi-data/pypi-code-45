import pyqtgraph as pg
from PyQt5 import QtCore, QtWidgets, QtGui
from exporters import ImageExporter
# import numpy as np


class CustomViewBox(pg.ViewBox):
    """
    Subclass of ViewBox
    """

    def __init__(self, window, item, parent=None):
        """
        Constructor of the CustomViewBox
        """
        super(CustomViewBox, self).__init__(parent)
        # self.plot = plot
        self.window = window
        self.item = item
        self.menu = None  # Override pyqtgraph ViewBoxMenu
        self.menu = self.getMenu()  # Create the menu

    def raiseContextMenu(self, ev):
        """
        Raise the context menu
        """
        if not self.menuEnabled():
            return
        menu = self.getMenu()
        pos = ev.screenPos()
        menu.popup(QtCore.QPoint(pos.x(), pos.y()))

    def getMenu(self):
        """
        Create the menu
        """
        if self.menu is None:
            self.menu = QtWidgets.QMenu()
            self.save_plot = QtWidgets.QAction("Save Figure", self.menu)
            self.save_plot.triggered.connect(self.export)
            self.menu.addAction(self.save_plot)
        return self.menu

    def export(self):
        # choose filename to save as
        save_filename, save_ext = QtWidgets.QFileDialog.getSaveFileName(QtGui.QWidget(), 'Save Scores', '',
                                                                        'PNG (*.png);;JPG (*.jpg);;TIF (*.tif);;GIF (*.gif)')

        if save_filename == '':
            return

        # create an exporter instance, as an argument give it
        # the item you wish to export

        if 'GraphicsWindow' in str(self.item):
            # get the main plot which occurs at row=1, and column=0
            plotitem = self.item.getItem(0, 0)
            # turn off the infinite line marking where the cursor is
            # self.window.mouse_vLine.hide()

            exporter = ImageExporter(plotitem)

            # set export parameters if needed
            # exporter.parameters()['width'] = 100  # (note this also affects height parameter)

            # save to file
            exporter.export(save_filename)

            # self.window.mouse_vLine.show()

        elif 'PltWidget' in str(self.item):
            plotitem = self.item.getPlotItem()

            exporter = ImageExporter(plotitem)

            # set export parameters if needed
            # exporter.parameters()['width'] = 100  # (note this also affects height parameter)

            # save to file
            exporter.export(save_filename)


class RectangleItem(pg.GraphicsObject):
    def __init__(self, topLeft, size, brush=None, *args, **kwargs):
        pg.GraphicsObject.__init__(self)
        self.topLeft = topLeft
        self.size = size

        pen_kwargs = {}
        self.brush = None
        for kwarg in kwargs:
            if 'pen_' in kwarg:
                kwargNew = kwarg.split('pen_')[1]
                pen_kwargs[kwargNew] = kwargs[kwarg]
            elif 'brush' in kwargs:
                brush = kwarg

        self.pen_kwargs = pen_kwargs
        self.brush = brush

        self.generatePicture()

    def generatePicture(self):
        self.picture = QtGui.QPicture()
        p = QtGui.QPainter(self.picture)

        if len(self.pen_kwargs) > 0:
            p.setPen(pg.mkPen(**self.pen_kwargs))
        else:
            p.setPen(pg.mkPen('w'))

        if self.brush:
            p.setBrush(self.brush)

        tl = QtCore.QPointF(self.topLeft[0], self.topLeft[1])
        size = QtCore.QSizeF(self.size[0], self.size[1])
        p.drawRect(QtCore.QRectF(tl, size))
        p.end()

    def paint(self, p, *args):
        p.drawPicture(0, 0, self.picture)

    def boundingRect(self):
        return QtCore.QRectF(self.picture.boundingRect())
