# iTunesearch
iTunesearch is a mature and robust Python library for interfacing with the iTunes Store. The software combines both web scraping techniques and API wrapping utilities to replace the poorly engineered [iTunes Search API] (v2).

![artworks showcase](https://camo.githubusercontent.com/1998beb99d675c1fe1cc1d8fc1727606fe2a7476/687474703a2f2f696d672e77616c6c7061706572666f6c6465722e636f6d2f662f3742393533434346333936302f6974756e65732d617274776f726b2d7a6f6f6d2d616c62756d2d636f766572732e6a7067)

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
