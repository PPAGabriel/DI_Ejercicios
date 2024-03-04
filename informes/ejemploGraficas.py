import os

from reportlab.graphics.charts.legends import LineLegend, Legend
from reportlab.graphics.shapes import Drawing
from reportlab.platypus import Paragraph, Image, SimpleDocTemplate, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.linecharts import HorizontalLineChart
from reportlab.graphics.widgets.markers import makeMarker
from reportlab.graphics.charts.piecharts import Pie, Pie3d


hojaEstilo = getSampleStyleSheet()

estiloCuerpoTexto = hojaEstilo["BodyText"]
elementosDoc = []

temperaturas = [["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio","Julio","Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"],
         [15, 16, 20, 25, 27, 31, 35, 38, 30, 25, 20, 18],
         [-3, -4, -1, 4, 6, 9, 12, 15, 16, 10, 2,-2]
         ]

## definimos una area de dibujo
dibujo = Drawing(400,200)

## crear grafico de barras
gb = VerticalBarChart()
## le damos valores al punto x
gb.x =50
## le damos valores al punto y
gb.y =50
## le damos valores al alto
gb.height = 125
## le damos valores al ancho
gb.width = 300

gb.data = temperaturas[1:]
gb.strokeColor = colors.black
gb.valueAxis.valueMin = -5
gb.valueAxis.valueMax=40
gb.valueAxis.valueStep = 5
gb.categoryAxis.labels.boxAnchor = 'ne'
gb.categoryAxis.labels.dx=8
gb.categoryAxis.labels.dy=-15
gb.categoryAxis.labels.angle=30
gb.categoryAxis.categoryNames = temperaturas[0]
gb.groupSpacing = 10
gb.barSpacing = 2

dibujo.add(gb)
elementosDoc.append(dibujo)
elementosDoc.append(Spacer(50, 50))

dibujo=Drawing(400,200)
gl=HorizontalLineChart()
gl.x=50
gl.y=50
gl.height=125
gl.width=300
gl.data=temperaturas[1:]
gl.categoryNames=temperaturas[0]
gl.categoryAxis.labels.boxAnchor='ne'
gl.categoryAxis.labels.angle=30
gl.categoryAxis.labels.dx=10
gl.categoryAxis.labels.dy=-20
gl.categoryAxis.categoryNames=temperaturas[0]
gl.valueAxis.valueMin=0
gl.valueAxis.valueMax=40
gl.valueAxis.valueStep=10
gl.lines[0].strokeWidth=1
gl.lines[0].symbol=makeMarker('FilledCircle')
gl.lines[1].strokeWidth=5

dibujo.add(gl)

leyenda=LineLegend()
leyenda.fontSize=8
leyenda.fontName="Helvetica"
leyenda.alignment="right"
leyenda.x=0
leyenda.y=-15
leyenda.columnMaximum=2
series=["Máximas","Minimas"]
leyenda.colorNamePairs=[(gl.lines[i].strokeColor, series[i]) for i in range(len(gl.data))]
# [('red','Máximas'),('green','Minimas')]

dibujo.add(leyenda)
elementosDoc.append(dibujo)
elementosDoc.append(Spacer(50, 35))

dibujo=Drawing(300,200)
tarta=Pie3d()
tarta.x=65
tarta.y=15
tarta.data=[10,5,20,25,40]
tarta.labels=['Edge','Brave','Firefox','Safari','Chrome']

tarta.slices.strokeWidth=0.5
tarta.slices[3].popout=10
tarta.slices[3].strokeWidth=2
tarta.slices[3].strokeDashArray=[2,2]
tarta.slices[3].labelRadius=2
tarta.slices[3].fontColor=colors.blue
tarta.sideLabels=1

dibujo.add(tarta)

leyenda=Legend()
leyenda.x=300
leyenda.y=5
leyenda.dx=10
leyenda.dy=10
leyenda.fontName="Helvetica"
leyenda.fontSize=7
leyenda.boxAnchor='n'
leyenda.columnMaximum=15
leyenda.strokeWidth=0.5
leyenda.strokeColor=colors.grey
leyenda.deltax=75
leyenda.deltay=10
leyenda.autoXPadding=5
leyenda.yGap=1
leyenda.dxTextSpace=3
leyenda.alignment="right"
leyenda.dividerLines=1|2|4
leyenda.dividerOffsY=4.5
leyenda.subCols.rpad=30

paresColorLeyenda=list()
colores=[colors.red,colors.green,colors.blue,colors.yellow,colors.pink]
for i,color in enumerate(colores):
    tarta.slices[i].fillColor=color
    paresColorLeyenda.append((color,tarta.labels[i]))

leyenda.colorNamePairs=paresColorLeyenda


dibujo.add(leyenda)
elementosDoc.append(dibujo)



documento = SimpleDocTemplate("ejemploGraficas.pdf", pagesize = A4)
documento.build(elementosDoc)