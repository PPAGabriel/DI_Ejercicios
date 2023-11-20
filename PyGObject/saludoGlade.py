import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk


class VentanaPrincipal():
    def __init__(self):

        builder=Gtk.Builder()
        builder.add_from_file("saludoGlade.glade")

        wndFestraPrincipal=builder.get_object("wndFiestraPrincipal")
        self.lblEtiqueta=builder.get_object("lblEtiqueta")
        self.txtName=builder.get_object("txtName")
        self.btnSaudo=builder.get_object("btnSaudo")
        sinais={
            "on_btnSaudo_clicked" : self.on_btnSaudo_clicked,
            "on_txtName_activate" : self.on_txtName_activate,
            "quit_project" : Gtk.main_quit
        }
        builder.connect_signals(sinais)


    def on_btnSaudo_clicked(self,boton):
        self.lblEtiqueta.set_text(self.txtName.get_text())

    def on_txtName_activate(self,entrada):
        self.lblEtiqueta.set_text(entrada.get_text())

if __name__ == "__main__":
    VentanaPrincipal()
    Gtk.main()