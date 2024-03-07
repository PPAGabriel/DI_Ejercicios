from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Table, TableStyle, Spacer, Flowable, Image

# FACTURA 2 EN PDF

hojaEstilo=getSampleStyleSheet()
elementosDoc=[]

# CABECERA E IMAGEN
cabecera_estilo=hojaEstilo["Heading1"] # Estilo de la cabecera
cabecera_estilo.alignment=0 # Alineación de la cabecera hacia la izquierda
cabecera_estilo.fontSize=16

# Contenido de la cabecera
cabecera=Paragraph("FACTURA Proforma", cabecera_estilo)

# Imagen
imagen=Image("imgLogo.png")

# Crear tabla con cabecera e imagen
tabla_cabecera = Table([
    [cabecera, imagen]
    ], colWidths=[200, 250])

# Añadir estilo a la tabla
tabla_cabecera.setStyle([
    ('VALIGN',(0,0),(0,0),'MIDDLE'),
])

# TABLA 1

# Datos de la tabla
datos_tabla1 = [
    ["FACTURAR A:","","Nº FACTURA:"],
    ["Cliente\nDomicilio\nCódigo postal/ciudad\n(NIF)","","Fecha\n\nNº de pedido\n\nFecha de vencimiento\n\nCondiciones de pago"]
    ]

# Crear tabla
tabla1 = Table(datos_tabla1,colWidths=[150, 150])

# Añadir estilo a la tabla
tabla1.setStyle([
    ('BACKGROUND',(0,0),(-1,-1),colors.lightgrey),
    ('FONTSIZE',(2,0),(2,0),12),
    ('VALIGN',(0,1),(0,1),'MIDDLE')
])

# TABLA 2

# Datos de la tabla
datos_tabla2 = [
    ["Pos.","Concepto/Descripción","Cantidad","Unidad","Precio\nunitario","Importe"],
    ["1","","","","",""],
    ["2","","","","",""],
    ["","","","","",""]
    ]

# Crear tabla
tabla2 = Table(datos_tabla2,colWidths=[45,145, 60, 50, 90,60])

# Añadir estilo a la tabla
tabla2.setStyle([
    ('BACKGROUND',(0,0),(-1,0),colors.grey),
    ('ALIGN',(0,0),(-1,0),'CENTER'),
    ('VALIGN',(0,0),(-1,0),'TOP'),
    ('GRID',(0,0),(-1,-1),1,colors.black)
])

# TABLA 3

## SubTabla 1
datos_subtabla1 = [
    ["Método de pago:"]
    ]

# Crear subtabla
subtabla1 = Table(datos_subtabla1,colWidths=[220], rowHeights=[50])

# Añadir estilo a la subtabla
subtabla1.setStyle([
    ('FONTSIZE',(0,0),(-1,-1),8),
    ('GRID',(0,0),(-1,-1),1,colors.black),
    ('ALIGN',(0,0),(-1,-1),'LEFT'),
    ('VALIGN',(0,0),(-1,-1),'TOP'),
])

## Subtabla 2
datos_subtabla2=[
    ["Importe neto",""],
    ["+ IVA de    %",""],
    ["- IRPFF de    %",""],
    ["IMPORTE BRUTO",""]
    ]

# Crear subtabla
subtabla2 = Table(datos_subtabla2,colWidths=[80,40])

# Añadir estilo a la subtabla
subtabla2.setStyle([
    ('FONTSIZE',(0,0),(-1,-1),8),
    ('FONT',(0,3),(0,3),'Helvetica-Bold'),
    ('GRID',(0,0),(-1,-1),1,colors.black),
    ('ALIGN',(0,0),(-1,-1),'LEFT'),
    ('BACKGROUND',(0,3),(-1,3),colors.grey)
])

# Añadiendo las subtablas en Tabla 3
datos_tabla3=[
    [subtabla1,"",subtabla2]
    ]

tabla3 = Table(datos_tabla3,colWidths=[220,110,130])

tabla3.setStyle([
    ('VALIGN',(0,0),(-1,-1),'TOP')
])

# PIE DE PÁGINA

# Estilo del pie de página
pie_estilo=hojaEstilo["BodyText"]
pie_estilo.alignment=0
pie_estilo.fontSize=10

# Contenido del pie de página
pie1=Paragraph("Gracias por su confianza.", pie_estilo)
pie2=Paragraph("Atentamente,", pie_estilo)


#######################################################################

#Añadimos los elementos al documento
elementosDoc.append(tabla_cabecera)
elementosDoc.append(Spacer(0,10))
elementosDoc.append(tabla1)
elementosDoc.append(Spacer(0,30))
elementosDoc.append(tabla2)
elementosDoc.append(Spacer(0,60))
elementosDoc.append(tabla3)
elementosDoc.append(Spacer(0,10))
elementosDoc.append(pie1)
elementosDoc.append(Spacer(0,20))
elementosDoc.append(pie2)

#Creamos el documento
doc=SimpleDocTemplate("Modelo_Factura2.pdf", pagesize=A4)
doc.build(elementosDoc)