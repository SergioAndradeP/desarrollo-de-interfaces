import gi # Imports necesarios
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

#Esta clase serán las ventanas generadas al clickar en las imagenes de nuestro programa
class Detail(Gtk.Window):  # Herencia de Window

    def __init__(self, title, image, description):
        super().__init__(title=title) # Generamos una ventana con un título recibido como parámetro mediante una llamada al constructor de la super clase
        self.set_default_size(500, 500)
        self.set_position(Gtk.WindowPosition.CENTER)
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL) # Creamos una box de orientación vertical
        box.pack_start(image, False, False, 0) # Incluimos la imagen en la box
        box.pack_start(Gtk.Label(label=description), True, True, 0) # Incluimos en la box una label cuyo texto será el parámetro description
        self.add(box) # Añadimos a la ventana la box
        self.connect("destroy", Gtk.main_quit) # Conectamos el evento destroy con clickar en cerrar la ventana
