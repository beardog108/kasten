from setuptools import setup, find_packages

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='kasten',
      version='0.0.5',
      description='Library desc',
      author='Author Name',
      author_email='beardog@mailbox.org',
      url='https://chaoswebs.net',
      packages=find_packages(exclude=['contrib', 'docs', 'tests']),
      install_requires=['mimcvdf', 'msgpack'],
      long_description=long_description,
      long_description_content_type='text/markdown',
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers"
      ],
     )
