from ycappuccino.storage.models.decorators import Item, Property, Reference, ItemReference, Empty
from ycappuccino.storage.models.model import Model
from ycappuccino.core.decorator_app import App

@Empty()
def empty():
    _empty = Lyrics()
    _empty.id("45_reasons")
    _empty.music("45 reasons")
    _empty.lyrics("test")
    return _empty

@App(name="yblues")
@Item(collection="lyrics",plural="lyrics", name="lyric", secure_write=True)
@ItemReference(from_name="lyric",field="music", item="music")
class Lyrics(Model):
    def __init__(self, a_dict=None):
        super().__init__(a_dict)
        self._music = None
        self._lyrics = None

    @Reference(name="music")
    def music(self, a_value):
        self._music = a_value

    @Property(name="lyrics")
    def lyrics(self, a_value):
        self._lyrics = a_value

empty()