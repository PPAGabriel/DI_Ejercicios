from reportlab.pdfgen import canvas


aux = canvas.Canvas("primerDocumento.pdf")

aux.drawString(0,0,"Posicion Origen (X,Y) = (0,0)")
aux.drawString(50,100, "Posicion (X,Y) = (50,100)")
aux.drawString(150,20,"Posicion (X,Y) = (150,20)")
aux.drawImage("check.png", 250,300,512,512)


aux.showPage()
aux.save()