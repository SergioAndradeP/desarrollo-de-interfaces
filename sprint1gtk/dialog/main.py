import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from window import MainWindow

win = MainWindow()     # Exactamente lo mismo que en hello_world.py pero creando una instancia de MainWindow en lugar
win.show_all()         # de generar un elemento Gtk.Window directamente

Gtk.main()