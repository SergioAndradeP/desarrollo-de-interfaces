import gi # Imports necesarios
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class NoWindow(Gtk.Window): # Herencia de window
    label = Gtk.Label("Has pulsado no") # Label con texto

    def __init__(self):
        super().__init__(title = "No") # Generamos una ventana con título "No" mediante la llamada al super constructor
        self.add(self.label) # Añadimos la label