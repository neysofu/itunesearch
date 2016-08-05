# iTunesearch
iTunesearch is a mature and robust Python library for interfacing with the iTunes Store. The software combines both web scraping techniques and API wrapping utilities to replace the poorly engineered [iTunes Search API] (v2).

![artworks showcase](http://img.wallpaperfolder.com/f/7B953CCF3960/itunes-artwork-zoom-album-covers.jpg)

## Features
- A customizable `Media` class, with callbacks and other advanced object oriented features.
- Robust and clean interface, no frills.
- Descriptive and comprehensive documentation.
- Support for both `search` and `lookup` actions.
- High-quality, official iTunes

Every store item is just one click away.

```
import itunesearch
app = itunesearch.Application

song = app.search_song('Adele')[0]
print(song.get_track_name())
```
