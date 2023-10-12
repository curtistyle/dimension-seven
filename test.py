# def consultar_usuario(**kwargs):
#     print(kwargs)
    
    

# consultar_usuario(nombre="Curtis", Apellido="Style", Year="23")



from interface import mySpotify

sp = mySpotify()

print(sp.search("the offspring"))