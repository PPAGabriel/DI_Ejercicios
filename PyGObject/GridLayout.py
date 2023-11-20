import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import Gdk


class VentanaPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Primera ventana con Gtk")

        boton1 = self.boton_con_color("red")
        boton2 = self.boton_con_color("yellow")
        boton3 = self.boton_con_color("purple")
        boton4 = self.boton_con_color("green")
        boton5 = self.boton_con_color("blue")
        boton6 = self.boton_con_color("orange")

        grid = Gtk.Grid()
        grid.add(boton1)
        grid.attach(boton2,1,0,2,1)
        grid.attach_next_to(boton3,boton1,Gtk.PositionType.BOTTOM,1,2) #COGE DE REFERENCIA, SIEMPRE Y CUANDO TENGA EL MISMO TAMAÑO
        grid.attach(boton4,1,1,2,1)
        grid.attach(boton5,1,2,1,1)
        grid.attach_next_to(boton6,boton5,Gtk.PositionType.RIGHT,1,1)

        self.add(grid)

        self.connect("delete-event",Gtk.main_quit)
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
    VentanaPrincipal()
    Gtk.main()