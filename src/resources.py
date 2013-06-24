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

  def load(self):
    self['pages'] = self.load_from_dirs(
        self['config']['pages'],
        default_template = 'page',
        pagetype = 'page')
    self['pages'].update(self.load_from_dirs(
        self['config']['articles'],
        default_template = 'article',
        pagetype = 'article'))
    self['sitemap'] = self.build_sitemap()

  def load_from_dirs(self, dirs, **kwargs):
    result = {}
    d = dirs if type(dirs) == list else [dirs]
    for d in dirs:
      for path, dirs, files in os.walk(self['config']['home'] + d):
        basepath = ('/%s/' % path).replace(self['config']['home'], '')
        for f in files:
          if f.endswith(self['config']['extension']):
            metadata = self.load_meta(path + '/' + f)
            metadata['pagetype'] = kwargs['pagetype']
            metadata['template'] = metadata.get('template') or \
                kwargs['default_template']
            result[metadata['route']] = metadata
    return result

  def load_meta(self, page):
    headers, content = open(page, 'r').read().split('...')[:2]
    metadata = yaml.safe_load(headers)
    metadata['content'] = content
    metadata['path'] = page
    metadata['route'] = '/' + metadata['path'].replace(
        self['config']['home'], '').replace(
        'pages/', '').replace(
        self['config']['extension'], '') + '/'
    return metadata

  def build_sitemap(self):
    result = {}
    result['pages'] = self.extract_by_type()
    return result

  def extract_by_type(self):
    result = {}
    for k in self['pages'].keys():
      page = self['pages'][k]
      current_level = result
      for part in page['route'].split('/')[1:-1]:
        print part, 
        if 'children' not in current_level:
          print "creating a child"
          current_level['children'] = []
        current_level['children'].append({'level': part})
        current_level = current_level['children'][-1]
      current_level.update({
        'pagetitle': page.get('pagetitle'),
        'longtitle': page.get('longtitle'),
        'menuindex': page.get('menuindex'),
        'published': page.get('published'),
        'excerpt': page.get('excerpt'),
        'route': page.get('route')
      })
    print result
    return result

