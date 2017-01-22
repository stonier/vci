#!/bin/bash

# Script for setting up the development environment.

if [ "${VIRTUAL_ENV}" == "" ]; then
  workon vcs_extras
  if [ $? -ne 0 ]; then
    mkvirtualenv vcs_extras
    if [ $? -ne 0 ]; then
    	sudo apt-get install virtualenvwrapper
        mkvirtualenv vcs_extras
    fi
    # probably some python setup.py target which will do this for you
    pip install vcstool
  fi
fi
# Always pulling for now
python setup.py develop

echo ""
echo "Leave the virtual environment with 'deactivate'"
echo ""
echo "I'm grooty, you should be too."
echo ""

