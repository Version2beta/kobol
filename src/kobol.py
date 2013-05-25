import os
import sys
import shutil
from datetime import datetime
from flask import Flask, render_template, abort, url_for, json, redirect
from flask_frozen import Freezer
import pygments.formatters
import boto
from boto.s3.key import Key

from configuration import Configuration
from resources import Site, Page

class Kobol(object):

  def __init__(self, directory = None):
    self.home = os.path.normpath(directory or os.getcwd()) + os.sep

  def configure(self):
    self.config = Configuration()

  def scaffold(self, **kwargs):
    if os.path.isfile(self.home + '/.kobol'):
      return False
    elif kwargs.get('dry') != True:
      skel = os.path.dirname(os.path.abspath(__file__)) + '/skel/'
      os.system("cp -R %s* %s.kobol %s" % (skel, skel, self.home))
    return True



  def main(self):
    self.configure()
    self.scaffold()
