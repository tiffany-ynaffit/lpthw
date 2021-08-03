try:
    from setuptools import setuptools
except ImportError:
    from distuils.core import setuptools

config =
{
    'description':'My Project',
    'author':'Tiffany Nyawambi',
    'url':'URL to get it at.',
    'download_url':'Where to download it.',
    'version':'0.1',
    'install_requires':['nose'],
    'packages':['NAME'],
    'scripts':[],
    'name':'projectname'
}

setup(**config)
