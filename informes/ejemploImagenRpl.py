from reportlab.graphics.shapes import Image, Drawing
from reportlab.graphics import renderPDF
from reportlab.lib.pagesizes import A4

imagenes = []

imagen= Image (0,0,100,100, "oli.jpeg")

dibujo=Drawing()
dibujo.add(imagen)

dibujo.translate(67,300)
imagenes.append(dibujo)

dibujo= Drawing()
dibujo.add(imagen)
dibujo.rotate(45)
dibujo.scale(3,2)
dibujo.translate(50,0)
imagenes.append(dibujo)

dibujo = Drawing(A4[0],A4[1])

for aux in imagenes:
    dibujo.add(aux)

renderPDF.drawToFile(dibujo, "ejemploImagenRpl.pdf")