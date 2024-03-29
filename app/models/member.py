from ycappuccino.core.models.decorators import Item,  Property, Reference, ItemReference, Empty
from ycappuccino.storage.models.model import Model
from ycappuccino.core.decorator_app import App

@Empty()
def empty():
    _empty = Member()
    _empty.id("test")
    _empty.name("yaiba")
    _empty.role("test")
    _empty.band("yblues")
    return _empty

@App(name="yblues")
@Item(collection="members",plural="members",name="member", secure_write=True)
@ItemReference(from_name="member",field="band", item="band")
class Member(Model):
    def __init__(self, a_dict=None):
        super().__init__(a_dict)
        self._band = None
        self._name = None
        self._role = None

    @Property(name="name")
    def name(self, a_value):
        self._name = a_value

    @Property(name="role")
    def role(self, a_value):
        self._role = a_value

    @Reference(name="band")
    def band(self, a_value):
        self._band = a_value

empty()