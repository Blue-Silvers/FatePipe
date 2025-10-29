from qtpy import QtWidgets
from abspipeline.core import engine
from pathlib import Path
from PySide6.QtGui import QFont

class interact(QtWidgets.QWidget):
    # inherits QWidget to have a sender() on button clic
    """
    Example ActionHandler.

    Implements a series of Buttons, as defined in the engine.
    Buttons call a function using the selected Sid.
    """

    def __init__(self):
        super(interact, self).__init__()
        self.selection = None
        self.buttons = []
        self.engine = engine.get()

    def init(self, parent_window, parent_widget):
        self.parent_window = parent_window
        self.action_box = QtWidgets.QGroupBox("Actions", parent_window)
        self.action_layout = QtWidgets.QHBoxLayout(parent_window)
        self.action_box.setLayout(self.action_layout)
        parent_widget.addWidget(self.action_box)
        #self.parent_window.setStyleSheet("background-color:  # 040f13;")

    def update(self, selection=None):

        self.selection = selection

        self.action_box.setTitle("Specific actions")
        font1 = QFont()
        font1.setFamilies([u"Terminal"])
        self.action_box.setFont(font1)
        self.action_box.setStyleSheet(
            "background-color: #071e26;"
            "border-radius: 5px;"
            "padding: 15px"
        )
        for b in self.buttons:
            b.setVisible(False)
            b.deleteLater()
        self.buttons = []

        actions = self.engine.actions
        for action in actions:
            button = QtWidgets.QPushButton("&" + action, self.parent_window)
            # button.setToolTip(
            #     (actions.get(action).__doc__ or "").strip().replace("\t", "")
            # )
            font1 = QFont()
            font1.setFamilies([u"Terminal"])
            font1.setPointSize(20)
            font1.setBold(False)
            font1.setItalic(False)
            font1.setUnderline(False)
            font1.setStrikeOut(False)
            button.setFont(font1)
            button.setStyleSheet(
                "background-color: #7D9191;"
                "border-radius: 5px;"
                "padding: 5px"
            )
            button.setObjectName(action)
            button.clicked.connect(self.run_action)
            self.action_layout.addWidget(button)
            self.buttons.append(button)

    def run_action(self):

        if not self.selection:
            return

        entity = self.selection
        action = self.sender().objectName()  # name of the button

        try:

            msg = f'Now running {action} on "{entity}"'
            print(msg)
            func = getattr(self.engine, action)
            func(entity)

        except Exception as e:
            print(e)


if __name__ == "__main__":
    # Running the ActionHandler without the Browser UI

    app = QtWidgets.QApplication.instance() or QtWidgets.QApplication([])

    action_ui = interact()
    action_ui.init(action_ui, QtWidgets.QGridLayout())

    from pathlib import Path

    selection = Path(__file__)

    action_ui.update(selection)
    action_ui.show()

    app.exec_()
