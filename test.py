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

# def swap(lyst, i, j):
#      """Exchanges the items at positions i and j."""
#      # You could say lyst[i], lyst[j] = lyst[j], lyst[i]
#      # but the following code shows what is really going on
#      temp = lyst[i]
#      lyst[i] = lyst[j]
#      lyst[j] = temp

# def bubbleSortWithTweak(lyst, key):
#     n = len(lyst)
#     while n > 1:
#         swapped = False
#         i = 1
#         while i < n:
#             if lyst[i][key] < lyst[i - 1][key]:   # Exchange if needed
#                 swap(lyst, i, i - 1)
#                 swapped = True
#             i += 1
#         if not swapped: return            # Return if no swaps
#         n -= 1

# def binarySearch(target, key, sortedLyst):
#     left = 0
#     right = len(sortedLyst) - 1
#     while left <= right:
#         midpoint = (left + right) // 2
#         if target == sortedLyst[midpoint][key]:
#             return midpoint
#         elif target < sortedLyst[midpoint][key]:
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


from database import agregar_lista

print(agregar_lista(1, 'Lista 5', "asd"))


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