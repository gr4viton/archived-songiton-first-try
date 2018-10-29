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

    def __init__(self, store=(), node_name=None):
        if node_name:
            self.node_name = node_name
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
        self.refresh_where()
        assert self.is_correct

    @property
    def store(self):
        return [node for node_list in self.nodes.values() for node in node_list if node_list]

    def by_node_name(self, node_name):
        cls = self.where[node_name]
        store = [
            node
            for node in self.nodes[cls]
            if node_name in node.node.names  # needed as the node_names are not connected only to node class
        ]
        return Node(store=store, node_name=node_name)

    @property
    def names(self):
        return self._names(self.base)

    @staticmethod
    def _names(node):
        '''return all node names'''
        names = [node.node_name]
        if node.node_names:
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
        if not isinstance(name, str):
            return False
        if not all(
            [
                char.isalnum() or char == '_'
                for char in name
            ]
        ):
            return False
        return True

    # def __iter__(
        

    def append(self, node):
        assert self._is_correct(node)
        cls = type(node)
        self.nodes[cls].append(node)
        for name in self._names(node):
            self.node_names[cls].append(name)
            self.refresh_where()
        return self.base

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
        return self.base

    @property
    def str(self):

        base = str(self.base)
        bas = base[:-1]
        use_comma = bas[-1] != '('
        node_reprs = []
        for node in self.store:
            if isinstance(node, Node):
                repr_ = node.node.str
            else:
                repr_ = str(node)
            node_reprs.append(repr_)

        nodes = ', '.join(node_reprs)
        mid = ''
        if use_comma and nodes:
            mid += ', '
        if nodes:
            mid += 'node.store=[{nodes}]'.format(nodes=nodes)
        txt = '{bas}{mid})'.format(bas=bas, mid=mid)
        return txt

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
        if self.type.value:
            return [self.type.value]

@attrs
class Tune(Node):
    node_name = 'tune'
    pass

@attrs
class Chord(Node):
    node_name = 'chord'
    name = attrib()

if __name__ == "__main__":
    song = Song("dople")
    verses = [
        Verse("holalalala", VerseType.chorus),
        Verse("holalala", VerseType.refren),
    ]
    song.node.extend(verses)

    verses = song.verse
    print('song.verse')
    print(verses)
    verses = song.verse.every
    print('song.verse.every')
    print(verses)
    for verse in verses:
        print(verse)
        print(type(verse))
        print(verse.text)

    choruses = song.chorus.every
        
    print(choruses)


    tunes = [
        Tune().node.extend(
            [
                Chord('A'),
                Chord('C'),
            ]
        ),
        Tune().node.extend(
            [
                Chord('D'),
                Chord('C'),
            ]
        ),
    ]

    print(tunes)

    # song,verse.chorus
    # song.verse.verse
    # song.verse[1]

    ver0 = song.verse.one
    ver0.node.extend(tunes)
    print(ver0.node.str)

