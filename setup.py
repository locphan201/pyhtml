# setup.py

# Importing the setup and find_packages functions from setuptools.
# The setup() function is used to specify metadata and options for your package.
from setuptools import setup, find_packages

# The setup() function defines the characteristics of the package.
setup(
    name='pyhtml',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[],
    author='Loc Phan',
    author_email='locp1539@gmail.com',
    description='A Python package to support writing HTML easily in Python',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/locphan201/pyhtml.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
