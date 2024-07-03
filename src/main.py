from PyQt5.QtWidgets import QApplication
from ui import PasswordManagerUI

def main():
    import sys
    app = QApplication(sys.argv)
    window = PasswordManagerUI()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
