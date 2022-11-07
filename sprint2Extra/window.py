import gi # Imports necesarios
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from random import randrange

class MainWindow(Gtk.Window): #Herencia de Window
    list = ["CASA", "CAMION", "GATO", "ESTERNOCLEIDOMASTOIDEO", "FRUTA", "HIDROGENO", "ORDENADOR"]
    palabra = list[randrange(len(list))]
    labelString = ""
    letra = ""
    fallos = 0
    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    label = Gtk.Label()
    entry = Gtk.Entry()
    img = Gtk.Image()
    button = Gtk.Button("Intro")

    def __init__(self, data_source):
        super().__init__(title="Ahorcado") # Generamos una ventana con el texto catálogo mediante llamada al constructor de la super clase
        self.set_position(Gtk.WindowPosition.CENTER) # Centramos la ventana al centro una vez se genere
        self.connect("destroy", Gtk.main_quit) # Conectamos el evento destruir con clickar en cerrar la ventana
        self.set_border_width(15) # Ajustamos ancho del borde
        self.set_default_size(800, 800) # Definimos tamaño por defecto
        self.data_source=data_source
        self.juego()

    def juego(self):
        self.entry.set_max_length(1)
        self.labelString = self.generarGuiones(self.palabra)
        self.label = Gtk.Label(label=self.labelString)
        self.img = self.generarImagen()
        self.button.connect("clicked", self.on_click)
        self.box.pack_start(self.label, False, False, 0)
        self.box.pack_start(self.img, False, False, 50)
        self.box.pack_start(self.entry, False, False, 0)
        self.box.pack_start(self.button, False, False, 0)
        self.add(self.box)

    def on_click(self, event):
        self.letra = self.entry.get_text().upper()
        if not self.existeLetra():
            self.fallos = self.fallos + 1
        self.modifyWindow()
        if self.fallos == 5:
            etiquetaP = Gtk.Label(label="PERDISTE")
            self.remove(self.box)
            self.box.remove(self.label)
            self.box.remove(self.img)
            self.box.remove(self.entry)
            self.box.remove(self.button)

            self.box.pack_start(self.label, False, False, 0)
            self.box.pack_start(self.img, False, False, 50)
            self.box.pack_start(etiquetaP, False, False, 0)
            self.add(self.box)

        else:
            if self.labelString == self.palabra:
                etiquetaG = Gtk.Label(label="GANASTE")
                self.remove(self.box)
                self.box.remove(self.label)
                self.box.remove(self.img)
                self.box.remove(self.entry)
                self.box.remove(self.button)

                self.box.pack_start(self.label, False, False, 0)
                self.box.pack_start(self.img, False, False, 50)
                self.box.pack_start(etiquetaG, False, False, 0)
                self.add(self.box)

    def modifyWindow(self):
        self.remove(self.box)
        self.box.remove(self.label)
        self.box.remove(self.img)
        self.box.remove(self.entry)
        self.box.remove(self.button)

        self.labelString = self.calcularNewLabel()
        self.label.set_label(self.labelString)
        self.img.set_from_pixbuf(self.generarImagen().get_pixbuf())
        self.box.pack_start(self.label, False, False, 0)
        self.box.pack_start(self.img, False, False, 50)
        self.box.pack_start(self.entry, False, False, 0)
        self.box.pack_start(self.button, False, False, 0)
        self.add(self.box)

    def calcularNewLabel(self):
        aux = ""
        i = 0
        if not self.letraYaJugada():
            for item in self.palabra:
                if self.letra == item:
                    aux = aux + self.letra
                else:
                    aux = aux + self.labelString[i]
                i = i + 1
        else:
            aux = self.labelString

        return aux

    def existeLetra(self):
        existe = False
        for item in self.palabra:
            if self.letra == item:
                existe = True
                break
        return existe

    def letraYaJugada(self):
        jugada = False
        for item in self.labelString:
            if item == self.letra:
                jugada = True
        return jugada

    def generarGuiones(self, palabra):
        i = 0
        guiones=""
        while i < len(palabra):
            guiones = guiones + "_"
            i = i + 1
        return guiones

    def generarImagen(self):
        img = Gtk.Image()
        for item in self.data_source:
            if item.get("fallos") == self.fallos:
                img = item.get("gtk_image")
        return img


