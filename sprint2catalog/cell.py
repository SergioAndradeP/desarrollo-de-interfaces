import gi                           # Imports necesarios
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from detail_window import Detail
from gi.repository import GdkPixbuf

# Esta clase serán celdas que incluiremos en una FlowBox
class Cell(Gtk.EventBox): # Herencia de EventBox necesaria para hacer que Cell sea como dicho elemento
    name = None           # Variables de clase
    image = Gtk.Image()   # Variable de clase tipo Imagen
    descripcion = None

    def __init__(self, name, image): # Hacemos que cell reciba los parámetros nombre e imagen
        super().__init__()           # Llamada al constructor de la super clase para generar una ventana
        self.name = name             # Igualamos dichos parámetros a las variables de clase
        self.image = image
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4) # Generamos una box vertical
        box.pack_start(Gtk.Label(label=name), False, False, 0) # Insertamos en la box una label que contiene el texto de la variable de clase "name"
        box.pack_start(image, True, True, 0)  # Insertamos la imagen en la box
        self.add(box) # Añadimos la box a la ventana generada
        self.connect("button-release-event", self.on_click) # Conectamos la acción de clickar y soltar el botón con las imagenes

    def on_click(self, widget, event): # Función on_click conectada que se llama mediante click en las imagenes
        self.image = self.getImage() # Igualamos la variable de clase image a una imagen devuelta por la función getImage()
        self.asignar_desripcion() # Llamada a la funcion asignar_descripcion() lo cual asigna la descripcion a description
        win = Detail(self.name, self.image, self.descripcion) # Generamos una detail window pasándole los parámetros necesarios
        win.show_all() # Mostramos la ventana
        Gtk.main()   # Dejamos que la ventana se mantenga abierta mediante esta función

    def asignar_desripcion(self): # Función que asigna un String a la variable de clase desciption en función del nombre de la imagen
        if self.name=="Shaco":
            self.descripcion="La skin por defecto de Shaco"
        elif self.name=="Shaco enmascarado":
            self.descripcion="La skin de Shaco enmascarado precio: 975 Rp"
        elif self.name=="Shaco estrella oscura":
            self.descripcion="La skin de Shaco estrella oscura precio: 1350 Rp"
        elif self.name == "Shaco arcano":
            self.descripcion = "La skin de Shaco arcano precio: 1350 Rp"
        elif self.name == "Shaco pesadilla en la ciudad sin ley":
            self.descripcion="La skin de Shaco pesadilla en la ciudad sin ley precio: 1350 Rp"

    def getImage(self): # Función que devuelve la imagen correspondiente en función del nombre de la imagen haciendo uso del GdkPixbuf
        img = Gtk.Image()
        pixbuf = None
        if self.name == "Shaco":
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/shaco_base.jfif", 200, 200, False)
        elif self.name == "Shaco enmascarado":
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/shaco_masked.jfif", 200, 200, False)
        elif self.name == "Shaco estrella oscura":
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/shaco_darkstar.jfif", 200, 200, False)
        elif self.name == "Shaco arcano":
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/shaco_arcane.jfif", 200, 200, False)
        elif self.name == "Shaco pesadilla en la ciudad sin ley":
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/shaco_crime_city_nightmare.jfif", 200, 200, False)
        img.set_from_pixbuf(pixbuf)
        return img
