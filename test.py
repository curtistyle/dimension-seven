# def consultar_usuario(**kwargs):
#     print(kwargs)
    
    

# consultar_usuario(nombre="Curtis", Apellido="Style", Year="23")



# from interface import mySpotify

# sp = mySpotify()

# print(sp.search("the offspring"))





# file = type_file 


# def fwrite(data : dict, index : list, *args, **kwargs):
#     for key, item in data.items():
#         if args:
#             if (key == index):
#                 item[index] = args
                

# fwrite(type_file,'user', id="123123")


# print(type_file)

# from interface import File

# File('fichero').add_user(id=123123, email="curtis@example.com")

# type_file = {
#     "user" : { "id" : None, "name" : None, "email" : None, "nickname" : None },
#     "list" : { "id" : None, "name" : None },
#     "data" : [
#         { "artist" : "Green Day", "album" : "Dookie", "track" : "She", "order" : 1 },
#         { "artist" : "The Offspring", "album" : "Americana", "track" : "Have You Ever", "order" : 2 },
#         { "artist" : "Sum 41", "album" : "All Killer No Filler", "track" : "Motivation", "order" : 3},
#         { "artist" : "Pantera", "album" : "The Great Southern Trendkill", "track" : "Drag the Waters", "order" : 4 },
#         { "artist" : "Metallica", "album" : "Garage Inc. DISC II", "track" : "Am I Evil?", "order" : 5 }
#     ]
# }

# def swap(matrix, i, j):
#      """Exchanges the items at positions i and j."""
#      # You could say matrix[i], matrix[j] = matrix[j], matrix[i]
#      # but the following code shows what is really going on
#      temp = matrix[i]
#      matrix[i] = matrix[j]
#      matrix[j] = temp

# def bubbleSortWithTweak(matrix, key):
#     n = len(matrix)
#     while n > 1:
#         swapped = False
#         i = 1
#         while i < n:
#             if matrix[i][key] < matrix[i - 1][key]:   # Exchange if needed
#                 swap(matrix, i, i - 1)
#                 swapped = True
#             i += 1
#         if not swapped: return            # Return if no swaps
#         n -= 1

# def binarySearch(target, key, sortedmatrix):
#     left = 0
#     right = len(sortedmatrix) - 1
#     while left <= right:
#         midpoint = (left + right) // 2
#         if target == sortedmatrix[midpoint][key]:
#             return midpoint
#         elif target < sortedmatrix[midpoint][key]:
#             right = midpoint - 1
#         else:
#             left = midpoint + 1
#     return None


# def data_append(**kwargs):
#     data = dict()
#     for key, item in kwargs.items():
#         data.update({key : item})
#     bubbleSortWithTweak(type_file.get('data'))
#     if binarySearch(data['track'], "track", type_file.get('data')) is not None:            
#         type_file.get('data').append(data)
#         return True
#     else:
#         return False

# bubbleSortWithTweak(type_file.get('data'), "track")

# print(binarySearch("Am I Evil?", "track", type_file.get('data')))

    # {
    #   "artist": "Pantera",
    #   "album": "The Great Southern Trendkill",
    #   "track": "Drag the Waters",
    #   "order": 4
    # },

# from interface import File, DataMethods

# data = File("fichero").data

# print(data)

# DataMethods.reorder(data.get('data'),"order", 4)



# print(data)




# from database import obtener_listas


# print(obtener_listas(1))


# from interface import File

# data = [
#     {'artist': 'Blink 182', 'album': 'Greates Hist', 'track':'First Date'},
#     {'artist': 'NOFX ', 'album': ' Ribbed ', 'track': 'Green Corn'},
#     {'artist': 'Nonpoint ', 'album': 'Development', 'track': 'Your Signs'},
#     {'artist': 'Paramore ', 'album': 'All We Know Is Falling', 'track': 'Emergency'}]

# error = []

# File('fichero').data_insert(data, error)

# print(error)


# from database import agregar_lista

# print(agregar_lista(1, 'Lista 5', "asd"))


# print(File('fichero').data_append(artist='Blink 182', album='Greates Hist', track='First Date'))

# {
#   "user": { "id": null, "name": null, "email": null, "nickname": null },
#   "list": { "id": null, "name": null, "amount": 6 },
#   "data": [
#     {
#       "artist": "Metallica",
#       "album": "Garage Inc. DISC II",
#       "track": "Am I Evil?",
#       "order": 5
#     },
#     {
#       "artist": "The Offspring",
#       "album": "Americana",
#       "track": "Have You Ever",
#       "order": 2
#     },
#     {
#       "artist": "Sum 41",
#       "album": "All Killer No Filler",
#       "track": "Motivation",
#       "order": 3
#     },
#     { "artist": "Green Day", "album": "Dookie", "track": "She", "order": 1 },
#     {
#       "artist": "Blink 182",
#       "album": "Greates Hist",
#       "track": "First Date",
#       "order": 6
#     }
#   ]
# }


# def to_list(**kwargs):
#     matrix = [{}] * 
#     print( f"{len(kwargs)=}" )
#     for key, items in kwargs.items():
#         print( f"{key=} - {items=}" )
#         for item in items:
#             print( " + ",item )
        
# to_list(order=order, artist=artist, album=album, track=track)

order = [1, 2, 3, 4, 5]
artist = ['Green Day', 'Pantera', 'Nirvana', 'The Offspring', 'Sum 41']
album = ['Dookie', 'Cowboys From Hell', 'Bleach', 'Americana', 'All the Good Shit']
track = ['She', 'Domination', 'School', 'The Kids Arent AlRight', 'Still Waiting']
time = ['02:23', '01:59', '02:43', '02:07', '03:01']

# def to_list(*args):
#     for item in args:
#         print(item)
        
# to_list(order, artist, album, track)

# def to_list(**kwargs):
#     model_dyct = dict()
#     lyst = list()
#     matrix = list()

#     for key, item in kwargs.items():
#         model_dyct.update( {key : None} )
#         matrix.append( item )
     
#     for col in range( 0, len( matrix[0] ) ):
#         new_dyct = model_dyct.copy()
#         for row in range( 0, len( matrix ) ):
#             keys = list( new_dyct.keys() )
#             new_dyct[ keys[ row ] ] = matrix[ row ][ col ]
#         lyst.append( new_dyct )    
         
#     return lyst
        
# print( to_list(order=order, artist=artist, album=album, track=track, time=time) )

# dyct = { 'order' : 1, 'artist': 'Green Day', 'album': 'Dookie', 'track': 'She' }

# print( dyct.keys() )



# from interface import File

# File('8').rename_file('_del')

# lyst = ["1", "2", "3", "4"]
# print( lyst )
# lyst = map( int, lyst )
# print( list(lyst) )

# print( int( lyst ) )


# for index, item in iter(map(lyst)):
#     print( f"{index=} - {item=}" )

# from database import modificar_privacy_en_lista

# modificar_privacy_en_lista( 10, "Publico" )

# from data_consistency import AlertMessages



# try:
#     AlertMessages("asd")
# except Exception as e:
#     print(e)



# from database import obtener_usuario

# print( obtener_usuario( 1 ) )

# from data_consistency import AlertMessages

# name_list = ''
# description = ''
# for i in range( 0, 50 ):
#     name_list += str(i)
# for j in range( 0 , 270 ):
#     description += str(j)

# print( len( name_list ) )
# print( len( description ) )

# error = AlertMessages._view_list( name_list, description, 0 )

# print( error )

# from database import actualizar_usuario

# actualizar_usuario( 2, 'Seba', 'Maldona', 'Curtis', 'guitar' )



def time_to_dict( time : str ):
    dyct = { 'hora' : 0, 'minuto' : None, 'segundo' : None }
    if( len( time.split(":") ) == 2 ):
        dyct['minuto'], dyct['segundo'] = map( int, time.split(":") )
    elif( len( tiempo.split(":") ) == 3 ):
        dyct['hora'], dyct['minuto'], dyct['segundo'] = map( int, time.split(":") )
    return dyct

def dict_to_time( time : dict ):
    segundo = str( time['segundo'] ) 
    minuto = str( time['minuto'] )
    hora = str( time['hora'] )
    if ( len( segundo ) == 1 ): 
        segundo = "0" + segundo
    if ( len( minuto ) == 1 ):
        minuto = "0" + minuto
    if ( len( hora ) == 1 ):
        hora = "0" + hora    
    return f"{hora}:{minuto}:{segundo}"

def time_accumulator( time : str, total_time : str ):
    time = time_to_dict( time )
    total_time = time_to_dict( total_time )
    segundo = total_time['segundo'] + time['segundo']
    if segundo > 60:
        total_time['segundo'] = segundo % 60
        resto = segundo // 60
    else:
        total_time['segundo'] = segundo
        resto = 0
        
    minuto = total_time['minuto'] + time['minuto']
    if minuto > 60:
        total_time['minuto'] = (resto + minuto) % 60
        resto = minuto // 60
    else:
        total_time['minuto'] = minuto + resto
        resto = 0
    
    total_time['hora'] = total_time['hora'] + time['hora'] + resto
    
    return dict_to_time( total_time )

def m( asd ):
    ...
    
tiempo = "01:02:22"

total = { "hora" : None, "minuto" : None, "segundo" : None }

horas, minutos, segundos = "","",""

if( len( tiempo.split(":") ) == 2 ):
    minutos, segundos = tiempo.split(":")
elif( len( tiempo.split(":") ) == 3 ):
    horas, minutos, segundos = tiempo.split(":")

print( f"{horas=}, {minutos=}, {segundos=}" )

horas = int(horas)
minutos = int(minutos)
segundos = int(segundos)

print( f"{horas=}, {minutos=}, {segundos=}" )

print( time_to_dict( "01:22" ) )

time = [
    {
      "artist": "Millencolin",
      "album": "Kingwood",
      "track": "Shut You Out",
      "order": 1,
      "time": "00:00"
    },
    {
      "artist": "Megadeth",
      "album": "Countdown To Extinction",
      "track": "Skin O' My Teeth",
      "order": 2,
      "time": "00:00"
    },
    {
      "artist": "Megadeth",
      "album": "Peace Sells... But Who's Buying?",
      "track": "Peace Sells",
      "order": 3,
      "time": "00:00"
    },
    {
      "artist": "Metallica",
      "album": "Garage Inc. DISC II",
      "track": "Am I Evil?",
      "order": 4,
      "time": "00:00"
    }
  ]

# total_time = "00:00"
# # time = ["01:51", "02:22", "03:45"]


# print( time_accumulator( "01:51", "03:45" ) )

# for item in time:
#     total_time = time_accumulator( item['time'], total_time )
    
# print( f"{total_time=}" )

# nueva_lista = []

# genres = [  ]

# lista1 = ["rojo", "rojo", "verde", "verde", "amarillo"]
# # lista2 = ["rojo", "rojo", "verde", "amarillo", "amarillo"]

# nueva_lista.extend( lista1 )
# # nueva_lista.extend( lista2 )

# set_lista = set(nueva_lista)

# for item in set_lista:
#     print( f"{item} - {nueva_lista.count( item )}" )
#     genres.append([item, nueva_lista.count( item )])

# # for item in range(0, len(nueva_lista)):
# #     print(nueva_lista[item])

# print( genres )


# nueva_lista = []



# lista3 = ["rojo", "verde", "amarillo", "rojo", "azul", "azul"]
# genres = [['rojo', 4], ['amarillo', 3], ['verde', 3]]
# genres = []



# def countGenres( lyst : list, genres : list ):
#     set_lyst = set( lyst )
#     new_lyst = []
#     for item in set_lyst:
#         new_lyst.append([item, lyst.count( item )])
#     if genres:
#         for a in new_lyst:
#             for b in genres:
#                 if a[0] == b[0]:
#                     b[1] += a[1]
#                     new_lyst.remove(a)
#         genres.extend( new_lyst )
#     else:
#         genres.extend( new_lyst )
#     return genres
# genres = countGenres( lista3, genres ).copy()
# print(genres)

lista = ["rojo", "verde", "azul", "permanent wave"]

print( lista.count("") )


