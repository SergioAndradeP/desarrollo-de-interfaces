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
        self.set_position(Gtk.WindowPosition.CENTER) # Centramos la ventana al centro una vez se genere
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

        mb = Gtk.MenuBar() # Generamos un elemento Gtk Menu Bar

        filemenu = Gtk.Menu() # Generamos un elemento Gtk Menu
        filem = Gtk.MenuItem("Ayuda") # Generamos un elemento Gtk Menu Item
        filem.set_submenu(filemenu) # Añadimos un submenu a ese Menu Item

        acercaDe = Gtk.MenuItem("Acerca de")   # Generamos otro Menu Item
        acercaDe.connect("activate", self.click) # Conectamos ese Menu Item a una función que se activa al hacer click
        filemenu.append(acercaDe) # Añadimos Menu Item "acercaDe" al Gtk Menu
        mb.append(filem) # Añadimos el Gtk Menu al Gtk Menu Bar

        vbox = Gtk.VBox(False, 2)                   # Creamos una VBox
        vbox.pack_start(mb, False, False, 0)        # Añadimos el Menu Bar a esa box
        vbox.pack_start(scrolled, True, True, 0)    # Añadimos la Ventana con scroll a la box
        self.add(vbox)                              # Añadimos la box a la propia ventana

        for item in data_source: # Esta clase recibe el elemento data source en el que previamente hemos almacenado la información de la petición GET mandada a la url
            cell = Cell(item.get("name"), item.get("gtk_image"), item.get("description")) # Mediante un bucle for generamos tantas celdas como items en data_source con sus respectivos parámetros
            self.flowbox.add(cell) # Añadimos cada celda a la Flowbox

    def click(self, event): # Función que se activa al hacer click en la opción de "Ayuda" y dentro de ayuda en "Acerca de"
        win = Gtk.Window(title = "Sobre el desarrollador") # Generamos una ventana con título
        self.set_position(Gtk.WindowPosition.CENTER)  # Ajustamos la posición por defecto
        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL) # Generamos una box que almacenará una label (aunque técnicamente no haría falta ya que solo va a haber un elemento label en la ventana, pero por claridad)
        label = Gtk.Label("SAMPLE TEXT") # Generamos una label con el texto
        box.pack_start(label, True, True, 0) # Añadimos la label a la box
        win.add(box) # Añadimos la box a la ventana
        win.show_all() # Mostramos todos los elementos de la ventana