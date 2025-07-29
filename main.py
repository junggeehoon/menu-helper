import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from api.google_image_search_api import search_image_urls
from gui.main_app import Ui_MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())
