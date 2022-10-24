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
        self.set_position(Gtk.WindowPosition.CENTER)
        self.connect("destroy", Gtk.main_quit) # Conectamos el evento destruir con clickar en cerrar la ventana
        self.set_border_width(15) # Ajustamos ancho del borde
        self.set_default_size(800, 800) # Definimos tamaño por defecto


        header = Gtk.HeaderBar(title="Imagenes") # Añadimos un header
        header.set_subtitle("Colección") # Añadimos un subtítulo
        header.props.show_close_button = True # Mostramos el botón de cierre

        self.set_titlebar(header) # Añadimos el header mediante la función set_titlebar

        scrolled = Gtk.ScrolledWindow() # Generamos una instancia de ScrolledWindow
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        scrolled.add(self.flowbox) # Añadimos a la ScrolledWindow nuestra FlowBox

        mb = Gtk.MenuBar()

        filemenu = Gtk.Menu()
        filem = Gtk.MenuItem("Ayuda")
        filem.set_submenu(filemenu)

        acercaDe = Gtk.MenuItem("Acerca De")
        acercaDe.connect("activate", self.click)
        filemenu.append(acercaDe)
        mb.append(filem)

        vbox = Gtk.VBox(False, 2)
        vbox.pack_start(mb, False, False, 0)
        vbox.pack_start(scrolled, True, True, 0)
        self.add(vbox)

        for item in data_source:
            cell = Cell(item.get("name"), item.get("gtk_image"), item.get("description"))
            self.flowbox.add(cell)

    def click(self, event):
        win = Gtk.Window(title = "Sobre el desarrollador")
        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        label = Gtk.Label("SAMPLE TEXT")
        box.pack_start(label, True, True, 0)
        win.add(box)
        win.show_all()
        Gtk.main()