# iTunesearch ![build](https://travis-ci.org/neysofu/itunesearch.svg?branch=master) ![license](https://img.shields.io/badge/license-MIT-blue.svg) ![status](https://img.shields.io/badge/maintained-yes-orange.svg)

iTunesearch is a mature and robust Python wrapper for the [infamous](https://medium.com/@ftxdri/the-itunes-api-the-epitome-of-bad-api-design-b83a9ac41132#.ka9dfyzd3) iTunes Search APIs. It features support for both `search` and `lookup` actions, comprehensive testing suits, and more.

    pip install itunesearch

Behold, the power of iTunesearch:

    >>> import itunesearch
	>>> happy = itunesearch.search_track('Happy')[0]
	>>> happy.get_price()
	(1.29, 'USD')
	>>> happy.grab_author().get_name()
	'Pharrell Williams'

![artworks showcase](http://i.stack.imgur.com/vR2sL.png)

## Future enhancements

 - [ ] Make backward compatibility changes to fully support Python 2.7+.
 - [ ] Write a descriptive, *up-to-date* dcoumentation.
 - [ ] Add support for `Book` and `Software` store items.

