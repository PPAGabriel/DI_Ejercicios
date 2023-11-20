import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import Gdk

class VentanaColor(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Ventana de Colores con GTK")

        ## Box almacena los objetos que puedan haber en el entorno grafico
        caja = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
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

        caja.pack_start(cajaColor1, True, True, 5)

        #Segunda Columna
        caja.pack_start(boton4, True, True, 5)

        #Tercera Columna
        cajaColor2.pack_start(boton5, True, True, 5)
        cajaColor2.pack_start(boton6, True, True, 5)

        caja.pack_start(cajaColor2,True,True,5)


        self.add(caja)

        self.connect("delete-event", Gtk.main_quit)

        self.show_all()

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


if __name__ == "__main__":
    VentanaColor()
    Gtk.main()