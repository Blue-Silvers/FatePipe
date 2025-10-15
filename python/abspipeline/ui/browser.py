import sys
import os
import qtpy
from qtpy import QtCore, QtWidgets, QtGui
from abspipeline import conf
from qtpy.uic import loadUi

ui_path = os.path.join(os.path.dirname(__file__), "qt/browser.ui")


from abspipeline.core import finder


class Browser(QtWidgets.QMainWindow):
    # cb = QtWidgets.QApplication.clipboard()  # exemple de clipboard

    def __init__(self):
        super(Browser, self).__init__()
        loadUi(ui_path, self)
        self.setWindowTitle(f"{conf.browser_title} - Browser")
        self.populate()

    def fill_asset_type(self):
        self.asset_type_comboBox.clear()
        pass

    def populate(self):
        # path = os.path.abspath(".../FatePipe/fileExplorer/Task/*")

        entities = finder.find("asset_type")

        # if not os.path.isdir(path):
        #     return

        # for item in os.listdir(path):
        #     item_path = os.path.join(path, item)
        #     if os.path.isdir(item_path):
        #         icon = self.style().standardIcon(QtWidgets.QStyle.SP_DirIcon)
        #     else:
        #         icon = self.style().standardIcon(QtWidgets.QStyle.SP_FileIcon)
        #
        #     list_item = QtWidgets.QListWidgetItem(icon, item)
        #     list_item.setData(QtCore.Qt.UserRole, item_path)
        #     self.lw_asset_type.addItem(list_item)

        for entity in entities:
            self.addListWidgetItem(self.lw_asset_type, entity, entity.data["asset_type"])

            # list_item = QtWidgets.QListWidgetItem()
            # list_item.setText(entity.data["asset_type"])
            #
            # list_item2 = QtWidgets.QListWidgetItem()
            # list_item2.setText(entity.data["asset_name"])
            #
            # #list_item.setData(QtCore.Qt.UserRole, item_path)
            # self.lw_asset_type.addItem(list_item)
            # self.lw_asset_name.addItem(list_item2)

    def addListWidgetItem(self,listWidget, data, label):
        item = QtWidgets.QListWidgetItem()
        item.setData(QtCore.Qt.UserRole, data)
        item.setText(label)
        listWidget.addItem(item)
        return item


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Browser()
    window.show()

    app.exec_()