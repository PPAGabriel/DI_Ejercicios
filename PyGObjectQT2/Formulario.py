import sys

from PyQt6.QtGui import QColor, QIcon, QPixmap
# importamos del pyqt6 los elementos que nos importa -> ventana principal, boton
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt, QAbstractListModel
class VentanaPrincipal(QMainWindow):
    # iniciamos a ventana
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Formulario")

        caixaV=QVBoxLayout()

        caixaH1=QHBoxLayout()
        caixaV.addLayout(caixaH1)

        caixaH2=QHBoxLayout()
        caixaV.addLayout(caixaH2)

        caixaH1_V1=QVBoxLayout()
        caixaH1.addLayout(caixaH1_V1)

        # icono de cd
        self.icono=QLabel()
        self.icono.setPixmap(QPixmap("cd.svg"))
        caixaH1_V1.addWidget(self.icono)
        caixaH1_V1.setAlignment(Qt.AlignmentFlag.AlignTop)

        # checkbox
        self.checkbox=QCheckBox("Animado")
        caixaH1_V1.addWidget(self.checkbox)

        caixaH1_V2 = QVBoxLayout()
        caixaH1.addLayout(caixaH1_V2)

        # ListView
        self.lista=QListView()
        self.lista.setFixedSize(600,400)
        caixaH1_V2.addWidget(self.lista)

        caixaH1_V3 = QVBoxLayout()
        caixaH1.addLayout(caixaH1_V3)

        # botones
        self.boton1=QPushButton("Añadir pista a reproducir")
        caixaH1_V3.addWidget(self.boton1)

        self.boton2=QPushButton("Subir en la lista")
        caixaH1_V3.addWidget(self.boton2)

        self.boton3=QPushButton("Bajar en la lista")
        caixaH1_V3.addWidget(self.boton3)

        # grid  para el boton saltar y comboBox
        self.grid1=QGridLayout()
        self.boton4=QPushButton("Saltar")
        self.grid1.addWidget(self.boton4)
        self.grid1.addWidget(self.boton4,0,0)

        self.comboBox1=QComboBox()
        self.grid1.addWidget(self.comboBox1,0,1)

        caixaH1_V3.addLayout(self.grid1)

        self.boton5=QPushButton("Abrir fichero...")
        caixaH1_V3.addWidget(self.boton5)

        self.boton6=QPushButton("Reproducir fichero...")
        caixaH1_V3.addWidget(self.boton6)

        self.boton7=QPushButton("Guardar como...")
        caixaH1_V3.addWidget(self.boton7)

        self.boton8=QPushButton("Eliminar lista")
        caixaH1_V3.addWidget(self.boton8)

        # grid2 (primer cuadro de la parte inferior)
        self.grid2 = QGridLayout()
        lblSon = QLabel("Son:")
        combSon = QComboBox()
        self.grid2.addWidget(lblSon, 0, 0, 1, 1)
        self.grid2.addWidget(combSon, 0, 1, 1, 2)

        lblRitmo = QLabel("Ritmo:")
        sldRitmo = QSlider(Qt.Orientation.Horizontal)
        sldRitmo.valueChanged.connect(lambda valor: lblRitmo.setText("Ritmo:    " + str(valor)))
        self.grid2.addWidget(lblRitmo, 1, 0, 1, 1)
        self.grid2.addWidget(sldRitmo, 1, 1, 1, 2)

        lblVolumen = QLabel("Volumen:")
        sldVolumen = QSlider(Qt.Orientation.Horizontal)
        sldVolumen.valueChanged.connect(lambda valor: lblVolumen.setText("Volumen:    " + str(valor)))
        self.grid2.addWidget(lblVolumen, 2, 0, 1, 1)
        self.grid2.addWidget(sldVolumen, 2, 1, 1, 2)

        lblFormato = QLabel("Formato:")
        combFormato = QComboBox()
        self.grid2.addWidget(lblFormato, 3, 0, 1, 1)
        self.grid2.addWidget(combFormato, 3, 1, 1, 2)

        lblSalida = QLabel("Salida de audio:")
        combSalida = QComboBox()
        self.grid2.addWidget(lblSalida, 4, 0, 1, 1)
        self.grid2.addWidget(combSalida, 4, 1, 1, 2)

        caixaH2.addLayout(self.grid2)

        # frame (segundo cuadro de la parte inferior)

        caixaH2_H2 = QHBoxLayout()
        frame1 = QGroupBox("Opciones de reproducción")
        frame1.setStyleSheet(
            "QGroupBox { "
            "            border: 1px solid black;"
            "            border-radius: 5px;"
            "}")
        frame1.setLayout(caixaH2_H2)
        caixaH2.addWidget(frame1)

        caixaH2_H2_V1 = QVBoxLayout()

        self.checkAsincrono = QCheckBox("Asincrono")
        caixaH2_H2_V1.addWidget(self.checkAsincrono)
        self.checkENome = QCheckBox("El nombre del fichero")
        caixaH2_H2_V1.addWidget(self.checkENome)
        self.checkXML = QCheckBox("XML persistente")
        caixaH2_H2_V1.addWidget(self.checkXML)

        caixaH2_H2.addLayout(caixaH2_H2_V1)

        caixaH2_H2_V2 = QVBoxLayout()

        self.checkFiltro = QCheckBox("Filtrar antes de reproducir")
        caixaH2_H2_V2.addWidget(self.checkFiltro)
        self.checkEXML = QCheckBox("Es XML")
        caixaH2_H2_V2.addWidget(self.checkEXML)
        self.checkNPL = QCheckBox("Reproducción NPL")
        caixaH2_H2_V2.addWidget(self.checkNPL)

        caixaH2_H2.addLayout(caixaH2_H2_V2)

        container = QWidget()
        container.setLayout(caixaV)
        self.setCentralWidget(container)

        self.setFixedSize(1000, 600)
        self.show()



# ejecutamos la union?
if __name__=="__main__":
    aplicacion=QApplication(sys.argv)
    ventana=VentanaPrincipal()
    aplicacion.exec()