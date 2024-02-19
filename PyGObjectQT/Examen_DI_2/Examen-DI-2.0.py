import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtSql import QSqlTableModel, QSqlDatabase
from PyQt6.QtWidgets import (QApplication, QMainWindow, QGridLayout, QVBoxLayout, QHBoxLayout, QWidget,
                             QLabel, QListWidget, QPushButton, QComboBox, QLineEdit,
                             QRadioButton, QGroupBox, QTableView, QMessageBox)


class FiestraPrincipal (QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exame 19-02-2024")

        # Creación da base de datos
        bd = QSqlDatabase("QSQLITE")  # Creación da base de datos
        bd.setDatabaseName("modelosClasicos.dat")
        bd.open()

        #CAJA VERTICAL
        cajaV = QVBoxLayout()

        #SECCION CLIENTE
        gpbCliente = QGroupBox("Cliente")
        cajaV.addWidget(gpbCliente)

        #GRID DENTRO DE LA SECCION CLIENTE
        self.gridCliente = QGridLayout()

        #Nro Cliente
        lblNumeroCliente = QLabel("Número Cliente")
        self.gridCliente.addWidget(lblNumeroCliente, 0, 0)
        self.txtNumeroCliente = QLineEdit()
        self.txtNumeroCliente.setPlaceholderText("4")
        self.gridCliente.addWidget(self.txtNumeroCliente, 0, 1)

        #Nome
        lblNomeCliente = QLabel("Nome")
        self.gridCliente.addWidget(lblNomeCliente, 0, 2)
        self.txtNomeCliente = QLineEdit()
        self.txtNomeCliente.setPlaceholderText("Gabriel")
        self.gridCliente.addWidget(self.txtNomeCliente, 0, 3)

        #Apelidos
        lblApelidosCliente = QLabel("Apelidos")
        self.gridCliente.addWidget(lblApelidosCliente, 2, 0)
        self.txtApelidosCliente = QLineEdit()
        self.txtApelidosCliente.setPlaceholderText("Perez")
        self.gridCliente.addWidget(self.txtApelidosCliente, 2, 1, 1, 3)

        #Dirección
        lblDireccion = QLabel("Dirección")
        self.gridCliente.addWidget(lblDireccion, 3, 0)
        self.txtDireccion = QLineEdit()
        self.txtDireccion.setPlaceholderText("Calle Garcia Barbon, 67, 2A")
        self.gridCliente.addWidget(self.txtDireccion, 3, 1, 1, 3)

        #Cidade
        lblCidade = QLabel("Cidade")
        self.gridCliente.addWidget(lblCidade, 4, 0)
        self.txtCidade = QLineEdit()
        self.txtCidade.setPlaceholderText("Vigo")
        self.gridCliente.addWidget(self.txtCidade, 4, 1)

        #Provincia
        lblProvinciaEstado = QLabel("Provincia")
        self.gridCliente.addWidget(lblProvinciaEstado, 4, 2)
        self.txtProvinciaEstado = QLineEdit()
        self.txtProvinciaEstado.setPlaceholderText("Pontevedra")
        self.gridCliente.addWidget(self.txtProvinciaEstado, 4, 3)

        #Codigo Postal
        lblCodigoPostal = QLabel("Código Postal")
        self.gridCliente.addWidget(lblCodigoPostal, 5, 0)
        self.txtCodigoPostal = QLineEdit()
        self.txtCodigoPostal.setPlaceholderText("36201")
        self.gridCliente.addWidget(self.txtCodigoPostal, 5, 1)

        #Telefono
        lblTelefono = QLabel("Teléfono")
        self.gridCliente.addWidget(lblTelefono, 5, 2)
        self.txtTelefono = QLineEdit()
        self.txtTelefono.setPlaceholderText("986123456")
        self.gridCliente.addWidget(self.txtTelefono, 5, 3)

        gpbCliente.setLayout(self.gridCliente)

        #SECCION TABLA Y BOTONES
        cajaV_H1 = QHBoxLayout()

        #Tabla:
        self.tvwClientes = QTableView()

        self.modelo = QSqlTableModel(db=bd)  # Creación del modelo de la tabla
        self.modelo.setEditStrategy(
            QSqlTableModel.EditStrategy.OnManualSubmit)  # Establece la estrategia de edición del modelo (manual)
        self.modelo.setTable("clientes")  # Establece la tabla de la base de datos a la que se conectará el modelo
        self.modelo.select()  # Realiza la consulta a la base de datos
        self.tvwClientes.setModel(self.modelo)  # Configuración del modelo de la tabla

        # Para que solo se pueda seleccionar una fila (de mantener el raton pulsado)
        self.tvwClientes.setSelectionMode(QTableView.SelectionMode.SingleSelection)

        # Para que seleccione todas las columnas de la fila seleccionada
        self.tvwClientes.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)

        cajaV_H1.addWidget(self.tvwClientes)

        #Caja Secundaria Vertical:
        cajaV_H1_V1 = QVBoxLayout()

        #Boton Engadir
        self.btnEngadir = QPushButton("Engadir")
        # Conexión de los botones
        self.btnEngadir.clicked.connect(self.on_btnEngadir_clicked)
        cajaV_H1_V1.addWidget(self.btnEngadir)

        # Boton Editar
        self.btnEditar = QPushButton("Editar")
        cajaV_H1_V1.addWidget(self.btnEditar)

        #Boton Borrar
        self.btnBorrar = QPushButton("Borrar")
        cajaV_H1_V1.addWidget(self.btnBorrar)

        cajaV_H1_V1.setAlignment(Qt.AlignmentFlag.AlignTop)
        cajaV_H1.addLayout(cajaV_H1_V1)

        cajaV.addLayout(cajaV_H1)

        #SECCION ACEPTAR Y CANCELAR
        cajaH2 = QHBoxLayout()

        #Boton Cancelar
        self.btnCancelar = QPushButton("Cancelar")
        cajaH2.addWidget(self.btnCancelar)

        #Boton Aceptar
        self.btnAceptar = QPushButton("Aceptar")
        cajaH2.addWidget(self.btnAceptar)

        cajaH2.setAlignment(Qt.AlignmentFlag.AlignRight)

        cajaV.addLayout(cajaH2)


        # CONTENEDOR PRINCIPAL

        container = QWidget()
        container.setLayout(cajaV)
        self.setCentralWidget(container)

        self.setFixedSize(500, 500)
        self.show()

    #METODO ENGADIR

    def on_btnEngadir_clicked(self):
        if (self.txtNumeroCliente.text()=="" or
            self.txtNomeCliente.text()=="" or
            self.txtApelidosCliente.text()=="" or
            self.txtDireccion.text()=="" or
            self.txtCidade.text()=="" or
            self.txtProvinciaEstado.text()=="" or
            self.txtCodigoPostal.text()=="" or
            self.txtTelefono.text()==""):
            self.warning = QMessageBox.warning(self, "Error", "Faltan datos por rellenar",
                                               QMessageBox.StandardButton.Ok)
        else:
            row = self.modelo.rowCount()
            self.modelo.insertRow(row)

            self.modelo.setData(self.modelo.index(row, 0), self.txtNumeroCliente.text())
            self.modelo.setData(self.modelo.index(row, 1), self.txtNomeCliente.text())
            self.modelo.setData(self.modelo.index(row, 2), self.txtApelidosCliente.text())
            self.modelo.setData(self.modelo.index(row, 3), self.txtTelefono.text())
            self.modelo.setData(self.modelo.index(row, 4), self.txtDireccion.text())
            self.modelo.setData(self.modelo.index(row, 5), self.txtCidade.text())
            self.modelo.setData(self.modelo.index(row, 6), self.txtProvinciaEstado.text())
            self.modelo.setData(self.modelo.index(row, 7), self.txtCodigoPostal.text())




            self.modelo.submitAll()

            self.warning = QMessageBox.information(self, "Aviso", "Engadido correctamente! :D",
                                                   QMessageBox.StandardButton.Ok)


'''
    MEDIDAS PARA MEJORAR LA USABILIDAD DE LA APLICACIÓN:
    1. Añadir un mensaje de confirmación al pulsar el botón "Borrar" para evitar borrados accidentales.
    2. En los placeholders de los campos de texto, añadir un texto que indique qué tipo de dato se espera en cada campo, dando un posible ejemplo del mismo.
    3. Control de errores en las entradas de datos, por ejemplo, que el tipo de dato en los campos de entrada de datos coincidan con los que requiere la BD.
    4. Al añadir un nuevo cliente, que los campos de texto se limpien automáticamente, y se indique por pantalla al usuario previo a la acción, que fue añadido satisfactoriamente.
    5. Mejorar la interfaz gráfica, añadiendo colores, imágenes, etc.

'''


if __name__=="__main__":

    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()

    aplicacion.exec()