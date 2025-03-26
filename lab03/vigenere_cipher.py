import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.vigenere import Ui_VigenereCipher
import requests

class VigenereApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_VigenereCipher()
        self.ui.setupUi(self)
        self.setCentralWidget(self.ui.widget)

        # Kết nối sự kiện nút bấm với hàm gọi API
        self.ui.btnEncrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btnDecrypt.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/vigenere/encrypt"
        payload = {   
            "plain_text": self.ui.txtPlainText.toPlainText(),
            "key": self.ui.txtKey.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txtCipherText.setText(data['encrypted_message'])
                QMessageBox.information(self, "Success", "Encryption successful!")
            else:
                QMessageBox.critical(self, "Error", "Failed to encrypt text.")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Request failed: {e}")

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/vigenere/decrypt"
        payload = {
            "cipher_text": self.ui.txtCipherText.toPlainText(),
            "key": self.ui.txtKey.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txtPlainText.setText(data['decrypted_message'])
                QMessageBox.information(self, "Success", "Decryption successful!")
            else:
                QMessageBox.critical(self, "Error", "Failed to decrypt text.")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Request failed: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VigenereApp()
    window.show()
    sys.exit(app.exec_())
