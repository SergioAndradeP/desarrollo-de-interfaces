import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import GdkPixbuf
from cell import Cell

class MainWindow(Gtk.Window):
    flowbox = Gtk.FlowBox()

    def __init__(self):
        super().__init__(title="Catalogo")
        self.connect("destroy", Gtk.main_quit)
        self.set_border_width(15)
        self.set_default_size(400, 400)

        header = Gtk.HeaderBar(title="Imagenes")
        header.set_subtitle("Colección")
        header.props.show_close_button = True

        self.set_titlebar(header)

        scrolled = Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        scrolled.add(self.flowbox)
        self.add(scrolled)

        image1 = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/shaco_base.jfif", 300, 300, False)
        image1.set_from_pixbuf(pixbuf)

        image2 = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/shaco_masked.jfif", 200, 200, False)
        image2.set_from_pixbuf(pixbuf)

        image3 = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/shaco_darkstar.jfif", 200, 200, False)
        image3.set_from_pixbuf(pixbuf)

        image4 = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/shaco_arcane.jfif", 200, 200, False)
        image4.set_from_pixbuf(pixbuf)

        image5 = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/shaco_crime_city_nightmare.jfif", 200, 200, False)
        image5.set_from_pixbuf(pixbuf)

        cell_one = Cell("Shaco", image1)
        cell_two = Cell("Shaco enmascarado", image2)
        cell_three = Cell("Shaco estrella oscura", image3)
        cell_four = Cell("Shaco arcano", image4)
        cell_five = Cell("Shaco pesadilla en la ciudad sin ley", image5)

        self.flowbox.add(cell_one)
        self.flowbox.add(cell_two)
        self.flowbox.add(cell_three)
        self.flowbox.add(cell_four)
        self.flowbox.add(cell_five)