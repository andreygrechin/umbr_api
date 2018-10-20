#!/usr/bin/env python3
"""umbr_api setup script."""

from os import path
from setuptools import setup

with open(path.join(path.dirname(__file__), "README.rst")) as read_file:
    LONG_DESCRIPTION = read_file.read()

ABOUT = {}
# pylint: disable=C0330
with open(path.join(
        path.dirname(__file__),
        "umbr_api",
        "__about__.py",
        )) as py_file:
    # pylint: disable=W0122
    exec(py_file.read(), ABOUT)

setup(
    name=ABOUT["__title__"],
    version=ABOUT["__version__"],
    description=ABOUT["__summary__"],
    long_description=LONG_DESCRIPTION,
    url=ABOUT["__uri__"],
    author=ABOUT["__author__"],
    author_email=ABOUT["__email__"],
    platforms="Darwin",
    license=ABOUT["__license__"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Education",
        "Intended Audience :: System Administrators",
        "Topic :: Internet :: Name Service (DNS)",
        "Topic :: Security",
        "Topic :: Utilities",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    keywords="cisco umbrella opendns security",
    packages=["umbr_api"],
    install_requires=[
        "requests ~= 2.19",
        "logzero ~= 1.5",
        "keyring ~= 15.0",
        "tabulate ~= 0.8.2",
    ],
    extras_require={
        "dev":  [
            "coverage>=4.5.1",
            "pytest>=3.8.0",
            "setuptools>=40.2.0",
            "twine>=1.12.0",
        ],
        "doc":  [
            "Sphinx>=1.8.0",
            "sphinx_rtd_theme>=0.4.2",
        ],
        "dev_lint": [
            "autopep8>=1.4",
            "pep257>=0.7.0",
            "pycodestyle>=2.4.0",
            "pydocstyle>=2.1.1",
            "pylint>=2.1.1",
        ],
    },
    package_data={
        "umbr_api": ["data/*_example.json"],
    },
    entry_points={
        "console_scripts": [
            "umbrella=umbr_api.umbrella:main",
        ],
    },
    project_urls={
        "Cisco Umbrella": "https://umbrella.cisco.com/",
        "Cisco Umbrella Enforcement API": "https://docs.umbrella.com/"
                                          "developer/enforcement-api/",
    },
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
)
