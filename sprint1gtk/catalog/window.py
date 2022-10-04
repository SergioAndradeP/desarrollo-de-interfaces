import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
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

        cell_one =  Cell("Shaco", Gtk.Image.new_from_file("data/edited/shaco_base.png"))
        cell_two = Cell("Shaco enmascarado", Gtk.Image.new_from_file("data/edited/shaco_masked.png"))
        cell_three = Cell("Shaco estrella oscura", Gtk.Image.new_from_file("data/edited/shaco_darkstar.png"))
        cell_four = Cell("Shaco arcano", Gtk.Image.new_from_file("data/edited/shaco_arcane.png"))
        cell_five = Cell("Shaco pesadilla en la ciudad sin ley", Gtk.Image.new_from_file("data/edited/shaco_crime_city_nightmare.png"))

        self.flowbox.add(cell_one)
        self.flowbox.add(cell_two)
        self.flowbox.add(cell_three)
        self.flowbox.add(cell_four)
        self.flowbox.add(cell_five)