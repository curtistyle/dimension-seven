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