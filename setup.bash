#!/bin/bash

##############################################################################
# Global Variables
##############################################################################

PROJECT=vci
VENV_DIR=${HOME}/.venv/${PROJECT}

#############################
# Colours
#############################

BOLD="\e[1m"

CYAN="\e[36m"
GREEN="\e[32m"
RED="\e[31m"
YELLOW="\e[33m"

RESET="\e[0m"

#############################
# Loggers
#############################

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

#############################
# Functions
#############################

# smart installer that doesn't call sudo if it doesn't need to
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


#############################
# Checks
#############################

[[ "${BASH_SOURCE[0]}" != "${0}" ]] && SOURCED=1
if [ -z "$SOURCED" ]; then
  pretty_error "This script needs to be sourced, i.e. source './setup.bash', not './setup.bash'"
  exit 1
fi

#############################
# System Dependencies
#############################

pretty_header "Deb Dependencies"

install_package libyaml-dev || return
install_package python3-dev || return
install_package python3-venv || return

#############################
# Virtual Env
#############################

pretty_header "Virtual Environment"
if [ -x ${VENV_DIR}/bin/pip3 ]; then
    pretty_print "  $(padded_message "virtual_environment" "found [${VENV_DIR}]")"
else
    python3 -m venv ${VENV_DIR}
    pretty_warning "  $(padded_message "virtual_environment" "created [${VENV_DIR}]")"
fi

source ${VENV_DIR}/bin/activate

#############################
# Pypi Dependencies
#############################

# approximate ubuntu system dependencies

pretty_header "PyPi Build Dependencies"
pip3 install "setuptools==45.2"
pip3 install wheel  # needed to build and install other pip3 dependencies

pretty_header "PyPi Packaging Dependencies"
pip3 install "stdeb==0.8"
pip3 install "twine==3.1"

pretty_header "PyPi Doc Dependencies"
pip3 install "Sphinx==1.8"
pip3 install "sphinx-argparse==0.2"
pip3 install "sphinx_rtd_theme==0.4"

pretty_header "PyPi Test Dependencies"
pip3 install "flake8==3.7"
pip3 install "yanc==0.3"
pip3 install "nose-htmloutput==0.6"
pip3 install "nose==1.3"
pip3 install "pydot==1.4"
pip3 install "pytest==4.6"

pretty_header "PyPi Project Dependencies"
pip3 install "PyYAML==5.3"

#############################
# Setup Project
#############################

pretty_header "Setup Development Environment"
python3 setup.py develop

pretty_print ""
pretty_print "Leave the virtual environment with 'deactivate'"
pretty_print ""
pretty_print "I'm grooty, you should be too."
pretty_print ""

