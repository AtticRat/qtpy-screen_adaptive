import sys

from qtpy.QtGui import QPixmap
from qtpy.QtWidgets import QPushButton, QApplication, QLabel, QLineEdit, QWidget, QFrame, QHBoxLayout

from QFlowLayout import QFlowLayout
from QScreenAdaptive import QKeepAspectRatio, QTextAdaptive, QImageAdaptive


@QKeepAspectRatio
@QTextAdaptive
@QImageAdaptive
class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QFlowLayout(self)
        self.setMinimumSize(640, 480)
        for i in range(10):
            button = QPushButton('Button' + str(i))
            image = QLabel()
            image.setFixedSize(80, 80)
            text = QLabel('<div>Text</div>')
            pixmap = QPixmap('img.png').scaled(image.width(), image.height())
            image.setPixmap(pixmap)
            line_edit = QLineEdit()

            self.layout.addWidget(button)
            self.layout.addWidget(image)
            self.layout.addWidget(text)
            self.layout.addWidget(line_edit)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    app.exec_()
