import sys
from PySide2.QtWidgets import (
    QApplication,
)

from main_widget import MainWidget


if __name__ == "__main__":
    tiny_linter_app = QApplication(sys.argv)

    main_widget = MainWidget()
    main_widget.resize(800, 600)
    main_widget.show()

    sys.exit(tiny_linter_app.exec_())