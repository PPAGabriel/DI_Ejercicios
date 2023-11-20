import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class VentanaPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Primera ventana con Gtk")

        lblEtiqueta = Gtk.Label(label="Hola! Soy Pikachu")

        imagen = Gtk.Image()
        imagen.set_from_file("pikachu.jpg")
        ## self.add(imagen)

        ## Box almacena los objetos que puedan haber en el entorno grafico
        caja = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 10)

        ## Segun lo que se rellene puede quedar mal
        ## Segun las palabras de Manuel, los que quedan bien son casi todos los de texto
        caja.pack_start(imagen, True, True, 5)
        caja.pack_start(lblEtiqueta, True, True, 5)

        self.textEdit=Gtk.Entry()
        caja.pack_start(self.textEdit,True,True,5)

        btnBoton = Gtk.Button(label = "Pulsa aquí")
        caja.pack_start(btnBoton, False, False, 5)
        self.add(caja)

        btnBoton.connect("clicked", self.on_btn_clicked, lblEtiqueta)
        self.connect("delete-event", Gtk.main_quit) ## el segundo argumento no debe tener el parentesis de funcion, ya que en ese caso la ejecutaria
        self.textEdit.connect("activate",self.on_btn_clicked,lblEtiqueta)

        self.show_all()

    def on_btn_clicked(self,boton,etiqueta):
        if(self.textEdit.get_text()==""):
            etiqueta.set_text("Hola! Soy Pikachu")
        else:
            etiqueta.set_text(self.textEdit.get_text())
            self.textEdit.set_text("")

if __name__ == "__main__":
    VentanaPrincipal()
    Gtk.main()