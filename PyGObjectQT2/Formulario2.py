import sys

from PyQt6.QtGui import QColor, QIcon, QPixmap
# importamos del pyqt6 los elementos que nos importa -> ventana principal, boton
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt, QAbstractListModel

class PersonasModelo(QAbstractListModel):

        def __init__(self, personas=None):
            super().__init__()
            self.personas= personas or []

        def data(self,index,role):
            if role==Qt.ItemDataRole.DisplayRole:
                nome, _, _, _= self.personas[index.row()]
                _, apelido, _, _ = self.personas[index.row()]
                _, _, telefono, _ = self.personas[index.row()]
                _, _, _, formato = self.personas[index.row()]
                return nome + " | " + apelido + " | " + telefono + " | " + formato

        def rowCount(self,indice):
            return len(self.personas)
class VentanaPrincipal(QMainWindow):
    # iniciamos la ventana
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Examen 12-12-_2022")

        listaPersonas=[("Juan","Perez","123456789","PDF"),("Ana","Garcia","987654321","XML")]
        self.modelo=PersonasModelo(listaPersonas)

        caixaV = QVBoxLayout()

        #GRID 1 (ENTRADAS DEL USUARIO)

        self.grid1=QGridLayout()

        #Nombre
        lblNome=QLabel("Nome")
        self.grid1.addWidget(lblNome,0,0)
        self.txtNome=QLineEdit()
        self.grid1.addWidget(self.txtNome,0,1)

        #Apellido
        lblApelido=QLabel("Apelido")
        self.grid1.addWidget(lblApelido,0,2)
        self.txtApelido=QLineEdit()
        self.grid1.addWidget(self.txtApelido,0,3)

        #Tratamiento
        lblTratamento=QLabel("Tratamento")
        self.grid1.addWidget(lblTratamento,1,0)
        self.txtTratamento=QLineEdit()
        self.grid1.addWidget(self.txtTratamento,1,1)

        #Telefono
        lblTelefono=QLabel("Telefono")
        self.grid1.addWidget(lblTelefono,1,2)
        self.txtTelefono=QLineEdit()
        self.grid1.addWidget(self.txtTelefono,1,3)

        #Formato
        lblFormato=QLabel("Formato")
        self.grid1.addWidget(lblFormato,2,0)
        self.txtFormato=QComboBox()
        self.txtFormato.addItem("PDF")
        self.txtFormato.addItem("XML")
        self.grid1.addWidget(self.txtFormato,2,1,1,3)

        caixaV.addLayout(self.grid1)

        #CAJA HORIZONTAL 2 (QlistView y  QCheckBox)

        caixaH2=QHBoxLayout()

        #QListView
        caixaH2_V1=QVBoxLayout()

        self.lista = QListView()
        self.lista.setModel(self.modelo)
        self.lista.setSelectionMode(QListView.SelectionMode.SingleSelection)
        self.lista.setFixedSize(360, 200)
        caixaH2_V1.addWidget(self.lista)

        caixaH2_V1_H1=QHBoxLayout()
        lblEmail = QLabel("Dirección de correo electrónico")
        caixaH2_V1_H1.addWidget(lblEmail)
        self.txtEmail = QLineEdit()
        caixaH2_V1_H1.addWidget(self.txtEmail)

        caixaH2_V1_H2=QHBoxLayout()

        self.boton1=QPushButton("Engadir")
        self.boton1.pressed.connect(self.on_btn1_pressed)
        caixaH2_V1_H2.addWidget(self.boton1)

        self.boton2=QPushButton("Editar")
        self.boton2.pressed.connect(self.on_lista_clicked)
        caixaH2_V1_H2.addWidget(self.boton2)

        self.boton3=QPushButton("Borrar")
        caixaH2_V1_H2.addWidget(self.boton3)

        self.boton4=QPushButton("Por defecto")
        caixaH2_V1_H2.addWidget(self.boton4)

        caixaH2_V1.addLayout(caixaH2_V1_H1)
        caixaH2_V1.addLayout(caixaH2_V1_H2)
        caixaH2.addLayout(caixaH2_V1)

        #QCheckButtons (con una etiqueta)
        caixaH2_V2=QVBoxLayout()
        containerV2=QWidget()

        lblFormato = QLabel("Formato de correo")
        caixaH2_V2.addWidget(lblFormato)

        self.chkHTML = QRadioButton("HTML",containerV2)
        self.chkHTML.toggled.connect(self.on_chkHTML_toggled)
        caixaH2_V2.addWidget(self.chkHTML)

        self.chkTextoPlano = QRadioButton("Texto plano", containerV2)
        self.chkTextoPlano.toggled.connect(self.on_TextPlano_toggled)
        caixaH2_V2.addWidget(self.chkTextoPlano)

        self.chkPersonalizado = QRadioButton("Personalizado",containerV2)
        self.chkPersonalizado.toggled.connect(self.on_chkPersonalizado_toggled)
        caixaH2_V2.addWidget(self.chkPersonalizado)

        containerV2.setLayout(caixaH2_V2)
        caixaH2.addWidget(containerV2)
        caixaH2_V2.setAlignment(Qt.AlignmentFlag.AlignTop)
        caixaH2.setAlignment(Qt.AlignmentFlag.AlignTop)

        caixaV.addLayout(caixaH2)

        # CAJA HORIZONTAL 3 (BOTONES)

        caixaH3=QHBoxLayout()

        self.boton5=QPushButton("Cancelar")
        self.boton5.pressed.connect(self.on_btnCancelar_pressed)
        caixaH3.addWidget(self.boton5)

        self.boton6=QPushButton("Aceptar")
        caixaH3.addWidget(self.boton6)

        caixaH3.setAlignment(Qt.AlignmentFlag.AlignRight)
        caixaV.addLayout(caixaH3)

        #CONTENEDOR PRINCIPAL

        container = QWidget()
        container.setLayout(caixaV)
        self.setCentralWidget(container)

        self.setFixedSize(500,400)
        self.show()

    #Función para que al pulsar el boton "Cancelar" se cierre la ventana
    def on_btnCancelar_pressed(self):
        self.close()

    #Funciones para los checkbuttons e imprima por terminal si están activados o no
    def on_chkHTML_toggled(self):
        if self.chkHTML.isChecked():
            print(self.chkHTML.text() + " activado")
        else:
            print(self.chkHTML.text() + " desactivado")

    def on_TextPlano_toggled(self):
        if self.chkTextoPlano.isChecked():
            print(self.chkTextoPlano.text() + " activado")
        else:
            print(self.chkTextoPlano.text() + " desactivado")

    def on_chkPersonalizado_toggled(self):
        if self.chkPersonalizado.isChecked():
            print(self.chkPersonalizado.text() + " activado")
        else:
            print(self.chkPersonalizado.text() + " desactivado")

    #Función para que al pulsar el boton "Engadir" se añada un elemento a la lista
    def on_btn1_pressed(self):
        persona=[]

        #Agregamos elementos en una sola lista
        persona.append(self.txtNome.text())
        persona.append(self.txtApelido.text())
        persona.append(self.txtTelefono.text())
        persona.append(self.txtFormato.currentText())

        print(persona)

        if (persona[0]!="" and persona[1]!="" and persona[2]!=""):
            self.modelo.personas.append(persona)
            self.modelo.layoutChanged.emit()
            self.txtNome.setText("")
            self.txtApelido.setText("")
            self.txtTelefono.setText("")

            print("Engadido correctamente!")
        else:
            self.warning = QMessageBox.warning(self, "Error", "Faltan datos por rellenar", QMessageBox.StandardButton.Ok)

    #Función para rellenar los campos al pulsar en un elemento de la lista
    def on_lista_clicked(self):
        self.txtNome.setText(self.modelo.personas[self.lista.currentIndex().row()][0])
        self.txtApelido.setText(self.modelo.personas[self.lista.currentIndex().row()][1])
        self.txtTelefono.setText(self.modelo.personas[self.lista.currentIndex().row()][2])
        self.txtFormato.setCurrentText(self.modelo.personas[self.lista.currentIndex().row()][3])

        print("Elemento seleccionado")

    #Función que eliminará el elemento seleccionado de la lista
    def on_btn3_pressed(self):
        self.modelo.personas.pop(self.lista.currentIndex().row())
        self.modelo.layoutChanged.emit()

        print("Elemento borrado")




# ejecutamos la union?
if __name__=="__main__":
    aplicacion=QApplication(sys.argv)
    ventana=VentanaPrincipal()
    aplicacion.exec()