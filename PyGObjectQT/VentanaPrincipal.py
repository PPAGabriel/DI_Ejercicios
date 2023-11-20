import sys

# importamos del pyqt6 los elementos que nos importa -> ventana principal, boton
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap

# creamos clase que heread de QMainWindow
class VentanaPrincipal (QMainWindow):
    # iniciamos a ventana
    def __init__(self):
        # llamamos al constructor de la superclase
        super().__init__()

        self.setWindowTitle( "Mi primera ventana con Qt")
        self.setFixedSize(400,400)

        # creamos lo que quereamos poner en la ventana:
        lblEtiqueta = QLabel ("Hola!")
        self.lblEtiqueta2= QLabel("Un hermoso paisaje")
        btnSaludo=QPushButton("Pincha aquí")
        btnSaludo.clicked.connect(self.on_btn_clicked)

        # solo se puede poner imagenes jpg?
        lblEtiqueta.setPixmap(QPixmap("paisaje.png"))

        # usamos una box para añadir varias cosas
        caixaV=QVBoxLayout()
        caixaV.addWidget(lblEtiqueta)
        caixaV.addWidget(self.lblEtiqueta2)
        caixaV.addWidget(btnSaludo)

        container= QWidget()
        container.setLayout(caixaV)

        # lo pone en el centro (solo verticalmente) -> solo podemos usar 1
       # self.setCentralWidget(lblEtiqueta)
        self.setCentralWidget(container)


        # mostramos la ventana
        self.show() # para que se vea a pantalla


    def on_btn_clicked(self):
        self.lblEtiqueta2.setText("No toques ahi!")

# ejecutamos la union?
if __name__=="__main__":
    aplicacion=QApplication(sys.argv)
    ventana=VentanaPrincipal()
    aplicacion.exec()