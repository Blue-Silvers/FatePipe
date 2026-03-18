import sys
import os
import shutil

from qtpy import QtCore, QtWidgets
from abspipeline import conf
from qtpy.uic import loadUi

from abspipeline.core.dt.entity import Entity

ui_path = os.path.join(os.path.dirname(__file__), "qt/browser.ui")

from abspipeline.ui import interact as handler

from abspipeline.core import finder


class Browser(QtWidgets.QMainWindow):
    # cb = QtWidgets.QApplication.clipboard()  # exemple de clipboard

    def __init__(self):
        super(Browser, self).__init__()

        #init self variable to None
        self.asset_type_comboBox = None
        self.action_ui = None
        self.selected_item = None
        self.selected_entity = None
        self.selected_list = None

        #init UI
        loadUi(ui_path, self)
        self.setWindowTitle(f"{conf.browser_title} - Browser")

        self.pb_asset.clicked.connect(self.on_asset_clicked)
        self.pb_shot.clicked.connect(self.on_shot_clicked)

        self.pb_open.clicked.connect(self.open_selected_asset)
        self.pb_delete.clicked.connect(self.delete_selected_asset)
        self.pb_folder.clicked.connect(self.create_folder)
        self.activate_folder_button()

        self.populate()

        self.childType = "asset_task"

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

        baseEntity = Entity("asset", {})
        self.selected_entity = baseEntity
        self.childType = "asset_type"

    def addListWidgetItem(self,listWidget, data, label):
        self.selected_list = listWidget
        item = QtWidgets.QListWidgetItem()
        item.setData(QtCore.Qt.UserRole, data)
        item.setText(label)
        listWidget.addItem(item)
        return item

#Button
    def activate_item_button(self):

        self.pb_open.setEnabled(True)
        self.pb_delete.setEnabled(True)
        self.pb_folder.setEnabled(False)
        self.pb_open.setStyleSheet(
            "background-color: #7D9191;"
        )
        self.pb_delete.setStyleSheet(
            "background-color: #7D9191;"
        )
        self.pb_folder.setStyleSheet(
            "background-color: #071e26;"
        )


        if hasattr(self, "action_ui") and self.action_ui is not None:
            self.action_ui.action_box.setVisible(False)

    def deactivate_item_button(self):
        self.pb_open.setEnabled(False)
        self.pb_delete.setEnabled(True)
        self.pb_folder.setEnabled(True)
        self.pb_open.setStyleSheet(
            "background-color: #071e26;"
        )
        self.pb_delete.setStyleSheet(
            "background-color: #7D9191;"
        )
        self.pb_folder.setStyleSheet(
            "background-color: #7D9191;"
        )

        if hasattr(self, "action_ui") and self.action_ui is not None:
            self.action_ui.action_box.setVisible(False)

    def activate_folder_button(self):
        self.pb_open.setEnabled(False)
        self.pb_delete.setEnabled(False)
        self.pb_folder.setEnabled(True)
        self.pb_open.setStyleSheet(
            "background-color: #071e26;"
        )
        self.pb_delete.setStyleSheet(
            "background-color: #071e26;"
        )
        self.pb_folder.setStyleSheet(
            "background-color: #7D9191;"
        )

        if hasattr(self, "action_ui") and self.action_ui is not None:
            self.action_ui.action_box.setVisible(False)

    def activate_only_delete_button(self):
        self.pb_open.setEnabled(False)
        self.pb_delete.setEnabled(True)
        self.pb_folder.setEnabled(False)
        self.pb_open.setStyleSheet(
            "background-color: #071e26;"
        )
        self.pb_delete.setStyleSheet(
            "background-color: #7D9191;"
        )
        self.pb_folder.setStyleSheet(
            "background-color: #071e26;"
        )

        if hasattr(self, "action_ui") and self.action_ui is not None:
            self.action_ui.action_box.setVisible(False)

    def on_asset_clicked(self):
        self.activate_folder_button()

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

        baseEntity = Entity("asset", {})
        self.selected_entity = baseEntity
        self.childType = "asset_type"

    def on_shot_clicked(self):
        self.pb_asset.setEnabled(True)
        self.pb_shot.setEnabled(False)
        self.activate_folder_button()

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

        baseEntity = Entity("shot", {})
        self.selected_entity = baseEntity
        self.childType = "shot_type"

#Asset clicked
    def on_asset_type_clicked(self, item):
        self.deactivate_item_button()

        label = item.text()
        self.selected_entity = item.data(QtCore.Qt.UserRole)
        self.childType = "asset_name"

        self.lw_asset_name.clear()
        self.lw_asset_task.clear()
        self.lw_asset_version.clear()
        self.lw_asset_item.clear()

        entities = finder.find("asset_name", {"asset_type": label})

        for entity in entities:
            self.addListWidgetItem(self.lw_asset_name, entity, entity.data["asset_name"])

        self.selected_item = item

    def on_asset_name_clicked(self, item):
        self.deactivate_item_button()

        itemData = item.data(QtCore.Qt.UserRole)
        self.selected_entity = item.data(QtCore.Qt.UserRole)
        self.childType = "asset_task"

        self.lw_asset_task.clear()
        self.lw_asset_version.clear()
        self.lw_asset_item.clear()

        entities = finder.find("asset_task", itemData.data)

        for entity in entities:
            self.addListWidgetItem(self.lw_asset_task, entity, entity.data["asset_task"])

        self.selected_item = item
        #print(entities)

    def on_asset_task_clicked(self, item):
        self.deactivate_item_button()

        itemData = item.data(QtCore.Qt.UserRole)
        self.selected_entity = item.data(QtCore.Qt.UserRole)
        self.childType = "asset_version"


        self.lw_asset_version.clear()
        self.lw_asset_item.clear()

        entities = finder.find("asset_version", itemData.data)

        for entity in entities:
            self.addListWidgetItem(self.lw_asset_version, entity, entity.data["asset_version"])

        self.selected_item = item
        #print(entities)

    def on_asset_version_clicked(self, item):
        self.activate_only_delete_button()

        itemData = item.data(QtCore.Qt.UserRole)
        self.selected_entity = item.data(QtCore.Qt.UserRole)
        self.childType = "asset_item"

        self.lw_asset_item.clear()

        entities = finder.find("asset_item", itemData.data)

        for entity in entities:
            self.addListWidgetItem(self.lw_asset_item, entity, entity.data["asset_item"])

        self.selected_item = item

    def on_asset_item_selected(self, item):
        self.activate_item_button()

        self.selected_item = item
        self.selected_entity = item.data(QtCore.Qt.UserRole)

        self.handler_buttons_asset()


#Shot clicked
    def on_shot_type_clicked(self, item):
        self.deactivate_item_button()

        label = item.text()
        self.selected_entity = item.data(QtCore.Qt.UserRole)
        self.childType = "shot_name"

        self.lw_asset_name.clear()
        self.lw_asset_task.clear()
        self.lw_asset_version.clear()
        self.lw_asset_item.clear()

        entities = finder.find("shot_name", {"shot_type": label})

        for entity in entities:
            self.addListWidgetItem(self.lw_asset_name, entity, entity.data["shot_name"])

        self.selected_item = item


    def on_shot_name_clicked(self, item):
        self.deactivate_item_button()

        itemData = item.data(QtCore.Qt.UserRole)
        self.selected_entity = item.data(QtCore.Qt.UserRole)
        self.childType = "shot_task"

        self.lw_asset_task.clear()
        self.lw_asset_version.clear()
        self.lw_asset_item.clear()

        entities = finder.find("shot_task", itemData.data)

        for entity in entities:
            self.addListWidgetItem(self.lw_asset_task, entity, entity.data["shot_task"])

        self.selected_item = item

    def on_shot_task_clicked(self, item):
        self.deactivate_item_button()

        itemData = item.data(QtCore.Qt.UserRole)
        self.selected_entity = item.data(QtCore.Qt.UserRole)
        self.childType = "shot_version"

        self.lw_asset_version.clear()
        self.lw_asset_item.clear()

        entities = finder.find("shot_version", itemData.data)

        for entity in entities:
            self.addListWidgetItem(self.lw_asset_version, entity, entity.data["shot_version"])

        self.selected_item = item

    def on_shot_version_clicked(self, item):
        self.activate_only_delete_button()

        itemData = item.data(QtCore.Qt.UserRole)
        self.selected_entity = item.data(QtCore.Qt.UserRole)
        self.childType = "shot_item"

        self.lw_asset_item.clear()

        entities = finder.find("shot_item", itemData.data)

        for entity in entities:
            self.addListWidgetItem(self.lw_asset_item, entity, entity.data["shot_item"])

        self.selected_item = item

    def on_shot_item_selected(self, item):
        self.activate_item_button()

        self.selected_item = item
        self.selected_entity = item.data(QtCore.Qt.UserRole)

        self.handler_buttons_asset()

#Open/delete button function
    def handler_buttons_asset(self):

        if hasattr(self, "selected_item") and self.selected_item:

            entity = self.selected_item.data(QtCore.Qt.UserRole)
            file_path = conf.root / conf.templates["asset_item"]["glob"].format(**entity.data)
            if not file_path:
                file_path = conf.root / conf.templates["shot_item"]["glob"].format(**entity.data)

            action_ui = handler.interact()
            action_ui.init(action_ui, self.hbl_handler)

            selection = handler.Path(file_path)

            action_ui.update(selection)
            self.action_ui = action_ui


    def open_selected_asset(self):
        if hasattr(self, "selected_item") and self.selected_item:
            entity = self.selected_item.data(QtCore.Qt.UserRole)
            file_path = conf.root / conf.templates["asset_item"]["glob"].format(**entity.data)
            if not file_path:
                file_path = conf.root / conf.templates["shot_item"]["glob"].format(**entity.data)

            if file_path and os.path.exists(file_path):
                if os.name == "nt":
                    os.startfile(file_path)
                print(f"Open : {file_path}")
            else:
                print(f"Fail to open : {file_path}")


    def delete_selected_asset(self):
        if hasattr(self, "selected_item") and self.selected_item:
            entity = self.selected_item.data(QtCore.Qt.UserRole)

            file_path = conf.root / conf.templates[entity.type]["glob"].format(**entity.data)

            reply = QtWidgets.QMessageBox.question(self,  "Delete Asset",  f"Are you sure you want to delete {file_path} ?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

            if reply == QtWidgets.QMessageBox.Yes:
                try:
                    if entity.type == "asset_item" or entity.type == "shot_item":
                        os.remove(file_path)
                    else:
                        shutil.rmtree(file_path)

                    if entity.type.endswith("_item"):
                        row = self.lw_asset_item.row(self.selected_item)
                        self.lw_asset_item.takeItem(row)
                    elif entity.type.endswith("_version"):
                        row = self.lw_asset_version.row(self.selected_item)
                        self.lw_asset_version.takeItem(row)
                        self.lw_asset_item.clear()
                    elif entity.type.endswith("_task"):
                        row = self.lw_asset_task.row(self.selected_item)
                        self.lw_asset_task.takeItem(row)
                        self.lw_asset_version.clear()
                    elif entity.type.endswith("_name"):
                        row = self.lw_asset_name.row(self.selected_item)
                        self.lw_asset_name.takeItem(row)
                        self.lw_asset_task.clear()
                    else:
                        row = self.lw_asset_type.row(self.selected_item)
                        self.lw_asset_type.takeItem(row)
                        self.lw_asset_name.clear()

                    print(f"Element delete : {file_path}")
                except Exception as e:
                    QtWidgets.QMessageBox.warning(self, "Error", f"Item can't deleted : {e}")



    def create_folder(self):

        if self.selected_entity:
            entity = self.selected_entity
            if entity.type == "asset_item" or entity.type == "shot_item" or entity.type == "asset_version" or entity.type == "shot_version":
                QtWidgets.QMessageBox.warning(self, "Error", "Don't add folder here")
                return

            file_path = conf.root / conf.templates[entity.type]["glob"].format(**entity.data)

            folder_name, ok = QtWidgets.QInputDialog.getText(self, "New Folder", "Folder name :", QtWidgets.QLineEdit.Normal, "new_folder")

            if not ok or not folder_name.strip():
                return

            new_folder_path = file_path / folder_name.strip()
            try:
                new_folder_path.mkdir(exist_ok=False)
            except FileExistsError:
                QtWidgets.QMessageBox.warning(self, "Error", "A folder with this name already exists.")
                return

            ###Add folder logic
            if conf.folderTemplates[self.selected_entity.type].get("name"):
                for nameFolderName in conf.folderTemplates[self.selected_entity.type].get("name"):
                    try:
                        os.makedirs(os.path.join(new_folder_path, nameFolderName), exist_ok=False)
                        for taskFolderName in conf.folderTemplates[self.selected_entity.type].get("task"):
                            try:
                                os.makedirs(os.path.join(new_folder_path, nameFolderName, taskFolderName), exist_ok=False)
                            except FileExistsError:
                                QtWidgets.QMessageBox.warning(self, "Error","A task subfolder with this name already exists.")
                                return
                            for entityFolderName in conf.folderTemplates[self.selected_entity.type].get("version"):
                                try:
                                    os.makedirs(os.path.join(new_folder_path, nameFolderName, taskFolderName, entityFolderName), exist_ok=False)
                                except FileExistsError:
                                    QtWidgets.QMessageBox.warning(self, "Error","A version subfolder with this name already exists.")
                                    return
                    except FileExistsError:
                        QtWidgets.QMessageBox.warning(self, "Error", "A name subfolder with this name already exists.")
                        return
            elif conf.folderTemplates[self.selected_entity.type].get("task"):
                for taskFolderName in conf.folderTemplates[self.selected_entity.type].get("task"):
                    try:
                        os.makedirs(os.path.join(new_folder_path, taskFolderName), exist_ok=False)
                        for versionFolderName in conf.folderTemplates[self.selected_entity.type].get("version"):
                            try:
                                os.makedirs(os.path.join(new_folder_path, taskFolderName, versionFolderName), exist_ok=False)
                            except FileExistsError:
                                QtWidgets.QMessageBox.warning(self, "Error","A version subfolder with this name already exists.")
                                return
                    except FileExistsError:
                        QtWidgets.QMessageBox.warning(self, "Error", "A task subfolder with this name already exists.")
                        return
            elif conf.folderTemplates[self.selected_entity.type].get("version"):
                for versionFolderName in conf.folderTemplates[self.selected_entity.type].get("version"):
                    try:
                        os.makedirs(os.path.join(new_folder_path, versionFolderName), exist_ok=False)
                    except FileExistsError:
                        QtWidgets.QMessageBox.warning(self, "Error","A version subfolder with this name already exists.")
                        return

            ###reload list
            if entity.type == "asset":
                self.on_asset_clicked()
            elif entity.type == "shot":
                self.on_shot_clicked()
            elif hasattr(self, "selected_item") and self.selected_item:
                select_entity = self.selected_item.data(QtCore.Qt.UserRole)
                self.selected_list.clear()
                select_entities = finder.find(self.childType, {**select_entity.data})
                for select_entity in select_entities:
                    self.addListWidgetItem(self.selected_list, select_entity, select_entity.data[self.childType])



#Main
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Browser()
    window.show()

    app.exec_()