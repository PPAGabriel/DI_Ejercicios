import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QGridLayout, QLabel,QMainWindow,QWidget

from VentanaColores import CaixaColor

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejemplo Grid Layout con QT")

        grid=QGridLayout()

        grid.addWidget(CaixaColor("red"))
        grid.addWidget(CaixaColor("blue"),0,1,1,2)
        grid.addWidget(CaixaColor("green"),1,0,2,1)
        grid.addWidget(CaixaColor("pink"),1,1,1,2)
        grid.addWidget(CaixaColor("orange"),2,1,1,1)
        grid.addWidget(CaixaColor("yellow"),2,2,1,1)

        container = QWidget()
        container.setLayout(grid)
        self.setCentralWidget(container)
        # mostramos la ventana
        self.show()

if __name__ == "__main__":
    # creamos un objeto de instancia qapplication
    aplicacion = QApplication(sys.argv)  # sys.argv -> unimos la aplicacion con el sistema operativo
    # creamos un objeto de la ventana
    ventana = VentanaPrincipal()
    # ejecutamos la union?
    aplicacion.exec()