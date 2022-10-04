try:
    from setuptools import setup

except ImportError:
    from distutils.core import setup

config = {
            'description': 'Advanced User Input',
            'author': 'Charles Ongom',
            'url': 'URL to get it at.',
            'download_url': 'Where to download it.',
            'author_email': 'charlieongom03@gmail.com',
            'version': '0.1',
            'install_requires': ['nose'],
            'packages': ['ex48'],
            'scripts': [],
            'name': 'projectname'
        }
setup(**config)

if __name__ == "__main__":
    print("This was run directly")
else:
    print("This was run as a module")