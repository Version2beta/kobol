import os
import tempfile
import shutil
import unittest
from expecter import expect
import dingus
import kobol
from kobol import Kobol

class TestDefaultConfiguration(unittest.TestCase):

  def test_theme_is_kobol(self):
    k = Kobol()
    expect(k.config['theme']) == 'kobol'

  def test_articles_are_articles(self):
    k = Kobol()
    expect(k.config['articles']) == ['articles']

  def test_deploy_is_empty(self):
    k = Kobol()
    expect(k.config['deploy']) == []

  def test_kobol_configures_self(self):
    tmp_dir = tempfile.mkdtemp()
    k = Kobol(tmp_dir)
    k.main()
    shutil.rmtree(tmp_dir)
    expect(k.config['theme']) == 'kobol'

class TestAddingConfigurationFiles(unittest.TestCase):

  def test_adding_one_more_file(self):
    k = Kobol()
    k.load_config_files('support/.kobol')
    expect(k.config.get('theme')) == 'kobol'

  def test_adding_two_more_file(self):
    k = Kobol()
    k.load_config_files([ 'support/.kobol', 'support/final_config.conf' ])
    expect(k.config.get('theme')) == 'RADTHEME'

class TestAddingSkeletonFiles(unittest.TestCase):

  def test_kobol_identifies_a_directory_to_scaffold(self):
    k = Kobol()
    expect(k.scaffold(dry = True)) == True

  def test_kobol_identifies_a_directory_not_to_scaffold(self):
    k = Kobol('./support/')
    expect(k.scaffold()) == False

  def test_kobol_scaffolds_a_project(self):
    tmp_dir = tempfile.mkdtemp()
    Kobol(tmp_dir).scaffold()
    expect(os.path.isfile(tmp_dir + '/.kobol')) == True
    #shutil.rmtree(tmp_dir)

class TestTheSiteDictionary(unittest.TestCase):

  def test_loading_the_site_configuration(self):
    k = Kobol('./support')
    expect(k.site['config']['title']) == 'kobol'

  def test_loading_pages_into_the_site_dictionary(self):
    k = Kobol('./support')
    k.site.load()
    expect(k.site['pages']['/test1/']['pagetitle']) == 'test1'

  def test_loading_articles_into_the_site_dictionary(self):
    k = Kobol('./support')
    k.site.load()
    expect(k.site['pages']['/articles/test2/']['pagetitle']) == 'test2'

  def test_site_map(self):
    k = Kobol('./support')
    k.site.load()
    expect(k.site['sitemap']) == {}

