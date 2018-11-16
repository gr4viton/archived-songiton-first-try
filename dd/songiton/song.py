from attr import attrib, attrs

@attrs
class Songiton(object):
    '''Song - with multiple particular realisations.'''
    songs = attrib(factory=list)

@attrs
class PersonName(Node)
    node_name = 'name'
    text = attrib()
    def node_names(self)
        if 
    

@attrs    
class MixinUtilPersonName(object):
    """Util methods fpr PersomName nodes.

    add to classes which should work with PersonName nodes
    """
    # container = attrib(factory=list)
    node_classes = [PersonName]
    def name(self)
    

    def fill_from_split(name_str):
        return cls(container=name_str.split(" "))

   # @property
    # def first(self)
        # return self.container[0]

    # @property
    # def last(self)
        # return self.container[-1]


class Person(Node, MixinUtilPersonName):
    node_name = 'person'
    node_classes = [MixinUtilPersonName.node_classes*]
    birth = attrib()

    @property
    def node_names(self):
        names = []
        if self.music_band.has or self.music_group.has
            'musician'

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
    node_allowed = [MusicBand, Person,
    name = attrib()
    musicians = attrib()
    interval = attrib()

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
    
class MixinVersed(Node)
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



if __name__ == "__main__":
    p = Person().node.extend(
        [
            Person.factory.parse_from_text('Honza Petrov'),
            Person.event.factory.birth(date),
        ]
    )

    p = Person.factory.from_wiki_str(


    p = Person(name=Person.name.factory.from_str('a b'), birthday=date)

    this way the name would be there also when you do not add the name node - can have methods to get it from wiki - lazy updsting


podobnost pisnicekk ruznych kapel
known la

udelat to skrze covery - lyrics z hlasu = a[ka uzivatel se nahraje jak zpiva - melodie a lyrics

chords se snad sdilet muzou - esi ne tak taky cover - vzdy jeden akor pridat nakonec nebo zacatek.

from youtube  ideos multiple - captions.

