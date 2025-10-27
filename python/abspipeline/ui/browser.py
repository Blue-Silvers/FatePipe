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

        self.pb_asset.clicked.connect(self.on_asset_clicked)
        self.pb_shot.clicked.connect(self.on_shot_clicked)

        self.populate()

    def fill_asset_type(self):
        self.asset_type_comboBox.clear()
        pass

    def populate(self):

        self.lw_asset_type.itemClicked.connect(self.on_asset_type_clicked) #connect label to function
        self.lw_asset_name.itemClicked.connect(self.on_asset_name_clicked)
        self.lw_asset_task.itemClicked.connect(self.on_asset_task_clicked)
        self.lw_asset_item.itemClicked.connect(self.on_asset_version_clicked)
        self.pb_asset.setStyleSheet(
            "background-color: #071e26;"
        )

        entities = finder.find("asset_type")

        for entity in entities:
            self.addListWidgetItem(self.lw_asset_type, entity, entity.data["asset_type"])


    def addListWidgetItem(self,listWidget, data, label):
        item = QtWidgets.QListWidgetItem()
        item.setData(QtCore.Qt.UserRole, data)
        item.setText(label)
        listWidget.addItem(item)
        return item

    def on_asset_clicked(self):

        self.pb_asset.setStyleSheet(
            "background-color: #071e26;"
        )
        self.pb_shot.setStyleSheet(
            "background-color: #7D9191;"
        )

        self.lw_asset_type.clear()
        self.lw_asset_name.clear()
        self.lw_asset_task.clear()
        self.lw_asset_version.clear()
        self.lw_asset_item.clear()

        self.lw_asset_type.itemClicked.connect(self.on_asset_type_clicked) #connect label to function
        self.lw_asset_name.itemClicked.connect(self.on_asset_name_clicked)
        self.lw_asset_task.itemClicked.connect(self.on_asset_task_clicked)
        self.lw_asset_item.itemClicked.connect(self.on_asset_version_clicked)

        entities = finder.find("asset_type")

        for entity in entities:
            self.addListWidgetItem(self.lw_asset_type, entity, entity.data["asset_type"])

    def on_shot_clicked(self):

        self.pb_shot.setStyleSheet(
            "background-color: #071e26;"
        )
        self.pb_asset.setStyleSheet(
            "background-color: #7D9191;"
        )

        self.lw_asset_type.clear()
        self.lw_asset_name.clear()
        self.lw_asset_task.clear()
        self.lw_asset_version.clear()
        self.lw_asset_item.clear()

        self.lw_asset_type.itemClicked.connect(self.on_shot_type_clicked) #connect label to function
        self.lw_asset_name.itemClicked.connect(self.on_shot_name_clicked)
        self.lw_asset_task.itemClicked.connect(self.on_shot_task_clicked)
        self.lw_asset_item.itemClicked.connect(self.on_shot_version_clicked)

        entities = finder.find("shot_type")

        for entity in entities:
            self.addListWidgetItem(self.lw_asset_type, entity, entity.data["shot_type"])

#Asset clicked
    def on_asset_type_clicked(self, item):
        label = item.text()

        self.lw_asset_name.clear()
        self.lw_asset_task.clear()
        self.lw_asset_version.clear()
        self.lw_asset_item.clear()

        entities = finder.find("asset_name", {"asset_type": label})

        for entity in entities:
            self.addListWidgetItem(self.lw_asset_name, entity, entity.data["asset_name"])

    def on_asset_name_clicked(self, item):
        itemData = item.data(QtCore.Qt.UserRole)

        self.lw_asset_task.clear()
        self.lw_asset_version.clear()
        self.lw_asset_item.clear()

        entities = finder.find("asset_task", itemData.data)

        for entity in entities:
            self.addListWidgetItem(self.lw_asset_task, entity, entity.data["asset_task"])

    def on_asset_task_clicked(self, item):
        itemData = item.data(QtCore.Qt.UserRole)

        self.lw_asset_version.clear()
        self.lw_asset_item.clear()

        entities = finder.find("asset_version", itemData.data)

        for entity in entities:
            self.addListWidgetItem(self.lw_asset_version, entity, entity.data["asset_version"])

    def on_asset_version_clicked(self, item):
        itemData = item.data(QtCore.Qt.UserRole)

        self.lw_asset_item.clear()

        entities = finder.find("asset_version", itemData.data)

        for entity in entities:
            self.addListWidgetItem(self.lw_asset_item, entity, entity.data["asset_version"])

#Shot clicked
    def on_shot_type_clicked(self, item):
        label = item.text()

        self.lw_asset_name.clear()
        self.lw_asset_task.clear()
        self.lw_asset_version.clear()
        self.lw_asset_item.clear()

        entities = finder.find("shot_name", {"shot_type": label})

        for entity in entities:
            self.addListWidgetItem(self.lw_asset_name, entity, entity.data["shot_name"])

    def on_shot_name_clicked(self, item):
        itemData = item.data(QtCore.Qt.UserRole)

        self.lw_asset_task.clear()
        self.lw_asset_version.clear()
        self.lw_asset_item.clear()

        entities = finder.find("shot_task", itemData.data)

        for entity in entities:
            self.addListWidgetItem(self.lw_asset_task, entity, entity.data["shot_task"])

    def on_shot_task_clicked(self, item):
        itemData = item.data(QtCore.Qt.UserRole)

        self.lw_asset_version.clear()
        self.lw_asset_item.clear()

        entities = finder.find("shot_version", itemData.data)

        for entity in entities:
            self.addListWidgetItem(self.lw_asset_version, entity, entity.data["shot_version"])

    def on_shot_version_clicked(self, item):
        itemData = item.data(QtCore.Qt.UserRole)

        self.lw_asset_item.clear()

        entities = finder.find("shot_version", itemData.data)

        for entity in entities:
            self.addListWidgetItem(self.lw_asset_item, entity, entity.data["shot_version"])


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Browser()
    window.show()

    app.exec_()