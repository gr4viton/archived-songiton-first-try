from attr import attrib, attrs

@attrs
class Songiton(object):
    '''Song - with multiple particular realisations.'''
    songs = attrib(factory=list)
 

@attrs    
class PersonName(object):
    container = attrib(factory=list)

    @classmethod
    def from_split(name_str):
        return cls(container=name_str.split(" "))
    @property
    def first(self)
        return self.container[0]

    @property
    def last(self)
        return self.container[-1]

class Person(MixinNode):
    name = attrib()
    birth = attrib()

class MusicBand(object):
    '''Group of time relevant MusicGroups
    
    Args:
        container (list of MusicGroup): time relevant musician filled groups
    '''
    container = attrib()

    @property
    def name(self):
        '''Main group name, or the most known, or the latest or the median.

        Taken from MusicGroups.name from ccontainer
        '''
        if not self.container:
            rerurn None
        
        latest = True
        if latest:
            return self.container[-1]

class MusicGroup(object):
    """
    just one name and one person
    characterized by interval in time
    if the group changes name - it is still one MusicBan, not MusicGroup
    """
    name = attrib()
    musicians = attrib()
    interval = attrib()
    band = attrib()

@attrs
class Song(object):
    '''One specific realisation of Songitom.'''
    title = attrib()
    author = attrib()
    group = attrib(default=None)
    created = attrib()

    def band(self)
        if not self.group:
            return None
        return self.group.band
    
class MixinVersed(MixinNode)
    def verses
        '''-from nodes of type verse - every'''
        self.verse.every()

    def lyrics(self)
        return self.verses.lyrics
    
    def chords(self)
        return self.verses.lyrics
    def tabs(self)
    def notes(self)

    def get_lyrics


song1 = jsonpickle(song1)
song.data = {
    verse
        type: chorus/refren
        chords used property
        tunes = tune store
        melody property- from tunes
        to_song_format- output str in some format
        lyrics property- from tunes
}

tune = {
    base = tune store 
    length property- from base.length or self.length_
    notes
    lyrics
    chords - can be generated from notes..
}
