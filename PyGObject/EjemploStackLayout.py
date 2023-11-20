import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import Gdk

class objetoColor(Gtk.Box):
    def __init__(self):
        super().__init__()

        self.set_orientation(Gtk.Orientation.HORIZONTAL)

        ## Box almacena los objetos que puedan haber en el entorno grafico
        cajaColor1=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        cajaColor2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

        boton1 = self.boton_con_color("red")
        boton2 = self.boton_con_color("yellow")
        boton3 = self.boton_con_color("purple")
        boton4 = self.boton_con_color("green")
        boton5 = self.boton_con_color("blue")
        boton6 = self.boton_con_color("orange")

        #Primera Columna
        cajaColor1.pack_start(boton1,True,True,5)
        cajaColor1.pack_start(boton2, True, True, 5)
        cajaColor1.pack_start(boton3, True, True, 5)

        self.pack_start(cajaColor1, True, True, 5)

        #Segunda Columna
        self.pack_start(boton4, True, True, 5)

        #Tercera Columna
        cajaColor2.pack_start(boton5, True, True, 5)
        cajaColor2.pack_start(boton6, True, True, 5)

        self.pack_start(cajaColor2,True,True,5)

    def on_debuxa(self,control,cr,datos):
        contexto=control.get_style_context()
        ancho=control.get_allocated_width()
        alto=control.get_allocated_height()
        Gtk.render_background(contexto,cr,0,0,ancho,alto)

        r,g,b,a=datos["color"]
        cr.set_source_rgba(r,g,b,a)
        cr.rectangle(0,0,ancho,alto)
        cr.fill()

    def boton_con_color(self,color):
        rgba=Gdk.RGBA()
        rgba.parse(color)

        boton=Gtk.Button()
        area=Gtk.DrawingArea()
        area.set_size_request(32,24)
        area.connect("draw",self.on_debuxa,{"color":rgba})
        boton.add(area)
        return boton

class VentanaPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Ejemplo de Stack Layout con Gtk")

        cajaV=Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=6)

        tarjetas=Gtk.Stack()
        tarjetas.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        tarjetas.set_transition_duration(1000)

        #Primera Tarjeta
        checkPulsame=Gtk.CheckButton(label="Pulsame")
        tarjetas.add_titled(checkPulsame,"Pulsame","Check Pulsame")

        #Segunda Tarjeta
        label=Gtk.Label()
        label.set_markup("<big>Esta es una etiqueta elegante</big>")
        tarjetas.add_titled(label,"etiqueta","Una etiqueta")

        #Tercera Tarjeta
        CajaconContenido=objetoColor()
        tarjetas.add_titled(CajaconContenido, "caja", "Caja con contenido")

        #Hace que cada tarjeta funcione como botones
        botonesTarjetas=Gtk.StackSwitcher()
        botonesTarjetas.set_stack(tarjetas)

        cajaV.pack_start(tarjetas,True,True,0)
        cajaV.pack_start(botonesTarjetas,True,True,0)

        self.add(cajaV)

        self.connect("delete-event",Gtk.main_quit)
        self.show_all()

if __name__ == "__main__":
    VentanaPrincipal()
    Gtk.main()