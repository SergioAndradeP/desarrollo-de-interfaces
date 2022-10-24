import copy

import gi                           # Imports necesarios
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from detail_window import Detail
from gi.repository import GdkPixbuf

# Esta clase serán celdas que incluiremos en una FlowBox
class Cell(Gtk.EventBox): # Herencia de EventBox necesaria para hacer que Cell sea como dicho elemento

    def __init__(self, name, image, description): # Hacemos que cell reciba los parámetros nombre e imagen
        super().__init__()           # Llamada al constructor de la super clase para generar una ventana
        self.name = name             # Igualamos dichos parámetros a las variables de clase
        self.image = image
        self.description = description
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4) # Generamos una box vertical
        box.pack_start(Gtk.Label(label=name), False, False, 0) # Insertamos en la box una label que contiene el texto de la variable de clase "name"
        box.pack_start(image, True, True, 0)  # Insertamos la imagen en la box
        self.add(box) # Añadimos la box a la ventana generada
        self.connect("button-release-event", self.on_click) # Conectamos la acción de clickar y soltar el botón con las imagenes

    def on_click(self, widget, event): # Función que se ejecuta al hacer click en cada elemento celda
        im = Gtk.Image() # Generamos una imagen Gtk
        im.set_from_pixbuf(self.image.get_pixbuf()) # Hacemos que esa imagen gtk sea una copia de la imagen Gtk que ya tiene la celda recogiendo el pixbuf de esa imagen inicial y creando esta imagen a partir de dicho pixbuf
        win = Detail(self.name, im, self.description) # Generamos una instancia de detail window
        win.show_all() # Mostramos todos los elementos de la ventana
        Gtk.main() # Hacemos que la ventana se siga mostrando quedando en un estado de espera mediante esta función

