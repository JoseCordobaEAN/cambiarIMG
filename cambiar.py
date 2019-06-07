import sys
from PyQt5 import uic, QtWidgets, QtGui
from random import choice
from PyQt5.QtGui import QIcon, QPixmap



class Cambiar(QtWidgets.QMainWindow):

    ICONOS = ['cat', 'dog', 'fish']

    def __init__(self):
        super(Cambiar, self).__init__()
        uic.loadUi('cambiar.ui', self)
        self.labelAnimal.setText('')
        self.btnCambiar.clicked.connect(self.cambio)
        self.show()

    def cambio(self):
        selecionado = choice(self.ICONOS)
        ruta = f'iconos/{selecionado}.png'
        pix = QPixmap(ruta)
        self.labelAnimal.setPixmap(pix)
        self.labelAnimal.resize(pix.width(),pix.height())
        self.show()





if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Cambiar()
    sys.exit(app.exec_())