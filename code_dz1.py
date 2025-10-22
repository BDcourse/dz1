import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QFont, QPixmap


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(50, 50, 250, 400)
        self.setWindowTitle("2.1 - User Profile GUI (PyQt6)")
        self.setUpMainWindow()
        self.show()

    def createImageLabels(self):
        images = ["images/photo_2025-10-22_18-51-26.jpg", "images/photo_2025-10-22_17-49-33.jpg"]

        for image in images:
            try:
                with open(image):
                    label = QLabel(self)
                    pixmap = QPixmap(image)
                    label.setPixmap(pixmap)
                    if image == "images/photo_2025-10-22_17-49-33.jpg":
                        label.move(80, 20)
            except FileNotFoundError as error:
                print(f"Image not found.\nError: {error}")

    def setUpMainWindow(self):
        self.createImageLabels()

        user_label = QLabel(self)
        user_label.setText("Иван Иванов")
        user_label.setFont(QFont("Arial", 20))
        user_label.move(70, 140)

        bio_label = QLabel(self)
        bio_label.setText("Биография")
        bio_label.setFont(QFont("Arial", 17))
        bio_label.move(15, 175)

        about_label = QLabel(self)
        about_label.setText("Я ипохондрик")
        about_label.setWordWrap(True)
        about_label.move(15, 195)

        skills_label = QLabel(self)
        skills_label.setText("Умения")
        skills_label.setFont(QFont("Arial", 17))
        skills_label.move(15, 240)

        languages_label = QLabel(self)
        languages_label.setText("Python | PHP | SQL | JavaScript")
        languages_label.move(15, 260)

        experience_label = QLabel(self)
        experience_label.setText("Опыт")
        experience_label.setFont(QFont("Arial", 17))
        experience_label.move(15, 290)

        developer_label = QLabel(self)
        developer_label.setText("Python разработчик")
        developer_label.move(15, 310)

        dev_dates_label = QLabel(self)
        dev_dates_label.setText("Март 2025 - Май 2025")
        dev_dates_label.setFont(QFont("Arial", 10))
        dev_dates_label.move(15, 330)

        driver_label = QLabel(self)
        driver_label.setText("Хоббихорсер")
        driver_label.move(15, 350)

        driver_dates_label = QLabel(self)
        driver_dates_label.setText("Январь 2020 - Настоящее время")
        driver_dates_label.setFont(QFont("Arial", 10))
        driver_dates_label.move(15, 370)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())