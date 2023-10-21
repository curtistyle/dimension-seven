from spotipy import Spotify, SpotifyClientCredentials
from band import Album, Artist, Track
import json 


class DataMethods():
    @staticmethod
    def get_pos():...
    
    @staticmethod
    def format_list(items : list):
        """Retorna una `lista` con los items formateados. Donde `item` contiene `artista`, `album`, `track`. `list_select` la lista seleccionada que hace referencia al item."""
        lyst = list()
        print("ITEMS: ", items)
        for item in items:
            words = item.split('¯')
            base = { 'artist': words[0], 'album': words[1], 'track' : words[2], 'time' : words[3] }
            lyst.append(base)
        return lyst  

    def bubbleSortWithTweak(lyst, key):
        n = len(lyst)
        while n > 1:    
            swapped = False
            i = 1
            while i < n:
                if lyst[i][key] < lyst[i - 1][key]:   
                    temp        = lyst[i]
                    lyst[i]     = lyst[i - 1]
                    lyst[i - 1] = temp
                    swapped = True
                i += 1
            if not swapped: return           
            n -= 1
    
    def binarySearch(target, key, sortedLyst):
        left = 0
        right = len(sortedLyst) - 1
        while left <= right:
            midpoint = (left + right) // 2
            if target == sortedLyst[midpoint][key]:
                return midpoint
            elif target < sortedLyst[midpoint][key]:
                right = midpoint - 1
            else:
                left = midpoint + 1
        return None

    @staticmethod
    def reorder(lyst : list, key : str, target : object):
        """Alinea la `lyst` a partir del `target` eliminado."""
        for index in range(0, len(lyst)):
            if lyst[index][key] > target:
                lyst[index][key] -= 1
    

class File():
    type_file = {
        "user" : { 'id' : None,  "email": None, "nickname": None},
        "list" : { 'id' : None, 'name' : None, 'amount' : 0, 'privacy' : "danger", "description" : None },
        "data" : []
    }
    
    def __init__(self, name) -> None:
        self.name = name
        self.__path = "json/" + self.name + ".json"
        self.__file = None
        self.__data = None
    
    @property
    def path(self):
        return self.__path
    
    @property
    def file(self):
        return self.__file
    
    @property
    def data(self):
        self.fread()
        return self.__data
    
    @data.setter
    def data(self, value):
        self.__data = value
    
    @file.setter
    def file(self, value):
        self.__file = value
    
    @path.setter
    def path(self, value):
        self.__path = value;

    def fread(self):
        self.__file = open(self.__path, "r")
        with self.__file as f:
            self.__data = json.load(f)
        self.file.close()
    
    # ! seguir editando
    def fcreate(self, id_user : int, name_list : str, email : str, nickname : str, description : str):
        try:
            self.__file = open(self.__path, "x")
            File.type_file.get('user')['id'] = id_user
            File.type_file.get('user')['nickname'] = nickname
            File.type_file.get('user')['email'] = email
            File.type_file.get('list')['name'] = name_list
            File.type_file.get('list')['id'] = self.name
            File.type_file.get('list')['description'] = description
            with self.__file as f:
                json.dump(File.type_file, f)
            self.__file.close()
        except FileExistsError:
            print("El archivo ya existe.")
    
    def fwrite(self : dict):
        self.__file = open(self.__path, "w")
        with self.__file as f:
            json.dump(self.__data, f)
        self.__file.close()

    def __add_user(self, **kwargs):
        data = dict()
        self.fread()
        for key, item in kwargs.items():
            data.update({key : item})    
        self.data['user'] = data
        self.fwrite()
        
    def __add_list(self, **kwargs):
        data = dict()
        self.fread()
        for key, item in kwargs.items():
            data.update({key : item})
        self.data['list'] = data
        self.fwrite()

    def __add_data(self, **kwargs):
        data = dict()
        self.fread()
        for key, item in kwargs.items():
            data.update({key : item})
        self.data['list'] = data
        self.fwrite()
        
    def update_user(self, **kwargs):
        self.fread()
        for key, item in kwargs.items():
            self.data.get("user")[key] = item
        self.fwrite()
    
    def update_list(self, **kwargs):
        self.fread()
        for key, item in kwargs.items():
            self.data.get("list")[key] = item
        self.fwrite()
      
        # ! falta
    def update_data(self, **kwargs):
        self.fread()
        items = self.__data.get('data')
      
                
            
        
        self.fwrite()

    
    def data_append(self, **kwargs):
        data = dict()
        for key, item in kwargs.items():
            data.update({key : item})
        self.fread()
        DataMethods.bubbleSortWithTweak(self.data.get('data'), 'track')
        if DataMethods.binarySearch(data['track'], "track", self.data.get('data')) is None:  
            self.inc_amount()
            data.update({"order" : self.get_amount() })          
            self.data.get('data').append(data)
            self.fwrite()
            return True
        else:
            return False

    def get_amount(self):
        return int(self.data.get("list")['amount'])
    
    def inc_amount(self):
        amount = self.get_amount() + 1
        print(amount)
        self.data.get("list")['amount'] = amount
        
    def data_insert(self, lyst : list, error : list):       
        self.fread()
        for item in range(0, len(lyst)):  
            DataMethods.bubbleSortWithTweak(self.__data.get('data'), 'track')
            print(f"lyst[item]['track']={lyst}")
            # print(f"self.__data.get('data')={self.__data.get('data')}")
            if DataMethods.binarySearch(lyst[item]['track'], "track", self.__data.get('data')) is None:   
                amount = self.__data.get('list')['amount']
                amount += 1
                lyst[item].update({'order' : amount})
                self.__data.get('list')['amount'] = amount
                self.__data.get('data').append(lyst[item])
            else: 
                error.append(lyst[item])
        self.fwrite()
        if error:
            return False
        else:
            return True

    def data_pop(self, **kwargs):
        data = dict()
        for key, item in kwargs.items():
            data.update({key : item})
        self.fread()
        pos = DataMethods.binarySearch(data['track'], "track", self.data.get('data'))
        if (pos is not None):
            order = self.data.get('data')[pos]['order']
            self.data.get('track').pop(pos)
            DataMethods.reorder(self.data.get('data'),"order", order)
            return True
        else:
            return False
    
    def get_list(self):
        self.fread()
        DataMethods.bubbleSortWithTweak(self.__data.get('data'), 'order')
        return self.__data.get('data')
        
class mySpotify():
    # credenciales de la aplicacion
    __client_id = "aad4ffcc488644c8ac36c765382751be"
    __client_secret = "dccf369fdec34a9f8de258890cae5b30"
    
    __auth_manager = SpotifyClientCredentials(client_id=__client_id, client_secret=__client_secret)
    
    def __init__(self) -> None:
        self.__sp = Spotify(auth_manager=mySpotify.__auth_manager)
    
    def search(self, name):
            
            # Buscar el artista
            results = self.__sp.search(q=name, type="artist", limit=1)
            
            if "artists" in results and "items" in results["artists"]:
                
                artist_item = results["artists"]["items"][0]
                artist_id = artist_item["id"]
                
                # * Artist()
                artist = Artist(artist_item["name"])
                
                # Lista de Album()
                list_albums = []
                pos = 1
                
                # Obtener los álbumes del artista
                sp_albums = self.__sp.artist_albums(artist_id, album_type="album")

                for sp_album in sp_albums["items"]:
                    
                    acordion_property = "panelsStayOpen-collapse" + str(pos)
                    
                    # * Album()
                    album = Album(sp_album["name"], sp_album["total_tracks"], sp_album['release_date'], sp_album['images'][0]['url'])
                    
                    sp_tracks = self.__sp.album_tracks(sp_album['id'])
                    
                    # Lista de Track()
                    track_list = []
                    
                    for sp_track in sp_tracks["items"]:
                        
                        # * Track()
                        track = Track(sp_track['name'], sp_track["track_number"], sp_track['duration_ms'])                        
                        
                        track_list.append({'title':track.title, 'time': track.time.fminseg()})
                        
                    list_albums.append({'title': album.title,'year':album.year, 'tracks':track_list,'property':acordion_property,'img':album.img})
                    pos += 1
            else:
                return None
                
            # ! garbage collector
            del artist, album, track
            return list_albums
    