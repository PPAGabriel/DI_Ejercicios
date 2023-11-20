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


class BoxModificado(QHBoxLayout):
    # definimos la interfaz
    def __init__(self):
        super().__init__()

        # una caja que contenga varios cuadrados
        squares1 = QVBoxLayout()
        # añadimos los coloes
        squares1.addWidget(CaixaColor("red"))
        squares1.addWidget(CaixaColor("yellow"))
        squares1.addWidget(CaixaColor("purple"))

        # caja que contenga otra etiqueta
        square2 = QVBoxLayout()
        square2.addWidget(CaixaColor("green"))

        # caja que contrnga otras etiquetas
        square3 = QVBoxLayout()
        square3.addWidget(CaixaColor("blue"))
        square3.addWidget(CaixaColor("orange"))

        # añadimos a la caja grande las otras cajas
        self.addLayout(squares1)
        self.addLayout(square2)
        self.addLayout(square3)


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejemplo QStacked Layout con QT")

        cajaV=QVBoxLayout()
        cajaBotones=QHBoxLayout()
        self.tarjetas=QStackedLayout()
        cajaV.addLayout(self.tarjetas)
        cajaV.addLayout(cajaBotones)

        # CREACION DE BOTONES (SU POSICION SEGUN SEAN CREADOS ES INDEPENDIENTE AL ORDEN DE ADICION. ESTE ULTIMO ES EL QUE IMPORTA)

        #BOTON ROJO
        btnRojo=QPushButton("Rojo")
        btnRojo.pressed.connect(self.on_btnRojo_pressed)

        cajaBotones.addWidget(btnRojo)

        #BOTON AZUL
        btnAzul = QPushButton("Azul")
        btnAzul.pressed.connect(self.on_btnAzul_pressed)

        cajaBotones.addWidget(btnAzul)

        #BOTON GRID
        btnGrid = QPushButton("Grid")
        btnGrid.pressed.connect(self.on_btnGrid_pressed)

        cajaBotones.addWidget(btnGrid)

        #BOTON BOX MODIFICADO
        btnGridM = QPushButton("Grid Modificado")
        btnGridM.pressed.connect(self.on_btnBoxM_pressed)

        cajaBotones.addWidget(btnGridM)

        #0
        self.tarjetas.addWidget(CaixaColor("red"))
        #1
        self.tarjetas.addWidget(CaixaColor("blue"))
        #2
        widgetGrid=QWidget()
        widgetGrid.setLayout(GridConContenido())
        self.tarjetas.addWidget(widgetGrid)
        #3
        widgetGridM = QWidget()
        widgetGridM.setLayout(BoxModificado())
        self.tarjetas.addWidget(widgetGridM)

        container = QWidget()
        container.setLayout(cajaV)
        self.setCentralWidget(container)
        # mostramos la ventana
        self.show()

    #CONOCIENDO LOS INDEX, PODEMOS LLAMARLOS EN ESTOS METODOS
    def on_btnRojo_pressed(self):
        self.tarjetas.setCurrentIndex(0)

    def on_btnAzul_pressed(self):
        self.tarjetas.setCurrentIndex(1)

    def on_btnGrid_pressed(self):
        self.tarjetas.setCurrentIndex(2)

    def on_btnBoxM_pressed(self):
        self.tarjetas.setCurrentIndex(3)

if __name__ == "__main__":
    # creamos un objeto de instancia qapplication
    aplicacion = QApplication(sys.argv)  # sys.argv -> unimos la aplicacion con el sistema operativo
    # creamos un objeto de la ventana
    ventana = VentanaPrincipal()
    # ejecutamos la union?
    aplicacion.exec()