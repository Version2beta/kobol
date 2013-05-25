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
from scaffold import Scaffold

class Kobol(object):

  def __init__(self, directory = '.'):
    self.home = directory

  def scaffold(self, **kwargs):
    if os.path.isfile(self.home + '/.kobol'):
      return False
    elif kwargs.get('dry') != True:
      shutil.copytree(
          os.path.dirname(os.path.abspath(__file__)) + '/skel/',
          os.getcwd())
    return True
