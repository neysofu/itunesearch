# iTunesearch
iTunesearch is a fully fledged API wrapper for surfing the iTunes Store. It provides a clean and simple interface.

## Features
- A customizable `Media` class, with callbacks and other advanced object oriented features.
- Robust and clean interface, no frills.
- Descriptive and comprehensive documentation.
- Support for both `search` and `lookup` actions.
- High-quality, official iTunes

![artworks showcase](http://img.wallpaperfolder.com/f/7B953CCF3960/itunes-artwork-zoom-album-covers.jpg)

Every store item is just one click away.

```
import itunesearch
app = itunesearch.Application

song = app.search_song('Adele')[0]
print(song.get_track_name())
```
