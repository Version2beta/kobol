from flask import json

DEFAULT_CONFIGURATION_FILES = [
  '/etc/kobol.conf',
  '~/.kobol',
  './.kobol',
]
DEFAULT_CONFIGURATION = {
  'title': 'kobol',
  'description': 'a site built with kobol',
  'url': 'http://kobol.version2beta.com',
  'theme': 'kobol',
  'pages': [ 'pages' ],
  'articles': [ 'articles' ],
  'assets': [ 'assets' ],
  'templates': [ 'templates' ],
  'deploy': []
}

class Configuration(object):
  """ Create a configuration object from various sources. """

  def __init__(self, files = DEFAULT_CONFIGURATION_FILES):
    self._dict = DEFAULT_CONFIGURATION.copy()
    files = files if type(files) == list else [files]
    for f in files:
      try:
        self._dict.update(json.load(open(f, 'r')))
      except IOError:
        pass

  def __getitem__(self, key):
    return self._dict[key]

  def get(self, key):
    return self._dict[key]

  def __setitem__(self, key, value):
    self._dict[key] = value

  def set(self, key, value):
    self._dict[key] = value

