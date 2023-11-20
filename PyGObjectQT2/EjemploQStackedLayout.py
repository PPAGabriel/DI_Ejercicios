import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QGridLayout,QHBoxLayout,QPushButton,
                             QVBoxLayout,QMainWindow,QWidget, QStackedLayout)

from VentanaColores import CaixaColor

class GridConContenido(QGridLayout):
    def __init__(self):
        super().__init__()

        self.addWidget(CaixaColor("red"))
        self.addWidget(CaixaColor("blue"),0,1,1,2)
        self.addWidget(CaixaColor("green"),1,0,2,1)
        self.addWidget(CaixaColor("pink"),1,1,1,2)
        self.addWidget(CaixaColor("orange"),2,1,1,1)
        self.addWidget(CaixaColor("yellow"),2,2,1,1)

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejemplo QStacked Layout con QT")

        cajaV=QVBoxLayout()
        cajaBotones=QHBoxLayout()
        self.tarjetas=QStackedLayout()
        cajaV.addLayout(self.tarjetas)
        cajaV.addLayout(cajaBotones)

        btnRojo=QPushButton("Rojo")
        btnRojo.pressed.connect(self.on_btnRojo_pressed)

        cajaBotones.addWidget(btnRojo)

        btnAzul = QPushButton("Azul")
        btnAzul.pressed.connect(self.on_btnAzul_pressed)

        cajaBotones.addWidget(btnAzul)

        btnGrid = QPushButton("Grid")
        btnGrid.pressed.connect(self.on_btnGrid_pressed)

        cajaBotones.addWidget(btnGrid)

        btnVerde = QPushButton("Verde")
        btnVerde.pressed.connect(self.on_btnVerde_pressed)

        cajaBotones.addWidget(btnVerde)

        self.tarjetas.addWidget(CaixaColor("red"))
        self.tarjetas.addWidget(CaixaColor("blue"))

        widgetGrid=QWidget()
        widgetGrid.setLayout(GridConContenido())
        self.tarjetas.addWidget(widgetGrid)

        self.tarjetas.addWidget(CaixaColor("green"))
        self.tarjetas.setCurrentIndex(1)

        container = QWidget()
        container.setLayout(cajaV)
        self.setCentralWidget(container)
        # mostramos la ventana
        self.show()

    def on_btnRojo_pressed(self):
        self.tarjetas.setCurrentIndex(0)

    def on_btnAzul_pressed(self):
        self.tarjetas.setCurrentIndex(1)

    def on_btnGrid_pressed(self):
        self.tarjetas.setCurrentIndex(2)

    def on_btnVerde_pressed(self):
        self.tarjetas.setCurrentIndex(3)

if __name__ == "__main__":
    # creamos un objeto de instancia qapplication
    aplicacion = QApplication(sys.argv)  # sys.argv -> unimos la aplicacion con el sistema operativo
    # creamos un objeto de la ventana
    ventana = VentanaPrincipal()
    # ejecutamos la union?
    aplicacion.exec()