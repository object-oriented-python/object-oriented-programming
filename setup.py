from setuptools import setup
from glob import glob

setup(name='oo-programming-exercises',
      version=2018.0,
      description="""Code for Object oriented programming in Python for mathematicians.""",
      author="David Ham",
      author_email="david.ham@imperial.ac.uk",
      #url="https://finite-element.github.io/",
      packages=[fibonacci],
      scripts=glob('scripts/*'))
