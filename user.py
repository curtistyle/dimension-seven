from dataclasses import dataclass


@dataclass
class Target():
    lyst : int
    genre : list
    
    @property
    def lyst(self):
        return self.__lyst
    
    @property
    def genre(self):
        return self.__genre
    
    @lyst.setter
    def lyst(self, value):
        self.__lyst = value
    
    @genre.setter
    def genre(self, value):
        self.__genre = value
        
        
    

    
class User():
    def __init__(self, id, name, surname, nickname, path_img) -> None:
        self.__id = id
        self.__name = name
        self.__surname = surname
        self.__nickname = nickname
        self.__path_img = path_img
        #self.target : Target
        
    @property
    def id(self):
        return self.__id
    
    @property
    def name(self):
        return self.__name
    
    @property
    def surname(self):
        return self.__surname
    
    @property
    def nickname(self):
        return self.__nickname
    
    @property
    def path_img(self):
        return self.__path_img
    

    
    
    @id.setter
    def id(self, value):
        self.__id = value
    
    @name.setter
    def name(self, value):
        self.__name = value
        
    @surname.setter
    def surname(self, value):
        self.__surname = value
    
    @nickname.setter
    def nickname(self, value):
        self.__nickname = value
    
    @path_img.setter
    def path_img(self, value):
        self.__path_img = value


    
    