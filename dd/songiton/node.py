from attr import attrib, attrs
from collections import defaultdict


class MixinNode(object):
    node_name = None
    _node = None

    @property
    def node(self):
        '''singleton
        
        just giving the node methods to the MixinNoded - though they are defined in Node class!
        '''
        if self._node is None:
            self._node = Node
        return self._node

    def __getattr__(self, value):
        '''acces inner node from nodes'''
        
        nodes = self.node.get_node(node_name=node_name)
        if True:
            if node.node_name == node_name:
                return node

        

'''example of usage:

class Song(MixinNoded):
    def verse_chorus(self):
        self.verse

s = Song(...)
s.verse.chorus.every()

s.verse = Node
'''


class  Node(object):
    _node = None
    node_name = None
    node_names = ()
    node_unique = False

    def __init__(self, store=()):
        if store:
            self.node.extend(store)       

    @property
    def node(self):
        '''singleton.'''
        if self._node is None:
            self._node = NodeUtil(node=self)
        return self._node

    def __getattr__(self, value):
        '''acces inner node from nodes'''
        if hasattr(self, value):
            print('has')
            return getattr(self, value)
        else:
            print('hasnot')
            return self.node.by_node_name(node_name=value)

    @property
    def is_empty(self):
        return bool(self.node.store)

    @property
    def every(self):
        return self.node.store

    @property
    def first(self):
    
        if self.node.store:
            return self.node.store[0]
        return None

    @property
    def one(self):
        return self.first


class NodeUtil(object):
    _store = None
    def __init__(self, node):
        self.base = node

        self.nodes = defaultdict(list)  # key=cls, value=list of nodes
        self.node_names = defaultdict(list)  # key=cls, value=list of node_name
        assert self.is_correct

    @property
    def store(self):
        return [node for node in self.nodes.values()]

    def by_node_name(self, node_name):
        store = self.where[node_name]
        return Node(store=nodes)

    @property
    def names(self):
        return self._names(self.base)

    @staticmethod
    def _names(node):
        '''return all node names'''
        names = [node.node_name]
        names.extend(node.node_names)
        return names

    @property
    def is_correct(self):
        return self._is_correct(self.base)

    @classmethod
    def _is_correct(cls, node):
        return all(
            (
                isinstance(node, Node),
                all(
                    cls._is_correct_name(name)
                    for name in cls._names(node)
                )
            )
        )
        
    @staticmethod
    def _is_correct_name(name):
        return all(
            (
                isinstance(name, str),
                all(
                    char.isalnum() or char == '_'
                    for char in name
                ),
            )
        )

    def append(self, node):
        assert self._is_correct(node)
        cls = type(node)
        self.nodes[cls].append(node)
        for name in self._names(node):
            self.node_names[cls].append(name)
            self.refresh_where()

    def refresh_where(self):
        where = {}
        for cls, names in self.node_names.items():
            where.update(
                {
                    name: cls
                    for name in names
                }
            )
            
        self.where = where

    def remove(self, node):
        cls = type(node)
        self.nodes[cls].remove(node)
        if not self.nodes[cls]:
            del self.nodes[cls]
            del self.node_names[cls]
            self.refresh_where()


    def extend(self, nodes):
        for node in nodes:
            self.append(node)


@attrs
class Song(Node):
    node_name = 'song'
    title = attrib()

from enum import Enum
class VerseType(Enum):
    chorus = 'chorus'
    refren = 'refren'

@attrs
class Verse(Node):
    node_name = 'verse'
    text = attrib()
    type = attrib()

    @property
    def node_names(self):
        return [self.type.value]

if __name__ == "__main__":
    song = Song("dople")
    verses = [
        Verse("holalalala", VerseType.chorus),
        Verse("holalala", VerseType.refren),
    ]
    song.node.extend(verses)

    verses = song.verse
    verses = song.verse.every
    for verse in verses:
        print(verse.text)

    choruses = song.chorus
        
