from reportlab.pdfgen import canvas

frase = ["Estas es una bonita frase,","para tener distintas partes",
         "a las que incluir en nuestro","texto de ejemplo."]

aux = canvas.Canvas("ejemploTexto.pdf")
objTexto = aux.beginText()
objTexto.setTextOrigin(100,500)
objTexto.setFont("Courier", 16)
for liña in frase:
    objTexto.textLine(liña)

objTexto.setFillGray(0.5)

parragrafo = '''
Este es un texto multiliña para poner el ejemplo.
En el escribimos varias frases en un parragrafo
para que despues dentro del documento o drawText de canvas.
'''
objTexto.textLines(parragrafo)
aux.drawText(objTexto)
aux.showPage()

aux.save()