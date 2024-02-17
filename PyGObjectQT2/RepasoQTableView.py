import sys

from PyQt6 import QtGui
from PyQt6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QComboBox,
                             QWidget, QCheckBox, QHBoxLayout, QLineEdit, QTableView, QPushButton)
from PyQt6.QtCore import Qt, QAbstractTableModel, QModelIndex


class ModeloTabla(QAbstractTableModel):
    def __init__(self, tabla,cabecera):
        super().__init__()
        self.tabla = tabla # Se almacena la tabla en un atributo de la clase
        self.cabecera=cabecera # Se almacena la cabecera en un atributo de la clase

    # Métodos abstractos que deben implementarse
    def rowCount(self, indice): # Devuelve el número de filas de la tabla
        return len(self.tabla)

    def columnCount(self, indice): # Devuelve el número de columnas de la tabla
        return len(self.tabla[0])

    def data(self, indice, rol): # Devuelve el dato que se encuentra en el índice de la tabla
        if indice.isValid(): # Si el índice es válido
            # Si el rol es de edición o visualización de datos de la tabla
            if rol == Qt.ItemDataRole.EditRole or rol == Qt.ItemDataRole.DisplayRole:
                valor = self.tabla[indice.row()][indice.column()]
                return valor

        #Hacer que el contenido de la fila tenga un color "Rojo" si el usuario está fallecido
        if rol == Qt.ItemDataRole.ForegroundRole:
            if self.tabla[indice.row()][3]==True:
                return QtGui.QColor(Qt.GlobalColor.red)

        #Hacer que el fondo de la fila tenga un color "Verde" si el usuario es "Hombre", "Magenta" si el usuario es "Mujer" y "Amarillo" si el usuario es "Otros"
        if rol==Qt.ItemDataRole.BackgroundRole:
            if self.tabla[indice.row()][2]=="Hombre":
                return QtGui.QColor("green")
            elif self.tabla[indice.row()][2]=="Mujer":
                return QtGui.QColor("magenta")
            elif self.tabla[indice.row()][2]=="Otros":
                return QtGui.QColor("yellow")

        #Hacer que el contenido de la fila tenga un icono de "check.png" si el usuario está fallecido y un icono de "uncheck.png" si el usuario no está fallecido
        if rol==Qt.ItemDataRole.DecorationRole:
            if isinstance(self.tabla[indice.row()][indice.column()],bool):
                if self.tabla[indice.row()][indice.column()]==True:
                    return QtGui.QIcon("check.png")
                else:
                    return QtGui.QIcon("uncheck.png")


    def setData(self, index, value, role): # Establece el dato en el índice de la tabla
        if role == Qt.ItemDataRole.EditRole: # Si el rol es de edición de datos de la tabla
            self.tabla[index.row()][index.column()] = value # Se establece el valor en la tabla
            return True
        return False

    def flags(self, index): # Devuelve los flags de edición de la tabla
        return Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsEditable | Qt.ItemFlag.ItemIsSelectable # Se devuelven los flags de edición de la tabla

    def headerData(self, section, orientation, role): #Establece la cabecera de la tabla
        if role == Qt.ItemDataRole.DisplayRole and orientation == Qt.Orientation.Horizontal:
            return self.cabecera[section]
        return None

    def removeRow(self, row, parent=QModelIndex()):
        self.beginRemoveRows(parent, row, row)
        del self.tabla[row]
        self.endRemoveRows()
        return True

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        # Inicializa la clase base QMainWindow
        super().__init__()

        #Establece el título de la ventana
        self.setWindowTitle("Repaso de QTableView con modelo y sin Base de Datos con Qt")

        #Datos de la tabla
        self.datos = [
            ["Ana Pérez", "12345678Y", "Mujer", True],
            ["Luis González", "87654321K", "Hombre", False],
            ["María Sánchez", "87654891H", "Mujer", False],
            ["Jorge Ruíz", "32754981U", "Otros", True],
        ]
        #Cabecera de la tabla
        self.cabecera = [
            "Nombre", "DNI", "Genero", "Fallecido"
        ]

        #Creación de la caja vertical
        cajaV= QVBoxLayout()

        self.tabla= QTableView() # Creación de la vista de la tabla
        modelo = ModeloTabla(self.datos, self.cabecera) # Creación del modelo de datos de la tabla
        self.tabla.setModel(modelo) # Configuración del modelo de datos de la tabla

        self.seleccion= self.tabla.selectionModel() # Selección de la fila
        self.seleccion.selectionChanged.connect(self.on_filaSeleccionada) # Conexión de la señal de selección de fila con el método 'on_filaSeleccionada'

        #Para que solo se pueda seleccionar una fila (de mantener el raton pulsado)
        self.tabla.setSelectionMode(QTableView.SelectionMode.SingleSelection)

        #Para que seleccione todas las columnas de la fila seleccionada
        self.tabla.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)

        cajaV.addWidget(self.tabla) # Añadir la tabla a la caja vertical

        #Creación de la caja horizontal (contenedor secundario)
        cajaH= QHBoxLayout()

        self.txtNombre=QLineEdit("Nombre") # Creación de la caja de texto para el nombre
        cajaH.addWidget(self.txtNombre)
        self.txtDni=QLineEdit("DNI") # Creación de la caja de texto para el DNI
        cajaH.addWidget(self.txtDni)
        self.cmbGenero=QComboBox() # Creación del combo box para el género
        self.cmbGenero.addItems(('Hombre', 'Mujer', 'Otros'))
        cajaH.addWidget(self.cmbGenero)
        self.chkFallecido=QCheckBox('Fallecido') # Creación del check box para saber su estado vital
        cajaH.addWidget(self.chkFallecido)
        self.btnEliminar= QPushButton("Eliminar")
        self.btnEliminar.clicked.connect(self.eliminarFila)
        cajaH.addWidget(self.btnEliminar)

        cajaV.addLayout(cajaH) # Añadir la caja horizontal a la caja principal

        # Contenedor principal
        container = QWidget()
        container.setLayout(cajaV)
        self.setCentralWidget(container)

        #No seleccionar ninguna fila al iniciar la aplicación
        self.tabla.selectRow(-1)

        # Configuración del tamaño fijo de la ventana y visualización
        self.setFixedSize(400, 400)
        self.show()


    #Método que se ejecuta al seleccionar una fila
    def on_filaSeleccionada(self):
        indices= self.tabla.selectedIndexes() # Se obtienen los índices de la fila seleccionada
        if indices!=[]:
            self.txtNombre.setText(indices[0].data()) # Se establece el nombre en la caja de texto del nombre
            self.txtDni.setText(indices[1].data()) # Se establece el DNI en la caja de texto del DNI
            self.cmbGenero.setCurrentText(indices[2].data()) # Se establece el género en el combo box del género
            self.chkFallecido.setChecked(indices[3].data()) # Se establece el estado vital en el check box del estado vital

    #Metodo que elimina la fila seleccionada
    def eliminarFila(self):
        indice= self.tabla.currentIndex() # Se obtienen los índices de la fila seleccionada
        print(indice.row())
        if indice.isValid():
            self.tabla.model().removeRow(indice.row()) # Se elimina la fila seleccionada
            print("Fila eliminada")


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    aplicacion.exec()