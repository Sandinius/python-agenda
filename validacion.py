import re



class Validar:


    def validar_agregar(var_hora,var_mensaje):

        texto = (var_hora.get())
        texto2 = (var_mensaje.get())
        opcion = "[0-9:_]+$"  
        opcion2 = "[0-9a-zA-Z?/.,¿¡;:|!#$%& _]+$"
        
        if not re.match(opcion, texto):
           raise ValueError("Revise que el formato de hora coincida con el siguiente: 12:00 o 1200")
           
        if not re.match(opcion2, texto2):
           raise ValueError("El campo mensaje no puede quedar vacio")     


    def validar_borrar(var_id_borrar):
        texto = (var_id_borrar.get())
        opcion = "[0-9_]+$"    
        if not re.match(opcion, texto):
            raise ValueError("El campo ID no puede estar vacio introduzca el numero de ID a borrar")

    def validar_modificar(var_id_modificar):
        texto = (var_id_modificar.get())
        opcion = "[0-9_]+$"    
        if not re.match(opcion, texto):
            raise ValueError("El campo ID no puede estar vacio introduzca el numero de ID a modificar")