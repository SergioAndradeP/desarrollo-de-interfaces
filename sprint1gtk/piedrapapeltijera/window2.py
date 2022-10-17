import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Ventana(Gtk.Window):

    def __init__(self, imagenJ, imagenM, result):
        super().__init__(title="Resultado")
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        box2= Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        box2.pack_start(imagenJ, False, False, 0)
        box2.pack_start(imagenM, False, False, 0)
        box.pack_start(box2, False, False, 0)
        box.pack_start(Gtk.Label(label=result), False, False, 0)
        self.add(box)
        self.connect("destroy", Gtk.main_quit)