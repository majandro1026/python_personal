import sys
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Login(tk.Tk):   
    def __init__(self):
        super().__init__()

        self.geometry('300x130')
        self.title('Login')
        self.resizable(0,0)

        ##### Grid #############

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self.columnconfigure(2, weight=3)
        self.rowconfigure(0,weight=1)
        self.rowconfigure(1,weight=1)
        self.rowconfigure(2,weight=2)

        ##### Etiquetas ######
        self._crear_componentes()

    ### definir el metodo crear_componentes
    def _crear_componentes(self):
        #usuario
        etiqueta1 = ttk.Label(self, text="Usuario:")
        etiqueta1.grid(row=0, column=0, pady=1, sticky='E')
        etiqueta2 = ttk.Label(self, text="Contraseña:")
        etiqueta2.grid(row=1, column=0, pady=1, sticky='E')


        #### Entradas ##################

        self.entrada1 = ttk.Entry(self, width=30)
        self.entrada1.grid(row=0, column=1, columnspan=2)
        self.entrada2 = ttk.Entry(self, width=30, show='*')
        self.entrada2.grid(row=1, column=1, columnspan=2)

        #### Botones ####################

        boton1 = ttk.Button(self, text='Login', command=self._enviar)
        boton2 = ttk.Button(self, text='Salir', command=self._salir)
        boton1.grid(row=2, column=1, ipadx=1, ipady=1, padx=2, sticky='E')
        boton2.grid(row=2, column=2, ipadx=1, ipady=1, sticky='W',padx=4)
    
    ###### Metodos ################

    def _enviar(self):
        mensaje1 = self.entrada1.get()
        mensaje2 = self.entrada2.get()
        if mensaje1 and mensaje2:
            messagebox.showinfo('Datos de Login', 'Usuario: '+mensaje1+' , Contraseña: '+mensaje2)
        else:
            messagebox.showerror("Error", "Debe ingresar usuario y contraseña")


    def _salir(self):
        self.quit()
        messagebox.showinfo('Salir', "Hasta pronto")
        self.destroy()
        sys.exit()


if __name__ == '__main__':
    login_ventana = Login()
    login_ventana.mainloop()
