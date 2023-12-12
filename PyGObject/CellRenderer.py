import gi
import sqlite3 as dbapi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class FestraPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Ejemplo Treeview con CellRendererPixbuf")

        self.set_default_size(250, 100)
        self.set_border_width(10)
        caja = Gtk.Box (orientation=Gtk.Orientation.VERTICAL, spacing=4)

        modelo = Gtk.ListStore(str, str)
        modelo.append(("Nuevo", "document-new"))
        modelo.append(("Abrir", "document-open"))
        modelo.append(("Guardar", "document-save)"))

        treeView = Gtk.TreeView(model=modelo)

        celdaTexto = Gtk.CellRendererText()
        columnaTexto = Gtk.TreeViewColumn("Texto", celdaTexto, text=0)
        treeView.append_column(columnaTexto)

        celdaImagen = Gtk.CellRendererPixbuf()
        columnaImagen = Gtk.TreeViewColumn("Imagen", celdaImagen, icon_name=1)
        treeView.append_column(columnaImagen)
        caja.pack_start(treeView, True, True, 0)




        self.add(caja)

        self.connect("delete-event", Gtk.main_quit)  ## la el segundo argumento no debe tener el parentesis de funcion, ya que en ese caso la ejecutaria

        self.show_all()

if __name__ == "__main__":
    FestraPrincipal()
    Gtk.main()