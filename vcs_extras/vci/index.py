#
# License: BSD
#    https://raw.githubusercontent.com/stonier/vcs_extras/devel/LICENSE
#
##############################################################################
# Documentation
##############################################################################

"""
Manage version control index lists.
"""

##############################################################################
# Imports
##############################################################################

import argparse
import os

import vcs_extras.console as console

from . import common

##############################################################################
# Constants
##############################################################################

DEFAULT_INDEX_URL = 'https://raw.github.com/stonier/devel/pax_repos_index/kinetic.yaml'

##############################################################################
# Methods
##############################################################################


def list_index_database():
    print("List local index database")


def get_index():
    print("Get the index")


def set_index(index_url):
    '''
      Set a uri for the vcs index to use for retrieval.
    '''
    print("Set a new index url %s" % index_url)

    # could actually check that it is a valid uri though.
    filename = os.path.join(common.home(), "settings")
    f = open(filename, 'w+')
    try:
        f.write(index_url.encode('utf-8'))
    finally:
        f.close()
    return index_url


def parse_args(args):
    """
    Execute the command given the incoming args.
    """
    if args.get:
        get_index()
    if args.set:
        set_index(args.set)
    else:
        list_index_database()

    print("Execute index")


def add_subparser(subparsers):
    """
    Add our own argparser to the parent.

    :param subparsers: the subparsers factory from the parent argparser.
    """
    subparser = subparsers.add_parser(
        "index",
        description="""Manage the list of version control index url's and their keys.""",
        help="manage the version control index list",  # this shows in the parent parser
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    subparser.set_defaults(func=parse_args)
    group = subparser.add_mutually_exclusive_group()
    add = group.add_argument
    add('-g', '--get', action='store_true', help="show the currently stored url of the index used for retrieval")
    add('-s', '--set', action='store', default=None, help="set the url for the index to use for retrieval")
