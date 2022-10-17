import gi # Imports necesarios
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class YesWindow(Gtk.Window): # Herencia de Window
    label = Gtk.Label("Has pulsado si") # Label con texto

    def __init__(self):
        super().__init__(title="Yes") # Generamos una ventana con título "No" mediante la llamada al super constructor
        self.add(self.label) # Añadimos la label

