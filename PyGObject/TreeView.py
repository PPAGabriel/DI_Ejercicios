import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Pango

columnas = ("Nombre", "Apellido", "Numero de teléfono")
agendaTelefonica = (("Pepe", "Pérez", "986 444 555"),
                    ("Ana", "Yañéz", "985 333 777"),
                    ("Roque", "Díz", "987 222 889"),
                    )


class FestraPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Ejemplo listin telefonico con Treeview")

        self.set_default_size(250, 100)
        self.set_border_width(10)

        # Establecemos el tipo que tendra en cada columna
        modelo = Gtk.ListStore(str, str, str)

        for usuario in agendaTelefonica:
            modelo.append(usuario)
        vistaVerdista = Gtk.TreeView(model=modelo)
        for i, nombreColumna in enumerate(columnas):
            celda = Gtk.CellRendererText()
            if i == 0:
                celda.props.weight_set = True
                celda.props.weight = Pango.Weight.BOLD
            col = Gtk.TreeViewColumn(nombreColumna, celda, text=i)
            vistaVerdista.append_column(col)

        """
        El tema es que esto tiene varias cosas que darle.

        Darle un modelo, luego el treeview, luego un Gtk.TreeviewColumn, y luego los celdas
        """

        ## Box almacena los objetos que puedan haber en el entorno grafico
        caja = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

        caja.pack_start(vistaVerdista, True, True, 0)

        self.add(caja)

        self.connect("delete-event",
                     Gtk.main_quit)  ## la el segundo argumento no debe tener el parentesis de funcion, ya que en ese caso la ejecutaria

        self.show_all()


if __name__ == "__main__":
    FestraPrincipal()
    Gtk.main()