from ycappuccino.storage.models.decorators import Item, Property, Empty
from ycappuccino.storage.models.model import Model
from ycappuccino.core.decorator_app import App

@Empty()
def empty():
    _empty = Band()
    _empty.id("test")
    _empty.name("test")
    _empty.bio("test")
    _empty.address("7 rue test")
    _empty.city("Grenoble")
    return _empty

@App(name="yblues")
@Item(collection="bands", plural="bands",name="band", secure_write=True)
class Band(Model):
    def __init__(self, a_dict=None):
        super().__init__(a_dict)
        self._name = None
        self._bio = None
        self._address = None
        self._city = None



    @Property(name="name")
    def name(self, a_value):
        self._name = a_value

    @Property(name="bio", maxLength=250)
    def bio(self, a_value):
        self._bio = a_value
        
    @Property(name="address")
    def address(self, a_value):
        self._address = a_value

    @Property(name="city")
    def city(self, a_value):
        self._city = a_value

empty()