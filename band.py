class Artist():
    """ Constructor """
    def __init__(self, name=''):
        self.__name : str = name
    
    def __repr__(self):
        return (
            f"{self.__class__.__name__} ( "
            f"name={self.__name!r} ) "     
        ) 
   
    """ Get Name atribute from Artist Object """
    @property
    def name(self):
        return self.__name
    
    """ Set Name atribute in Artist Object """
    @name.setter
    def name(self, value):
        self.__name = value
        
class Album():
    """ Constructor: se llama cuando se crea una nueva instancia de la clase. """
    def __init__(self, title='', count=0, year=0, img=''):
        self.__title      : str = title
        self.__count      : int = count
        self.__year       : int = year
        self.__img        : str = img        
    
    def __len__(self):
        return len(self.__title)
    
    def __eq__(self, other):
        """ Define la igualdad entre dos Objetos. """
        if other.__class__ is self.__class__: 
            return (
                self.__title,
                self.__count,
                self.__year,
                self.__img,
            ) == (
                other.__title,
                other.__count,
                other.__year,
                other.__img
            )
        else:
            return NotImplemented
    def __ne__(self, other):
        """ Define la desigualdad entro dos Objetos. """ 
        result = self.__eq__(other)
        if result in NotImplemented:
            return NotImplemented
        else:
            return not result
    def __repr__(self):
        """ Devuelve una representacion en cadena de caracteres que se utiliza para la representacion oficial del Objeto """
        return (
            f"{self.__class__.__name__} ( "
            f"title={self.__title!r}, "
            f"count={self.__count!r}, "
            f"year={self.__year!r}, "
            f"img={self.__img!r} ) "   
        )
    
    def __str__(self):
        return f"title={self.__title}, count={self.__count}, year={self.__year}, img={self.__img}"
    
    def __hash__(self):
        return hash((
            self.__class__,  
            self.__title, 
            self.__count, 
            self.__year, 
            self.__img
        ))   
    
    @property
    def title(self):
        return self.__title

    @property
    def count(self):
        return self.__count

    @property
    def year(self):
        return self.__year
    
    @property
    def img(self):
        return self.__img
    
    @title.setter
    def title(self, value):
        self.__title = value

    @count.setter
    def count(self, value):
        if (value >= 0):
            self.__count = value
        else:
            assert ValueError("No puede ser negativo.")
    
    @year.setter
    def year(self, value):
        if (value >= 0):
            self.__year = value
        else:
            assert ValueError("No puede ser negativo.") # raise
    
    @img.setter
    def img(self, value):
        self.__img = value

class Time():
    def __init__(self, ms='') -> None:
        self.__ms : str = ms
        
    @property
    def ms(self):
        return self.__ms
    
    @ms.setter
    def ms(self, value):
        self.__ms = value
        
    def fminseg(self):
        seg, self.ms = divmod(self.ms, 1000)
        mints, seg = divmod(seg, 60)  
        return f'{mints:02}:{seg:02}'
 
class Track():
    def __init__(self, title='', number=0, time=''):
        self.__title  : str = title
        self.__number : str = number 
        self.__time   = Time(time)

    def __str__(self) -> str:
        return f"number='{self.__number}' title='{self.__title}' time='{self.__time}'"
    
    def __repr__(self):
        return (
            f"{self.__class__.__name__} ( "
            f"name={self.__title!r}, "
            f"time={self.__time!r}, "
            f"number={self.__number!r} ) "
            
        )
        
    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return (
                self.__title,
                self.__tme,
                self.__number
            ) == (
                other.__title,
                other.__time,
                other.__number
            )
        else:
            return NotImplemented
         
    def __bool__(self):
        return ((len(self.__title) > 0) and (self.__time > 0) and (self.__number > 0))
        
    @property
    def title(self):
        """Get `Title` atribute from `Track` object."""
        return self.__title
    
    # ! EDIT
    @property
    def time(self):
        """Get `Title` atribute from `Track` object."""
        return self.__time
    
    @property
    def number(self):
        """Get `Number` atribute from `Truck` object."""
        return self.__number
    
    
    @title.setter
    def title(self, value):
        if isinstance(value, str):
            self.__title = value
        else:
            raise ValueError("El valor que ingreso debe ser de tipo 'str'.")
        
    @time.setter
    def time(self, value):
        self.__time = value

    @number.setter
    def number(self, value):
        if (value >= 0):
            self.__number = value
        else:
            raise ValueError("No puede ser negativo.")
  
    @staticmethod
    def time_accumulator( time : str, total_time : str ):
        ...