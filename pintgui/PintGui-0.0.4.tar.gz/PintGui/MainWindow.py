from PySide2.QtWidgets import QApplication
from PySide2.QtQuick import QQuickView
from PySide2.QtCore import QUrl,QObject,Slot
from pathlib import Path

import pint
ureg = pint.UnitRegistry()
Q_ = ureg.Quantity


def run():
  app = QApplication([])
  app.setApplicationName("PintGui")
  view = QQuickView()
  qml_file = Path(__file__).parent/"MainWindow.qml"
  url = QUrl(str(qml_file))

  view.setSource(url)
  view.setResizeMode(QQuickView.SizeRootObjectToView)

  backend = Backend()
  view.rootContext().setContextProperty("backend",backend)

  view.show()

  return app.exec_()

class Backend(QObject):
  def __init__(self):
    super().__init__()

  @Slot(str,str,result=str)
  def convert(self,quantity,unit):
    try:
      if unit.strip().lower() == "base units":
        return str(Q_(quantity).to_base_units())
      else:
        return str(Q_(quantity).to(unit))
    except pint.errors.DimensionalityError as e:
      return "Requested units don't have same dimensions as given quantity."
    except pint.errors.UndefinedUnitError as e:
      return str(e)
    except Exception as e:
      return "Unknown Error (Sorry)"

