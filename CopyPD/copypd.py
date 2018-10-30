# Copys everything when a pd is atatched on ubuntu


import os
import datetime
import shutil
from shutil import copytree, ignore_patterns

files = os.listdir('/media/<username>/')

destination = '/home/<username>/Backup/back_%s'%datetime.datetime.now()
try :
    for f in files:
        source = '/media/<username>/%s' % f
        copytree(source, destination, ignore=ignore_patterns('*.pyc', 'tmp*'))    
except Exception as e:
    print e
