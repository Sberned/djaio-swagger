#!/usr/bin/env python
import os
from setuptools import setup, find_packages

base = os.path.dirname(os.path.abspath(__file__))

README_PATH = os.path.join(base, "README.rst")

install_requires = [
    'transmute-core>=0.2.2',
    'aiohttp',
    'PyYAML>==3.12,<=4',
]

tests_require = []

setup(name='djaio-swagger',
      version='0.0.1b',
      description='The battery to generate additional swagger-spec json routes for '
                  'your ClassBasedView methods (get,post,put,delete). Based on aiothh-transmute app by Yusuke Tsutsumi.',
      long_description=open(README_PATH).read(),
      author='Alexander Sivov',
      author_email='aasivov@sberned.ru',
      url='',
      packages=find_packages(),
      install_requires=install_requires,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Operating System :: MacOS',
          'Operating System :: POSIX :: Linux',
          'Topic :: System :: Software Distribution',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
      ],
      tests_require=tests_require
)
