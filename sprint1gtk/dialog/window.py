import gi                       # Imports necesarios
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from yes_window import YesWindow
from no_window import  NoWindow
class MainWindow(Gtk.Window):  #Herencia de MainWindow con Gtk.Window
    box1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)   # Generamos variables de clase de tipo box, una vertical y otra horizontal
    box2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
    label = Gtk.Label("Necesita Shaco un rework?")      # Elemento etiqueta con texto
    button1 = Gtk.Button(label="Si")    #Elementos botón con etiquetas dentro
    button2 = Gtk.Button(label="No")

    def __init__(self):
        super().__init__(title="Main") # Llamamos al super constructor de la clase heredada y generamos una ventana con título "Main"
        self.connect("destroy", Gtk.main_quit)
        self.add(self.box1) # Añadimos a la ventana el elemento de tipo box con orientación vertical
        self.box1.pack_start(self.label, True, True, 0) # Añadimos sobre la box vertical la label declarada en la clase
        self.box1.pack_start(self.box2, True, True, 0) # Añadimos sobre la box vertical la box horizontal
        self.box2.pack_start(self.button1, True, True, 0) #Añadimos sobre la box horizontal los botones 1 y 2
        self.box2.pack_start(self.button2, True, True, 0)
        self.button1.connect("clicked", self.on_button1_clicked)  # Conectamos los elementos botón con la acción de clickarlos
        self.button2.connect("clicked", self.on_button2_clicked)  # y los vinculamos a una función que definimos posteriormente

    def on_button1_clicked(self, widget):  # Función que genera una instancia de YesWindow()
        win = YesWindow()
        win.show_all()

    def on_button2_clicked(self, widget): # Función que genera una instancia de NoWindow()
        win = NoWindow()
        win.show_all()