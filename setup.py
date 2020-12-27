from setuptools import setup
from glob import glob

setup(name='oo-programming-exercises',
      version=2020.0,
      description="""Code for Object oriented programming in Python for mathematicians.""",
      author="David Ham",
      author_email="david.ham@imperial.ac.uk",
      url="https://object-oriented-python.github.io/",
      packages=["fibonacci", "example_code"],
      scripts=glob('scripts/*'))
