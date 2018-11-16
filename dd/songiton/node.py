'''example of usage:

class Song(MixinNoded):
    def verse_chorus(self):
        self.verse

s = Song(...)
s.verse.chorus.every()

s.verse = Node
'''
from attr import attrib, attrs
from collections import defaultdict, Sequence


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

        


class  Node(Sequence):
    _node = None
    node_name = None
    node_names = ()
    node_unique = False
    _node_index = None

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

    def __getitem__(self, index):
        return self.node.store[index]
    def __len__(self):
        return len(self.node.store)

    @property
    def is_empty(self):
        return bool(self.node.store)

    @property
    def every(self):
        return self.node.store

    @property
    def last(self):
    
        if self.node.store:
            return self.node.store[-1]
        return None

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
        for index, node in enumerate(store):
            node._node_index = index
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

        # assert check node_name collfirstisions
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

from enum import Enum
class SongTextFormat(Enum):
    plain_lyrics = 'plain_lyrics'

class SongFactory(object):
    @classmethod
    def from_text(cls, text, song_text_format=None):
        sform = song_text_format
        if sform is None:
            sform = cls.detect_song_text_format(text)
        if sform is sform.plain_lyrics:
            return cls.from_text_plain_lyrics(text)

    @classmethod
    def detect_song_text_format(cls, text):
        return SongTextFormat.plain_lyrics
    @classmethod
    def from_text_plain_lyrics(cls, text):
        verses = []
        verse = []
        for line in text.splitlines():
            if line:
                verse.append(line)
            else:
                verses.append(verse)
                verse = []
        else:
            if verse:
                verses.append(verse)

        verses = [
            VerseFactory.from_text(verse)
            for verse in verses
        ]


class LineCategory(Enum):
    lyrics = 'lyrics'
    chords = 'chords'


@attrs
class Line(object):
    
    text = attrib()

    @property
    def chord_alpha_chars(self):
        major_chars = {chr(num) for num in range(ord('a'), ord('h'))}
        other = set('misu')
        return major_chars + other


    @property
    def category(self):
            """Anotate this way some number of verses, thsn create nn to categorise it for you and learn it on the annotated verses."""
        alpha_chars = {char.lower() for char in set(self.text) if char.alpha}
        cnt = sum([
            1 for char in alpha_chars
            if char not in set(chord_alpha_chars):
        ])
        if cnt*10 < alpha_chars:
            return LineCategory.chords
        else:
            LineCategory.lyrics

class VerseFactory(object):

    @classmethod
    def from_text(cls, text):
        if not isinstance(text, Iterable):
            if isinstance(text, str):
                text = text.splitlines()

        prev_chords = None

        for line in text:
            lin = Line(line)
            if lin.category is lin.category.chords:
                prev_chords = lin
                continue

            tune = Tune.from_lines([lin, prev_chords])
            if prev_chords:
                lin.node.append(prev_chords)
                prev_chords = None



@attrs
class Song(Node):
    node_name = 'song'
    title = attrib()
    factory = SongFactory
    fill = None
    shaper = None

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
    @classmethod
    def from_lines(cls, lyric_line, chord_line):
        ref = '(\[\w+\])'
        re.match(ref, chord_line)
        for chord_txt in regex.groups():
            print(chord_txt)
    pass

@attrs
class Chord(Node):
    node_name = 'chord'
    name = attrib()

def test_node():
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

    # Chords.A = Chord('A')
    # Chord('A', guitar_position=base/barre)
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

    ver0 = song.verse.one
    ver0.node.extend(tunes)
    print(ver0.node.str)

    
    print('\n song.chorus')
    print(song.chorus.node.nodes)
    print(song.chorus.node.node_names)
    # song.v
    assert song.chorus.first == song.verse.chorus.first
    assert song.verse.verse.first == song.verse.first

    verses = song.verse.every
    for verse in verses:
        print(verse._node_index, verse)

    print('first verse')
    print(song.verse[0])
    print('last verse')
    print(song.verse[-1])

def test_song_parser():
    fname = 'lyric.txt'
    with open(fname, 'r') as fil:
        text = fil.read()
    song = Song.factory.from_text(text)
    
if __name__ == "__main__":
    # test_node()
    test_song_parser()
