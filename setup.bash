#!/bin/bash

##############################################################################
# Global Variables
##############################################################################

NAME=vci

##############################################################################
# Colours
##############################################################################

BOLD="\e[1m"

CYAN="\e[36m"
GREEN="\e[32m"
RED="\e[31m"
YELLOW="\e[33m"

RESET="\e[0m"

##############################################################################
# Loggers
##############################################################################

padded_message ()
{
  line="........................................"
  printf "%s %s${2}\n" ${1} "${line:${#1}}"
}

pretty_header ()
{
  echo -e "${BOLD}${1}${RESET}"
}

pretty_print ()
{
  echo -e "${GREEN}${1}${RESET}"
}

pretty_warning ()
{
  echo -e "${YELLOW}${1}${RESET}"
}

pretty_error ()
{
  echo -e "${RED}${1}${RESET}"
}

##############################################################################
# Methods
##############################################################################

install_package ()
{
  PACKAGE_NAME=$1
  dpkg -s ${PACKAGE_NAME} > /dev/null
  if [ $? -ne 0 ]; then
    sudo apt-get -q -y install ${PACKAGE_NAME} > /dev/null
  else
    pretty_print "  $(padded_message ${PACKAGE_NAME} "found")"
    return 0
  fi
  if [ $? -ne 0 ]; then
    pretty_error "  $(padded_message ${PACKAGE_NAME} "failed")"
    return 1
  fi
  pretty_warning "  $(padded_message ${PACKAGE_NAME} "installed")"
  return 0
}

##############################################################################

install_package virtualenvwrapper || return

# To use the installed python3
VERSION="--python=/usr/bin/python3"
# To use a specific version
# VERSION="--python=python3.6"

# Script for setting up the development environment.

if [ "${VIRTUAL_ENV}" == "" ]; then
  workon ${NAME}
  if [ $? -ne 0 ]; then
    mkvirtualenv ${VERSION} ${NAME}
  fi
fi

# Get all dependencies for testing, doc generation
pip install -e .[docs]
pip install -e .[test]
pip install -e .[debs]

# NB: this automagically nabs install_requires
python setup.py develop

echo ""
echo "Leave the virtual environment with 'deactivate'"
echo ""
echo "I'm grooty, you should be too."
echo ""

