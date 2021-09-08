from setuptools import setup
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='TiddlPy',
      version='0.2',
      description='API for interfacng with Tiddlywiki 5 files.',
      url='https://github.com/opencoca/TiddlPy',
      author='OpenCo',
      author_email='admin@openco.ca',
      license='LGPL',   # MIT, BSD
      packages=['TiddlPy'],
      long_description=read('README.md'),
      keywords = ["wiki, database, personal, DBMS"],
      classifiers=[
          "Development Status :: 3 - Alpha",
          "Topic :: Utilities",
          "Programming Language :: Python",
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: BSD GNU General Public License (GPL)",
          "Operating System :: OS Independent"],
      zip_safe=True
      )



# https://pypi.python.org/pypi?%3Aaction=list_classifiers
# # Development Status :: 1 - Planning
# Development Status :: 2 - Pre-Alpha
# Development Status :: 3 - Alpha
# Development Status :: 4 - Beta
# Development Status :: 5 - Production/Stable
# Development Status :: 6 - Mature
# Development Status :: 7 - Inactive
