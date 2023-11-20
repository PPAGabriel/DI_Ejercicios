import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class VentanaPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Ejemplo con check y radio button con Gtk")

        ## Box almacena los objetos que puedan haber en el entorno grafico
        caja = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 10)
        cajaRbt=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing = 10)

        frame = Gtk.Frame(label="Opciones excluyentes")
        frame.add(cajaRbt)

        caja.pack_start(frame,False,False,2)


        rbtBoton1=Gtk.RadioButton.new_with_label_from_widget(None,"Boton 1")
        rbtBoton1.connect("toggled",self.on_rbtBoton_toggled,"1")
        cajaRbt.pack_start(rbtBoton1,False,False,2)

        rbtBoton2 = Gtk.RadioButton.new_from_widget(rbtBoton1)
        rbtBoton2.set_label("Boton 2")
        rbtBoton2.connect("toggled",self.on_rbtBoton_toggled,"2")
        cajaRbt.pack_start(rbtBoton2, False, False, 2)

        rbtBoton3 = Gtk.RadioButton.new_with_mnemonic_from_widget(rbtBoton1,"_Boton 3")
        rbtBoton3.connect("toggled", self.on_rbtBoton_toggled, "3")
        cajaRbt.pack_start(rbtBoton3, False, False, 2)

        chkBoton4 =  Gtk.CheckButton()
        chkBoton4.set_label("Check 4")
        chkBoton4.connect("toggled",self.on_chkBoton_toggled)
        caja.pack_start(chkBoton4,False,False,2)

        chkBoton5 = Gtk.CheckButton.new_with_label("Check 5")
        chkBoton5.connect("toggled", self.on_chkBoton_toggled)
        caja.pack_start(chkBoton5, False, False, 2)



        self.add(caja)

        self.connect("delete-event", Gtk.main_quit) ## el segundo argumento no debe tener el parentesis de funcion, ya que en ese caso la ejecutaria
        self.show_all()

################################## FUNCIONES ############################################
    def on_rbtBoton_toggled(self,boton,numero):
        if boton.get_active():
            print("Boton",numero,"fue activado")
        else:
            print("Boton",numero,"fue desactivado")

    def on_chkBoton_toggled(self,boton):
        if boton.get_active():
            print(boton.get_label(),"activado")
        else:
            print(boton.get_label(),"desactivado")

###################### MAIN ###############################
if __name__ == "__main__":
    VentanaPrincipal()
    Gtk.main()