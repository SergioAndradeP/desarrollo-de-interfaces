import gi # Imports necesarios
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import GdkPixbuf
from cell import Cell

# Esta clase será una ScrolledWindow que contendrá una FLowBox

class MainWindow(Gtk.Window): #Herencia de Window
    flowbox = Gtk.FlowBox() # Generamos una FlowBox como variable de clase

    def __init__(self, data_source):
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


        for item in data_source:
            print(item.get("name"))
            print(item.get("image_url"))
            cell = Cell(item.get("name"), item.get("gtk_image"))
            self.flowbox.add(cell)
