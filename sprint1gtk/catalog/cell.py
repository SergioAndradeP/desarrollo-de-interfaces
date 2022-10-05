import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from detail_window import Detail
from gi.repository import GdkPixbuf

class Cell(Gtk.EventBox):
    name = None
    image = Gtk.Image()
    descripcion = None

    def __init__(self, name, image):
        super().__init__()
        self.name = name
        self.image = image
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        box.pack_start(Gtk.Label(label=name), False, False, 0)
        box.pack_start(image, True, True, 0)
        self.add(box)
        self.connect("button-release-event", self.on_click)

    def on_click(self, widget, event):
        self.image = self.getImage()
        self.asignar_desripcion()
        win = Detail(self.name, self.image, self.descripcion)
        win.show_all()
        Gtk.main()

    def asignar_desripcion(self):
        if self.name=="Shaco":
            self.descripcion="La skin por defecto de Shaco"
        elif self.name=="Shaco enmascarado":
            self.descripcion="La skin de Shaco enmascarado precio: 975 Rp"
        elif self.name=="Shaco estrella oscura":
            self.descripcion="La skin de Shaco estrella oscura precio: 1350 Rp"
        elif self.name == "Shaco arcano":
            self.descripcion = "La skin de Shaco arcano precio: 1350 Rp"
        elif self.name == "Shaco pesadilla en la ciudad sin ley":
            self.descripcion="La skin de Shaco pesadilla en la ciudad sin ley precio: 1350 Rp"
    def getImage(self):
        img = Gtk.Image()
        pixbuf = None
        if self.name == "Shaco":
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/shaco_base.jfif", 200, 200, False)
        elif self.name == "Shaco enmascarado":
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/shaco_masked.jfif", 200, 200, False)
        elif self.name == "Shaco estrella oscura":
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/shaco_darkstar.jfif", 200, 200, False)
        elif self.name == "Shaco arcano":
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/shaco_arcane.jfif", 200, 200, False)
        elif self.name == "Shaco pesadilla en la ciudad sin ley":
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/shaco_crime_city_nightmare.jfif", 200, 200, False)
        img.set_from_pixbuf(pixbuf)
        return img
