import gi # Imports necesarios
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from window import MainWindow

win = MainWindow()  # Generamos una instancia de MainWindow
win.show_all() # Mostramos la ventana y todos sus componentes

Gtk.main() # Hacemos que no se cierre mediante esta función