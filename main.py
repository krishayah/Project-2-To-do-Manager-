import sys

from PyQt6.QtWidgets import QMainWindow, QApplication
from Logic import APPLogic
from gui import Ui_To_Do_List

class MainWindow (QMainWindow):
    """
    Main application window for To-Do List Manager
    """
    def __init__(self):
        super().__init__()
        self.ui = Ui_To_Do_List()
        self.ui.setupUi(self)

def main():
    """
    Main entry point for the application.
    """
    app = QApplication(sys.argv)  # Create the application
    window = MainWindow()         # Create the main window
    window.show()                 # Show the main window
    sys.exit(app.exec())          # Execute the application event loop

if __name__ == "__main__":
    main()