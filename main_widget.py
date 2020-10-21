from PySide2.QtWidgets import (
    QLabel,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QTextEdit,
    QComboBox,
)

from PySide2.QtCore import Slot, Qt
from file_type import FileType

from json_validator import JsonValidator
from yaml_validator import YamlValidator


class MainWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.__text = QLabel("Enter the code below:")
        self.__text_edit = QTextEdit()

        self.__text.setAlignment(Qt.AlignCenter)

        self.__lint_button = QPushButton("Validate")
        self.__lint_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        self.__file_types_combo_box = QComboBox()
        self.__file_types_combo_box.addItem(
            FileType.JSON.name, userData=JsonValidator()
        )
        self.__file_types_combo_box.addItem(
            FileType.YAML.name, userData=YamlValidator()
        )

        self.__hbox_layout = QHBoxLayout()
        self.__hbox_layout.addWidget(self.__lint_button)
        self.__hbox_layout.addWidget(self.__file_types_combo_box)

        self.__vbox_layout = QVBoxLayout()
        self.__vbox_layout.addWidget(self.__text)
        self.__vbox_layout.addWidget(self.__text_edit)
        self.__vbox_layout.addLayout(self.__hbox_layout)
        self.setLayout(self.__vbox_layout)

        # Connecting the signal
        self.__lint_button.clicked.connect(self.on_lint_button_clicked)

    @Slot()
    def on_lint_button_clicked(self):
        self.validate()

    # TODO
    def validate(self):
        validator = self.__file_types_combo_box.currentData()
        validator.validate()