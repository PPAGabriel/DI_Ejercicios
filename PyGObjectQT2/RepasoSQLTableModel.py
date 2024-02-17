import sys

from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout,
                             QWidget, QHBoxLayout, QTableView, QComboBox, QLabel, QLineEdit, QGridLayout, QCheckBox,
                             QMessageBox)
from PyQt6.QtCore import QSize
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        # Inicializa la clase QMainWindow
        super().__init__()

        # Establece el título de la ventana
        self.setWindowTitle("Repaso QSTableModelView con modelo, con base de datos sql con Qt")

        # Creación de la base de datos
        bd = QSqlDatabase("QSQLITE") # Creación de la base de datos
        bd.setDatabaseName("baseDatos.dat") # Establece el nombre de la base de datos en uso
        bd.open() # Abre la base de datos

        # Creación de la caja vertical
        cajaV= QVBoxLayout()

        # Creación de la tabla
        self.tabla = QTableView()

        self.modelo = QSqlTableModel(db=bd) # Creación del modelo de la tabla
        self.modelo.setEditStrategy(QSqlTableModel.EditStrategy.OnManualSubmit) # Establece la estrategia de edición del modelo (manual)
        self.modelo.setTable("usuarios")  # Establece la tabla de la base de datos a la que se conectará el modelo
        self.modelo.select()  # Realiza la consulta a la base de datos

        self.tabla.setModel(self.modelo) # Configuración del modelo de la tabla

        # EN CASO DE SELECCIONAR FILA PARA RELLENAR LOS CAMPOS (SOLO PUEDE SELECCIONAR UNA FILA DESDE EL INDICE)
        #self.tabla.selectionModel().selectionChanged.connect(self.on_filaSeleccionada) # Conexión de la señal de selección de fila con el método 'on_filaSeleccionada'

        # GRID 1 (ENTRADAS DEL USUARIO)

        self.grid1 = QGridLayout()

        # DNI
        lblDNI = QLabel("DNI")
        self.grid1.addWidget(lblDNI, 0, 0)
        self.txtDNI = QLineEdit()
        self.grid1.addWidget(self.txtDNI, 0, 1)

        # Nombre
        lblNombre = QLabel("Nombre")
        self.grid1.addWidget(lblNombre, 0, 2)
        self.txtNombre = QLineEdit()
        self.grid1.addWidget(self.txtNombre, 0, 3)

        # Edad
        lblEdad = QLabel("Edad")
        self.grid1.addWidget(lblEdad, 1, 0)
        self.txtEdad = QLineEdit()
        self.grid1.addWidget(self.txtEdad, 1, 1)

        # Genero
        lblGenero = QLabel("Genero")
        self.grid1.addWidget(lblGenero, 1, 2)
        self.cmbGenero = QComboBox()
        self.cmbGenero.addItem("Hombre")
        self.cmbGenero.addItem("Mujer")
        self.cmbGenero.addItem("Otros")
        self.grid1.addWidget(self.cmbGenero, 1, 3)

        # Fallecido
        lblFallecido = QLabel("Fallecido")
        self.grid1.addWidget(lblFallecido, 2, 0)
        self.chckFallecido = QCheckBox()
        self.grid1.addWidget(self.chckFallecido, 2, 1)

        cajaV.addLayout(self.grid1)

        # Boton de Añadir
        self.btnAnadir = QPushButton("Añadir")
        self.btnAnadir.clicked.connect(self.on_btnAnadir_clicked)
        cajaV.addWidget(self.btnAnadir)

        # Boton de Eliminar
        self.btnEliminar = QPushButton("Eliminar")
        self.btnEliminar.clicked.connect(self.on_btnEliminar_clicked)
        cajaV.addWidget(self.btnEliminar)

        # Creación de la caja horizontal
        cajaH = QHBoxLayout()

        # Creación de los botones
        btnAceptar = QPushButton("Aceptar")
        btnCancelar = QPushButton("Cancelar")

        # Añadir los botones a la caja horizontal
        cajaH.addWidget(btnAceptar)
        cajaH.addWidget(btnCancelar)
        btnAceptar.clicked.connect(self.on_btnAceptar_clicked)
        btnCancelar.clicked.connect(self.on_btnCancelar_clicked)

        cajaV.addWidget(self.tabla) # Añadir la tabla a la caja vertical
        cajaV.addLayout(cajaH) # Añadir la caja horizontal a la caja vertical

        # Contenedor principal
        container = QWidget()
        container.setLayout(cajaV)
        self.setCentralWidget(container)

        # Configuración del tamaño minimo de la ventana y visualización
        self.setMinimumSize(QSize(530, 300))
        self.show()


    #Método que se ejecuta al seleccionar una fila (LIMITADO A SELECCIONAR SÓLO UNA FILA DESDE EL ÍNDICE)

    '''
     def on_filaSeleccionada(self):
        indices = self.tabla.selectedIndexes() # Se obtienen los índices de la fila seleccionada
        if indices!=[]:
            self.txtDNI.setText(indices[0].data())
            self.txtNombre.setText(indices[1].data())
            self.txtEdad.setText(str(indices[2].data())) #Se convierte a string para que se muestre en el campo de texto
            self.cmbGenero.setCurrentText(indices[3].data())
            self.chckFallecido.setChecked(bool(indices[4].data())) #Se convierte a booleano para que se muestre en el campo de texto
    
    '''
   #Metodos de botones
    def on_btnAceptar_clicked(self):
        self.modelo.submitAll() # Realiza los cambios en la base de datos
        print("Cambios realizados en la BD") # Mensaje de depuración

    def on_btnCancelar_clicked(self):
        self.modelo.revertAll() # Cancela los cambios realizados en la base de datos
        print("Cambios cancelados") # Mensaje de depuración

    def on_btnAnadir_clicked(self):
        if self.chckFallecido.isChecked():
            fallecido = 1
        else:
            fallecido = 0

        if self.txtDNI.text()=="" or self.txtNombre.text()=="" or self.txtEdad.text()=="":
            self.warning = QMessageBox.warning(self, "Error", "Faltan datos por rellenar",
                                               QMessageBox.StandardButton.Ok)
        else:
            row = self.modelo.rowCount()
            self.modelo.insertRow(row)

            self.modelo.setData(self.modelo.index(row, 0), self.txtDNI.text())
            self.modelo.setData(self.modelo.index(row, 1), self.txtNombre.text())
            self.modelo.setData(self.modelo.index(row, 2), self.txtEdad.text())
            self.modelo.setData(self.modelo.index(row, 3), self.cmbGenero.currentText())
            self.modelo.setData(self.modelo.index(row, 4),fallecido)

            print("Fila añadida (recuerde darle al boton 'ACEPTAR' para guardar los cambios)")

            self.txtNombre.setText("")
            self.txtDNI.setText("")
            self.txtEdad.setText("")

    def on_btnEliminar_clicked(self):
        indice= self.tabla.currentIndex()
        print(f"Fila a eliminar: {indice.row()}")
        if indice.isValid():
            self.modelo.removeRow(indice.row())
            print("Fila eliminada (recuerde darle al boton 'ACEPTAR' para guardar los cambios)")


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    aplicacion.exec()