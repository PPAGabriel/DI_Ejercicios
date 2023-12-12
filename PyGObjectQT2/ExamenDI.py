import sys

from PyQt6.QtGui import QColor, QIcon, QPixmap
# importamos del pyqt6 los elementos que nos importa -> ventana principal, boton
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt, QAbstractListModel

# EXAMEN DI 12-12-2022 , GABRIEL PEREZ
class PersonasModelo(QAbstractListModel):

    def __init__(self, personas=None):
        super().__init__()
        self.personas = personas or []

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            tratamento, _, _, _ = self.personas[index.row()]
            _, nome, _, _ = self.personas[index.row()]
            _, _, apelido, _ = self.personas[index.row()]
            _, _, _, email = self.personas[index.row()]
            return tratamento + " , " + nome + " , " + apelido + " , " + email

    def rowCount(self, indice):
        return len(self.personas)


class VentanaPrincipal(QMainWindow):
    # iniciamos la ventana
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Examen 12-12-_2022")

        listaPersonas = [("Fisio", "Gabriel", "Perez", "gperez@daniel.com"), ("Neuro", "Alan", "Garcia", "alan@hotmail.com")]
        self.modelo = PersonasModelo(listaPersonas)

        caixaV = QVBoxLayout()

        #GRID 1 (ENTRADAS DEL USUARIO)

        self.grid1=QGridLayout()

        #Nombre
        lblNome=QLabel("Nome")
        self.grid1.addWidget(lblNome,0,0)
        self.txtNome=QLineEdit()
        self.grid1.addWidget(self.txtNome,1,0)

        #Tratamiento
        lblTratamento=QLabel("Tratamento")
        self.grid1.addWidget(lblTratamento,0,1)
        self.txtTratamento=QLineEdit()
        self.grid1.addWidget(self.txtTratamento,1,1)

        #Apelido
        lblApelido=QLabel("Apelido")
        self.grid1.addWidget(lblApelido,2,0)
        self.txtApelido=QLineEdit()
        self.grid1.addWidget(self.txtApelido,3,0)

        #Usuario
        lblUsuario=QLabel("Usuario")
        self.grid1.addWidget(lblUsuario,2,1)
        self.txtUsuario=QLineEdit()
        self.grid1.addWidget(self.txtUsuario,3,1)

        caixaV.addLayout(self.grid1)

        #CAJA HORIZONTAL 2 (FORMATO)

        caixaH2=QHBoxLayout()

        #Formato
        lblFormato=QLabel("Formato")
        caixaH2.addWidget(lblFormato)

        #ComboBox
        self.comboFormato=QComboBox()
        self.comboFormato.addItem("HTML")
        self.comboFormato.addItem("Texto Plano")
        self.comboFormato.addItem("Personalizado")
        self.comboFormato.setFixedSize(430,25)
        caixaH2.addWidget(self.comboFormato)
        caixaH2.setAlignment(Qt.AlignmentFlag.AlignLeft)

        caixaV.addLayout(caixaH2)

        #CAJA HORIZONTAL 3 (email, lista, botones)

        caixaH3=QHBoxLayout()
        caixaH3_V1=QVBoxLayout()
        caixaH3_V2=QVBoxLayout()

        caixaH3_V1_H1 = QHBoxLayout()

        #email
        lblEmail = QLabel("Dirección de correo")
        caixaH3_V1_H1.addWidget(lblEmail)
        self.txtEmail = QLineEdit()
        caixaH3_V1_H1.addWidget(self.txtEmail)
        caixaH3_V1.addLayout(caixaH3_V1_H1)
        caixaH3.addLayout(caixaH3_V1)

        #lista
        self.lista=QListView()
        self.lista.setModel(self.modelo)
        self.lista.setSelectionMode(QListView.SelectionMode.SingleSelection)
        self.lista.setFixedSize(395,200)
        caixaH3_V1.addWidget(self.lista)

        #botones
        self.boton1 = QPushButton("Engadir")
        self.boton1.pressed.connect(self.on_btn1_pressed)
        caixaH3_V2.addWidget(self.boton1)

        self.boton2 = QPushButton("Editar")
        caixaH3_V2.addWidget(self.boton2)

        self.boton3 = QPushButton("Borrar")
        self.boton3.pressed.connect(self.on_btn3_pressed)
        caixaH3_V2.addWidget(self.boton3)

        self.boton4 = QPushButton("Por defecto")
        caixaH3_V2.addWidget(self.boton4)
        caixaH3.addLayout(caixaH3_V2)
        caixaH3_V2.setAlignment(Qt.AlignmentFlag.AlignTop)

        caixaV.addLayout(caixaH3)

        # CAJA VERTICAL 4 (Qradios)
        caixaV4=QVBoxLayout()

        #etiqueta formato de correo
        lblFormatoCorreo=QLabel("Formato de correo:")
        caixaV4.addWidget(lblFormatoCorreo)

        containerV2 = QWidget()


        #qradiobuttons
        caixaV4_H1=QHBoxLayout()
        self.chkHTML = QRadioButton("HTML",containerV2)
        self.chkHTML.toggled.connect(self.on_chkHTML_toggled)
        caixaV4_H1.addWidget(self.chkHTML)

        self.chkTextoPlano = QRadioButton("Texto Plano",containerV2)
        self.chkTextoPlano.toggled.connect(self.on_TextPlano_toggled)
        caixaV4_H1.addWidget(self.chkTextoPlano)

        self.chkPersonalizado = QRadioButton("Personalizado",containerV2)
        self.chkPersonalizado.toggled.connect(self.on_chkPersonalizado_toggled)
        caixaV4_H1.addWidget(self.chkPersonalizado)

        containerV2.setLayout(caixaV4_H1)

        caixaV4.addWidget(containerV2)
        caixaV4.setAlignment(Qt.AlignmentFlag.AlignLeft)
        caixaV.addLayout(caixaV4)

        #CAJA HORIZONTAL 5 (ACEPTAR Y CANCELAR)

        caixaH5 = QHBoxLayout()

        self.boton5 = QPushButton("Cancelar")
        caixaH5.addWidget(self.boton5)

        self.boton6 = QPushButton("Aceptar")
        caixaH5.addWidget(self.boton6)

        caixaH5.setAlignment(Qt.AlignmentFlag.AlignRight)
        caixaV.addLayout(caixaH5)

        #CONTENEDOR PRINCIPAL

        container = QWidget()
        container.setLayout(caixaV)
        self.setCentralWidget(container)

        self.setFixedSize(500,500)
        self.show()

    #Función para que al pulsar el boton "Engadir" se añada un elemento a la lista
    def on_btn1_pressed(self):
        persona=[]

        #Agregamos elementos en una sola lista
        persona.append(self.txtTratamento.text())
        persona.append(self.txtNome.text())
        persona.append(self.txtApelido.text())
        persona.append(self.txtEmail.text())

        print(persona)

        if (persona[0]!="" and persona[1]!="" and persona[2]!="" and persona[3]!=""):
            self.modelo.personas.append(persona)
            self.modelo.layoutChanged.emit()
            self.txtTratamento.setText("")
            self.txtNome.setText("")
            self.txtApelido.setText("")
            self.txtEmail.setText("")

            print("Engadido correctamente!")
        else:
            self.warning = QMessageBox.warning(self, "Error", "Faltan datos por rellenar", QMessageBox.StandardButton.Ok)


    # Función que eliminará el elemento seleccionado de la lista
    def on_btn3_pressed(self):
        self.modelo.personas.pop(self.lista.currentIndex().row())
        self.modelo.layoutChanged.emit()

        print("Eliminado correctamente!")

    #Funciones para sincronizar los Radio Button con el ComboBox
    def on_chkHTML_toggled(self):
        if self.chkHTML.isChecked():
            self.comboFormato.setCurrentText(self.chkHTML.text())
            print(self.chkHTML.text() + " activado")
        else:
            print(self.chkHTML.text() + " desactivado")

    def on_TextPlano_toggled(self):
        if self.chkTextoPlano.isChecked():
            self.comboFormato.setCurrentText(self.chkTextoPlano.text())
            print(self.chkTextoPlano.text() + " activado")
        else:
            print(self.chkTextoPlano.text() + " desactivado")

    def on_chkPersonalizado_toggled(self):
        if self.chkPersonalizado.isChecked():
            self.comboFormato.setCurrentText(self.chkPersonalizado.text())
            print(self.chkPersonalizado.text() + " activado")
        else:
            print(self.chkPersonalizado.text() + " desactivado")




# ejecutamos la union?
if __name__=="__main__":
    aplicacion=QApplication(sys.argv)
    ventana=VentanaPrincipal()
    aplicacion.exec()