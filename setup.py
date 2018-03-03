#!/usr/bin/env python3
"""umbr_api setup script."""

from os import path
from setuptools import setup

with open(path.join(path.dirname(__file__), "README.rst")) as read_file:
    long_description = read_file.read()

base_dir = path.dirname(__file__)
about = {}
with open(path.join(base_dir, "umbr_api", "__about__.py")) as py_file:
    # pylint: disable=W0122
    exec(py_file.read(), about)

setup(
    name=about["__title__"],
    version=about["__version__"],
    description=about["__summary__"],
    long_description=long_description,
    url=about["__uri__"],
    author=about["__author__"],
    author_email=about["__email__"],
    platforms="Darwin",
    license=about["__license__"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Education",
        "Intended Audience :: System Administrators",
        "Topic :: Internet :: Name Service (DNS)",
        "Topic :: Security",
        "Topic :: Utilities",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3 :: Only"
    ],
    keywords='cisco umbrella opendns security',
    packages=['umbr_api'],
    install_requires=[
        'requests >= 2.18',
        'logzero >= 1.3.1',
        'keyring >= 11.0.0',
    ],
    extras_require={
        'dev':  [
            "coverage>=4.5.1",
            "pytest>=3.4.1",
            "setuptools>=38.5.1",
            "Sphinx>=1.7.1",
            "sphinx_rtd_theme>=0.2.4",
            "twine>=1.9.1"
        ],
        'dev_recommended': [
            "autopep8>=1.3.4",
            "pep257>=0.7.0",
            "pycodestyle>=2.3.1",
            "pydocstyle>=2.1.1",
            "pylint>=1.8.2"
        ],
    },
    package_data={
        'umbr_api': ['data/customer_key_example.json'],
    },
    entry_points={
        'console_scripts': [
            'umbrella=umbr_api.umbrella:main',
        ],
    },
    project_urls={
        'Cisco Umbrella': 'https://umbrella.cisco.com/',
        'Cisco Umbrella Enforcement API': 'https://docs.umbrella.com/' + \
            'developer/enforcement-api/'
    },
)
