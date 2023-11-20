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

        self.setWindowTitle( "Mi primera ventana con Qt")
        self.setFixedSize(400,400)

        self.txtSaludo=QLineEdit()
        self.txtSaludo.editingFinished.connect(self.on_btn_clicked)


        # creamos lo que quereamos poner en la ventana:
        self.lblEtiqueta = QLabel ("Hola :)")
        fuente=self.lblEtiqueta.font()
        fuente.setPointSize(30)
        self.lblEtiqueta.setFont(fuente)
        btnSaludo=QPushButton("Pincha aquí")
        btnSaludo.clicked.connect(self.on_btn_clicked)

        # usamos una box para añadir varias cosas
        caixaV=QVBoxLayout()
        caixaV.addWidget(self.lblEtiqueta)
        caixaV.addWidget(self.txtSaludo)
        caixaV.addWidget(btnSaludo)

        container= QWidget()
        container.setLayout(caixaV)

        # lo pone en el centro (solo verticalmente) -> solo podemos usar 1
       # self.setCentralWidget(lblEtiqueta)
        self.setCentralWidget(container)

        # mostramos la ventana
        self.show() # para que se vea a pantalla

    def on_btn_clicked(self):
        if len(self.txtSaludo.text())==0:
            self.lblEtiqueta.setText(self.txtSaludo.text())
        else:
            saludo=self.txtSaludo.text()
            self.lblEtiqueta.setText(saludo)


# ejecutamos la union?
if __name__=="__main__":
    aplicacion=QApplication(sys.argv)
    ventana=VentanaPrincipal()
    aplicacion.exec()