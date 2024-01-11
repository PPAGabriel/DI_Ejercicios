import pathlib

import gi
import sqlite3 as dbapi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio

class FestraPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Explorador de archivos")

        self.set_default_size(250, 100)
        self.set_border_width(10)

        area= Gtk.FlowBox()
        contenidoCarpeta = pathlib.Path('.')

        for elemento in contenidoCarpeta.iterdir():
            caja = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
            tipo = "folder" if elemento.is_dir() else "text-x-generic"
            icono = Gio.ThemedIcon(name=tipo)
            imagen = Gtk.Image.new_from_gicon(icono, Gtk.IconSize.DIALOG)
            caja.pack_start(imagen, False, False, 0)
            caja.pack_start(Gtk.Label(label=str(elemento.name)), True, True, 0)
            area.add(caja)


        self.add(area)

        self.connect("delete-event", Gtk.main_quit)  ## la el segundo argumento no debe tener el parentesis de funcion, ya que en ese caso la ejecutaria

        self.show_all()

if __name__ == "__main__":
    FestraPrincipal()
    Gtk.main()