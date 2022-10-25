import shutil
import gi # Imports necesarios
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib
import requests, threading
from window import MainWindow

class LoadWindow(Gtk.Window): # Herencia de LoadWindow al elemento Window de Gtk
    label = Gtk.Label("Cargando elementos...") # Label con texto mientras se cargan los elementos
    spinner = Gtk.Spinner()  # Declaramos un Gtk Spinner que muestra un circulo girando el cual será usado durante la carga
    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)

    def __init__(self):
        super().__init__(title="Pantalla de Carga") # Generamos la ventana mediante llamada al constructor de la super clase
        self.set_position(Gtk.WindowPosition.CENTER) #Posicionamos la ventana en el centro nada más se genera
        self.set_default_size(400, 400) # Ajustamos tamaño por defecto
        self.connect("destroy", Gtk.main_quit) # Conectamos la acción de cerrar a la ventana
        self.set_border_width(60) # Ajustamos el ancho del borde
        self.set_resizable(False) # Hacemos que el usuario no pueda cambiar su tamaño
        self.spinner.props.active = True # Activamos el spinner

        self.box.pack_start(self.label, False, False, 0)  # Metemos todos los elementos en la box en el orden adecuado
        self.box.pack_start(self.spinner, False, False, 0)
        self.add(self.box)                                    # Añadimos a la ventana la box

        self.launch_load() # Llamammos a la función de la clase de nombre launch_load

    def launch_load(self): # Inicia otro hilo en paralelo con el principal
        thread = threading.Thread(target=self.load_json(), args=())
        thread.start()

    def load_json(self):  # Función que se encarga de recuperar la información almacenada en un JSON mediante una petición GET
        response = requests.get("https://raw.githubusercontent.com/SergioAndradeP/desarrollo-de-interfaces/master/API-REST/catalog.json") # Dirección a la que se envía la petición GET
        json_list = response.json() # Almacenamos la respuesta que será un array JSON

        result = [] # Generamos una lista llamada result

        for json_item in json_list:  # Bucle que va recogiendo la información del array json con la respuesta
            name = json_item.get("name") # y la va almacenando en la lista result además de convertir
            description = json_item.get("description") # Las urls de la imagen en elementos imagen Gtk y almacenarlos
            image_url = json_item.get("image_url") # también en la lista
            r = requests.get(image_url, stream=True)
            with open ("temp.png", "wb") as f:
                shutil.copyfileobj(r.raw, f)
            image = Gtk.Image.new_from_file("temp.png")
            result.append({"name": name, "description": description, "gtk_image": image})

        GLib.idle_add(self.start_main_window, result) # Pasamos al hilo principal y ejecutamos la función start_main_window

    def start_main_window(self, loaded_item_list): # Función que genera una ventana MainWindow
        win = MainWindow(loaded_item_list)
        win.show_all()
        self.disconnect_by_func(Gtk.main_quit)
        self.close()



