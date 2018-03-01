#!/bin/bash

# turn echo on
set -x

# set directory of the script as a current directory
cd "$( dirname "$0" )"

# activate Python's virtual environment
source venv/bin/activate

# build the package
python3 setup.py sdist

# build the docs
pushd docs ; make html ; popd

# read -p "Press Enter to upload package to test PyPI [ENTER]" </dev/tty
# twine upload --repository-url https://test.pypi.org/legacy/ dist/*

read -p "Press Enter to upload package to production PyPI [ENTER]" </dev/tty
twine upload dist/*

read -p "Press Enter to deactivate venv [ENTER]" </dev/tty
deactivate
