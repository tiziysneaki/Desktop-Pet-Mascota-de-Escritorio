# Desktop-Pet-Mascota-de-Escritorio
IMPORTANTE:
para correr el archivo o modificar su contenido, tenes que tener instalado un editor de codigo [ej: Visual Studio Code]

Esto es un archivo de python que utiliza varias imagenes para representar una "mascota" en tu escritorio.
El repositorio ya tiene imagenes por defecto por si alguien desea usarlas, pero si queres usar tus propias imagenes, hay que cambiar el codigo y te voy a enseñar a como hacerlo.

1- se van a necesitar 6 imagenes de tu mascota (puede ser un personaje, tu mascota de verdad o cualquier cosa), 3 imagenes para represantar como camina hacia la derecha, y 3 imagenes para que este quieto/durmiendo/parpadeando
CUIDADO!: asegura que las imagenes esten en la misma carpeta que el archivo "desktop_pet.py" por que sino python no las va poder encontrar 

2-abrir con tu editor de codigo el archivo "desktop_pet.py" y busca en las lineas de codigo algo asi

"self.walk_right = [
            tk.PhotoImage(file=os.path.join(Base_dir,"tank-0.png")),
            tk.PhotoImage(file=os.path.join(Base_dir,"tank-1.png")),
            tk.PhotoImage(file=os.path.join(Base_dir,"tank-2.png")),
        ]"
y

"self.idle_frames = [
            tk.PhotoImage(file=os.path.join(Base_dir,"idle-0.png")),
            tk.PhotoImage(file=os.path.join(Base_dir,"idle-1.png")),
            tk.PhotoImage(file=os.path.join(Base_dir,"idle-2.png")),
        ]"

    lo unico que vas a cambiar son los strings (eg: "tank-0.png") al nombre de tus imagenes (eg: "perro-0.png")
    asegurate de que las extensiones de tus imagenes sean .png