import gi # Imports necesarios
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from random import randrange

class MainWindow(Gtk.Window): #Herencia de Window
    def __init__(self, data_source):
        super().__init__(title="Ahorcado") # Generamos una ventana con el texto catálogo mediante llamada al constructor de la super clase
        self.set_position(Gtk.WindowPosition.CENTER) # Centramos la ventana al centro una vez se genere
        self.connect("destroy", Gtk.main_quit) # Conectamos el evento destruir con clickar en cerrar la ventana
        self.set_border_width(15) # Ajustamos ancho del borde
        self.set_default_size(800, 800) # Definimos tamaño por defecto
        self.data_source=data_source
        self.juego()




    def click(self, event): # Función que se activa al hacer click en la opción de "Ayuda" y dentro de ayuda en "Acerca de"
       pass

    def getFallos(self, data_source):
        for item in data_source: # Esta clase recibe el elemento data source en el que previamente hemos almacenado la información de la petición GET mandada a la url
           # cell = Cell(item.get("name"), item.get("gtk_image"), item.get("description")) # Mediante un bucle for generamos tantas celdas como items en data_source con sus respectivos parámetros
            pass
        pass

    def juego(self):
        list = ["CASA", "CAMION", "GATO", "ESTERNOCLEIDOMASTOIDEO", "FRUTA", "HIDROGENO", "ORDENADOR"]
        palabra = list[randrange(len(list))]
        fallos=0
        label = self.generarGuiones(palabra)
        entry = Gtk.Entry()
        while fallos < 5:
            box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
            label = Gtk.Label(label=label)
            img = self.generarImagen(fallos)
            box.pack_start(label, False, False, 0)
            box.pack_start(img, False, False, 0)
            box.pack_start(entry, False, False, 0)
            self.add(box)
            fallos = fallos + 1
        pass

    def generarGuiones(self, palabra):
        i = 0
        guiones=""
        while i < len(palabra):
            guiones = guiones + " ____ "
            i = i + 1
        return guiones

    def generarImagen(self, fallos):
        img = Gtk.Image()
        for item in self.data_source:
            if item.get("fallos")==fallos:
                img = item.get("gtk_image")
        return img

    def coincide(self, palabra):
        for item in palabra:
            pass

