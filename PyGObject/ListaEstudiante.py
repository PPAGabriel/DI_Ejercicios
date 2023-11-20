import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

# App that save students data in a list
class VentanaPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Estudiapp")
        self.set_default_size(600, 300)

        #list of students
        self.studentsList=[]

        # Box where the widgets are stored
        mainBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        boxData=Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

        boxModules=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        boxCOD=Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        boxPROG=Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        boxSI=Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

        boxModules.pack_start(boxCOD,False,False,2)
        boxModules.pack_start(boxPROG,False,False,2)
        boxModules.pack_start(boxSI,False,False,2)

        frame1=Gtk.Frame(label="Datos del estudiante")
        frame1.add(boxData)

        frame2=Gtk.Frame(label="Modulos")
        frame2.add(boxModules)

        mainBox.pack_start(frame1,False,False,5)
        mainBox.pack_start(frame2,False,False,5)

        # Entry where the user inputs the name and last name
        self.labelName=Gtk.Label(label="Nombre:")
        boxData.pack_start(self.labelName, False, False, 5)
        self.nameEntry = Gtk.Entry()
        self.nameEntry.set_placeholder_text("Introduzca el nombre")
        self.nameEntry.set_max_length(10)
        boxData.pack_start(self.nameEntry, False, False, 5)

        self.labelLastName = Gtk.Label(label="Apellido:")
        boxData.pack_start(self.labelLastName, False, False, 5)
        self.lastNameEntry = Gtk.Entry()
        self.lastNameEntry.set_placeholder_text("Introduzca el apellido")
        self.lastNameEntry.set_max_length(10)
        boxData.pack_start(self.lastNameEntry, False, False, 5)

        #Entry where the user inputs the grade of each module and if its bilingual, can check it

        #COD Module
        self.labelCOD = Gtk.Label(label="COD:")
        self.labelCOD.set_width_chars(5)
        boxCOD.pack_start(self.labelCOD, False, False, 5)
        self.gcodEntry = Gtk.Entry()
        self.gcodEntry.set_width_chars(2)
        self.gcodEntry.set_max_length(2)
        boxCOD.pack_start(self.gcodEntry, False, False, 5)
        self.checkCOD=Gtk.CheckButton()
        boxCOD.pack_start(self.checkCOD, False, False, 5)
        self.labelCOD = Gtk.Label(label=" Bilingüe")
        boxCOD.pack_start(self.labelCOD, False, False, 5)

        #PROG Module
        self.labelPROG = Gtk.Label(label="PROG:")
        self.labelPROG.set_width_chars(5)
        boxPROG.pack_start(self.labelPROG, False, False, 5)
        self.gprogEntry = Gtk.Entry()
        self.gprogEntry.set_width_chars(2)
        self.gprogEntry.set_max_length(2)
        boxPROG.pack_start(self.gprogEntry, False, False, 5)
        self.checkPROG=Gtk.CheckButton()
        boxPROG.pack_start(self.checkPROG, False, False, 5)
        self.labelPROG = Gtk.Label(label=" Bilingüe")
        boxPROG.pack_start(self.labelPROG, False, False, 5)

        #SI Module
        self.labelSI = Gtk.Label(label="SI:")
        self.labelSI.set_width_chars(5)
        boxSI.pack_start(self.labelSI, False, False, 5)
        self.gsiEntry = Gtk.Entry()
        self.gsiEntry.set_width_chars(2)
        self.gsiEntry.set_max_length(2)
        boxSI.pack_start(self.gsiEntry, False, False, 5)
        self.checkSI=Gtk.CheckButton()
        boxSI.pack_start(self.checkSI, False, False, 5)
        self.labelSI = Gtk.Label(label=" Bilingüe")
        boxSI.pack_start(self.labelSI, False, False, 5)

        # Button that saves the data
        self.saveButton = Gtk.Button(label="Guardar")
        self.saveButton.connect("clicked", self.on_saveButton_clicked)

        mainBox.pack_start(self.saveButton, False, False, 5)


        self.connect("delete-event", Gtk.main_quit)

        self.add(mainBox)
        self.show_all()

    # Function that saves the data
    def on_saveButton_clicked(self, button):
        # Get the data from the entries
        name = self.nameEntry.get_text()
        lastName = self.lastNameEntry.get_text()
        gcod = self.gcodEntry.get_text()
        gprog = self.gprogEntry.get_text()
        gsi = self.gsiEntry.get_text()

        # Check if the data is correct
        if name == "" or lastName == "" or gcod == "" or gprog == "" or gsi == "":
            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR, Gtk.ButtonsType.OK, "Error")
            dialog.format_secondary_text("Debe rellenar todos los campos")
            dialog.run()
            dialog.destroy()
        else:
            # Check if the grade is correct
            if int(gcod) < 0 or int(gcod) > 10 or int(gprog) < 0 or int(gprog) > 10 or int(gsi) < 0 or int(gsi) > 10:
                dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR, Gtk.ButtonsType.OK, "Error")
                dialog.format_secondary_text("Las notas deben estar entre 0 y 10")
                dialog.run()
                dialog.destroy()
            else:
                # Check if the name and last name are correct
                if name.isalpha() and lastName.isalpha():
                    # Check if the student is bilingual
                    if self.checkCOD.get_active():
                        codChecked = "True"
                    else:
                        codChecked = "False"

                    if self.checkPROG.get_active():
                        progChecked = "True"
                    else:
                        progChecked = "False"

                    if self.checkSI.get_active():
                        siChecked = "True"
                    else:
                        siChecked = "False"

                    # Add the student data to the list

                    self.codModule = ["COD",codChecked, gcod]
                    self.progModule = ["PROG",progChecked, gprog]
                    self.siModule = ["SI",siChecked, gsi]

            self.studentData = [name, lastName, self.codModule, self.progModule, self.siModule]
            self.studentsList.append(self.studentData)

        # Show the student saved
        for student in self.studentsList:
            print(student)

if __name__ == "__main__":
    VentanaPrincipal()
    Gtk.main()