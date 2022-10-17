import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from window2 import Ventana
from gi.repository import GdkPixbuf
from random import randrange

class Celda(Gtk.EventBox):
    name = None
    image = Gtk.Image()
    imageM = Gtk.Image()
    jugador = None
    maquina = None
    resultado = None

    def __init__(self, name, image):
        super().__init__()
        self.name = name
        self.image = image
        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=4)
        box.pack_start(image, True, True, 0)
        self.add(box)
        self.connect("button-release-event", self.on_click)

    def on_click(self, widget, event):
        self.seleccionJugador()
        self.seleccionMaquina()
        self.getImagePlayer()
        self.getImageMachine()

        self.result()

        win = Ventana(self.image, self.imageM,self.resultado)
        win.show_all()
        Gtk.main()

    def seleccionJugador(self):
        if self.name=="piedra":
            self.jugador=1
        if self.name=="papel":
            self.jugador=2
        if self.name=="tijera":
            self.jugador=3

    def seleccionMaquina(self):
        maquina = randrange(1, 4)
        self.maquina=maquina

    def getImagePlayer(self):
        img = Gtk.Image()
        pixbuf = None
        if self.name == "piedra":
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/piedra.jfif", 200, 200, False)
        elif self.name == "papel":
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/papel.jfif", 200, 200, False)
        elif self.name == "tijera":
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/tijera.jfif", 200, 200, False)
        img.set_from_pixbuf(pixbuf)
        self.image = img

    def getImageMachine(self):
        img = Gtk.Image()
        pixbuf = None
        if self.maquina == 1:
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/piedra.jfif", 200, 200, False)
        elif self.maquina == 2:
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/papel.jfif", 200, 200, False)
        elif self.maquina == 3:
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/tijera.jfif", 200, 200, False)
        img.set_from_pixbuf(pixbuf)
        self.imageM=img

    def result(self):
        result = None
        if self.jugador==self.maquina:
            result= "Habeis seleccionado lo mismo, habeis empatado!"
        if self.jugador==1 and self.maquina==2:
            result= "Has seleccionado piedra, la máquina ha seleccionado papel, has perdido!"
        if self.jugador==1 and self.maquina==3:
            result = "Has seleccionado piedra, la máquina ha seleccionado tijeras, has ganado!"
        if self.jugador==2 and self.maquina==1:
            result ="Has seleccionado papel, la máquina ha seleccionado piedra, has ganado!"
        if self.jugador==2 and self.maquina==3:
            result = "Has seleccionado papel, la máquina ha seleccionado tijeras, has perdido!"
        if self.jugador==3 and self.maquina==1:
            result = "Has seleccionado tijeras, la máquina ha seleccionado piedra, has perdido!"
        if self.jugador==3 and self.maquina==2:
            result = "Has seleccionado tijeras, la máquina ha seleccionado papel, has ganado!"

        self.resultado=result