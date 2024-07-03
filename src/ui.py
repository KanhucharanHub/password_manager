import os
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, 
                             QMessageBox, QTableWidget, QTableWidgetItem)
from encryption import EncryptionManager
from database import DatabaseManager
from password_generator import generate_password
from authentication import AuthenticationManager
from utils import get_asset_path

class PasswordManagerUI(QWidget):
    def __init__(self):
        super().__init__()
        self.db_manager = DatabaseManager()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.service_label = QLabel('Service:')
        self.service_input = QLineEdit()
        
        self.username_label = QLabel('Username:')
        self.username_input = QLineEdit()
        
        self.password_label = QLabel('Password:')
        self.password_input = QLineEdit()
        
        self.generate_button = QPushButton('Generate Password')
        self.generate_button.clicked.connect(self.generate_password)
        
        self.save_button = QPushButton('Save Password')
        self.save_button.clicked.connect(self.save_password)
        
        self.show_passwords_button = QPushButton('Show Saved Passwords')
        self.show_passwords_button.clicked.connect(self.show_saved_passwords)

        layout.addWidget(self.service_label)
        layout.addWidget(self.service_input)
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.generate_button)
        layout.addWidget(self.save_button)
        layout.addWidget(self.show_passwords_button)

        self.passwords_table = QTableWidget()
        self.passwords_table.setColumnCount(3)
        self.passwords_table.setHorizontalHeaderLabels(['Service', 'Username', 'Password'])
        layout.addWidget(self.passwords_table)

        self.setLayout(layout)
        self.setWindowTitle('Password Manager')

        css_path = get_asset_path('assets/styles/styles.css')
        with open(css_path, 'r') as file:
            self.setStyleSheet(file.read())

    def generate_password(self):
        password = generate_password()
        self.password_input.setText(password)
    
    def save_password(self):
        service = self.service_input.text()
        username = self.username_input.text()
        password = self.password_input.text()

        # Encrypt the password before saving
        encryption_key = EncryptionManager.generate_key()
        encryption_manager = EncryptionManager(encryption_key)
        encrypted_password = encryption_manager.encrypt(password)

        self.db_manager.add_password(service, username, encrypted_password)
        QMessageBox.information(self, 'Success', 'Password saved successfully!')

    def show_saved_passwords(self):
        passwords = self.db_manager.get_all_passwords()
        self.passwords_table.setRowCount(len(passwords))
        for row, (service, username, password) in enumerate(passwords):
            self.passwords_table.setItem(row, 0, QTableWidgetItem(service))
            self.passwords_table.setItem(row, 1, QTableWidgetItem(username))
            self.passwords_table.setItem(row, 2, QTableWidgetItem(password))

def main():
    app = QApplication([])
    window = PasswordManagerUI()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
