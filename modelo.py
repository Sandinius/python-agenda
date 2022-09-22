import re
from tkinter import (END, messagebox)
from peewee import *
import validacion

db = SqliteDatabase("agenda.db")

class Basemodel(Model):
    class Meta:
        database = db


class Tabla(Basemodel):
    dia = CharField()
    hora = CharField()
    mensaje = CharField()

try:
    db.connect()
    db.create_tables([Tabla])
except:
    messagebox.showerror(message="Fallo al conectar la base de datos", title="Ha ocurrido un error")
class ABMM:

    def agregar(var_dia, var_hora, var_mensaje, id_entry, id_entry_modificar, hora_entry, mensaje_entry, label_alta, 
    label_borrar, label_modificar, tabla):
        label_alta.grid_forget()
        label_borrar.grid_forget()
        label_modificar.grid_forget()


        try: 
            validacion.Validar.validar_agregar(var_hora,var_mensaje) 
            agendar = Tabla()
            agendar.dia=var_dia.get()
            agendar.hora=var_hora.get()
            agendar.mensaje=var_mensaje.get()
            agendar.save()
            id_entry.delete(0, END)
            id_entry_modificar.delete(0, END)
            hora_entry.delete(0, END)
            mensaje_entry.delete(0,END)
            ABMM.mostrar(tabla, label_alta, 
            label_borrar, label_modificar)
            label_alta.grid(row=6 ,column=1)
        except ValueError as falla: 
            messagebox.showerror("Ha ocurrido un error",str(falla))

        


    def mostrar(tabla, label_alta, 
    label_borrar, label_modificar):
        label_alta.grid_forget()
        label_borrar.grid_forget()
        label_modificar.grid_forget()

        for x in tabla.get_children():
            tabla.delete(x)

        for x in Tabla.select():
           try:
             tabla.insert("", 0, values=(x.id, x.dia, x.hora, x.mensaje))
           except:
            messagebox.showerror(message="No se ha podido recuperar la informacion", title="Ha ocurrido un error")



    def borrar(var_id_borrar, id_entry,tabla,  label_alta, 
    label_borrar, label_modificar):
        label_alta.grid_forget()
        label_borrar.grid_forget()
        label_modificar.grid_forget()
        
        try:
            validacion.Validar.validar_borrar(var_id_borrar)
            borrado = Tabla.get(Tabla.id==var_id_borrar.get())
            
        except ValueError as falla:
            messagebox.showerror(("Ha ocurrido un error"), str(falla)) 
        else:
            borrado.delete_instance()
            id_entry.delete(0, END)
            ABMM.mostrar(tabla, label_alta, 
    label_borrar, label_modificar)
            label_borrar.grid(row=6 ,column=1) 



    def modificar(var_dia, var_hora, var_mensaje, var_id_modificar, id_entry_borrar, id_entry_modificar, hora_entry, mensaje_entry,  label_alta, 
    label_borrar, label_modificar, tabla):
        label_alta.grid_forget()
        label_borrar.grid_forget()
        label_modificar.grid_forget()
 
        
        try:
            validacion.Validar.validar_modificar(var_id_modificar)
            actualizar = Tabla.update(dia = var_dia.get(), hora = var_hora.get(), mensaje = var_mensaje.get()).where(Tabla.id==var_id_modificar.get())
        except ValueError as falla:
            messagebox.showerror(("Ha ocurrido un error"), str(falla)) 
        else:
            actualizar.execute()
            id_entry_borrar.delete(0, END)
            id_entry_modificar.delete(0, END)
            hora_entry.delete(0, END)
            mensaje_entry.delete(0, END)
            ABMM.mostrar(tabla, label_alta, 
    label_borrar, label_modificar)
            label_modificar.grid(row=6 ,column=1) 
          