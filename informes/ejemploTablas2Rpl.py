from reportlab.platypus import (Paragraph, Image, SimpleDocTemplate, Spacer,Table,TableStyle)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen.canvas import Color

hojaEstilo=getSampleStyleSheet()

elementosDoc=[]

temperaturas=[['','Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'],
              ["Máximas", 15, 16, 20, 25, 27, 31, 35, 38, 30, 25, 20, 18],
              ["Minimas", -3, -4, -1, 4, 6, 9, 12, 15, 16, 10, 2,-2]
              ]

estilo=[('TEXTCOLOR',(0,0),(-1,0),colors.grey),
        ('TEXTCOLOR',(0,1),(0,-1),colors.grey),
        ('BOX',(1,1),(-1,-1),1.50,colors.grey),
        ('INNERGRID',(1,1),(-1,-1),0.5,colors.white)
        ]

for i,fila in enumerate(temperaturas):
        for j,temperatura in enumerate(fila):
                if type(temperatura)==int:
                        estilo.append(('TEXTCOLOR',(j,i),(j,i),colors.black))
                        if temperatura>30:
                                estilo.append(('BACKGROUND', (j, i), (j, i), colors.fidred))
                        elif temperatura<=30 and temperatura>20:
                                estilo.append(('BACKGROUND', (j, i), (j, i), colors.orange))
                        elif temperatura<=20 and temperatura>10:
                                estilo.append(('BACKGROUND', (j, i), (j, i), colors.lightpink))
                        elif temperatura<=10 and temperatura>0:
                                estilo.append(('BACKGROUND', (j, i), (j, i), colors.lightblue))
                        else:
                                estilo.append(('TEXTCOLOR',(j,i),(j,i),colors.blue))
                                estilo.append(('BACKGROUND',(j,i),(j,i),colors.lightgrey))


tabla=Table(data=temperaturas)
tabla.setStyle(estilo)

elementosDoc.append(tabla)

documento=SimpleDocTemplate("ejemploTablas2.pdf", pagesize=A4)
documento.build(elementosDoc)