#!/usr/bin/env python3

"""setup.py: setuptools control"""


import re
from setuptools import setup

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('pybnf/pybnf.py').read(),
    re.M
    ).group(1)

with open('README.md', 'rb') as f:
    long_desc = f.read().decode('utf-8')

setup(name='pybnf',
      packages=['pybnf'],
      entry_points={'console_scripts': ['pybnf = pybnf.pybnf:main']},
      version=version,
      description='An application for parallel fitting of BioNetGen and SBML models using metaheuristics',
      long_description=long_desc,
      author='Eshan Mitra, Ryan Suderman, Alex Ionkov',
      install_requires=['distributed>=2.22.0', 'paramiko', 'numpy', 'scipy',
                        'nose', 'pyparsing', 'libroadrunner>=1.5.2',
                        'dask>=2.22.0', 'tornado>5.0.0'],
      python_requires=">=3.5,<3.8")
