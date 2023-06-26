# TiddlPy

Welcome to TiddlPy, a Python module for interacting with TiddlyWiki files, a unique non-linear notebook.

## Description

TiddlPy is designed to read, search, delete, and write tiddlers (entries) within TiddlyWiki files. It was originally created by Neil Griffin and is currently maintained by OpenCo.

The module uses BeautifulSoup to parse the HTML structure of TiddlyWiki files. It provides the following functionalities:

- Load tiddlers from a TiddlyWiki file and convert them into Python dictionaries.
- Find and search for specific tiddlers in a TiddlyWiki file.
- Edit (delete and write) tiddlers in a TiddlyWiki file.

## Requirements

- Python 3.x
- BeautifulSoup

## Usage

### `tid2dict(tiddler)`

Converts tiddler as a BeautifulSoup object into a Python dictionary.

### `loadtiddlers(wiki, tidnames='_loadall')`

Loads the specified tiddlers from the specified TiddlyWiki file and returns the successfully loaded tiddlers as a list of dictionaries. If tidnames is not supplied, it loads all ordinary tiddlers in the storeArea.

### `findtiddlers(wiki, tidnames='_loadall')`

Search for the specified tiddlers in the specified TiddlyWiki file. Return the list of tiddler titles successfully matched. If tidnames is not supplied, search all ordinary tiddlers in the storeArea.

### `searchtiddlers(wiki, srchtxt, fieldlist, caseinsensitive=True)`

Search all tiddlers, returning a list of tiddler titles for those tiddlers that match the regex search text in any of the specified fields. Case insensitive by default. 

### `wikiedit(wiki, tiddlers, deletelist, modi=u'python')`

Deletes tiddlers in the deletelist and the tiddlers list, if they currently exist, then writes the tiddlers list, adding/replacing the modifier attribute with the specified or default value. Timestamps modified and/or created dates in UTC.

Returns (writtenlist, deletedlist) - list of tiddlers successfully deleted and written.

## Contribution

Feel free to contribute to this project. Any kind of feedback, suggestion or bug reporting is highly appreciated.

## License

This project is open-source and available under the AGPL

## Contact

If you have any questions, comments, or need further information, please don't hesitate to reach out.
