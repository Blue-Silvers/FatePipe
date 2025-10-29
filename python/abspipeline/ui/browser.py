import sys
import os
import qtpy
from qtpy import QtCore, QtWidgets, QtGui
from abspipeline import conf
from qtpy.uic import loadUi

ui_path = os.path.join(os.path.dirname(__file__), "qt/browser.ui")

from abspipeline.ui import interact as handler

from abspipeline.core import finder

class Browser(QtWidgets.QMainWindow):
    # cb = QtWidgets.QApplication.clipboard()  # exemple de clipboard

    def __init__(self):
        super(Browser, self).__init__()
        loadUi(ui_path, self)
        self.setWindowTitle(f"{conf.browser_title} - Browser")

        self.pb_asset.clicked.connect(self.on_asset_clicked)
        self.pb_shot.clicked.connect(self.on_shot_clicked)

        self.pb_open.clicked.connect(self.open_selected_asset)
        self.pb_delete.clicked.connect(self.delete_selected_asset)
        self.deactivate_item_button()

        self.populate()

    def fill_asset_type(self):
        self.asset_type_comboBox.clear()
        pass

    def populate(self):

        self.lw_asset_type.itemClicked.connect(self.on_asset_type_clicked) #connect label to function
        self.lw_asset_name.itemClicked.connect(self.on_asset_name_clicked)
        self.lw_asset_task.itemClicked.connect(self.on_asset_task_clicked)
        self.lw_asset_version.itemClicked.connect(self.on_asset_version_clicked)
        self.lw_asset_item.itemClicked.connect(self.on_asset_item_selected)
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

#Button
    def activate_item_button(self):

        self.pb_open.setEnabled(True)
        self.pb_delete.setEnabled(True)
        self.pb_open.setStyleSheet(
            "background-color: #7D9191;"
        )
        self.pb_delete.setStyleSheet(
            "background-color: #7D9191;"
        )


        if hasattr(self, "action_ui") and self.action_ui is not None:
            self.action_ui.action_box.setVisible(False)

    def deactivate_item_button(self):
        self.pb_open.setEnabled(False)
        self.pb_delete.setEnabled(False)
        self.pb_open.setStyleSheet(
            "background-color: #071e26;"
        )
        self.pb_delete.setStyleSheet(
            "background-color: #071e26;"
        )

        if hasattr(self, "action_ui") and self.action_ui is not None:
            self.action_ui.action_box.setVisible(False)

    def on_asset_clicked(self):
        self.deactivate_item_button()

        self.pb_asset.setEnabled(False)
        self.pb_shot.setEnabled(True)
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
        self.lw_asset_version.itemClicked.connect(self.on_asset_version_clicked)
        self.lw_asset_item.itemClicked.connect(self.on_asset_item_selected)

        entities = finder.find("asset_type")

        for entity in entities:
            self.addListWidgetItem(self.lw_asset_type, entity, entity.data["asset_type"])

    def on_shot_clicked(self):
        self.pb_asset.setEnabled(True)
        self.pb_shot.setEnabled(False)
        self.deactivate_item_button()

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
        self.lw_asset_version.itemClicked.connect(self.on_shot_version_clicked)
        self.lw_asset_item.itemClicked.connect(self.on_shot_item_selected)

        entities = finder.find("shot_type")

        for entity in entities:
            self.addListWidgetItem(self.lw_asset_type, entity, entity.data["shot_type"])

#Asset clicked
    def on_asset_type_clicked(self, item):
        self.deactivate_item_button()

        label = item.text()

        self.lw_asset_name.clear()
        self.lw_asset_task.clear()
        self.lw_asset_version.clear()
        self.lw_asset_item.clear()

        entities = finder.find("asset_name", {"asset_type": label})

        for entity in entities:
            self.addListWidgetItem(self.lw_asset_name, entity, entity.data["asset_name"])

    def on_asset_name_clicked(self, item):
        self.deactivate_item_button()

        itemData = item.data(QtCore.Qt.UserRole)

        self.lw_asset_task.clear()
        self.lw_asset_version.clear()
        self.lw_asset_item.clear()

        entities = finder.find("asset_task", itemData.data)

        for entity in entities:
            self.addListWidgetItem(self.lw_asset_task, entity, entity.data["asset_task"])

    def on_asset_task_clicked(self, item):
        self.deactivate_item_button()

        itemData = item.data(QtCore.Qt.UserRole)

        self.lw_asset_version.clear()
        self.lw_asset_item.clear()

        entities = finder.find("asset_version", itemData.data)

        for entity in entities:
            self.addListWidgetItem(self.lw_asset_version, entity, entity.data["asset_version"])

    def on_asset_version_clicked(self, item):
        self.deactivate_item_button()

        itemData = item.data(QtCore.Qt.UserRole)

        self.lw_asset_item.clear()

        entities = finder.find("asset_item", itemData.data)

        for entity in entities:
            self.addListWidgetItem(self.lw_asset_item, entity, entity.data["asset_item"])

    def on_asset_item_selected(self, item):
        self.activate_item_button()

        self.selected_item = item
        self.handler_buttons_asset()


#Shot clicked
    def on_shot_type_clicked(self, item):
        self.deactivate_item_button()

        label = item.text()

        self.lw_asset_name.clear()
        self.lw_asset_task.clear()
        self.lw_asset_version.clear()
        self.lw_asset_item.clear()

        entities = finder.find("shot_name", {"shot_type": label})

        for entity in entities:
            self.addListWidgetItem(self.lw_asset_name, entity, entity.data["shot_name"])

    def on_shot_name_clicked(self, item):
        self.deactivate_item_button()

        itemData = item.data(QtCore.Qt.UserRole)

        self.lw_asset_task.clear()
        self.lw_asset_version.clear()
        self.lw_asset_item.clear()

        entities = finder.find("shot_task", itemData.data)

        for entity in entities:
            self.addListWidgetItem(self.lw_asset_task, entity, entity.data["shot_task"])

    def on_shot_task_clicked(self, item):
        self.deactivate_item_button()

        itemData = item.data(QtCore.Qt.UserRole)

        self.lw_asset_version.clear()
        self.lw_asset_item.clear()

        entities = finder.find("shot_version", itemData.data)

        for entity in entities:
            self.addListWidgetItem(self.lw_asset_version, entity, entity.data["shot_version"])

    def on_shot_version_clicked(self, item):
        self.deactivate_item_button()

        itemData = item.data(QtCore.Qt.UserRole)

        self.lw_asset_item.clear()

        entities = finder.find("shot_item", itemData.data)

        for entity in entities:
            self.addListWidgetItem(self.lw_asset_item, entity, entity.data["shot_item"])

    def on_shot_item_selected(self, item):
        self.activate_item_button()

        self.selected_item = item
        self.handler_buttons_asset()

#Open/delete button function
    def handler_buttons_asset(self):

        if hasattr(self, "selected_item") and self.selected_item:

            entity = self.selected_item.data(QtCore.Qt.UserRole)
            file_path = conf.root + "/" + conf.templates["asset_item"]["glob"].format(**entity.data)
            if not file_path:
                file_path = conf.root + "/" + conf.templates["shot_item"]["glob"].format(**entity.data)

            file_path = os.path.normpath(file_path)

            action_ui = handler.interact()
            action_ui.init(action_ui, self.hbl_handler)

            selection = handler.Path(file_path)

            action_ui.update(selection)
            self.action_ui = action_ui


    def open_selected_asset(self):
        if hasattr(self, "selected_item") and self.selected_item:
            entity = self.selected_item.data(QtCore.Qt.UserRole)
            file_path = conf.root + "/" + conf.templates["asset_item"]["glob"].format(**entity.data)
            if not file_path:
                file_path = conf.root + "/" + conf.templates["shot_item"]["glob"].format(**entity.data)

            file_path = os.path.normpath(file_path)


            if file_path and os.path.exists(file_path):
                if os.name == "nt":
                    os.startfile(file_path)
                print(f"Open : {file_path}")
            else:
                print(f"Fail to open : {file_path}")


    def delete_selected_asset(self):
        if hasattr(self, "selected_item") and self.selected_item:
            entity = self.selected_item.data(QtCore.Qt.UserRole)
            file_path = conf.root + "/" + conf.templates["asset_item"]["glob"].format(**entity.data)
            if not file_path:
                file_path = conf.root + "/" + conf.templates["shot_item"]["glob"].format(**entity.data)

            file_path = os.path.normpath(file_path)

            reply = QtWidgets.QMessageBox.question(self,  "Delete Asset",  f"Are you sure you want to delete {file_path} ?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

            if reply == QtWidgets.QMessageBox.Yes:
                try:
                    os.remove(file_path)
                    row = self.lw_asset_item.row(self.selected_item)
                    self.lw_asset_item.takeItem(row)
                    print(f"Element delete : {file_path}")
                except Exception as e:
                    QtWidgets.QMessageBox.warning(self, "Erreur", f"Item can't deleted : {e}")

#Main
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Browser()
    window.show()

    app.exec_()