import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class FilaListBoxConDatos(Gtk.ListBoxRow):
    def __init__(self, palabra):
        super().__init__()
        self.palabra = palabra
        self.add(Gtk.Label(label=palabra))
class VentanaColor(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Ventana de Colores con GTK")

        ## Box almacena los objetos que puedan haber en el entorno grafico
        caja = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

        listBox=Gtk.ListBox()
        caja.pack_start(listBox,True,True,0)

        elementos="Esta es una cadena para ordenar con ListBox, para el ListBox".split()

        for palabra in elementos:
            listBox.add(FilaListBoxConDatos(palabra))

        def funcion_ordenacion(fila1,fila2):
            return fila1.palabra.lower() > fila2.palabra.lower()

        def funcion_filtrado(fila):
            return False if fila.palabra=="ListBox" else True

        listBox.set_sort_func(funcion_ordenacion)
        listBox.set_filter_func(funcion_filtrado)
        listBox.connect("row-activated",self.on_row_activated)


        self.add(caja)

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def on_row_activated(self,control,fila):
        print(fila.palabra)


if __name__ == "__main__":
    VentanaColor()
    Gtk.main()