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

lyst = ["1", "2", "3", "4"]
print( lyst )
lyst = map( int, lyst )
print( list(lyst) )

# print( int( lyst ) )


# for index, item in iter(map(lyst)):
#     print( f"{index=} - {item=}" )




