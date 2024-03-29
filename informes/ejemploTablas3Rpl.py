from reportlab.platypus import (Paragraph, Image, SimpleDocTemplate, Spacer,Table,TableStyle)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen.canvas import Color

hojaEstilo=getSampleStyleSheet()

elementosDoc=[]

imagen=Image("oli.jpeg",50,50)
estiloCuerpoTexto=hojaEstilo["BodyText"]
estiloCuerpoTexto2=hojaEstilo["Heading4"]
estiloCuerpoTexto.textColor=Color(150,0,0,1)
parrafo=Paragraph("Optare",estiloCuerpoTexto)
parrafo2=Paragraph("Optare",estiloCuerpoTexto2)

datos=[ ["Empresas","Candidato 1","Candidato 2","Especificaciones"],
        ["Ayco","Marcos","Ruben","Desarrollo web con PHP"],
        [[parrafo,parrafo2],"Borja","Juan","Reconocimiento de imagenes con OpenCV"],
        [[parrafo,imagen],"Lidier","Lucas","Aplicaciones para las Telco"] ]

estilo=[("TEXTCOLOR",(0,0),(0,-1),colors.green),
        ("TEXTCOLOR",(1,0),(-1,0),colors.blueviolet),
        ("TEXTCOLOR",(1,1),(-1,-1),colors.grey),
        ("BOX",(1,1),(-1,-1),1.25,colors.grey),
        ("INNERGRID",(1,1),(-1,-1),1.25,colors.lightgrey),
        ("VALING",(0,0),(-1,-1),"MIDDLE")
        ]

tabla=Table(data=datos)
tabla.setStyle(estilo)

elementosDoc.append(tabla)

documento=SimpleDocTemplate("ejemploTablas3.pdf", pagesize=A4)
documento.build(elementosDoc)