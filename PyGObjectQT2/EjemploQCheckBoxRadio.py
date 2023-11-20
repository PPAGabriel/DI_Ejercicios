import sys

# importamos del pyqt6 los elementos que nos importa -> ventana principal, boton
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt

# creamos clase que heread de QMainWindow
class VentanaPrincipal (QMainWindow):
    # iniciamos a ventana
    def __init__(self):
        # llamamos al constructor de la superclase
        super().__init__()

        self.setWindowTitle( "Ejemplo con QCheckBox y QRadioButton")

        caixaV= QVBoxLayout()

        self.chkBoton1=QCheckBox("Boton 1")
        self.chkBoton1.toggled.connect(self.on_chkBoton1_toggled)
        caixaV.addWidget(self.chkBoton1)

        self.chkBoton2 = QCheckBox("Boton 2")
        self.chkBoton2.toggled.connect(self.on_chkBoton2_toggled)
        caixaV.addWidget(self.chkBoton2)

        #Creacion de una segunda caja vertical
        caixaV2=QVBoxLayout()
        containerV2=QWidget()
        containerV2.setLayout(caixaV2)
        caixaV.addWidget(containerV2)

        self.rbtRadioButton1=QRadioButton("Opción 1",containerV2)
        self.rbtRadioButton1.toggled.connect(self.on_rbtradioButton1_toggled)
        caixaV2.addWidget(self.rbtRadioButton1)

        self.rbtRadioButton2 = QRadioButton("Opción 2",containerV2)
        self.rbtRadioButton2.toggled.connect(self.on_rbtradioButton2_toggled)
        caixaV2.addWidget(self.rbtRadioButton2)

        self.rbtRadioButton3 = QRadioButton("Opción 3",containerV2)
        self.rbtRadioButton3.toggled.connect(self.on_rbtradioButton3_toggled)
        caixaV2.addWidget(self.rbtRadioButton3)

        #Creacion de una tercera caja vertical
        caixaV3=QVBoxLayout()
        caixaV.addLayout(caixaV3)

        self.rbtRadioButton4=QRadioButton("Opción 1 Grupo 2")
        self.rbtRadioButton4.toggled.connect(self.on_rbtradioButton4_toggled)
        caixaV3.addWidget(self.rbtRadioButton4)

        self.rbtRadioButton5 = QRadioButton("Opción 2 Grupo 2")
        self.rbtRadioButton5.toggled.connect(self.on_rbtradioButton5_toggled)
        caixaV3.addWidget(self.rbtRadioButton5)

        self.rbtRadioButton6 = QRadioButton("Opción 3 Grupo 2")
        self.rbtRadioButton6.toggled.connect(self.on_rbtradioButton6_toggled)
        caixaV3.addWidget(self.rbtRadioButton6)

        container= QWidget()
        container.setLayout(caixaV)
        self.setCentralWidget(container)

        self.setFixedSize(400,300)
        self.show() # para que se vea a pantalla

    def on_chkBoton1_toggled(self):
        if self.chkBoton1.isChecked():
            print("Boton check seleccionado:",self.chkBoton1.text())
        else:
            print("Boton check deseleccionado:",self.chkBoton1.text())

    def on_chkBoton2_toggled(self):
        if self.chkBoton2.isChecked():
            print("Boton check seleccionado:",self.chkBoton2.text())
        else:
            print("Boton check deseleccionado:",self.chkBoton2.text())


    def on_rbtradioButton1_toggled(self):
        if self.rbtRadioButton1.isChecked():
            print("Boton radio seleccionado:",self.rbtRadioButton1.text())
        else:
            print("Boton radio deseleccionado:",self.rbtRadioButton1.text())

    def on_rbtradioButton2_toggled(self):
        if self.rbtRadioButton2.isChecked():
            print("Boton radio seleccionado:",self.rbtRadioButton2.text())
        else:
            print("Boton radio deseleccionado:",self.rbtRadioButton2.text())

    def on_rbtradioButton3_toggled(self):
        if self.rbtRadioButton3.isChecked():
            print("Boton radio seleccionado:",self.rbtRadioButton3.text())
        else:
            print("Boton radio deseleccionado:",self.rbtRadioButton3.text())

    def on_rbtradioButton4_toggled(self):
        if self.rbtRadioButton4.isChecked():
            print("Boton radio seleccionado:",self.rbtRadioButton4.text())
        else:
            print("Boton radio deseleccionado:",self.rbtRadioButton4.text())

    def on_rbtradioButton5_toggled(self):
        if self.rbtRadioButton5.isChecked():
            print("Boton radio seleccionado:",self.rbtRadioButton5.text())
        else:
            print("Boton radio deseleccionado:",self.rbtRadioButton5.text())

    def on_rbtradioButton6_toggled(self):
        if self.rbtRadioButton6.isChecked():
            print("Boton radio seleccionado:",self.rbtRadioButton6.text())
        else:
            print("Boton radio deseleccionado:",self.rbtRadioButton6.text())


# ejecutamos la union?
if __name__=="__main__":
    aplicacion=QApplication(sys.argv)
    ventana=VentanaPrincipal()
    aplicacion.exec()