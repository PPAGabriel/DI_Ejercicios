from tkinter import *
from tkinter import messagebox as MessageBox
import gi
import sqlite3 as dbapi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Pango, Gdk,GLib

class FestraPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Ejemplo TreeView filtrado")

        self.set_default_size(400, 100)
        self.set_border_width(10)
        cajaPrincipal=Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=4)
        cajaV1=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)

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

        #Creamos un scroll
        self.scroll=Gtk.ScrolledWindow()
        self.scroll.set_policy(Gtk.PolicyType.NEVER,Gtk.PolicyType.AUTOMATIC)
        self.scroll.set_size_request(100,132)

        #trvDatosUsuarios=Gtk.TreeView(model=modelo)
        self.trvDatosUsuarios=Gtk.TreeView(model=modelo_filtrado)
        cambiar=self.trvDatosUsuarios.get_selection()
        cambiar.connect("changed",self.on_obxectoSeleccion_changed)

        for i,tituloColumna in enumerate(["DNI","Nombre"]):
            celda=Gtk.CellRendererText()
            columna=Gtk.TreeViewColumn(tituloColumna,celda,text=i)
            self.trvDatosUsuarios.append_column(columna)

        celda=Gtk.CellRendererProgress()
        columna=Gtk.TreeViewColumn("Edad",celda,value=2)
        self.trvDatosUsuarios.append_column(columna)

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
        self.trvDatosUsuarios.append_column(columna)

        self.scroll.add(self.trvDatosUsuarios)
        cajaV1.pack_start(self.scroll,True,True,0)

        cajaH=Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,spacing=2)
        cajaV1.pack_start(cajaH,True,True,0)

        rbtAll=Gtk.RadioButton(label="All",group=None)
        rbtHome1=Gtk.RadioButton(label="Home",group=rbtAll)
        rbtMuller1=Gtk.RadioButton(label="Muller",group=rbtAll)
        rbtOutros1=Gtk.RadioButton(label="Outros",group=rbtAll)

        cajaH.pack_start(rbtAll,True,True,0)
        cajaH.pack_start(rbtHome1,True,True,0)
        cajaH.pack_start(rbtMuller1,True,True,0)
        cajaH.pack_start(rbtOutros1,True,True,0)

        rbtAll.connect("toggled",self.on_xenero_toggled,"None",modelo_filtrado)
        rbtHome1.connect("toggled",self.on_xenero_toggled,"Home",modelo_filtrado)
        rbtMuller1.connect("toggled",self.on_xenero_toggled,"Muller",modelo_filtrado)
        rbtOutros1.connect("toggled",self.on_xenero_toggled,"Outros",modelo_filtrado)

        cajaPrincipal.pack_start(cajaV1,True,True,0)

        # Agregamos un nuevo apartado
        cajaV2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)

        cajaV2_H1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=4)
        cajaV2_H1.set_size_request(50,20)
        lblNome = Gtk.Label(label="Nome")
        cajaV2_H1.pack_start(lblNome, True, True, 0)
        self.txt1 = Gtk.Entry()
        self.txt1.set_tooltip_text("Nombre de la persona a crear ou modificar")
        #imposibilitamos que se pueda editar el nombre
        self.txt1.set_sensitive(False)
        cajaV2_H1.pack_start(self.txt1, True, True, 0)
        lblDNI = Gtk.Label(label="DNI")
        cajaV2_H1.pack_start(lblDNI, True, True, 0)
        self.txt2 = Gtk.Entry()
        self.txt2.set_tooltip_text("DNI de la persona a crear o modificar")
        #imposibilitamos que se pueda editar el DNI
        self.txt2.set_sensitive(False)
        cajaV2_H1.pack_start(self.txt2, True, True, 0)

        cajaV2_H2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=4)
        cajaV2_H2.set_size_request(50,20)

        #Edad
        lblEdade = Gtk.Label(label="Edade")
        cajaV2_H2.pack_start(lblEdade, True, True, 0)
        self.txt3 = Gtk.Entry()
        self.txt3.set_tooltip_text("Edad de la persona a crear o modificar")
        #imposibilitamos que se pueda editar la edad
        self.txt3.set_sensitive(False)
        self.txt3.set_width_chars(2)
        cajaV2_H2.pack_start(self.txt3, True, True, 0)

        #Genero: radio buttons
        lblXenero = Gtk.Label(label="Xenero")
        cajaV2_H2.pack_start(lblXenero, True, True, 0)

        cajaV2_H2_V = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        self.rbtHome2 = Gtk.RadioButton(label="Home", group=rbtHome1)
        self.rbtHome2.set_sensitive(False)
        self.rbtHome2.connect("toggled",self.on_xenero_toggled2,"Home")
        cajaV2_H2_V.pack_start(self.rbtHome2, True, True, 0)
        self.rbtMuller2 = Gtk.RadioButton(label="Muller", group=rbtHome1)
        self.rbtMuller2.set_sensitive(False)
        self.rbtMuller2.connect("toggled",self.on_xenero_toggled2,"Muller")
        cajaV2_H2_V.pack_start(self.rbtMuller2, True, True, 0)
        self.rbtOutros2 = Gtk.RadioButton(label="Outros", group=rbtHome1)
        self.rbtOutros2.set_sensitive(False)
        self.rbtOutros2.connect("toggled",self.on_xenero_toggled2,"Outros")
        cajaV2_H2_V.pack_start(self.rbtOutros2, True, True, 0)
        cajaV2_H2.pack_start(cajaV2_H2_V, True, True, 0)

        #Fallecido
        lblFallecido = Gtk.Label(label="Fallecido")
        cajaV2_H2.pack_start(lblFallecido, True, True, 0)
        self.chkFallecido = Gtk.CheckButton()
        self.chkFallecido.set_sensitive(False)
        cajaV2_H2.pack_start(self.chkFallecido, True, True, 0)

        #Barra de Progreso
        self.barraProgreso = Gtk.ProgressBar()
        cajaV2_H2.pack_start(self.barraProgreso, True, True, 0)
        self.contadorActividad = 100
        self.temporizador=GLib.timeout_add(100,self.on_contador,None)

        cajaV2_H3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=4)

        #Botones
        self.flag=0

        self.btnNovo = Gtk.Button.new_with_mnemonic("_Novo") #el atajo es la primera letra de la palabra (se aplica con alt+letra)
        self.btnNovo.connect("clicked", self.on_novo_clicked, modelo)

        self.btnEditar = Gtk.Button.new_with_mnemonic("_Editar") #el atajo es la primera letra de la palabra (se aplica con alt+letra)
        self.btnEditar.connect("clicked", self.on_editar_clicked, modelo)

        self.btnAceptar = Gtk.Button.new_with_mnemonic("_Aceptar") #el atajo es la primera letra de la palabra (se aplica con alt+letra)
        self.btnAceptar.connect("clicked", self.on_aceptar_clicked, modelo,modelo_filtrado)

        self.btnCancelar = Gtk.Button.new_with_mnemonic("_Cancelar") #el atajo es la primera letra de la palabra (se aplica con alt+letra)
        self.btnCancelar.connect("clicked", self.on_cancelar_clicked, modelo,modelo_filtrado)

        cajaV2_H3.pack_start(self.btnNovo, True, True, 0)
        cajaV2_H3.pack_start(self.btnEditar, True, True, 0)
        cajaV2_H3.pack_start(self.btnAceptar,True,True,0)
        cajaV2_H3.pack_start(self.btnCancelar, True, True, 0)

        cajaV2_H4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=4)

        #Text View
        self.txtViewConsola = Gtk.TextView()
        self.bufferTexto=Gtk.TextBuffer()
        self.txtViewConsola.set_buffer(self.bufferTexto)
        self.txtViewConsola.set_sensitive(False)
        cajaV2_H4.pack_start(self.txtViewConsola, True, True, 0)

        cajaV2.pack_start(cajaV2_H1, True, True, 0)
        cajaV2.pack_start(cajaV2_H2, True, True, 0)
        cajaV2.pack_start(cajaV2_H3,True,True,0)
        cajaV2.pack_start(cajaV2_H4, True, True, 0)

        cajaPrincipal.pack_start(cajaV2, True, True, 0)

        self.add(cajaPrincipal)

        self.connect("delete-event",Gtk.main_quit)

        self.show_all()
        self.btnAceptar.hide()
        self.btnCancelar.hide()
        self.barraProgreso.hide()


    def on_contador(self,datosExtendidosUsuario):
        if self.contadorActividad<100:
            self.contadorActividad+=10
            self.barraProgreso.set_fraction(self.contadorActividad/100)
        else:
            self.barraProgreso.hide()
        return True

    def on_obxectoSeleccion_changed(self, seleccion):
        (modelo, fila) = seleccion.get_selected()

        # Verificar si fila no es None
        if fila is not None:
            # Verificar si modelo[fila] es None
            if modelo[fila] is not None:
                # Verificar cada campo antes de asignarlo al Entry
                dni = modelo[fila][0] if modelo[fila][0] is not None else ""
                nombre = modelo[fila][1] if modelo[fila][1] is not None else ""
                edad = str(modelo[fila][2]) if modelo[fila][2] is not None else ""

                self.txt1.set_text(nombre)
                self.txt2.set_text(dni)
                self.txt3.set_text(edad)

                if modelo[fila][3] == "Home":
                    self.rbtHome2.set_active(True)
                elif modelo[fila][3] == "Muller":
                    self.rbtMuller2.set_active(True)
                elif modelo[fila][3] == "Outros":
                    self.rbtOutros2.set_active(True)

                if modelo[fila][4] == True:
                    self.chkFallecido.set_active(True)
                else:
                    self.chkFallecido.set_active(False)
            else:
                # Limpiar los Entry si el modelo[fila] es None
                self.txt1.set_text("")
                self.txt2.set_text("")
                self.txt3.set_text("")
                # Desactivar los botones de opción
                self.rbtHome2.set_active(False)
                self.rbtMuller2.set_active(False)
                self.rbtOutros2.set_active(False)
        else:
            # Limpiar los Entry si fila es None
            self.txt1.set_text("")
            self.txt2.set_text("")
            self.txt3.set_text("")
            # Desactivar los botones de opción
            self.rbtHome2.set_active(False)
            self.rbtMuller2.set_active(False)
            self.rbtOutros2.set_active(False)

    def on_novo_clicked(self, boton, modelo):
        #desaparece el boton de editar
        if self.flag==0:

            self.trvDatosUsuarios.set_sensitive(False)

            self.txt1.set_sensitive(True)
            self.txt2.set_sensitive(True)
            self.txt3.set_sensitive(True)
            self.rbtHome2.set_sensitive(True)
            self.rbtMuller2.set_sensitive(True)
            self.rbtOutros2.set_sensitive(True)
            self.chkFallecido.set_sensitive(True)

            # vaciar los campos
            self.txt1.set_text("")
            self.txt2.set_text("")
            self.txt3.set_text("")

            self.btnEditar.hide()
            self.btnNovo.hide()
            self.btnAceptar.show()
            self.btnCancelar.show()
            self.flag=1

    def on_editar_clicked(self, boton, modelo):
        if self.txt1.get_text() != "" and self.txt2.get_text() != "" and self.txt3.get_text() != "":
            self.txt1.set_sensitive(True)
            self.txt2.set_sensitive(True)
            self.txt3.set_sensitive(True)
            self.rbtHome2.set_sensitive(True)
            self.rbtMuller2.set_sensitive(True)
            self.rbtOutros2.set_sensitive(True)
            self.chkFallecido.set_sensitive(True)

            self.btnEditar.hide()
            self.btnNovo.hide()
            self.btnAceptar.show()
            self.btnCancelar.show()
            self.flag=2

    def on_aceptar_clicked(self, boton, modelo,modelo_filtrado):

        if self.flag==2:

            self.txt1.set_sensitive(False)
            self.txt2.set_sensitive(False)
            self.txt3.set_sensitive(False)
            self.rbtHome2.set_sensitive(False)
            self.rbtMuller2.set_sensitive(False)
            self.rbtOutros2.set_sensitive(False)
            self.chkFallecido.set_sensitive(False)



            #aqui se hace el update
            try:
                if self.chkFallecido.get_active():
                    self.fallecido = True
                else:
                    self.fallecido = False

                database = dbapi.connect("baseDatos2.dat")
                cursor = database.cursor()
                cursor.execute("update usuarios set nome = ?, edade = ?, genero=?,fallecido=? where dni = ?", (self.txt1.get_text(), self.txt3.get_text(), self.xeneroActivo,self.fallecido,self.txt2.get_text()))
                database.commit()

                cursor.close()
                database.close()

                # Obtener el modelo sin filtrar
                modelo.clear()
                try:
                    database = dbapi.connect("baseDatos2.dat")
                    cursor = database.cursor()
                    cursor.execute("select * from usuarios")

                    for usuario in cursor:
                        modelo.append(usuario)

                except dbapi.StandardError as e:
                    print("Error al cargar la base de datos")
                finally:
                    cursor.close()
                    database.close()

                # Refiltrar el modelo filtrado
                modelo_filtrado.refilter()
                self.barraProgreso.show()
                self.contadorActividad = 0

            except dbapi.DatabaseError as e:
                print(e)

        elif self.flag==1:

            self.txt1.set_sensitive(False)
            self.txt2.set_sensitive(False)
            self.txt3.set_sensitive(False)
            self.rbtHome2.set_sensitive(False)
            self.rbtMuller2.set_sensitive(False)
            self.rbtOutros2.set_sensitive(False)
            self.chkFallecido.set_sensitive(False)



            #aqui se hace agrega el nuevo usuario
            try:
                if self.chkFallecido.get_active():
                    self.fallecido = True
                else:
                    self.fallecido = False

                #comprobar que el dni tiene el formato correcto

                css_provider = Gtk.CssProvider()
                css_provider.load_from_path('style.css')
                context = Gtk.StyleContext()
                screen = Gdk.Screen.get_default()

                if len(self.txt2.get_text())==9:
                    if self.txt2.get_text()[0:8].isdigit() and self.txt2.get_text()[8].isalpha() and self.txt2.get_text()[8]:

                        self.txt2.set_name("correct")

                        context.add_provider_for_screen(screen, css_provider,
                                                        Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

                        self.btnEditar.show()
                        self.btnNovo.show()
                        self.btnAceptar.hide()
                        self.btnCancelar.hide()
                        self.flag = 0

                        #Hacer mayuscula la letra del dni:
                        dniMayuscula=self.txt2.get_text()[0:8]+self.txt2.get_text()[8].upper()

                        database = dbapi.connect("baseDatos2.dat")
                        cursor = database.cursor()
                        cursor.execute("insert into usuarios values (?,?,?,?,?)", (
                        dniMayuscula, self.txt1.get_text(), self.txt3.get_text(), self.xeneroActivo,
                        self.fallecido))
                        database.commit()

                        cursor.close()
                        database.close()

                        # Obtener el modelo sin filtrar
                        modelo.clear()
                        try:
                            database = dbapi.connect("baseDatos2.dat")
                            cursor = database.cursor()
                            cursor.execute("select * from usuarios")

                            for usuario in cursor:
                                modelo.append(usuario)

                        except dbapi.StandardError as e:
                            print("Error al cargar la base de datos")
                        finally:
                            cursor.close()
                            database.close()

                        # Refiltrar el modelo filtrado
                        modelo_filtrado.refilter()
                        self.barraProgreso.show()
                        self.contadorActividad = 0

                        self.trvDatosUsuarios.set_sensitive(True)

                    else:
                        self.txt2.set_name("error")

                        context.add_provider_for_screen(screen, css_provider,
                                                        Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)


                        txtError="El DNI debe tener 8 numeros y una letra"
                        self.bufferTexto.insert_at_cursor(txtError+"\n",len(txtError+"\n"))
                        self.txt1.set_sensitive(True)
                        self.txt2.set_sensitive(True)
                        self.txt3.set_sensitive(True)
                        self.rbtHome2.set_sensitive(True)
                        self.rbtMuller2.set_sensitive(True)
                        self.rbtOutros2.set_sensitive(True)
                        self.chkFallecido.set_sensitive(True)

                else:
                    txtError="El DNI requiere de 9 caracteres"
                    self.bufferTexto.insert_at_cursor(txtError+"\n",len(txtError+"\n"))

                    self.txt2.set_name("error")

                    context.add_provider_for_screen(screen, css_provider,
                                                    Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

                    self.txt1.set_sensitive(True)
                    self.txt2.set_sensitive(True)
                    self.txt3.set_sensitive(True)
                    self.rbtHome2.set_sensitive(True)
                    self.rbtMuller2.set_sensitive(True)
                    self.rbtOutros2.set_sensitive(True)
                    self.chkFallecido.set_sensitive(True)
            except dbapi.DatabaseError as e:
                print(e)




    def on_cancelar_clicked(self, boton, modelo,modelo_filtrado):

        self.trvDatosUsuarios.set_sensitive(True)

        self.txt1.set_sensitive(False)
        self.txt2.set_sensitive(False)
        self.txt3.set_sensitive(False)
        self.rbtHome2.set_sensitive(False)
        self.rbtMuller2.set_sensitive(False)
        self.rbtOutros2.set_sensitive(False)
        self.chkFallecido.set_sensitive(False)

        self.btnEditar.show()
        self.btnNovo.show()
        self.btnAceptar.hide()
        self.btnCancelar.hide()
        self.flag = 0

        # Obtener el modelo sin filtrar
        modelo.clear()
        try:
            database = dbapi.connect("baseDatos2.dat")
            cursor = database.cursor()
            cursor.execute("select * from usuarios")

            for usuario in cursor:
                modelo.append(usuario)

        except dbapi.StandardError as e:
            print("Error al cargar la base de datos")
        finally:
            cursor.close()
            database.close()

        # Refiltrar el modelo filtrado
        modelo_filtrado.refilter()


    ##############################################################################
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

    def on_xenero_toggled2(self, botonSeleccionado, xenero):
        if botonSeleccionado.get_active():
            self.xeneroActivo = xenero

    def filtro_usuarios_xenero(self,modelo,fila,datos):
        if (self.filtradoXenero is None or self.filtradoXenero=="None"):
            return True
        else:
            return modelo[fila][3]==self.filtradoXenero





if __name__ == "__main__":
    FestraPrincipal()
    Gtk.main()