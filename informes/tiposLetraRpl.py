from reportlab.pdfgen import canvas

frase="Esta es una bonita frase para ver los distintos tipos de letra."

aux = canvas.Canvas("tiposLetra.pdf")
obxTexto = aux.beginText()
obxTexto.setTextOrigin(20,700)
obxTexto.setFillColor("green")
#obxTexto.setFillColorRGB(0,1,0)
espacioCaracteres=0

for tipoLetra in aux.getAvailableFonts():
    obxTexto.setCharSpace(espacioCaracteres)
    obxTexto.setFont(tipoLetra, 12)
    obxTexto.textLine(tipoLetra + ": " + frase)
    obxTexto.moveCursor(20,15)
    espacioCaracteres+=1

obxTexto.setFillGray(0.3)
obxTexto.setFont("Helvetica", 15)
obxTexto.setCharSpace(0)
obxTexto.setTextOrigin(20,200)

for i in range(10):
    obxTexto.setWordSpace(i)
    obxTexto.textLine(frase)

aux.drawText(obxTexto)
aux.save()
