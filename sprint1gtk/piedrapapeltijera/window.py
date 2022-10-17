import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import GdkPixbuf
from celda import Celda

class MainWindow(Gtk.Window):
    flowbox = Gtk.FlowBox()

    def __init__(self):
        super().__init__()
        self.connect("destroy", Gtk.main_quit)
        self.set_border_width(15)
        self.set_default_size(400, 400)

        header = Gtk.HeaderBar(title="Piedra, papel, tijera!")
        header.set_subtitle("Selecciona que quieres jugar")
        header.props.show_close_button = True

        self.set_titlebar(header)

        scrolled = Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        scrolled.add(self.flowbox)
        self.add(scrolled)

        image1 = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/piedra.jfif", 200, 200, False)
        image1.set_from_pixbuf(pixbuf)

        image2 = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/papel.jfif", 200, 200, False)
        image2.set_from_pixbuf(pixbuf)

        image3 = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/tijera.jfif", 200, 200, False)
        image3.set_from_pixbuf(pixbuf)

        cell_one = Celda("piedra", image1)
        cell_two = Celda("papel", image2)
        cell_three = Celda("tijera", image3)

        self.flowbox.add(cell_one)
        self.flowbox.add(cell_two)
        self.flowbox.add(cell_three)