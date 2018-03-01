#!/bin/bash

# to build html for local testing

# set directory of the script as a current directory
cd "$( dirname "$0" )"

# activate Python's virtual environment
source venv/bin/activate

# turn echo on
set -x

# build the docs
pushd docs ; rm -dfr _build/ ; make html ; popd

# turn echo on
set +x

# deactivate Python's virtual environment
deactivate
