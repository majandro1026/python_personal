import sys
from time import sleep
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext


class ComponentesVentana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('600x400+450+200') #El tecer y cuarto parametro son la posición en px del monitor
        self.title('Componentes')
        self._crear_tabuladores()

    def _crear_componentes_tabulador1(self, tabulador):
        # Agregar una etiqueta y un componente de entrada
        etiqueta1 = ttk.Label(tabulador, text= 'Nombre')
        etiqueta1.grid(row=0, column=0, sticky=tk.E)

        entrada1 = ttk.Entry(tabulador, width=30)
        entrada1.grid(row=0, column=1, padx=5, pady=5)

        #Metodos
        def enviar():
            messagebox.showinfo('Mensaje', f'{entrada1.get()}')

        # boton
        boton1 = ttk.Button(tabulador, text='Enviar', command= enviar)
        boton1.grid(row=1, column=0,columnspan=2)


    def _crear_componentes_tabulador2(self, tabulador):
        contenido = 'Este es mi texto con el contenido'
        # Creamos el componente de scroll
        scroll = scrolledtext.ScrolledText(tabulador, width= 50, height = 10, wrap = tk.WORD) # propiedad Wrap: para que las palabras se visualicen completas
        scroll.insert(tk.INSERT, contenido)
        #Mostramos el componente
        scroll.grid(row=0, column=0)

    def _crear_componentes_tabulador3(self, tabulador):
        #creamos una lista usando data list comprhensions

        datos = [x+1 for x in range(0,10)]
        combobox = ttk.Combobox(tabulador, width=15, values=datos)
        combobox.grid(row=0, column=0, padx=10, pady=10)
        ## seleccionamos un elemento por default a mostrar
        combobox.current(0)
        
        def mostrar_valor():
            messagebox.showinfo('Valor seleccionado', f'Valor Seleccionada: {combobox.get()}')

        # Agregar un boton para saber que opcion seleccionó el usuario
        boton1 = ttk.Button(tabulador, text='Mostrar Valor seleccionado', command=mostrar_valor)
        boton1.grid(row= 0, column=1)

    def _crear_componentes_tabulador4(self, tabulador):
        imagen = tk.PhotoImage('python-logo.png')
        def mostrar_titulo():
            messagebox.showinfo('Mas info de la imagen', f'Nombre de la imagen: {imagen.cget("file")}')
        boton_imagen = ttk.Button(tabulador, image=imagen, command=mostrar_titulo)
        boton_imagen.grid(row=0, column=0)

    def _crear_componentes_tabulador5(self, tabulador):
        #creamos el componente de barra de progreso
        barra_progreso = ttk.Progressbar(tabulador, orient='horizontal', length=550)
        barra_progreso.grid(row=0, column=0, padx=10, pady=10, columnspan=4)
        
        def ejecutar_barra():
            barra_progreso['maximum'] = 100
            for valor in range(0,101,1):
                # Mandamos a esperar un poco antes de continuar con la ejecución
                sleep(0.05)
                # incrementamos la barra de brogreso
                barra_progreso['value'] = valor
                # actualizar barra de progreso
                barra_progreso.update()
            barra_progreso['value'] = 0


        def ejecutar_ciclo():
            barra_progreso.start()
        
        def detener():
            barra_progreso.stop()
        
        def detener_despues():
            esperar_ms = 1000
            self.after(esperar_ms, barra_progreso.stop)


        ### botones para controlar los eventos de una barra de progreso

        boton_inicio = ttk.Button(tabulador, text='Ejecutar barra de progreso', command=ejecutar_barra)
        boton_inicio.grid(row=1, column=0)

        boton_ciclo = ttk.Button(tabulador, text='ejecutar ciclo', command=ejecutar_ciclo)
        boton_ciclo.grid(row=1, column=1)

        boton_detener = ttk.Button(tabulador, text='Detener ejecución', command=detener)
        boton_detener.grid(row=1, column=2)

        boton_despues = ttk.Button(tabulador, text='Detener ejecución despues', command=detener_despues)
        boton_despues.grid(row=1, column=3)

    def _crear_tabuladores(self):
        #Creamos un tab control, para ello usamos la clase de notebook

        control_tabulador = ttk.Notebook(self)

        #Agregamos un marco o Frame para agregar dentro del tabulador y organizar los elementos que agreguemos
        tabulador1 = ttk.Frame(control_tabulador)
        
        #Agregamos este tabulador al control de tabuladores

        control_tabulador.add(tabulador1, text='Tabulador 1')
        control_tabulador.pack(fill='both')

        # creamos las componentes del tabulador
        self._crear_componentes_tabulador1(tabulador1)

        #segundo tabulador

        tabulador2 = ttk.Labelframe(control_tabulador, text='Contenido')
        control_tabulador.add(tabulador2, text='Tabulador 2')

        #creamos los componentes del segundo tabulador

        self._crear_componentes_tabulador2(tabulador2)

        ## Tercer tabulador
        tabulador3 = ttk.Frame(control_tabulador)
        control_tabulador.add(tabulador3, text='Tabulador 3')

        ## componentes del tercer tabulador
        self._crear_componentes_tabulador3(tabulador3)

        ### crear cuarto tabulador
        tabulador4 = ttk.Labelframe(control_tabulador, text='Imagen')
        control_tabulador.add(tabulador4, text='Tabulador 4')

        self._crear_componentes_tabulador4(tabulador4)

        # Crearar un quinto tabulador
        tabulador5 = tk.LabelFrame(control_tabulador, text='Progress Bar')
        control_tabulador.add(tabulador5, text='Tabulador 5')

        self._crear_componentes_tabulador5(tabulador5)
        
if __name__ == '__main__':
  componentes_ventana = ComponentesVentana()
  componentes_ventana.mainloop()
