from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Table, TableStyle, Spacer, Flowable

# FACTURA 1 EN PDF

hojaEstilo=getSampleStyleSheet()
elementosDoc=[]


#BORDE IZQUIERDO (EN TABLA)

class PositionedTable(Flowable):
    def __init__(self, table, x, y):
        Flowable.__init__(self)
        self.table = table
        self.x = x
        self.y = y

    def draw(self):
        self.canv.saveState()
        self.canv.translate(self.x, self.y)
        self.table.wrapOn(self.canv, 0, 0)
        self.table.drawOn(self.canv, 0, 0)
        self.canv.restoreState()


tabla_border_izq = Table([ [""],
                                [""],
                                [""],
                                [""]
                               ], colWidths=[20], rowHeights=[50, 255,5,140])
tabla_border_izq.setStyle([
    ('BACKGROUND',(0,0),(0,0),colors.darkgreen),
    ('BACKGROUND',(0,1),(0,1),colors.lightgreen),
    ('BACKGROUND',(0,2),(0,2),colors.white),
    ('BACKGROUND',(0,3),(0,3),colors.lightgreen)
])

# Añadimos el borde izquierdo a la tabla
borde_posicionado = PositionedTable(tabla_border_izq, -60, -445)

# CABECERA
cabecera_estilo=hojaEstilo["Heading1"] # Estilo de la cabecera
cabecera_estilo.textColor = colors.darkolivegreen # Color de la cabecera
cabecera_estilo.alignment=2 # Alineación de la cabecera hacia la derecha
cabecera_estilo.fontSize=16

# Contenido de la cabecera
cabecera=Paragraph("FACTURA SIMPLIFICADA", cabecera_estilo)

# NOMBRE Y LOGO
texto1_estilo=hojaEstilo["Heading2"] # Estilo del texto
texto1_estilo.textColor=colors.darkgreen # Color del texto
texto1_estilo.fontSize=16
texto1_estilo.alignment=0 # Alineación del texto hacia la izquierda
texto1=Paragraph("Nombre de tu empresa",texto1_estilo) # Texto

texto2_estilo=hojaEstilo["Heading2"] # Estilo del texto
texto2_estilo.textColor=colors.darkgreen # Color del texto
texto2_estilo.fontSize=12
texto2=Paragraph("Logo de la empresa",texto2_estilo) # Texto

# Crear tabla con nombre y logo
tabla_NombreLogo = Table([
                [texto1,"","","",texto2]
              ], colWidths=[100, 100, 100, 50, 150])

# Estilo de la tabla
tabla_NombreLogo.setStyle(TableStyle([
                           ('SPAN',(0,0),(1,0)),
                          ]))

# DATOS DE DIRECCION
datos_factura = [
    ["Dirección","","","",""],
    ["Ciudad y País","","","",""],
    ["CIF/NIF","","","Fecha Emisión","DD/MMM/AAA"],
    ["Teléfono","","","Número de Factura","A0001"],
    ["Mail","","","",""]
]

# Estilo de la tabla
estilo_tabla_factura = [
    ('FONT',(0,0),(0,-1),'Helvetica-BoldOblique'),
    ('FONT',(3,0),(3,-1),'Helvetica-Bold'),
    ('ALIGN',(3,2),(3,2),'RIGHT'),
    ('TEXTCOLOR',(0,0),(-1,-1),colors.darkgreen),
]

# Crear tabla con los datos de la factura
tabla_DatosFactura = Table(datos_factura, colWidths=[100, 100, 100, 100, 100])
tabla_DatosFactura.setStyle(estilo_tabla_factura)

# TABLA DE PRODUCTOS

# Datos de los productos
datos_productos = [
    ["Descripción","Importe","Cantidad","Total"],
    ["Producto 1","3,2","5","16,00"],
    ["Producto 2","2,1","3","6,30"],
    ["Producto 3","2,9","76","220,40"],
    ["Producto 4","5","23","115,00"],
    ["Producto 5","4,95","3","14,85"],
    ["Producto 6","6","2","12,00"]
]

# Estilo de la tabla
estilo_tabla_productos = [
    ('FONT',(0,0),(-1,0),'Helvetica-Bold'),
    ('BACKGROUND',(0,0),(-1,0),colors.darkgreen),
    ('TEXTCOLOR',(0,0),(-1,0),colors.white),
    ('BACKGROUND',(0,1),(-1,-1),colors.lightgreen),
    ('TEXTCOLOR',(0,1),(-1,-1),colors.black),
    ('ALIGN',(0,0),(-1,-1),'CENTER'),
    ('GRID',(0,0),(-1,-1),1,colors.white),
]

# Crear tabla con los datos de los productos
tabla_Productos = Table(datos_productos, colWidths=[190, 100, 100, 100])
tabla_Productos.setStyle(estilo_tabla_productos)

# TABLA DE TOTALES

# Datos de los totales
datos_totales = [
    ["","","TOTAL","385 €"],
]

# Estilo de la tabla
estilo_tabla_totales = [
    ('FONT',(2,0),(3,0),'Helvetica-Bold'),
    ('BACKGROUND',(2,0),(3,0),colors.darkgreen),
    ('TEXTCOLOR',(2,0),(3,0),colors.white),
    ('ALIGN',(2,0),(3,0),'CENTER'),
    ('VALIGN',(2,0),(3,0),'MIDDLE'),
    ('GRID',(2,0),(3,0),1,colors.white),
    ('FONTSIZE',(2,0),(3,0),12)
]

# Crear tabla con los datos de los totales
tabla_Totales = Table(datos_totales, colWidths=[190, 100, 100, 100], rowHeights=30)
tabla_Totales.setStyle(estilo_tabla_totales)

# LINEA DE SEPARACION
linea_separacion = Table([["","","",""]], colWidths=[190, 100, 100, 100])

# Estilo de la tabla
estilo_linea_separacion = [
    ('LINEBELOW',(0,0),(-1,-1),1,colors.black),
]

# Aplicamos el estilo a la tabla
linea_separacion.setStyle(estilo_linea_separacion)

# PIE DE PÁGINA
pie_estilo=hojaEstilo["BodyText"] # Estilo de la cabecera
pie_estilo.textColor = colors.darkgreen # Color de la cabecera
pie_estilo.alignment=1 # Alineación de la cabecera hacia la derecha
pie_estilo.fontName="Helvetica-Bold"
pie_estilo.fontSize=10

# Contenido deL pie de página
pie=Paragraph("GRACIAS POR SU CONFIANZA", pie_estilo)

################################################################################################

# Añadimos los elementos al documento
elementosDoc.append(borde_posicionado)
elementosDoc.append(cabecera)
elementosDoc.append(Spacer(50, 15))
elementosDoc.append(tabla_NombreLogo)
elementosDoc.append(tabla_DatosFactura)
elementosDoc.append(Spacer(50, 15))
elementosDoc.append(tabla_Productos)
elementosDoc.append(Spacer(50, 7))
elementosDoc.append(tabla_Totales)
elementosDoc.append(Spacer(50, 25))
elementosDoc.append(linea_separacion)
elementosDoc.append(Spacer(50, 25))
elementosDoc.append(pie)

# Documento
documento=SimpleDocTemplate("Modelo_Factura1.pdf", pagesize=A4)
documento.build(elementosDoc)

