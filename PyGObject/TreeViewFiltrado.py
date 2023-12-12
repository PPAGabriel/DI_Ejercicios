import gi
import sqlite3 as dbapi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Pango

class FestraPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Ejemplo TreeView filtrado")

        self.set_default_size(250, 100)
        self.set_border_width(10)
        caja=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)

        self.filtradoXenero="None"
        modelo=Gtk.ListStore(str,str,int,str,bool)
        modelo_filtrado=modelo.filter_new()
        modelo_filtrado.set_visible_func(self.filtro_usuarios_xenero)

        try:
            database=dbapi.connect("baseDatos2.dat")
            cursor=database.cursor()
            cursor.execute("select * from usuarios")

            for usuario in cursor:
                modelo.append(usuario)

        except dbapi.StandardError as e:
            print("Error al cargar la base de datos")
        finally:
            cursor.close()
            database.close()

        #trvDatosUsuarios=Gtk.TreeView(model=modelo)
        trvDatosUsuarios=Gtk.TreeView(model=modelo_filtrado)

        for i,tituloColumna in enumerate(["DNI","Nombre"]):
            celda=Gtk.CellRendererText()
            columna=Gtk.TreeViewColumn(tituloColumna,celda,text=i)
            trvDatosUsuarios.append_column(columna)

        celda=Gtk.CellRendererProgress()
        columna=Gtk.TreeViewColumn("Edad",celda,value=2)
        trvDatosUsuarios.append_column(columna)

        modeloCombo=Gtk.ListStore(str)
        modeloCombo.append(["Home",])
        modeloCombo.append(["Muller",])
        modeloCombo.append(["Outros",])
        celda=Gtk.CellRendererCombo()
        celda.set_property("editable",True)
        celda.props.model=modeloCombo
        #celda.set_property("model",modeloCombo)
        celda.set_property("text-column",0)
        celda.set_property("has-entry",False)

        #linea nueva (hay que dar el nuevo modelo, porque sino coge los indices del modelo original)
        celda.connect("edited",self.on_celda_edited,modelo_filtrado,3)

        columna=Gtk.TreeViewColumn("Genero",celda,text=3)
        trvDatosUsuarios.append_column(columna)

        caja.pack_start(trvDatosUsuarios,True,True,0)

        cajaH=Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,spacing=2)
        caja.pack_start(cajaH,True,True,0)

        rbtAll=Gtk.RadioButton(label="All",group=None)
        rbtHome=Gtk.RadioButton(label="Home",group=rbtAll)
        rbtMuller=Gtk.RadioButton(label="Muller",group=rbtAll)
        rbtOutros=Gtk.RadioButton(label="Outros",group=rbtAll)

        cajaH.pack_start(rbtAll,True,True,0)
        cajaH.pack_start(rbtHome,True,True,0)
        cajaH.pack_start(rbtMuller,True,True,0)
        cajaH.pack_start(rbtOutros,True,True,0)

        rbtAll.connect("toggled",self.on_xenero_toggled,"None",modelo_filtrado)
        rbtHome.connect("toggled",self.on_xenero_toggled,"Home",modelo_filtrado)
        rbtMuller.connect("toggled",self.on_xenero_toggled,"Muller",modelo_filtrado)
        rbtOutros.connect("toggled",self.on_xenero_toggled,"Outros",modelo_filtrado)

        self.add(caja)

        self.connect("delete-event",Gtk.main_quit)

        self.show_all()

    def on_celda_edited(self,celda,fila,texto,modelo,indice):
        modelo[fila][indice]=texto
        try:
            baseDatos=dbapi.connect("baseDatos2.dat")
            cursor=baseDatos.cursor()
            cursor.execute("UPDATE usuarios set xenero=? where dni=?",(texto,modelo[fila][0]))
            baseDatos.commit()
        except dbapi.DatabaseError as e:
            print(e)

    def on_xenero_toggled(self,botonSeleccionado,xenero,modelo):
        if botonSeleccionado.get_active():
            self.filtradoXenero=xenero
            modelo.refilter()

    def filtro_usuarios_xenero(self,modelo,fila,datos):
        if (self.filtradoXenero is None or self.filtradoXenero=="None"):
            return True
        else:
            return modelo[fila][3]==self.filtradoXenero




if __name__ == "__main__":
    FestraPrincipal()
    Gtk.main()