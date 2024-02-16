import sys

from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QComboBox,
                             QWidget, QCheckBox, QHBoxLayout, QLineEdit, QTableView)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        # Inicializa la clase base QMainWindow
        super().__init__()
        self.setWindowTitle("Ejemplo QSTableModelView con modelo, con base de datos sql con Qt")

        bd = QSqlDatabase("QSQLITE")
        bd.setDatabaseName("baseDatos.dat")
        bd.open()



        cajaV= QVBoxLayout()

        self.tabla = QTableView()
        self.modelo = QSqlTableModel(db=bd)
        # self.modelo.setEditStrategy(QSqlTableModel.EditStrategy.OnFieldChange)
        # self.modelo.setEditStrategy(QSqlTableModel.EditStrategy.OnRowChange)
        self.modelo.setEditStrategy(QSqlTableModel.EditStrategy.OnManualSubmit)

        self.tabla.setModel(self.modelo)

        self.modelo.setTable("usuarios")
        self.modelo.select()


        cajaH = QHBoxLayout()
        btnAceptar = QPushButton("Aceptar")
        btnCancelar = QPushButton("Cancelar")
        cajaH.addWidget(btnAceptar)
        cajaH.addWidget(btnCancelar)
        btnAceptar.clicked.connect (self.on_btnAceptar_clicked)
        btnCancelar.clicked.connect (self.on_btnCancelar_clicked)


        cajaV.addWidget(self.tabla)
        cajaV.addLayout(cajaH)

        contenedor = QWidget()
        contenedor.setLayout(cajaV)
        self.setCentralWidget(contenedor)
        self.setMinimumSize(QSize(500, 300))
        self.show()

    def on_btnAceptar_clicked(self):
        self.modelo.submitAll()
        print("Aceptar")
    def on_btnCancelar_clicked(self):
        self.modelo.revertAll()
        print("Cancelar")


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    aplicacion.exec()