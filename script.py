import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.uic import loadUi

# Define a function that prints "test"
operation = ""
def oper():
    global operation
    try:
        sender = app.sender()    
        if sender.text() == "AC":
            widget.result.setText("")
            operation = ""
        elif sender.text() == "DEL":
            operation = operation[:-1]
            widget.result.setText(operation)
        elif sender.text() == "=":
            result = eval(operation)
            result = operation + "=" + str(result)
            a = rech(result)
            widget.result.setText(a)
        else:
            
            operation = operation + sender.text()
            widget.result.setText(operation)
    except:
        widget.result.setText("ERROR")
        
def rech(ch):
    res = ""
    for i in range(len(ch)):
        if ch[i] == "=":
            res = ch[i+1:]
    return res

    
        


# Create the application instance
app = QApplication(sys.argv)




# Load the UI file
widget = loadUi('calculator.ui')
widget.show()
buttons = [widget.num0,widget.num1,widget.num2,widget.num3,widget.num4,widget.num5,widget.num6,widget.num7,widget.num8,widget.num9,widget.equal,widget.plus,widget.division,widget.multiple,widget.delet,widget.ac,widget.right,widget.left,widget.point,widget.minus
]
for i in range(len(buttons)):
    buttons[i].clicked.connect(oper)
sys.exit(app.exec_())
