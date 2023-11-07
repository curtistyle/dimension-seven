from spotipy import Spotify, SpotifyClientCredentials
from band import Album, Artist, Track
from os import rename
from werkzeug.utils import secure_filename
import os
import json 


class DataMethods():
    
    GENRES = {'punk', 'alternative metal', 'post-grunge', 'punk', 'rock', 'skate punk', 'socal pop punk', 'modern rock', 'alternative rock', 'conscious hip hop', 'funk metal', 'hard rock', 'nu metal', 'political hip hop','rap metal', 'rap rock', 'metal', 'old school thrash', 'thrash metal'}
    
    @staticmethod
    def get_pos():...
    
    @staticmethod
    def format_list(items : list, genres):
        """Retorna una `lista` con los items formateados. Donde `item` contiene `artista`, `album`, `track`. `list_select` la lista seleccionada que hace referencia al item."""
        lyst = list()
        print("ITEMS: ", items)
        for item in items:
            words = item.split('¯')
            base = { 'artist': words[0], 'album': words[1], 'track' : words[2], 'time' : words[3], 'genres': genres }
            lyst.append(base)
        return lyst  

    @staticmethod
    def values_to_listDyct(**kwargs):
        dyct = {}
        lyst = []
        for key, item in kwargs.items():
            dyct.update({key : item})
        lyst.append(dyct)
        return lyst
        
        

    @staticmethod
    def listString_to_listInt( lyst : list ):
        lyst_str = lyst.copy()
        lyst_int = map( int, lyst_str )
        lyst_int = list( lyst_int )
        return lyst_int
    
    @staticmethod
    def kwargsLists_to_dictionaryList(**kwargs):
        model_dyct = dict()
        lyst = list()
        matrix = list()
        for key, item in kwargs.items():
            model_dyct.update( {key : None} )
            matrix.append( item )
        for col in range( 0, len( matrix[ 0 ] ) ):
            new_dyct = model_dyct.copy()
            for row in range( 0, len( matrix ) ):
                keys = list( new_dyct.keys() )
                new_dyct[ keys[ row ] ] = matrix[ row ][ col ]
            lyst.append( new_dyct )    
        return lyst
    
    @staticmethod
    def countGenres( lyst : list, genres : list ):
        if (lyst.count("permanent wave")) > 0:
            lyst.remove("permanent wave")
        set_lyst = set( lyst )
        new_lyst = []
        for item in set_lyst:
            new_lyst.append([item, lyst.count( item )])
            
        aux = []
        if genres:
            for a in new_lyst:
                index = 0
                for b in genres:
                    if (a[0] == b[0]):
                        b[1] += a[1]
                    else:
                        index += 1
                if index == len(genres):
                    aux.append(a)
        else:
            genres.extend( new_lyst )
        if aux:
            genres.extend(aux)
        return genres
    
    @staticmethod
    def recount( lyst : list ):
        counter = 0
        for item in lyst:
            counter += 1
            time = item['time']
            new_time = DataMethods.time_accumulator( time, "00:00" )
        return new_time, counter
    
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
    
    
    def time_to_dict( time : str ):
        dyct = { 'hora' : 0, 'minuto' : None, 'segundo' : None }
        if( len( time.split(":") ) == 2 ):
            dyct['minuto'], dyct['segundo'] = map( int, time.split(":") )
        elif( len( time.split(":") ) == 3 ):
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

    @staticmethod
    def time_accumulator( time : str, total_time : str ):
        time = DataMethods.time_to_dict( time )
        total_time = DataMethods.time_to_dict( total_time )
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
        
        return DataMethods.dict_to_time( total_time )
    

class FileUpload():
    ALLOWED_EXTENSIONS = set(['png', 'jpg'])
    def __init__(self, file) -> bool:
        self.upload = file
        self.filename = secure_filename(file.filename)
        self.name = self.filename.split('.')[0]
        self.extension = self.filename.split('.')[1]
        if self.extension in FileUpload.ALLOWED_EXTENSIONS:
            return True
        else:
            return False
    
    def toString(self):
        print( f"file={self.upload}\n"
               f"name={self.name}\n"
               f"extension={self.extension}\n"
              )
      
class File():
    
    
    
    type_file = {
        "user" : { 'id' : None,  "email": None, "nickname": None},
        "list" : { 'id' : None, 'name' : None, 'amount' : 0, 'total_time' : "00:00", 'privacy' : "danger", "description" : None, 'genres' : { 'gen' : [] } },
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
      
        # ! falta, refactorizar
    def overwrite(self, data : list, **info ):
        self.fread()
        self.__data['data'] = data
        for key, item in info.items():
            if key in self.__data['list'].keys():
                self.__data['list'][key] = item
        self.fwrite()
        
    def delete(self, data : list, **info ):
        self.fread()
        if (len( data ) != len(self.__data['data'])):
            for key, item in info.items():
                if key in self.__data['list'].keys():
                    self.__data['list'][key] = item
            DataMethods.bubbleSortWithTweak( self.__data['data'], 'track' ) # ? track list file
            
            new_list = []
            for item in data:
                pos = DataMethods.binarySearch( item['track'], 'track', self.__data['data'] )
                if pos is not None:
                    new_list.append( self.__data['data'][pos] )
                    # self.__data['data'].pop(pos)
            
            new_genre = [] 
            for item in new_list:
                new_genre = DataMethods.countGenres( item['genres'], new_genre )    
            
            self.__data['data'] = new_list
            self.__data['list']['genres'] = new_genre
            self.fwrite()
        else:
            self.overwrite(data,info=info)
            new_genre = self.__data['list']['genres']
        return new_genre
    
    def rename_file(self, value):
        original_path = self.__path
        new_path = "json/" + value + ".json"
        try:
            rename(original_path, new_path)
        except FileNotFoundError:
            print( "The origial file no exist!" )
        except PermissionError:
            print( "You do not have permission to rename the file." )
            
    
    
    def data_append(self, **kwargs):
        data = dict()
        for key, item in kwargs.items():
            data.update({key : item})
        self.fread()
        DataMethods.bubbleSortWithTweak(self.data__.get('data'), 'track')
        if DataMethods.binarySearch(data['track'], "track", self.data__.get('data')) is None:  
            self.inc_amount()
            data.update({"order" : self.get_amount() })          
            self.data__.get('data').append(data)
            self.fwrite()
            return True
        else:
            return False

    def get_amount(self):
        return int(self.data__.get("list")['amount'])
    
    def inc_amount(self):
        amount = self.get_amount() + 1
        self.data.get("list")['amount'] = amount
        
    def data_insert(self, lyst : list, genre : list, error=[]):       
        self.fread()
        total_time = self.__data.get('list')['total_time']
        old_gen = self.__data.get('list')['genres']
        
        print("####################")
        print( f"{genre=}", end="\n\n" )
        print( f"{old_gen=}", end="\n\n" )
        
        new_gen = DataMethods.countGenres( genre, old_gen )
        self.__data.get('list')['genres'] = new_gen
        for item in range(0, len(lyst)):
            
            DataMethods.bubbleSortWithTweak(self.__data.get('data'), 'track')
            print( f"lyst[item]['track']={lyst}" )
            
            if DataMethods.binarySearch(lyst[item]['track'], "track", self.__data.get('data')) is None:   
                amount = self.__data.get('list')['amount']
                amount += 1
                
                # ! EDITANDO  
                
                # genres : set
                # genres = lyst[item]['genres']
                # self.__data.get('list')['genres']
                
                total_time = DataMethods.time_accumulator( lyst[item]['time'], total_time )

                lyst[item].update({'order' : amount})
                self.__data.get('list')['amount'] = amount
                self.__data.get('data').append(lyst[item])
            else: 
                error.append(lyst[item])
        self.__data.get('list')['total_time'] = total_time
        self.fwrite()
        return total_time, amount, {'gen':new_gen}

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
    
    def get_info(self):
        self.fread()
        return self.__data.get('list')
    
    def get_data(self):
        self.fread()
        DataMethods.bubbleSortWithTweak(self.__data.get('data'), 'order')
        return self.__data.get('data')
        
    @staticmethod
    def get_lists( ids_lists : list ) -> list:
        """ get lists of multiples files"""
        lyst = []
        for id_list in ids_lists:
            item = File( str( id_list[0] ) ).data.get( 'list' ) 
            lyst.append( item )
        return lyst
    
    @staticmethod
    def fileupload( file, folder, id_user ):
        ALLOWED_EXTENSIONS = set(['png', 'jpg'])
        name = file.filename.split(".")[0]
        extension = file.filename.split(".")[1]
        file.filename = f"img_profile-{id_user}.{extension}"
        filename = secure_filename(file.filename)
        if extension in ALLOWED_EXTENSIONS:
            file.save( os.path.join( folder, filename ) )
            return filename, None
        else:
            return None, extension
    
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
                artist = Artist(artist_item["name"], artist_item["genres"])
                
                # Lista de Album()
                list_albums = []
                pos = 1
                
                print( f"{artist_item['genres']=}", end="\n\n" )
                
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
                        
                    list_albums.append({'title': album.title,'year':album.year, 'tracks':track_list,'property':acordion_property,'img':album.img,'genres':artist.genres})
                    pos += 1
            else:
                return None
                
            # ! garbage collector
            del artist, album, track
            return list_albums
    