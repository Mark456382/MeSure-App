from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
import sys


class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(390, 660)
        self.setWindowTitle("MeSureApp")
        self.setStyleSheet("""background-color: #4169C1;""")
        self.main()

    def main(self):

        my_pocket_gp = QPushButton("", self)
        my_pocket_gp.setGeometry(50, 240, 120, 120)
        my_pocket_gp.clicked.connect(self.my_pocket_GP)
        my_pocket_gp.setStyleSheet("""
                                    background-image: url(WorkImg/MyPocketGP.jpg);
                                    border: none;
                                    border-radius: 16px;
                                    """)

        health_dairy = QPushButton("", self)
        health_dairy.setGeometry(220, 240, 120, 120)
        health_dairy.clicked.connect(self.health_dairy)
        health_dairy.setStyleSheet("""
                                    background-image: url(WorkImg/Health Dairy.jpg);
                                    border: none;
                                    border-radius: 16px;
                                    """)
        
        mpg_text = QLabel("My PocketGP", self)
        mpg_text.setFont(QFont('Poppins', 12))
        hd_text= QLabel("Health Dairy", self)
        hd_text.setFont(QFont('Poppins', 12))
        mpg_text.resize(130, 40)
        hd_text.resize(130, 40)
        mpg_text.move(60, 365)
        hd_text.move(230, 365)

        settings = QPushButton("", self)
        settings.setGeometry(10, 10, 50, 50)
        settings.clicked.connect(self.settings)
        settings.setStyleSheet("""
                                background-image: url(/home/mark/Документы/GitHub/ReactNodeApp/WorkImg/settings.png);
                                border: none;
                                """)
        
        profile = QPushButton('', self)
        profile.setGeometry(330, 10, 50, 50)
        profile.clicked.connect(self.profile)
        profile.setStyleSheet("""
                                background-image: url(/home/mark/Документы/GitHub/ReactNodeApp/WorkImg/profile.png);
                                border: none;
                                """)

    def profile(self): print('Profile')

    def settings(self): print('Settings')

    def my_pocket_GP(self): print("My Pocket GP")

    def health_dairy(self): print("Health Dairy")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = App()
    win.show()  
    sys.exit(app.exec())



