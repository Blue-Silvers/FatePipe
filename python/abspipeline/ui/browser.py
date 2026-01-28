import sys
import os
import qtpy
from qtpy import QtCore, QtWidgets, QtGui
from abspipeline import conf
from qtpy.uic import loadUi

ui_path = os.path.join(os.path.dirname(__file__), "qt/browser.ui")

from abspipeline.ui import interact as handler

from abspipeline.core import finder

#from typing import Optional

#from spil import FindInAll as Finder, Sid, conf


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
        self.pb_folder.clicked.connect(self.create_folder)
        self.deactivate_folder_button()

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
        self.selected_list = listWidget  #####
        self.selected_entity = data
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

    def deactivate_folder_button(self):
        self.pb_open.setEnabled(False)
        self.pb_delete.setEnabled(False)
        self.pb_folder.setEnabled(False)
        self.pb_open.setStyleSheet(
            "background-color: #071e26;"
        )
        self.pb_delete.setStyleSheet(
            "background-color: #071e26;"
        )
        self.pb_folder.setStyleSheet(
            "background-color: #071e26;"
        )

        if hasattr(self, "action_ui") and self.action_ui is not None:
            self.action_ui.action_box.setVisible(False)

    def on_asset_clicked(self):
        self.deactivate_folder_button()

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
        self.deactivate_folder_button()

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

        self.selected_item = item

    def on_asset_name_clicked(self, item):
        self.deactivate_item_button()

        itemData = item.data(QtCore.Qt.UserRole)

        self.lw_asset_task.clear()
        self.lw_asset_version.clear()
        self.lw_asset_item.clear()

        entities = finder.find("asset_task", itemData.data)

        for entity in entities:
            self.addListWidgetItem(self.lw_asset_task, entity, entity.data["asset_task"])

        self.selected_item = item
        print(entities)

    def on_asset_task_clicked(self, item):
        self.deactivate_item_button()

        itemData = item.data(QtCore.Qt.UserRole)

        self.lw_asset_version.clear()
        self.lw_asset_item.clear()

        entities = finder.find("asset_version", itemData.data)

        for entity in entities:
            self.addListWidgetItem(self.lw_asset_version, entity, entity.data["asset_version"])

        self.selected_item = item
        print(entities)

    def on_asset_version_clicked(self, item):
        self.deactivate_item_button()

        itemData = item.data(QtCore.Qt.UserRole)

        self.lw_asset_item.clear()

        entities = finder.find("asset_item", itemData.data)

        for entity in entities:
            self.addListWidgetItem(self.lw_asset_item, entity, entity.data["asset_item"])

        self.selected_item = item

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

        self.selected_item = item


    def on_shot_name_clicked(self, item):
        self.deactivate_item_button()

        itemData = item.data(QtCore.Qt.UserRole)

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

        self.lw_asset_version.clear()
        self.lw_asset_item.clear()

        entities = finder.find("shot_version", itemData.data)

        for entity in entities:
            self.addListWidgetItem(self.lw_asset_version, entity, entity.data["shot_version"])

        self.selected_item = item

    def on_shot_version_clicked(self, item):
        self.deactivate_item_button()

        itemData = item.data(QtCore.Qt.UserRole)

        self.lw_asset_item.clear()

        entities = finder.find("shot_item", itemData.data)

        for entity in entities:
            self.addListWidgetItem(self.lw_asset_item, entity, entity.data["shot_item"])

        self.selected_item = item

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

            file_path = conf.root + "/" + conf.templates[entity.type]["glob"].format(**entity.data)

            file_path = os.path.normpath(file_path)

            reply = QtWidgets.QMessageBox.question(self,  "Delete Asset",  f"Are you sure you want to delete {file_path} ?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

            if reply == QtWidgets.QMessageBox.Yes:
                try:
                    if entity.type == "asset_item" or entity.type == "shot_item":
                        os.remove(file_path)
                    else:
                        os.rmdir(file_path)

                    if entity.type.endswith("_item"):
                        row = self.lw_asset_item.row(self.selected_item)
                        self.lw_asset_item.takeItem(row)
                    elif entity.type.endswith("_version"):
                        row = self.lw_asset_version.row(self.selected_item)
                        self.lw_asset_version.takeItem(row)
                    elif entity.type.endswith("_task"):
                        row = self.lw_asset_task.row(self.selected_item)
                        self.lw_asset_task.takeItem(row)
                    elif entity.type.endswith("_name"):
                        row = self.lw_asset_name.row(self.selected_item)
                        self.lw_asset_name.takeItem(row)
                    else:
                        row = self.lw_asset_type.row(self.selected_item)
                        self.lw_asset_type.takeItem(row)

                    print(f"Element delete : {file_path}")
                except Exception as e:
                    QtWidgets.QMessageBox.warning(self, "Error", f"Item can't deleted : {e}")



    def create_folder(self):

        if hasattr(self, "selected_item") and self.selected_item:

            entity = self.selected_item.data(QtCore.Qt.UserRole)

            if entity.type == "asset_item" or entity.type == "shot_item" or entity.type == "asset_version" or entity.type == "shot_version":
                QtWidgets.QMessageBox.warning(self, "Error", "Don't add folder here")
                return

            file_path = conf.root + "/" + conf.templates[entity.type]["glob"].format(**entity.data)

            file_path = os.path.normpath(file_path)
            folder_name, ok = QtWidgets.QInputDialog.getText( self, "New Folder", "Folder name :", QtWidgets.QLineEdit.Normal, "new_folder")

            if not ok or not folder_name.strip():
                return

            new_folder_path = os.path.join(file_path, folder_name.strip())

            try:
                os.makedirs(new_folder_path, exist_ok=False)
            except FileExistsError:
                QtWidgets.QMessageBox.warning(self, "Error", "A folder with this name already exists.")
                return

            ###Add folder logic
            if conf.folderTemplates[entity.type].get("name"):
                for nameFolderName in conf.folderTemplates[entity.type].get("name"):
                    try:
                        os.makedirs(os.path.join(new_folder_path, nameFolderName), exist_ok=False)
                        for taskFolderName in conf.folderTemplates[entity.type].get("task"):
                            try:
                                os.makedirs(os.path.join(os.path.join(new_folder_path, nameFolderName), taskFolderName), exist_ok=False)
                            except FileExistsError:
                                QtWidgets.QMessageBox.warning(self, "Error","A subfolder with this name already exists.")
                                return
                            for entityFolderName in conf.folderTemplates[entity.type].get("version"):
                                try:
                                    os.makedirs(os.path.join(os.path.join(os.path.join(new_folder_path, nameFolderName), taskFolderName), entityFolderName), exist_ok=False)
                                except FileExistsError:
                                    QtWidgets.QMessageBox.warning(self, "Error","A subfolder with this name already exists.")
                                    return
                    except FileExistsError:
                        QtWidgets.QMessageBox.warning(self, "Error", "A subfolder with this name already exists.")
                        return
            elif conf.folderTemplates[entity.type].get("task"):
                for taskFolderName in conf.folderTemplates[entity.type].get("task"):
                    try:
                        os.makedirs(os.path.join(new_folder_path, taskFolderName), exist_ok=False)
                        for versionFolderName in conf.folderTemplates[entity.type].get("version"):
                            try:
                                os.makedirs(os.path.join(os.path.join(new_folder_path, taskFolderName), versionFolderName), exist_ok=False)
                            except FileExistsError:
                                QtWidgets.QMessageBox.warning(self, "Error", "A subfolder with this name already exists.")
                                return
                    except FileExistsError:
                        QtWidgets.QMessageBox.warning(self, "Error", "A subfolder with this name already exists.")
                        return
            elif conf.folderTemplates[entity.type].get("version"):
                for versionFolderName in conf.folderTemplates[entity.type].get("version"):
                    try:
                        os.makedirs(os.path.join(new_folder_path, versionFolderName), exist_ok=False)
                    except FileExistsError:
                        QtWidgets.QMessageBox.warning(self, "Error", "A subfolder with this name already exists.")
                        return


            ###reload list
            self.selected_list.clear()
            entities = finder.find( self.selected_entity.type, {**entity.data})
            #print(entities)

            for entity in entities:
                self.addListWidgetItem(self.selected_list, entity, entity.data[self.selected_entity.type])

'''
def open_browser(
    sid: Optional[Sid | str] = None, do_new: Optional[bool] = False
) -> Browser:
    """
    Opens a browser window.
    If the window already exists, brings the existing one to the front.
    If do_new is set to True, a new Window instance is created

    (The Qt Application must already exist)

    Args:
        sid: the ui navigates to the given Sid upon startup
        do_new: if True, opens a new window instance, else brings the existing one to the front (default).

    Returns:
        the Browser window object
    """

    global browser_window
    try:
        if not browser_window:
            browser_window = None
    except:
        browser_window = None

    if do_new or not browser_window:
        browser_window = Browser(search=sid)
        browser_window.show()
    else:
        browser_window.activateWindow()
        browser_window.raise_()
        browser_window.setWindowState(
            browser_window.windowState() & ~QtCore.Qt.WindowMinimized
            | QtCore.Qt.WindowActive
        )
        browser_window.show()

    return browser_window


def app(sid: Optional[Sid | str] = None) -> None:
    """
    Gets or creates a QApplication instance,
    and opens the Browser window.

    Args:
        sid: Optional Sid instance or String to start with

    """

    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)  # fix
    app = QtWidgets.QApplication.instance() or QtWidgets.QApplication([])

    open_browser(sid)
    app.exec_()
'''

#Main
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Browser()
    window.show()

    app.exec_()

    #sid = "Character\Model\v010\Publish"
    #app(sid)

    '''
import sys;sys.path.extend(['C:/Users/fury8/PycharmProjects/FatePipe/.venv/Lib/site-packages', 'C:/Users/fury8/PycharmProjects/FatePipe/python'])
from abspipeline.ui.browser import Browser
Browser()

import sys;sys.path.extend(['C:/Users/enzo.lahana/Documents/PycharmProjects/FatePipe/.venv/Lib/site-packages', 'C:/Users/enzo.lahana/Documents/PycharmProjects/FatePipe/python'])
from abspipeline.ui.browser import Browser
Browser()

Good version :
import sys;sys.path.extend(['C:/Users/enzo.lahana/REZ/package/internals/FatePipe/0.1.0/.venv/Lib/site-packages', 'C:/Users/enzo.lahana/REZ/package/internals/FatePipe/0.1.0/python'])
from abspipeline.ui.browser import Browser
window = Browser()
window.show()
    '''