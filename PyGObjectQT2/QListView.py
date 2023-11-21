import sys

from PyQt6.QtGui import QColor, QIcon
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
            _, texto=self.tareas[index.row()]
            return texto
        elif role == Qt.ItemDataRole.DecorationRole:
            estado, _ = self.tareas[index.row()]
            if estado:
                return QIcon("check.png")
            else:
                return QIcon("uncheck.png")

    ''' EN CASO DE QUERER PONER EL COLOR DE FONDO
            if role==Qt.ItemDataRole.BackgroundRole:
            estado, texto=self.tareas[index.row()]
            if estado:
                return QColor("green")
            else:
                return QColor("transparent")
    '''


    def rowCount(self,indice):
        return len(self.tareas)

class VentanaPrincipal(QMainWindow):
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

        self.lista=QListView()
        self.lista.setModel(self.modelo)
        self.lista.setSelectionMode(QListView.SelectionMode.MultiSelection)
        caixaV.addWidget(self.lista)

        # Creacion de una segunda caja horizontal
        caixaH2 = QHBoxLayout()
        caixaV.addLayout(caixaH2)

        btnBorrar = QPushButton("Borrar")
        btnBorrar.pressed.connect(self.on_btnBorrar_pressed)
        caixaH2.addWidget(btnBorrar)

        btnHecho = QPushButton("Hecho")
        btnHecho.pressed.connect(self.on_btnHecho_pressed)
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

    # Funcion que se ejecuta al pulsar el boton y añade una tarea a la lista
    def on_btnAgregar_pressed(self):
        texto=self.txtCampo.text().strip()
        # Si hay texto, lo añadimos a la lista
        if texto:
            self.modelo.tareas.append((False,texto))
            self.modelo.layoutChanged.emit()
            self.txtCampo.setText("")

    # Funcion que se ejecuta al pulsar el boton y borra una tarea de la lista
    def on_btnBorrar_pressed(self):
        # Obtenemos la lista de tareas seleccionadas
        seleccionadas=self.lista.selectedIndexes()
        # Si hay tareas seleccionadas, las borramos

        ''' EN CASO DE SER SOLO UNA SELECCIÓN
                if seleccionadas:
                  del self.modelo.tareas[seleccionadas[0].row()]
                self.modelo.layoutChanged.emit()
                self.lista.clearSelection()
            '''

        if seleccionadas:
            for indice in sorted(seleccionadas, reverse=True):
                del self.modelo.tareas[indice.row()]
            self.modelo.layoutChanged.emit()
            self.lista.clearSelection()

    # Funcion que se ejecuta al pulsar el boton y marca una tarea como hecha
    def on_btnHecho_pressed(self):
        # Obtenemos la lista de tareas seleccionadas
        seleccionadas=self.lista.selectedIndexes()
        # Si hay tareas seleccionadas, las borramos

        ''' EN CASO DE SER SOLO UNA SELECCIÓN
                if seleccionadas:
                  del self.modelo.tareas[seleccionadas[0].row()]
                self.modelo.layoutChanged.emit()
                self.lista.clearSelection()
            '''

        if seleccionadas:
            for indice in sorted(seleccionadas, reverse=True):
                estado, texto=self.modelo.tareas[indice.row()]

                self.modelo.tareas[indice.row()]=(not estado, texto)

            self.modelo.layoutChanged.emit()
            self.lista.clearSelection()

# ejecutamos la union?
if __name__=="__main__":
    aplicacion=QApplication(sys.argv)
    ventana=VentanaPrincipal()
    aplicacion.exec()