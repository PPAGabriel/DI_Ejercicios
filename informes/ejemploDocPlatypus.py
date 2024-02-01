import os

from reportlab.platypus import Paragraph, Image, SimpleDocTemplate, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

hojaEstilo = getSampleStyleSheet()


guion = []

elementosDoc = []

cabecera = hojaEstilo["Heading4"]

cabecera.pageBreakBefore = 0
cabecera.keepWithNext = 0
cabecera.backColor = colors.dimgrey

paragrafo = Paragraph("Cabecera del documento", cabecera)
elementosDoc.append(paragrafo)
elementosDoc.append(Spacer(0,5))

contenidoDocumento = "Este es el contenido del documento, el cual va a ocupar múltiples lineas. "*100

estiloCuerpoTexto = hojaEstilo["BodyText"]
paragrafo = Paragraph(contenidoDocumento, estiloCuerpoTexto)
elementosDoc.append(paragrafo)
elementosDoc.append(Spacer(0,20))

imagen = Image("oli.jpeg",100,100)
elementosDoc.append(imagen)

documento = SimpleDocTemplate("ejemploDocPlatypus.pdf", pagesize = A4)
documento.build(elementosDoc)