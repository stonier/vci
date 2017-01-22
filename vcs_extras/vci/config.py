#
# License: BSD
#    https://raw.githubusercontent.com/stonier/vcs_extras/devel/LICENSE
#
##############################################################################
# Documentation
##############################################################################

"""
Configure version control index settings.
"""

##############################################################################
# Imports
##############################################################################

import argparse
import os
import urllib2
import urlparse
import yaml

import vcs_extras.console as console

from . import common

##############################################################################
# Constants
##############################################################################

DEFAULT_INDEX_URL = 'https://raw.githubusercontent.com/stonier/vcs_extras/repos/kinetic.yaml'

##############################################################################
# Library
##############################################################################


def get_index():
    filename = os.path.join(common.home(), "settings")
    try:
        f = open(filename, 'r')
    except IOError:
        return set_index(DEFAULT_INDEX_URL)
    index_url = f.read()
    f.close()
    return index_url


def set_index(index_url):
    '''
      Set a uri for the vcs index to use for retrieval.
    '''
    # could actually check that it is a valid uri though.
    filename = os.path.join(common.home(), "settings")
    f = open(filename, 'w+')
    try:
        f.write(index_url.encode('utf-8'))
    finally:
        f.close()
    return index_url

##############################################################################
# Command Parser
##############################################################################


def examples_string():
    examples = console.bold + "Examples\n\n" + console.reset  \
        + console.cyan + "  vci config" \
        + console.reset + " : " + console.yellow \
        + "display the current index url\n" + console.reset \
        + console.cyan + "  vci config --set file:///home/stonier/kinetic.yaml" \
        + console.reset + " : " + console.yellow \
        + "set the index to a local file\n" + console.reset \
        + console.cyan + "  vci config --set https://raw.githubusercontent.com/stonier/vcs_extras/repos/kinetic.yaml" \
        + console.reset + " : " + console.yellow \
        + "set the index to a public github file\n" + console.reset
    examples = console.bold + "Examples\n\n" + console.reset  \
        + "  1) Display the current index url\n\n" \
        + console.cyan + "      vci config\n\n" + console.reset \
        + "  2) Set the index to a local file\n\n" \
        + console.cyan + "      vci config " + console.yellow + "--set file:///home/stonier/kinetic.yaml\n\n" + console.reset \
        + "  3) Set the index to a public github file\n\n" \
        + console.cyan + "      vci config " + console.yellow + "--set https://raw.githubusercontent.com/stonier/vcs_extras/repos/kinetic.yaml\n\n" + console.reset
    return examples


def parse_args(args):
    """
    Execute the command given the incoming args.
    """
    if args.set:
        set_index(args.set)
    index_url = get_index()
    print("\n" + console.cyan + "URL " + console.reset + ": " + console.yellow + index_url + console.reset + "\n")


def add_subparser(subparsers):
    """
    Add our own argparser to the parent.

    :param subparsers: the subparsers factory from the parent argparser.
    """
    subparser = subparsers.add_parser(
        "config",
        description="""Manage the list of version control index url's and their keys.""",
        help="manage the version control index list",  # this shows in the parent parser
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    subparser.epilog = examples_string()
    subparser.set_defaults(func=parse_args)
    group = subparser.add_mutually_exclusive_group()
    add = group.add_argument
    add('-s', '--set', action='store', default=None, help="set the url for the index to use for retrieval")
