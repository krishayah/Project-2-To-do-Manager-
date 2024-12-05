import sys
from PyQt6.QtWidgets import *
from Logic import APPLogic
from gui import Ui_To_Do_List

def main():
    app = QApplication(sys.argv)  # Create the application
    window = QMainWindow()         # Create the main window

    #setup UI & logic
    ui = Ui_To_Do_List()
    ui.setupUi(window)

    #Pass UI instance to logic class
    logic = APPLogic

    window.show()                 # Show the main window
    sys.exit(app.exec())          # Execute the application event loop

if __name__ == "__main__":
    main()