import os
import tempfile
import unittest
from expecter import expect
import dingus
import kobol
from kobol import Kobol

class TestDefaultConfiguration(unittest.TestCase):

  def test_theme_is_kobol(self):
    c = kobol.Configuration()
    expect(c['theme']) == 'kobol'

  def test_articles_are_articles(self):
    c = kobol.Configuration()
    expect(c['articles']) == ['articles']

  def test_deploy_is_empty(self):
    c = kobol.Configuration()
    expect(c['deploy']) == []


class TestAddingConfigurationFiles(unittest.TestCase):

  def test_adding_one_more_file(self):
    c = kobol.Configuration('support/.kobol')
    expect(c.get('pages')) == [ 'mypages' ]

  def test_adding_two_more_file(self):
    c = kobol.Configuration( [ 'support/.kobol', 'support/final_config.conf' ] )
    expect(c.get('theme')) == 'RADTHEME'

class TestAddingSkeletonFiles(unittest.TestCase):

  def test_kobol_identifies_a_directory_to_scaffold(self):
    k = Kobol('.')
    expect(k.scaffold(dry = True)) == True

  def test_kobol_identifies_a_directory_not_to_scaffold(self):
    k = Kobol('./support/')
    expect(k.scaffold(dry = True)) == False

  def test_kobol_scaffolds_a_project(self):
    tmp_dir = tempfile.mkdtemp()
    Kobol(tmp_dir).scaffold()
    expect(os.path.isfile(tmp_dir + '/.kobol')) == True
    os.unlink(tmp_dir)

