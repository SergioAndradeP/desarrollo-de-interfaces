import gi # Imports necesarios
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import GdkPixbuf

class MainWindow(Gtk.Window): #Herencia de Window

    def __init__(self, data_source):
        super().__init__(title="Ahorcado") # Generamos una ventana con el texto catálogo mediante llamada al constructor de la super clase
        self.set_position(Gtk.WindowPosition.CENTER) # Centramos la ventana al centro una vez se genere
        self.connect("destroy", Gtk.main_quit) # Conectamos el evento destruir con clickar en cerrar la ventana
        self.set_border_width(15) # Ajustamos ancho del borde
        self.set_default_size(800, 800) # Definimos tamaño por defecto

    def click(self, event): # Función que se activa al hacer click en la opción de "Ayuda" y dentro de ayuda en "Acerca de"
       pass

    def getFallos(self):
        pass