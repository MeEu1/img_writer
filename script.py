import sys
from os import path as op
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

app = QApplication([])

app.setStyle('Fusion')

window = QWidget()
window.setWindowTitle('Hider')
window.setFixedWidth(600)
window.setFixedHeight(400)

layout = QHBoxLayout()
left_layout = QVBoxLayout()
form_layout = QFormLayout()

imgPath = QLineEdit()
imgPath.setFixedHeight(380)
imgPath.setAlignment(Qt.AlignTop)
imgPath.setPlaceholderText('Img\'s Path:')

layout.addWidget(imgPath)

msg_box = QLineEdit()
msg_box.setFixedWidth(130)
msg_box.setPlaceholderText('Message')

def write_msg():
    alert_box = QMessageBox()

    if(op.isfile(imgPath.text()) and op.splitext(imgPath.text())[1] == '.jpeg'):
        with open(imgPath.text(), 'ab') as fp:
            fp.write(b'%a' % msg_box.text())
            alert_box.setWindowTitle('Success!')
            alert_box.setText('\'{}\' was written with success!'.format(msg_box.text()))
    elif(not op.isfile(imgPath.text())):
        alert_box.setWindowTitle('Error')
        alert_box.setText('{} is not a file'.format(imgPath.text()))
    elif(not op.splitext(imgPath.text())[1] == '.jpeg'):
        alert_box.setWindowTitle('Error')
        alert_box.setText('{} files are not supported'.format(op.splitext(imgPath.text())[1]))
    alert_box.exec()

write_btn = QPushButton('Write')
write_btn.clicked.connect(write_msg)

img_info = QLineEdit()
img_info.setReadOnly(True)
img_info.setPlaceholderText('Output')

def read_info():
    alert_box = QMessageBox()
    alert_box.setWindowTitle('Error')

    if(op.isfile(imgPath.text()) and op.splitext(imgPath.text())[1] == '.jpeg'):
        with open(imgPath.text(), 'rb') as fp:
            content = fp.read()
            offset = content.index(bytes.fromhex('FFD9'))

            fp.seek(offset + 2)
            img_info.setText(fp.read().decode('utf-8'))
    elif(not op.isfile(imgPath.text())):
        alert_box.setText('{} does not exist'.format(imgPath.text()))
        alert_box.exec()
    elif(not op.splitext(imgPath.text())[1] == '.jpeg'):
        alert_box.setText('{} files are not supported'.format(op.splitext(imgPath.text())[1]))
        alert_box.exec()

read_btn = QPushButton('Read')
read_btn.setFixedWidth(130)
read_btn.clicked.connect(read_info)

form_layout.addRow(msg_box, write_btn)
form_layout.addRow(read_btn, img_info)

def clear_text():
    imgPath.clear()
    msg_box.clear()
    img_info.clear()

clear_btn = QPushButton('Clear')
clear_btn.clicked.connect(clear_text)

def exit_app():
    sys.exit()

exit_btn = QPushButton('Exit')
exit_btn.clicked.connect(exit_app)

left_layout.addLayout(form_layout)
left_layout.addWidget(clear_btn)
left_layout.addWidget(exit_btn)

layout.addLayout(left_layout)

window.setLayout(layout)

window.show()
app.exec_()
