import gi                            # Importamos las librerías necesarias
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

window = Gtk.Window(title="Hello World")   # Generamos un elemento Window de Gtk con título Hello World
window.show()  # Mostramos la ventana
window.connect("destroy", Gtk.main_quit) # Conectamos la acción destroy con cerrar la ventana
Gtk.main()  #Invocamos esta función de Gtk para que la ventana se mantenga abierta