import gi # Imports necesarios
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import GdkPixbuf
from cell import Cell

# Esta clase será una ScrolledWindow que contendrá una FLowBox

class MainWindow(Gtk.Window): #Herencia de Window
    flowbox = Gtk.FlowBox() # Generamos una FlowBox como variable de clase

    def __init__(self):
        super().__init__(title="Catalogo") # Generamos una ventana con el texto catálogo mediante llamada al constructor de la super clase
        self.connect("destroy", Gtk.main_quit) # Conectamos el evento destruir con clickar en cerrar la ventana
        self.set_border_width(15) # Ajustamos ancho del borde
        self.set_default_size(400, 400) # Definimos tamaño por defecto

        header = Gtk.HeaderBar(title="Imagenes") # Añadimos un header
        header.set_subtitle("Colección") # Añadimos un subtítulo
        header.props.show_close_button = True # Mostramos el botón de cierre

        self.set_titlebar(header) # Añadimos el header mediante la función set_titlebar

        scrolled = Gtk.ScrolledWindow() # Generamos una instancia de ScrolledWindow
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        scrolled.add(self.flowbox) # Añadimos a la ScrolledWindow nuestra FlowBox
        self.add(scrolled) # Añadimos a la ventana la ScrolledWindow que ya contiene la FlowBox dentro

        image1 = Gtk.Image() # Generamos una imagen
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/shaco_base.jfif", 200, 200, False) # Usamos pixbuf para ajustar el tamaño
        image1.set_from_pixbuf(pixbuf) # Asignamos la imagen ya modificada mediante el pixbuf a nuestra variable imagen

        # Procedemos a hacer lo mismo para todas las imagenes

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

        cell_one = Cell("Shaco", image1)  # Generamos las 5 celdas cada una con sus parámetros correspondientes
        cell_two = Cell("Shaco enmascarado", image2)
        cell_three = Cell("Shaco estrella oscura", image3)
        cell_four = Cell("Shaco arcano", image4)
        cell_five = Cell("Shaco pesadilla en la ciudad sin ley", image5)

        self.flowbox.add(cell_one)  # Añadimos todas nuestras celdas a la FlowBox
        self.flowbox.add(cell_two)
        self.flowbox.add(cell_three)
        self.flowbox.add(cell_four)
        self.flowbox.add(cell_five)