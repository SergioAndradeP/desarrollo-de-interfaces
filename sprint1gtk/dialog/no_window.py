import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class NoWindow(Gtk.Window):
    label = Gtk.Label("Has pulsado no")

    def __init__(self):
        super().__init__(title = "No")
        self.add(self.label)