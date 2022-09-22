from vista import Vista_
from tkinter import Tk


def main():
    
    agenda = Tk() 
    
    
    vista = Vista_()
    tabla = vista.crear_tabla(agenda)
    hora_entry, mensaje_entry, label_alta, label_borrar, id_entry_borrar, id_entry_modificar, label_modificar = vista.crear_labels(agenda)
    vista.crear_botones(agenda, tabla, hora_entry, mensaje_entry, label_alta, label_borrar, id_entry_borrar, id_entry_modificar, label_modificar)
    vista.crear_select(agenda)
    agenda.mainloop()



main()



