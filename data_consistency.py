from interface import DataMethods
class Consistency():
    
    # TODO: Agregar Lista
    @staticmethod
    def agregar_lista(name : str, description : str):
        if ((len(name)) <= 50 and (len(description) <= 255)):
            return None
        elif (len(description) > 255):
            return f"La descripcion de la lista no debe superar los 255 caracteres. ({len(description)})"
        elif (len(name) > 50):
            return f"El nombre de la lista no debe superar los 50 caracteres. ({len(name)})"
        else:
            return f"El nombre de la lista no debe superar los 50 caracteres ({len(name)}) y la descripcion los 255 caracteres ({len(description)})."      
 
    @staticmethod
    def _agregar_lista( name_list : str, description : str ):
        error = [None]
        if ( len( name_list ) > 50 ):
            error.append( f"'name_list' No se puede exeder de los 50 caracteres." )
        if ( len( description ) > 255 ):
            error.append( f"'description' No se puede exeder de los 255 caracteres." )
        return error 
 
    def alcualizar_usuario( first_name : str, last_name : str, user_name : str ):
        error = [None]
        if ( len( first_name ) > 20 ):
            error.append( f"'first_name' No se puede exeder de los 20 caracteres." )
        if ( len( last_name ) > 20 ):
            error.append( f"'last_name' No puede exeder a los 20 caracteres." )
        if ( len( user_name ) > 20 ):
            error.append( f"'user_name' No puede exeder a los 20 caracteres." )
        return error
      
      
      
class TerminalMessages:
    
    def out( message : str, **kwargs ):
        info = f"{message} : ("
        for key, item in kwargs.items():
            info += f" {key}={item} "
        info += ")"
        print( info )
        
    
class AlertMessages:
    

        
    def view_list( name_list : str, description : str, id_list : int ):
        error = { "message" : None, "style_box" : None, "id_lista" : None }
        errors = []
        if ( len( name_list ) > 50 ):
            error['message'] = f"'name_list' No puede exeder los 50 caracteres. c({len( name_list )})"
            error['style_box'] = "warning"
            errors.append( error.copy() )
        if ( len( description ) > 255 ):
            error['message'] = f"'description' No puede exeder los 50 caracteres. c({len( description )})"
            error['style_box'] = "warning"
            errors.append( error.copy() )
        if ( id_list == None ):
            error['message'] = f"La lista '{name_list}'. Se agrego exitosamente!"
            error['style_box'] = "success"
            errors.append( error.copy() )
        else:
            error['message'] = f"La lista '{name_list}'. Ya existe!"
            error['style_box'] = "danger"
            errors.append ( error.copy() )
        return errors
    
    