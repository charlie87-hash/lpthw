
'''
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py

pip install virtual env
mkdir . venvs
.\.venvs\lpthw\Scripts\activate
pip install nose

$ mkdir projects
$ cd projects/
$ mkdir skeleton
$ cd skeleton
$ mkdir bin NAME tests docs
$ touch NAME/ __init__.py
$ touch tests/ __init__.py

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
             'description': 'My Project',
             'author': 'My Name',
             'url': 'URL to get it at.',
             'download_url': 'Where to download it.',
             'author_email': 'My email.',
             'version': '0.1',
             'install_requires': ['nose'],
             'packages': ['NAME'],
             'scripts': [],
             'name': 'projectname'
             }

setup(**config)


from nose.tools import *
import NAME

def setup():
    print("SETUP!")

def teardown():
    print("TEAR DOWN!")

def test_basic():
    print("I RAN!", end='')

directory structure
skeleton/
    NAME/
        __init__.py
    bin/
    docs/
    setup.py
    tests/
        NAME_tests.py
        __init__.py

'''

'''
1. Make a copy of your skeleton directory. Name it after your new project.
2. Rename (move) the NAME directory to be the name of your project or whatever you want to call
your root module.
3. Edit your setup.py to have all the information for your project.
4. Rename tests/NAME_tests.py to also have your module name.
5. Double check it’s all working by using nosetests again.
6. Start coding.

'''
