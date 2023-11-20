import sys

# importamos del pyqt6 los elementos que nos importa -> ventana principal, boton
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt, QAbstractListModel

# creamos clase que hereda de QMainWindow

class TareasModelo(QAbstractListModel):

    def __init__(self, tareas=None):
        super().__init__()
        self.tareas= tareas or []

    def data(self,index,role):
        if role==Qt.ItemDataRole.DisplayRole:
            estado, texto=self.tareas[index.row()]
            return texto

    def rowCount(self,indice):
        return len(self.tareas)

class VentanaPrincipal (QMainWindow):
    # iniciamos a ventana
    def __init__(self):

        # Llamamos al constructor de la superclase
        super().__init__()

        self.setWindowTitle( "QListView")
        self.setFixedSize(400,300)

        listaTareas=[(False,'Una tarea'),(False,'Segunda tarea')]
        self.modelo=TareasModelo(listaTareas)

        # Creacion de una caja vertical (principal)
        caixaV= QVBoxLayout()

        lista=QListView()
        lista.setModel(self.modelo)
        caixaV.addWidget(lista)

        # Creacion de una segunda caja horizontal
        caixaH2 = QHBoxLayout()
        caixaV.addLayout(caixaH2)

        btnCerrar = QPushButton("Cerrar")
        caixaH2.addWidget(btnCerrar)

        btnHecho = QPushButton("Hecho")
        caixaH2.addWidget(btnHecho)

        # Creacion de la caja de texto y el boton
        self.txtCampo = QLineEdit()
        self.txtCampo.editingFinished.connect(self.on_btnAgregar_pressed)
        caixaV.addWidget(self.txtCampo)

        btnAgregar = QPushButton("Añadir tarea")
        btnAgregar.pressed.connect(self.on_btnAgregar_pressed)
        caixaV.addWidget(btnAgregar)

        container= QWidget()
        container.setLayout(caixaV)

        # Asignamos la caja vertical a la ventana y la mostramos
        self.setCentralWidget(container)
        self.show()

    def on_btnAgregar_pressed(self):
        texto=self.txtCampo.text().strip()
        # Si hay texto, lo añadimos a la lista
        if texto:
            self.modelo.tareas.append((False,texto))
            self.modelo.layoutChanged.emit()
            self.txtCampo.setText("")


# ejecutamos la union?
if __name__=="__main__":
    aplicacion=QApplication(sys.argv)
    ventana=VentanaPrincipal()
    aplicacion.exec()