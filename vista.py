from tkinter import ttk, StringVar, Label, Entry, Frame, Scrollbar, Button, OptionMenu, W
from modelo import ABMM 





        
class Vista_:
    def __init__(self):
        self.dias= ['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']
        self.var_dia = StringVar()
        self.var_hora = StringVar()
        self.var_mensaje = StringVar()
        self.var_id_borrar = StringVar()
        self.var_id_modificar = StringVar()


    def crear_select(self, agenda):
        opciones = OptionMenu(agenda, self.var_dia, *self.dias)
        opciones.grid(row= 1, column=1)
    
    def crear_botones(self, agenda, tabla, hora_entry, mensaje_entry, label_alta, label_borrar, id_entry_borrar, id_entry_modificar, label_modificar):
        boton_agregar = Button(
            agenda,
             text= "Alta",
             background="LIGHT GREEN" ,
             command=
                lambda: ABMM.agregar(
                    self.var_dia,
                    self.var_hora,
                    self.var_mensaje,
                    id_entry_borrar,
                    id_entry_modificar,
                    hora_entry,
                    mensaje_entry,
                    label_alta, 
                    label_borrar, 
                    label_modificar,  
                    tabla))
        boton_agregar.grid(row=4, column=0)

        boton_borrar = Button(agenda, 
                                text= "Borrar",
                                background= "RED" ,
                                command=
                                    lambda: ABMM.borrar(
                                        self.var_id_borrar, 
                                        id_entry_borrar, 
                                        tabla, 
                                        label_alta, 
                                        label_borrar, 
                                        label_modificar))
        boton_borrar.grid(row=4, column=1)

        boton_mostrar = Button(agenda, 
                                text= "Mostrar",
                                background="YELLOW" ,
                                command=lambda: ABMM.mostrar(
                                            tabla,
                                            label_alta, 
                                            label_borrar, 
                                            label_modificar))
        boton_mostrar.grid(row=4, column=2)

        boton_modificar = Button(agenda, 
                                    text= "Modificar",
                                    background="ORANGE" ,
                                    command=lambda: ABMM.modificar(
                                                self.var_dia, 
                                                self.var_hora, 
                                                self.var_mensaje, 
                                                self.var_id_modificar, 
                                                id_entry_borrar,
                                                id_entry_modificar, 
                                                hora_entry, 
                                                mensaje_entry, 
                                                label_alta, 
                                                label_borrar, 
                                                label_modificar,
                                                tabla))
        boton_modificar.grid(row=4, column=3)

    def crear_tabla(self,agenda):

        tabla_frame = Frame(agenda)
        tabla_frame.grid(row=10, column=0, columnspan=4)

        tabla_scroll = Scrollbar(tabla_frame)

        tabla = ttk.Treeview(tabla_frame, yscrollcommand=tabla_scroll.set)
        
        tabla_scroll.config(command=tabla.yview)
        
        tabla["column"]=("c1", "c2", "c3","c4")
        tabla.column("#0", width=0, minwidth=0, anchor=W)
        tabla.column("c1", width=100, minwidth=80)
        tabla.column("c2", width=100, minwidth=80)
        tabla.column("c3", width=100, minwidth=80)
        tabla.column("c4", width=500, minwidth=80)
        tabla.heading("c1", text="ID")
        tabla.heading("c2", text="Dia")
        tabla.heading("c3", text="Hora")
        tabla.heading("c4", text="Mensaje")
        tabla.grid(row=10, column=0, columnspan=4)

        return tabla

    def crear_labels(self, agenda):

        agenda.title('                                                                                                                Agenda personal semanal')

        agenda.geometry('802x346')

        self.dias= ['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']
        self.var_dia = StringVar()
        self.var_dia.set(self.dias[0])


        self.dia = Label(agenda,text= "Dia")
        self.dia.grid(row= 1, column = 0)

        self.hora = Label(agenda,text= "Hora")
        self.hora.grid(row= 2, column = 0)

        self.mensaje = Label(agenda,text= "Mensaje")
        self.mensaje.grid(row= 3, column = 0)

        self.id_ = Label(agenda,text= "ID")
        self.id_.grid(row=5,column=0)

        self.var_hora = StringVar()

        self.var_mensaje = StringVar()

        self.var_id_borrar = StringVar()

        self.var_id_modificar = StringVar()

        id_entry_borrar = Entry(agenda, textvariable= self.var_id_borrar, width=5)
        id_entry_borrar.grid(row=5, column= 1)

        id_entry_modificar = Entry(agenda, textvariable= self.var_id_modificar, width=5)
        id_entry_modificar.grid(row=5, column= 3)

        hora_entry = Entry(agenda, textvariable= self.var_hora, width=10)
        hora_entry.grid(row=2, column=1)

        mensaje_entry = Entry(agenda, textvariable= self.var_mensaje, width=50)
        mensaje_entry.grid(row= 3, column=1)
        
        label_alta = Label(agenda, text= "Agendado correctamente", foreground= 'GREEN')

        label_borrar = Label(agenda, text= "Borrado correctamente", foreground= 'GREEN')

        label_modificar = Label(agenda,text= "Modificado correctamente", foreground= 'GREEN')

        return hora_entry, mensaje_entry, label_alta, label_borrar, id_entry_borrar, id_entry_modificar, label_modificar
    