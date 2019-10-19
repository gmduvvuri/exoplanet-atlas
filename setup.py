from setuptools import setup, find_packages
import os,sys

def readme():
    with open('README.md') as f:
        return f.read()

# a little kludge to get the version number from __version__
exec(open('exopop/version.py').read())

setup(name = "exopop",
    version = version,
    description = "Tools for compiling and plotting populations of transiting exoplanets.",
    long_description = readme(),
    author = "Zachory K. Berta-Thompson",
    author_email = "zkbt@mit.edu",
    url = "https://github.com/zkbt/exopop",
    packages = find_packages(),
    package_data = {'':[]},
    scripts = [],
    classifiers=[
      'Intended Audience :: Science/Research',
      'Programming Language :: Python',
      'Topic :: Scientific/Engineering :: Astronomy'
      ],
    install_requires=['numpy>=1.9'],
    zip_safe=False
)
