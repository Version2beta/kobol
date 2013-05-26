import os
import sys
import yaml
from glob import glob

class Site(dict):
  """ Create a dictionary from the site content. """

  def __init__(self, *args, **kwargs):
    super(Site, self).__init__(*args, **kwargs)

  def config(self, configuration):
    self['config'] = configuration

  def load(self, page = None):
    self['pages'] = self.load_from_dirs(self['config']['pages'])
    self['pages'].sort(key = lambda x: x.get('menuindex'))
    self['articles'] = self.load_from_dirs(self['config']['articles'])
    self['articles'].sort(key = lambda x: x.get('published'), reverse = True)
    if page:
      self['page'] = self.load_page(page)

  def load_from_dirs(self, dirs):
    result = []
    if type(dirs) != list:
      dirs = [dirs]
    for d in dirs:
      for path, dirs, files in os.walk(self['config']['home'] + d):
        for f in files:
          if f.endswith(self['config']['extension']):
            metadata = self.load_meta(path + '/' + f)
            metadata['path'] = path + '/' + f
            metadata['directory'] = ('/%s/' % path).replace(
                self['config']['home'], '')
            metadata['filename'] = f.replace(self['config']['extension'], '')
            metadata['route'] = metadata['directory'] + metadata['filename']
            result.append(metadata)
    return result

  def load_meta(self, page):
    metadata = open(page, 'r').read().split('...')[0]
    return yaml.safe_load(metadata)

  def load_content(self, page):
    pass

  def load_page(self, page):
    pass
