import sys

from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout,
                             QWidget, QHBoxLayout, QTableView)
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
        self.setMinimumSize(QSize(500, 300))
        self.show()


    #Métodos para los botones
    def on_btnAceptar_clicked(self):
        self.modelo.submitAll() # Realiza los cambios en la base de datos
        print("Cambios realizados en la BD") # Mensaje de depuración

    def on_btnCancelar_clicked(self):
        self.modelo.revertAll() # Cancela los cambios realizados en la base de datos
        print("Cambios cancelados") # Mensaje de depuración


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    aplicacion.exec()