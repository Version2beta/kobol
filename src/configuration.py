import os
import sys
from flask import json

DEFAULT_CONFIGURATION_FILES = [
  '/etc/kobol.conf',
  '~/.kobol',
  './.kobol',
]
DEFAULT_CONFIGURATION = {
  'title': 'kobol',
  'description': 'a site built with kobol',
  'author': 'blogger',
  'url': 'http://kobol.version2beta.com/',
  'theme': 'kobol',
  'pages': [ 'pages' ],
  'articles': [ 'articles' ],
  'assets': [ 'assets' ],
  'templates': [ 'templates' ],
  'extension': '.yaml',
  'deploy': []
}

class Configuration(dict):
  """ Create a configuration object from various sources. """

  def __init__(self, *args, **kwargs):
    super(Configuration, self).__init__(*args, **kwargs)
    self.update(DEFAULT_CONFIGURATION)
    self.load(DEFAULT_CONFIGURATION_FILES)

  def load(self, files):
    files = files if type(files) == list else [files]
    for f in files:
      try:
        self.update(json.load(open(os.path.expanduser(f), 'r')))
      except IOError:
        pass
      except:
        sys.stderr.write("Warning: could not read configuration file %s." % f)

