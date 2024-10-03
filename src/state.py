from src.models.components import BaseObject
from src.view import View


class State:
    def __init__(self):
        self.objects: list[BaseObject] = []

        # general
        self.view = View.BATTLE

    def view_setter(self, view):
        def inner():
            self.view = view

        return inner

    def add(self, object):
        self.objects.append(object)

    def remove(self, object):
        self.objects.remove(object)


state = State()
