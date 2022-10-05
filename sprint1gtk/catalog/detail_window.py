import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Detail(Gtk.Window):

    def __init__(self, title, image, description):
        super().__init__(title=title)
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        box.pack_start(image, False, False, 0)
        box.pack_start(Gtk.Label(label=description), True, True, 0)
        self.add(box)
