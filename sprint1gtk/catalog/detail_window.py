import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Detail(Gtk.Window):
    title = None
    image = Gtk.Image()
    descripcion = None

    def __init__(self, title, image, description):
        super().__init__(title=self.title)
        self.title = title
        self.image = image
        self.descripcion = description
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        box.pack_start(self.image, False, False, 0)
        box.pack_start(Gtk.Label(label=self.descripcion), True, True, 0)
        self.add(box)
